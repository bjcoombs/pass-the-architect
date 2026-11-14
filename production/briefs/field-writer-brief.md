# Writer brief: Know the Field

You are writing one complete episode of a two-host podcast about the companies Claude competes with. The episode is rendered to speech later with ElevenLabs, so every character you write will be spoken and billed: write for the ear, and only what earns its airtime. Paths are relative to `production/`.

## Read first, in this order

1. `SERIES.md`: the base bible. Transcript format and accuracy discipline apply. Its exam facts and episode list do not.
2. `KNOW-THE-FIELD.md`: the series bible. It overrides `SERIES.md`. Its episode table gives your slug, title, scope, minutes and word target.
3. The research sheets in `field/research/` named for your episode below, in full, then skim the others for cross-references.
4. `briefs/pushback-brief.md` and `briefs/intro-outro-brief.md` for the pushback and three-pass shapes. Ignore their exam-specific references; this series has no exam.
5. One finished episode as a model of tone, pacing and format: `developer/transcripts/D06-agents.md`, with its cards file `cards/D06-agents.json`.

## Shared vocabulary across the series

Every episode uses the same six layers, introduced in K00, by these names: **the model**, **the developer platform**, **the agent stack**, **the coding agent**, **the enterprise wrapper** (the chat product, admin, compliance and data controls), and **the route to market** (direct, a cloud marketplace, a bundle such as Microsoft 365). Refer back to them by name. Episodes after K00 may assume the listener has heard K00.

Anthropic's current line-up, for reference when comparing: Claude Fable 5.2, Opus 5.5, Sonnet 5.5 and Haiku 5.5, with Mythos 5.2 on restricted access. Check `field/research/field.md` section 0 before naming any of them.

## Fairness rules

- Every competitor gets at least two things it does better than Claude today, stated plainly and backed by the research.
- Every claim that Claude is ahead names the evidence (an independent benchmark, a feature the competitor lacks, a documented limit) and its source type. Vendor-reported numbers are called vendor-reported. The Menlo Ventures market report is named with the fact that Menlo is an Anthropic investor.
- Drills reward fitting the customer's stated constraint. In at least one drill per episode the right answer is a competitor's product or a Claude purchase through a competitor's cloud.
- No sneering, no "they're just copying us". Convergence between products is stated as convergence.

## Accuracy

- Use High-confidence facts from the research sheets plainly. Hedge Moderate ones ("reportedly", "according to"). Leave Low ones out, unless the point is that a claim is unverified.
- Follow the bible's rule on fast-moving facts: K00 to K07 avoid prices, benchmark scores and version-specific lists unless the argument needs one, and then say "as of November twenty twenty-six" once. K08 holds the numbers.
- Do not invent product names, features, prices, dates or limits. If it is not in the research or in documentation you fetched and checked, leave it out.
- Drills are original customer scenarios with four options (five for choose-two), plus at least one per-statement true or false item.

## What to produce

1. **The transcript** at `field/transcripts/K<NN>-<slug>.md`, with front matter:
   ```
   ---
   episode: "K01"
   series: "FIELD"
   slug: openai
   title: "OpenAI"
   description: "One or two sentences for the RSS feed."
   domain: "OpenAI"
   weight: ""
   target_minutes: 22
   ---
   ```
   Body rules, as in `SERIES.md`: only `ALEX:` and `SAM:` turns, one per line, blank line between; `## ` chapter headings before the first turn and after every `[sting]`; `[pause]` ends every drill question line; `[sting]` ends a segment's closing line; numbers spelled out; names as spoken ("G P T six Astra", "Gemini four Carbon", "M C P", "A to A", "A P I", "rag"); hyphens, never em dashes. The opening turn welcomes the listener to "Know the Field, from Pass the Architect" and says the episode number as spoken ("This is episode four" for K04, "episode zero" for K00).
2. **The cards file** at `cards/K<NN>-<slug>.json`, in the format of `cards/D06-agents.json`: `drills` for every pause-and-answer item and the cold open (`mcq` with `question_line` and `answer_line` as exact prefixes of one turn each; `recall` for per-statement items), and `segments` mapping every `## ` heading to 3 to 6 short bullets. "Five to remember" gets exactly five; the recap gets up to eight "X → Y" tells. No bullet names a drill's answer before the drill is answered.
3. **Self-check**, free: from `production/`, run `uv run --with requests --with mutagen --with pillow tools/render.py --dry-run field/transcripts/<file>`. Fix every error it prints. Never run it without `--dry-run`: real renders spend credits.

## Report back

Under 200 words: the files written, the dry-run line (characters and chapters), the word count, and any claim you softened or dropped because the research did not support it. Do not commit, push or open pull requests. Touch no file other than your transcript and cards file.
