#!/usr/bin/env python3
"""Render ALEX/SAM transcripts to MP3 with the ElevenLabs text-to-speech API.

Usage: uv run --with requests --with mutagen --with pillow tools/render.py [--limit N] [--dry-run] [--out DIR] transcript.md...

Each speaker turn becomes one TTS request, cached by a hash of the request
including the neighbouring turns, so reruns cost nothing. A turn whose own text
is unchanged reuses its clip even when a neighbour was edited, so an edit pays
only for the edited turn. --dry-run reports the characters a render would bill. Turns are joined with short gaps. A "## Title" line in the body starts an
MP3 chapter at the next turn. cards/<stem>.json adds a chapter at each drill
question (artwork showing the options) and at its answer (artwork marking the
correct ones). Chapters are embedded as ID3 CHAP frames with titles and images,
and written to <stem>.chapters.json (Podcasting 2.0) with images in cards/<stem>/.
The API key is read from ELEVENLABS_API_KEY or the elevenlabs MCP server
entry in ~/.claude.json.
"""
import argparse
import concurrent.futures
import hashlib
import json
import os
import pathlib
import re
import shutil
import subprocess
import sys

import requests
from mutagen.id3 import APIC, CHAP, CTOC, ID3, TIT2, CTOCFlags

import cards

VOICES = {
    "ALEX": "JBFqnCBsd6RMkjVDRZzb",  # George - warm British male
    "SAM": "Xb7hH8MSUJpSbSDYk0k2",  # Alice - clear British female educator
}
MODEL = "eleven_turbo_v2_5"
VOICE_SETTINGS = {"stability": 0.45, "similarity_boost": 0.75, "style": 0.0, "use_speaker_boost": True}
TURN_GAP_S = 0.35
PAUSE_GAP_S = TURN_GAP_S  # listener prefers continuous playback; raise (e.g. 4.0) to leave time to answer drills
TAG = re.compile(r"\[(pause|sting|laughs|sighs|thoughtful|excited)\]")
MUSIC = pathlib.Path(__file__).resolve().parent.parent / "music"
# Spoken-only respellings for words the TTS model mispronounces; transcripts keep the real spelling.
PRONUNCIATIONS = {
    r"\bretries\b": "re-tries",  # otherwise read as "re-trees"
    r"\bRetries\b": "Re-tries",
    r"\bevals\b": "ee-vals",  # otherwise read as "evils"
    r"\bEvals\b": "Ee-vals",
    r"\beval\b": "ee-val",
    r"\bEval\b": "Ee-val",
}


def api_key():
    key = os.environ.get("ELEVENLABS_API_KEY")
    if key:
        return key
    cfg = json.loads((pathlib.Path.home() / ".claude.json").read_text())
    return cfg["mcpServers"]["elevenlabs"]["env"]["ELEVENLABS_API_KEY"]


def parse(path):
    text = path.read_text()
    _, front, body = text.split("---", 2)
    meta = {}
    for line in front.strip().splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip().strip('"')
    turns = []
    chapter = None
    for line in body.splitlines():
        if line.startswith("## "):
            chapter = line[3:].strip()
            continue
        m = re.match(r"^(ALEX|SAM): (.*)$", line)
        if not m:
            continue
        speaker, speech = m.groups()
        pause = "[pause]" in speech
        sting = "[sting]" in speech
        speech = re.sub(r"\s+", " ", TAG.sub("", speech)).strip()
        for pattern, spoken in PRONUNCIATIONS.items():
            speech = re.sub(pattern, spoken, speech)
        if speech:
            turns.append({"speaker": speaker, "text": speech, "pause": pause, "sting": sting, "chapter": chapter,
                          "line": line})
            chapter = None
    return meta, turns


def synth(session, key, turn, prev_text, next_text, cache):
    payload = {
        "text": turn["text"],
        "model_id": MODEL,
        "voice_settings": VOICE_SETTINGS,
        "previous_text": prev_text,
        "next_text": next_text,
    }
    voice = VOICES[turn["speaker"]]
    digest = hashlib.sha256(json.dumps([voice, payload], sort_keys=True).encode()).hexdigest()[:20]
    out = cache / f"{digest}.mp3"
    same_text = {k: payload[k] for k in ("text", "model_id", "voice_settings")}
    alias = cache / f"text-{hashlib.sha256(json.dumps([voice, same_text], sort_keys=True).encode()).hexdigest()[:20]}.mp3"
    if out.exists() and out.stat().st_size > 0:
        if not alias.exists():
            alias.symlink_to(out.name)
        return out
    if alias.exists():
        return alias
    if key is None:  # dry run
        return len(turn["text"])
    for attempt in range(5):
        r = session.post(
            f"https://api.elevenlabs.io/v1/text-to-speech/{voice}",
            params={"output_format": "mp3_44100_128"},
            headers={"xi-api-key": key},
            json=payload,
            timeout=120,
        )
        if r.status_code == 429 or r.status_code >= 500:
            import time
            time.sleep(2 ** attempt)
            continue
        if r.status_code == 401:
            sys.exit(f"ElevenLabs auth failed: {r.text[:200]}")
        r.raise_for_status()
        out.write_bytes(r.content)
        if not alias.exists():
            alias.symlink_to(out.name)
        return out
    raise RuntimeError(f"giving up after retries: {r.status_code} {r.text[:200]}")


def silence(cache, seconds):
    out = cache / f"silence-{seconds}.mp3"
    if not out.exists():
        subprocess.run(
            ["ffmpeg", "-y", "-loglevel", "error", "-f", "lavfi", "-i", "anullsrc=r=44100:cl=mono",
             "-t", str(seconds), "-b:a", "128k", str(out)],
            check=True,
        )
    return out


def duration(path, _seen={}):
    if path not in _seen:
        out = subprocess.run(
            ["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
            capture_output=True, text=True, check=True,
        )
        _seen[path] = float(out.stdout.strip())
    return _seen[path]


def chapter_marks(path, meta, turns):
    """Chapters keyed by turn index: segment headings, plus question and answer cards from cards/<stem>.json."""
    episode = meta.get("title", path.stem)
    marks = {}
    for i, t in enumerate(turns):
        if t["chapter"]:
            marks[i] = (t["chapter"], cards.segment(t["chapter"], episode))
    data = MUSIC.parent / "cards" / f"{path.stem}.json"
    drills = json.loads(data.read_text())["drills"] if data.exists() else []

    def find(prefix):
        hits = [i for i, t in enumerate(turns) if t["line"].startswith(prefix)]
        if len(hits) != 1:
            sys.exit(f"{data.name}: {len(hits)} turns start with {prefix[:60]!r}")
        return hits[0]

    for n, d in enumerate(drills, 1):
        q = find(d["question_line"])
        seg = marks.get(q, (None,))[0]
        if d["kind"] == "mcq":
            if not set(d["correct"]) <= set(d["options"]) or len(d["correct"]) != d.get("choose", 1):
                sys.exit(f"{data.name}: drill {n} correct {d['correct']} does not fit its options or choose count")
            title = f"Question {n}: {d.get('scenario') or d.get('label', 'Drill')}"
            marks[q] = (f"{seg} - {title}" if seg else title, cards.question(d, episode, n))
            if d.get("answer_line"):
                marks[find(d["answer_line"])] = (f"Answer {n}", cards.answer(d, episode, n))
        else:
            title = f"Pause and answer {n}"
            marks[q] = (f"{seg} - {title}" if seg else title, cards.recall(d, episode, n, reveal=False))
            if d.get("answer_line"):
                marks[find(d["answer_line"])] = (f"Answer {n}", cards.recall(d, episode, n, reveal=True))
    return marks


def write_chapters(mp3, meta, chapters, total, stem, out_dir):
    """Embed ID3 chapters with titles and artwork, and write Podcasting 2.0 JSON plus the images beside the MP3."""
    tags = ID3(mp3)
    tags.delall("CHAP")
    tags.delall("CTOC")
    img_dir = out_dir / "cards" / stem
    shutil.rmtree(img_dir, ignore_errors=True)
    img_dir.mkdir(parents=True)
    ids, entries = [], []
    for n, (start, title, img) in enumerate(chapters):
        end = chapters[n + 1][0] if n + 1 < len(chapters) else total
        cid = f"ch{n:03d}"  # zero-padded so frame order matches play order
        ids.append(cid)
        tags.add(CHAP(element_id=cid, start_time=int(start * 1000), end_time=int(end * 1000),
                      sub_frames=[TIT2(encoding=3, text=[title]),
                                  APIC(encoding=3, mime="image/jpeg", type=0, desc=cid, data=img)]))
        name = f"{n:02d}.jpg"
        (img_dir / name).write_bytes(img)
        entries.append({"startTime": round(start, 2), "title": title, "img": name})
    tags.add(CTOC(element_id="toc", flags=CTOCFlags.TOP_LEVEL | CTOCFlags.ORDERED, child_element_ids=ids,
                  sub_frames=[TIT2(encoding=3, text=["Chapters"])]))
    tags.save(mp3, v2_version=3)
    (out_dir / f"{stem}.chapters.json").write_text(json.dumps(
        {"version": "1.2.0", "title": meta.get("title", stem), "chapters": entries}, indent=2) + "\n")


def episode_label(episode):
    return f"{int(episode):02d}" if episode.isdigit() else episode


def render(path, out_dir, cache, key, limit, album, dry_run=False):
    meta, turns = parse(path)
    if limit:
        turns = turns[:limit]
    session = requests.Session()
    if dry_run:
        billed = [synth(session, None, t, turns[i - 1]["text"] if i else "",
                        turns[i + 1]["text"] if i + 1 < len(turns) else "", cache) for i, t in enumerate(turns)]
        billed = [b for b in billed if isinstance(b, int)]
        print(f"{path.name}  turns to synthesize={len(billed)} chars={sum(billed)}")
        return sum(billed)
    with concurrent.futures.ThreadPoolExecutor(max_workers=4) as pool:
        futures = [
            pool.submit(
                synth, session, key, t,
                turns[i - 1]["text"] if i > 0 else "",
                turns[i + 1]["text"] if i + 1 < len(turns) else "",
                cache,
            )
            for i, t in enumerate(turns)
        ]
        clips = [f.result() for f in futures]
    gap, pause = silence(cache, TURN_GAP_S), silence(cache, PAUSE_GAP_S)
    beat = silence(cache, 0.6)
    intro, sting, outro = (MUSIC / f"{name}-norm.mp3" for name in ("intro", "sting", "outro"))
    entries = [intro, beat] if intro.exists() else []
    by_turn = chapter_marks(path, meta, turns) if not limit else {}
    marks = []  # (index into entries, chapter title, card image)
    for i, (t, clip) in enumerate(zip(turns, clips)):
        if i in by_turn:
            marks.append((len(entries), *by_turn[i]))
        entries += [clip, pause if t["pause"] else gap]
        if t["sting"] and sting.exists():
            entries += [sting, beat]
    if outro.exists():
        entries += [beat, outro]
    playlist = cache / f"{path.stem}.txt"
    playlist.write_text("".join(f"file '{e}'\n" for e in entries))
    suffix = "-sample" if limit else ""
    out = out_dir / f"{path.stem}{suffix}.mp3"
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(playlist),
         "-af", "aresample=44100", "-ac", "1", "-b:a", "128k",  # resample: mixed TTS/music frames break lame otherwise
         "-metadata", f"title={episode_label(meta.get('episode', ''))} {meta.get('title', path.stem)}",
         "-metadata", f"album={album}",
         "-metadata", "artist=Pass the Architect",
         "-metadata", f"track={meta.get('episode', '')}",
         "-metadata", "genre=Podcast",
         str(out)],
        check=True,
    )
    n_chapters = 0
    if marks:
        starts, total = [], 0.0
        for e in entries:
            starts.append(total)
            total += duration(e)
        chapters = [(0.0 if n == 0 else starts[i], title, img) for n, (i, title, img) in enumerate(marks)]
        write_chapters(out, meta, chapters, total, path.stem, out_dir)
        n_chapters = len(chapters)
    chars = sum(len(t["text"]) for t in turns)
    print(f"{out}  turns={len(turns)} chars={chars} chapters={n_chapters}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcripts", nargs="+", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, help="default: audio/ beside the transcripts folder")
    # Outside the checkout so it survives worktree cleanup; without it every rerender is billed in full.
    ap.add_argument("--cache", type=pathlib.Path, default=pathlib.Path.home() / ".cache/pass-the-architect/tts-cache")
    ap.add_argument("--dry-run", action="store_true", help="report characters to be billed; call no API")
    ap.add_argument("--budget", type=int, default=0, help="maximum characters this run may bill (default 0)")
    ap.add_argument("--limit", type=int, default=0, help="render only the first N turns (sample)")
    ap.add_argument("--album", default="Pass the Architect: CCAR-P")
    args = ap.parse_args()
    args.cache.mkdir(parents=True, exist_ok=True)
    if not args.dry_run:  # refuse to spend more than --budget characters
        billed = sum(render(p, None, args.cache.resolve(), None, args.limit, args.album, True) or 0 for p in args.transcripts)
        if billed > args.budget:
            sys.exit(f"would bill {billed} characters, over --budget {args.budget}; rerun with a higher --budget")
    key = None if args.dry_run else api_key()
    total = 0
    for path in args.transcripts:
        out = args.out or path.resolve().parent.parent / "audio"
        out.mkdir(parents=True, exist_ok=True)
        total += render(path, out.resolve(), args.cache.resolve(), key, args.limit, args.album, args.dry_run) or 0
    if args.dry_run:
        print(f"total chars to bill={total}")


if __name__ == "__main__":
    main()
