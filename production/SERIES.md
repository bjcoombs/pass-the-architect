# Pass the Architect - CCAR-P podcast series bible

A two-host audio series built to get one listener through the Claude Certified Architect - Professional exam (exam code CCAR-P). Every episode exists to raise the probability of answering exam items correctly. Anything that does not serve that goal is cut.

## Exam facts that shape the series (from the official exam guide, v1.0, July 2026)

- 63 items in 120 minutes: about one minute fifty per item.
- Multiple-choice AND multiple-response items. Each item states how many responses to select. Multiple-response items are where marks leak: every chosen option must be independently true for the scenario.
- Pass mark: scaled 720 on 100-1,000. Score report shows percent correct per domain.
- The candidate profile is a mid-to-senior architect: business problem to production system, trade-offs across cost, latency, performance, safety and maintainability, and the stakeholder conversations around them.
- Domain weights:

| # | Domain | Weight |
|---|--------|--------|
| 1 | Solution Design & Architecture | 17% |
| 2 | Claude Models, Prompting & Context Engineering | 13% |
| 3 | Integration | 19% |
| 4 | Evaluation, Testing & Optimization | 16% |
| 5 | Governance, Safety & Risk Management | 14% |
| 6 | Stakeholder Communication & Lifecycle Management | 14% |
| 7 | Developer Productivity & Operational Enablement | 7% |

- The official sample items show the house style: the right answer removes the risk at its root (remove unneeded tools rather than log them), fixes the stated constraint without discarding something required (prompt caching rather than truncation), and diagnoses the component that the trigger actually touched (retrieval after a document refresh, not model weights). Distractors are detective or compensating controls dressed as fixes, "use a bigger model", blunt cuts that lose required content, and causes unrelated to the trigger.

## Episode list

| # | Slug | Title | Domain | Target | Words |
|---|------|-------|--------|--------|-------|
| 00 | game-plan | The Game Plan: format, multiple-response items, and how to read a question | All | 12 min | 1,700-2,000 |
| 01 | solution-design | Solution Design & Architecture | D1 17% | 20 min | 2,800-3,200 |
| 02 | models-prompting | Models, Prompting & Context Engineering | D2 13% | 18 min | 2,500-2,900 |
| 03 | integration-security | Integration I: protocols, capability bloat, identity and auth, progressive discovery | D3 19% | 20 min | 2,800-3,200 |
| 04 | integration-rag | Integration II: RAG, retrieval strategy, accuracy-latency, observability | D3 19% | 20 min | 2,800-3,200 |
| 05 | evaluation | Evaluation, Testing & Optimization | D4 16% | 20 min | 2,800-3,200 |
| 06 | governance | Governance, Safety & Risk Management | D5 14% | 18 min | 2,500-2,900 |
| 07 | stakeholders | Stakeholder Communication & Lifecycle Management | D6 14% | 18 min | 2,500-2,900 |
| 08 | dev-productivity | Developer Productivity & Operational Enablement | D7 7% | 10 min | 1,400-1,700 |
| 09 | final-drill | The Final Drill: night-before rapid fire | All | 18 min | 2,500-2,900 |
| 10 | miss-patterns | Your Five Miss Patterns | All | 18 min | 2,500-2,900 |
| 11 | foundations-gaps | Closing the Foundations Gaps | Cross-domain | 20 min | 2,800-3,200 |

Episodes 10 and 11 are personalised from the listener's Foundations score report: 10 drills five habits that cost marks, 11 re-teaches the applied configuration and API mechanics that scored zero to fifty percent, as scenarios.

Listening order: 00 to 08, then 10 and 11, then 09 the night before and the morning of the exam. Files are numbered from 00 by position, and the hosts say that number aloud, so 09 The Final Drill is published as eleven and announces itself so.

## Hosts

- **ALEX** - the candidate's stand-in. Experienced engineer, has shipped with Claude, sitting the exam soon. Asks what the listener would ask, commits to answers out loud, and is sometimes wrong in exactly the way the distractors hope. Never a straw man.
- **SAM** - an architect who has delivered Claude systems for enterprise clients and knows how the exam is written. Explains the mechanism, then the trap. Concise. When the exam's preferred answer is narrower than real life, says so and says which to pick.

Plain conversational English. No catchphrases repeated across episodes, no sponsor bits, no "great question".

## Episode structure (every domain episode)

1. **Cold open (30-60 s)** - SAM reads an exam-style scenario item with four options (or five for a "choose two" item). ALEX commits. No answer yet.
2. **Why this matters** - domain weight and the task statements from the blueprint this episode covers, in plain words.
3. **Core segments (3-5)** - one per blueprint task statement or cluster: the mechanism, a concrete enterprise example (financial services, healthcare, retail, public sector, field service), the tempting wrong answer and the specific reason it loses.
4. **Pause-and-answer drills** - at least three, and at least one of them a multiple-response item ("choose two"). SAM says "Pause here and answer before we go on", reads the item, `[pause]`, then answers, ruling every option in or out.
5. **Cold open resolved** - reveal the answer and walk through every option.
6. **Five to remember** - SAM and ALEX trade the five facts most likely to earn marks, phrased so they stick.
7. **Next episode tease** - one line.

Episodes 00 and 09 adapt this; see their briefs.

## Learning design rules

- Retrieval over re-reading: ask before telling.
- Distractor literacy: for every key concept, name the wrong answer that looks right and why it loses. Lean on the families in the sample-item analysis above.
- Interleave: each episode recalls at least one fact from another domain in passing.
- Concrete over abstract: every principle gets a one-sentence enterprise example.
- Mnemonics only where they genuinely compress a list.
- Cover every task statement in the episode's blueprint domain. Weight airtime toward the statements the course treats in depth.

## Accuracy rules

- Ground every technical claim in the sources below. The official prep course captures are the primary source: the exam is written against the same blueprint. Do not invent API parameters, product features, model names, prices or limits. If a detail is not in the sources and you are not certain, leave it out.
- When sources disagree, prefer: exam guide, then prep course capture, then factoids, then `claude-kb`, then Foundations study material.
- Do not name the hypothetical companies in course "Watch Out" stories as real; retell the failure pattern generically.
- Drill items must be original. Never copy a course checkpoint or sample item verbatim; the three official sample items may be discussed in episode 00 only.

## Sources (paths relative to `~/dev/github.com/forgd-ai/`, private forgd repositories)

- Exam guide text: the official exam guide PDF converted with pdftotext (`pro-guide.txt`, not committed: Anthropic's document) (blueprint, task statements, sample items).
- Official prep course captures, one per module, at `factoid_data/factoid_data-main/sources/<slug>/capture.txt`:
  - `cca-pro-m1-platform-solution-design` - D1 and D2 (behaviour properties, platform map, primitives, decomposition, pattern selection, model selection, prompting, context, reference architectures).
  - `cca-pro-m2-enterprise-integration-production` - D3 and D4 (evals, POC to production, cost and reliability, sizing and feasibility, enterprise integration, identity and auth, data handling, observability, RAG).
  - `cca-pro-m3-responsible-ai-safety-risk-for-archit` - D5.
  - `cca-pro-m4-stakeholder-engagement-lifecycle-gtm` - D6.
  - `cca-pro-m5-developer-productivity-enablement` - D7.
- Distilled, verified facts from those captures: `factoid_data/factoid_data-main/factoids/{judgment,tools-product,glossary}/*.md`. Each file names its sources on line 3; find a module's files with `rg -l "<slug>" factoids`. The `judgment` kind is closest to how exam items are written.
- `claude-kb/claude-kb-main/` - Anthropic-grounded knowledge base, for verifying product claims.
- `cca-f-study-pack/cca-f-study-pack-main/` and `ccf-a-exam-app/ccf-a-exam-app-main/app/questions.json` - Foundations material; secondary, useful for agent and tool design detail only.

## Transcript format (ElevenLabs-ready)

One Markdown file per episode at `podcast/transcripts/<NN>-<slug>.md`:

```
---
episode: 1
slug: solution-design
title: "Solution Design & Architecture"
description: "One or two sentences for the RSS feed."
domain: "Solution Design & Architecture"
weight: "17%"
target_minutes: 20
---

ALEX: ...

SAM: ...
```

Rules for the dialogue body:

- Every line starts with `ALEX:` or `SAM:` followed by speech. One speaker turn per line, blank line between turns. Nothing else in the body except `## ` chapter headings: no bullets or stage directions outside the tags below.
- Write for the ear. No code blocks, tables or URLs. Say names as a person would: "a CLAUDE dot md file", "the M C P server", "R A G" or "rag" consistently (use "rag"), "A to A" for agent-to-agent.
- Turns stay short: mostly one to four sentences.
- Tags, handled by `tools/render.py` (never spoken): `[pause]` at the end of every pause-and-answer question line marks a drill (the listener asked for no silence, so `PAUSE_GAP_S` in `render.py` equals the normal turn gap; raise it to leave thinking time); `[sting]` at the end of a line plays the transition sting after it. The intro and outro music are added automatically. No other tags.
- Chapter headings: a `## Title` line in the body starts an MP3 chapter at the next turn. Put one before the first turn and after every `[sting]`. Headings are never spoken, so adding or renaming them costs nothing.
- Every episode opens with a preview of what the listener will be able to do by the end, and closes after "Five to remember" with a retrieval prompt then a recap framed as exam tells: three passes over the same topics, each framed differently.
- Spell out numbers and symbols TTS may misread: "seventeen percent", "seven hundred and twenty", "option B".
- Hyphens, never em dashes.
