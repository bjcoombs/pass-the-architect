#!/usr/bin/env python3
"""Render ALEX/SAM transcripts to MP3 with the ElevenLabs text-to-speech API.

Usage: uv run --with requests tools/render.py [--limit N] [--dry-run] [--out DIR] transcript.md...

Each speaker turn becomes one TTS request, cached by a hash of the request
including the neighbouring turns, so reruns cost nothing. A turn whose own text
is unchanged reuses its clip even when a neighbour was edited, so an edit pays
only for the edited turn. --dry-run reports the characters a render would bill. Turns are joined with short gaps. A "## Title" line in the body starts an
MP3 chapter at the next turn; chapters are also written to <stem>.chapters.json
in Podcasting 2.0 format for the RSS feed.
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
import subprocess
import sys

import requests

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
            turns.append({"speaker": speaker, "text": speech, "pause": pause, "sting": sting, "chapter": chapter})
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


def chapter_files(meta, playlist, marks, stem, cache, out_dir):
    """Turn (playlist index, title) marks into an ffmetadata file and a chapters JSON."""
    starts, t = [], 0.0
    for i, entry in enumerate(playlist):
        starts.append(t)
        t += duration(entry)
    total = t
    chapters = [(0.0 if n == 0 else starts[i], title) for n, (i, title) in enumerate(marks)]
    ffmeta = [";FFMETADATA1"]
    for n, (start, title) in enumerate(chapters):
        end = chapters[n + 1][0] if n + 1 < len(chapters) else total
        ffmeta += ["[CHAPTER]", "TIMEBASE=1/1000", f"START={int(start * 1000)}", f"END={int(end * 1000)}",
                   "title=" + re.sub(r"([=;#\\\n])", r"\\\1", title)]
    meta_path = cache / f"{stem}.ffmeta"
    meta_path.write_text("\n".join(ffmeta) + "\n")
    (out_dir / f"{stem}.chapters.json").write_text(json.dumps(
        {"version": "1.2.0", "title": meta.get("title", stem),
         "chapters": [{"startTime": round(s, 2), "title": title} for s, title in chapters]}, indent=2) + "\n")
    return meta_path, len(chapters)


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
    marks = []  # (index into entries, chapter title)
    for t, clip in zip(turns, clips):
        if t["chapter"]:
            marks.append((len(entries), t["chapter"]))
        entries += [clip, pause if t["pause"] else gap]
        if t["sting"] and sting.exists():
            entries += [sting, beat]
    if outro.exists():
        entries += [beat, outro]
    playlist = cache / f"{path.stem}.txt"
    playlist.write_text("".join(f"file '{e}'\n" for e in entries))
    suffix = "-sample" if limit else ""
    out = out_dir / f"{path.stem}{suffix}.mp3"
    chapter_args, n_chapters = [], 0
    if marks and not limit:
        meta_path, n_chapters = chapter_files(meta, entries, marks, path.stem, cache, out_dir)
        chapter_args = ["-f", "ffmetadata", "-i", str(meta_path), "-map", "0:a", "-map_chapters", "1"]
    subprocess.run(
        ["ffmpeg", "-y", "-loglevel", "error", "-f", "concat", "-safe", "0", "-i", str(playlist), *chapter_args,
         "-af", "aresample=44100", "-ac", "1", "-b:a", "128k",  # resample: mixed TTS/music frames break lame otherwise
         "-metadata", f"title={episode_label(meta.get('episode', ''))} {meta.get('title', path.stem)}",
         "-metadata", f"album={album}",
         "-metadata", "artist=Pass the Architect",
         "-metadata", f"track={meta.get('episode', '')}",
         "-metadata", "genre=Podcast",
         str(out)],
        check=True,
    )
    chars = sum(len(t["text"]) for t in turns)
    print(f"{out}  turns={len(turns)} chars={chars} chapters={n_chapters}")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("transcripts", nargs="+", type=pathlib.Path)
    ap.add_argument("--out", type=pathlib.Path, help="default: audio/ beside the transcripts folder")
    ap.add_argument("--cache", type=pathlib.Path, default=MUSIC.parent / ".tts-cache")
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
