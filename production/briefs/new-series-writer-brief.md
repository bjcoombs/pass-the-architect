# Writer brief: a new Foundations series

You are writing one or more complete episodes of a two-host exam-prep podcast. The episodes are rendered to speech later with ElevenLabs, so every character you write will be spoken and billed: write for the ear, and only what earns its airtime. Paths are relative to `production/`.

## Read first, in this order

1. `SERIES.md`: the base bible. Hosts, episode structure, learning-design rules, accuracy rules and the transcript format all apply.
2. The series bible you are writing for (`DEVELOPER-FOUNDATIONS.md` or `ASSOCIATE-FOUNDATIONS.md`). It overrides `SERIES.md` where they differ, and its episode table gives your slug, title, skills, minutes and word target.
3. The official exam guide text named in that bible, in full. Section 6 is what items are written against; teach every element it names for your episode's skills.
4. `briefs/pushback-brief.md` and `briefs/intro-outro-brief.md`. Apply both in the first draft. Ignore their references to a specific listener's score report; these series are for a first attempt.
5. Two finished episodes as models of tone, pacing and structure: `foundations/transcripts/F04-claude-code-config.md` and `transcripts/07-stakeholders.md`. Their cards files, `cards/F04-claude-code-config.json` and `cards/07-stakeholders.json`, show the cards format.

## What to produce for each episode

1. **The transcript** at the path the bible gives, with YAML front matter (`episode`, `series`, `slug`, `title`, `description`, `domain`, `weight`, `target_minutes`). Body rules:
   - only `ALEX:` and `SAM:` turns, one per line, blank line between;
   - `## ` chapter headings before the first turn and after every `[sting]`;
   - `[pause]` ends every drill question line, `[sting]` ends a segment's closing line;
   - numbers spelled out, acronyms as spoken ("M C P", "A P I", "Haiku", "rag"), hyphens never em dashes;
   - the opening turn says the episode number as its position, "This is episode four", matching the ID.
2. **The cards file** at `cards/<transcript stem>.json`:
   - `drills`: every pause-and-answer item and the cold open, in order. Use the `mcq` form for items with lettered options (`question_line` and `answer_line` are exact prefixes of one turn each; `correct` has as many letters as `choose`). Put the cold open's `answer_line` on the turn in the verdict segment where the correct letter is first stated. For a dropdown item, use the `recall` form with `prompt` giving the statements and `answer` giving the right choice for each.
   - `segments`: every `## ` heading mapped to 3 to 6 short bullets for the chapter artwork. "Five to remember" gets exactly five; the recap gets up to eight "X → Y" tells. No bullet names a drill's correct option before the drill is answered, including the cold open, which is answered late.
3. **Self-check**, free of charge: run `uv run --with requests --with mutagen --with pillow tools/render.py --dry-run <transcript>` from `production/`. It validates the cards file against the transcript and reports the characters a render would bill. Fix every error it prints. Do not run without `--dry-run`: real renders spend credits and are not yours to start.

## Accuracy

- Every product claim must trace to the exam guide or to documentation you fetched (platform.claude.com, code.claude.com, support.claude.com, modelcontextprotocol.io) or to `~/dev/github.com/forgd-ai/claude-kb/claude-kb-main/`. If you cannot confirm a parameter, flag, limit, price or feature name, describe it in words or leave it out.
- Teach the July 2026 guide's framing. Build no item on a feature released after July 2026.
- Drills are original. Discuss the guide's three sample items in the game-plan episode only.
- Prefer the exam's answer style named in the bible: the purpose-built mechanism that meets the stated constraint, over "faster", "bigger", a polite instruction, or pasting data in.

## Report back

For each episode: the files written, the dry-run line (characters and chapters), the word count, and any claim you could not verify and therefore left out or softened. Keep the report under 200 words per episode. Do not commit, push or open pull requests.
