# Making an exam-prep podcast series

This is how the two Pass the Architect series were made, written so the same process can produce a series for another exam. Paths are relative to `production/`.

## What the series is for

Each series is built for one listener sitting one exam on a fixed date. Every episode exists to raise the chance of answering items correctly, so the series follows the exam guide's blueprint and answer style rather than the product as it is today. Where current product behaviour differs from the guide, teach the guide's answer.

## Inputs

| Input | Why | Where it goes |
|---|---|---|
| Official exam guide (PDF) | Domains, weights, task statements and sample items. Together they show what the answer key rewards. | Convert with `pdftotext -layout` and keep the text local, because it is the vendor's document. |
| Prep course material | Written against the same blueprint as the exam items; the primary source for facts | Cited by path in the series bible |
| Listener profile | Score-report gaps and miss patterns, used to personalise drills and pushback | `~/.cache/pass-the-architect/listener-profile.md`, kept outside the repository; its structure is in `listener-profile.template.md` |
| A grounding knowledge base | Used to check every flag, file name and API value before it is spoken | Cited in the bible |

## Steps

1. **Write the series bible.** `SERIES.md` is the model; `FOUNDATIONS-RETAKE.md` is a variant that overrides only what differs. The bible fixes:
   - exam facts;
   - the episode list with domains, weights and word targets (about 140 spoken words a minute);
   - the two hosts and the episode structure;
   - learning-design and accuracy rules;
   - sources and the transcript format.

   Airtime follows domain weight.
2. **Fan out the writing.** One agent writes each episode. It gets the bible, its row in the episode list, and the sources for its domain. Episode 00 (game plan) and the final drill each get their own brief.
3. **Review pass.** A second set of agents checks every drill's answer key against the guide, removes claims the sources do not support, and checks the format rules. Fix problems before any audio is made, because audio changes cost credits and text changes do not.
4. **Pushback pass** (`briefs/pushback-brief.md`). Add five to seven exchanges per episode. In each, the candidate host argues a strong practitioner case for a distractor, and the expert ends on the tell: the word in the question that points to the exam's answer.
5. **Three passes over each topic** (`briefs/intro-outro-brief.md`). Each topic is covered three times:
   - an opening preview of what the listener will be able to do;
   - the body;
   - a retrieval prompt, then a recap framed as exam tells.
6. **Chapters.** Put a `## Title` line before the first turn and after each `[sting]`. Headings are never spoken, so they can be changed at any time for free.
   **Question and answer cards.** For each episode, `cards/<transcript stem>.json` lists every drill: the transcript line where it is asked, the line where the correct answer is first stated, a short on-screen stem, the options, the correct letters and a one-line reason. `render.py` turns each drill into two chapters. The question chapter's artwork shows the stem and options, so a listener who pauses can answer from the screen. The answer chapter's artwork highlights the correct options. Recall prompts get a prompt card and, where the transcript answers them, an answer card. The same file's `segments` maps each `## ` heading to 3 to 6 on-screen bullets: the intro's outcomes, the teaching points, the five to remember, and the recap's tells. Bullets never name a drill's correct option before it is asked and answered. Agents extracted the files from the finished transcripts; the renderer fails if a line prefix does not match exactly one turn.
7. **Render** with `tools/render.py`, then **publish** with `tools/publish.py`.

The learning design in short:
- the listener tries to answer before being told;
- every concept comes with a named distractor;
- episodes interleave material from other domains;
- every principle gets one concrete enterprise example;
- every topic is framed three ways.

## Transcript format

- YAML front matter: `episode`, `slug`, `title`, `description`, `domain`, `weight`, `target_minutes`.
- One `ALEX:` or `SAM:` turn per line, with a blank line between turns.
- `## ` chapter headings.
- `[pause]` at the end of drill questions; `[sting]` at the end of lines that close a segment.
- Numbers spelled out, acronyms written as spoken ("M C P"), and hyphens rather than em dashes.

The full rules are in `SERIES.md`.

## Audio

- **Model and voices:** ElevenLabs `eleven_turbo_v2_5`, with George for ALEX and Alice for SAM, both British.
- **Cost:** about 0.2 credits per character in practice, so a 20-minute episode of about 20,000 characters costs about 4,000 credits.
- **Caching:** each turn is one request, sent with the neighbouring turns as context. Results are cached in `~/.cache/pass-the-architect/tts-cache/`, outside the repository so it survives worktree cleanup. A rerender reuses the cache, so editing a turn pays only for that turn.
- **Spend cap:** `tools/render.py --dry-run` prints the characters a render would bill. A real render refuses to bill more than `--budget` characters (default 0), so every spend has to be asked for.
- **Pronunciation:** mispronounced words are fixed in `PRONUNCIATIONS` in `render.py`, as respellings used only for speech, such as "re-tries" and "ee-vals". The transcripts keep the real spelling. Test a fix on a short sample, run it back through speech-to-text, and only then rerender whole episodes.
- **Music:** the intro, sting and outro were generated once with ElevenLabs music and sound effects. They are normalised to -24 LUFS mono (`music/*-norm.mp3`) so they sit under speech, which is about -23 LUFS.
- **Chapters:** each MP3 carries ID3 chapters (CHAP frames, each with a title and a JPEG card, written with mutagen; `tools/cards.py` draws the cards). `<episode>.chapters.json` (Podcasting 2.0 format) and the card images are written beside it for the feed. Retag with mutagen, never ffmpeg: `-map_metadata -1` drops chapter titles and ffmpeg cannot write chapter images.

## Publishing

`tools/publish.py` holds the listening order for each series. It numbers files from 00 by position, and the hosts say that number aloud, so changing the order means changing the spoken lines too. `tools/renumber_retake.py` is a worked example.

```
uv run --with requests --with mutagen --with pillow tools/render.py --budget 0 transcripts/*.md
uv run --with requests --with mutagen --with pillow tools/render.py --budget 0 --album "..." foundations/transcripts/*.md
uv run --with mutagen tools/publish.py --icloud --github --site ../docs
```

Then commit `docs/` and push.

- **`--icloud`** copies each series to iCloud Drive as `NN - Title.mp3` and moves stale files to the Trash.
- **GUIDs** include a hash of the file, so podcast apps download an episode again when it changes.
- **`--github`** uploads the MP3s as release assets, one release per series, so the git history stays small. It also writes the feeds, chapter JSON, covers, OPML and index page into `docs/`, which GitHub Pages serves.
- **Keeping it unlisted:** the feeds carry `itunes:block` and the site carries `noindex`. Subscribe by URL and never submit a feed to a directory.

## Adapting to another exam

1. Copy `production/` with an empty `transcripts/`. Write a new bible from the new guide, and a listener profile.
2. Add the series to `SERIES` in `tools/publish.py`: slug, title, iCloud folder, colour, label and listening order.
3. Follow steps 2 to 7 above. Before writing anything, estimate the credits from the word targets: total characters times 0.2.
