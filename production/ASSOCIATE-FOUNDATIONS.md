# Pass the Architect - CCAO-F series bible

A two-host study series for Claude Certified Associate - Foundations (exam code CCAO-F), written for a first attempt. Hosts, transcript format, learning-design rules and accuracy rules are those in `SERIES.md` (same folder); this file overrides only what differs.

## Exam facts (official exam guide, v1.0, July 2026)

- 60 items in 120 minutes. Multiple-choice and multiple-response items; each item states how many to select.
- Scaled pass mark 720 on 100-1,000; the score report shows percent correct by domain, but only the total decides the result.
- The candidate uses Claude as a productivity tool in business roles (operations, consulting, sales, delivery) to complete tasks with minimal guidance, spots where Claude can improve a process, balances quality, efficiency and cost, recognises limits, and escalates technical work to Architects and Developers.
- Domain weights and objectives:

| # | Domain | Weight | Objectives |
|---|--------|--------|------------|
| 1 | Prompting and Task Execution | 14% | Effective prompts for business and technical tasks; task decomposition; iterating prompts; adapting strategy to task type (analysis, research, drafting, brainstorming) |
| 2 | Output Evaluation and Validation | 21% | Accuracy and completeness; hallucinations, inconsistencies and bias; fact-checking and validation; when human review is required; editing and comparing outputs for an audience; choosing formats (artifacts, inline, structured data) |
| 3 | Product and Model Selection | 12% | Product features (Projects, research mode, chat, artifacts); Haiku, Sonnet, Opus; matching model to cost, speed, quality; context limits and memory (restart, summarise, persist) |
| 4 | Workflow Integration and Solution Design | 16% | Analysing requirements and use cases; research, planning and process optimisation; supporting design and iteration; augmenting or redesigning workflows; communicating value and limits to stakeholders |
| 5 | Configuration and Knowledge Management | 12% | Projects with instructions and knowledge; uploaded knowledge and connectors (Google Drive, Gmail); system-level instructions; maintaining configurations |
| 6 | Governance, Risk, and Responsible Use | 15% | Appropriate and inappropriate use cases; data sensitivity, regulation and privacy; organisational AI policy; ethics |
| 7 | Troubleshooting and Optimization | 10% | Diagnosing underperforming prompts and poor outputs; adjusting to feedback; optimising workflows |

- Three official sample items (section 8): verify a confident citation against the source before it goes to compliance; a faster, cheaper model for high-volume simple drafts; anonymise regulated identifiers before upload. The house style: the answer is the diligent, proportionate step; distractors trust the model's confidence, overspend, ask the model to promise something a control should do, or abandon the task.

## Exam interface (Pearson VUE, from the listener's Architect sittings)

- The clock counts down in hours and minutes. Pace at about one minute fifty an item with a ten-minute flag reserve: item 20 at one hour twenty-three left, item 40 at forty-seven minutes left, item 60 at ten minutes left.
- Some items list four or five statements, each with its own dropdown of two or three choices. No option is a throwaway; each statement is its own small judgement.
- Items do not show their domain.

## Hosts for this series

ALEX is a capable operations or delivery professional who uses Claude every day in claude.ai and is sitting this exam for the first time. Practical, quick, sometimes too trusting of a fluent answer or too keen to paste everything in. SAM knows how the exam is written. Plain business language; no code. Technical terms only where the guide uses them (Projects, connectors, artifacts, model names). No retake storyline.

## Episode structure

As in `SERIES.md`, with the pushback exchanges (`briefs/pushback-brief.md`) and the three-pass shape (`briefs/intro-outro-brief.md`) built in from the first draft. At least four drills per core episode, at least one choose-two and at least one per-statement dropdown item. Drills are workplace scenarios: a finance analyst, an HR partner, a sales lead, a consultant preparing a client deck. Every drill is original; the three official samples may be discussed in A00 only. `## ` chapter headings before the first turn and after every `[sting]`.

## Episodes

| # | Slug | Title | Domain | Min | Words |
|---|------|-------|--------|-----|-------|
| A00 | game-plan | Associate game plan | Format, weights, method, the three sample items | 12 | 1,700-2,000 |
| A01 | prompting | Prompting and task execution | D1 14% | 18 | 2,500-2,900 |
| A02 | output-validation | Checking what Claude gives you | D2 21% | 22 | 3,100-3,500 |
| A03 | products-models | Choosing the product and the model | D3 12% | 16 | 2,200-2,600 |
| A04 | workflows | Bringing Claude into a workflow | D4 16% | 18 | 2,500-2,900 |
| A05 | projects-knowledge | Projects, knowledge and connectors | D5 12% | 16 | 2,200-2,600 |
| A06 | responsible-use | Governance, risk and responsible use | D6 15% | 18 | 2,500-2,900 |
| A07 | troubleshooting | Troubleshooting and optimisation | D7 10% | 14 | 1,900-2,300 |
| A08 | final-drill | Associate final drill | All, weighted by the blueprint | 18 | 2,500-2,900 |
| A09 | exam-day | Exam day | Logistics, noteboard, countdown pacing | 6 | 800-1,000 |

Listening order is A00 to A09; the spoken number matches the ID. A08 is for the night before; A09 for the morning.

## Sources

- Exam guide text: `~/.cache/pass-the-architect/guides/associate.txt` (not committed, because it is Anthropic's document).
- Official help and documentation, fetched as needed: support.claude.com (Projects, artifacts, research, memory, connectors, file uploads, usage limits, data and privacy), claude.com product pages, and platform.claude.com/docs for model comparisons and prompt engineering.
- `~/dev/github.com/forgd-ai/claude-kb/claude-kb-main/` for checking product claims.
- The free prep course on Anthropic Partner Academy is behind a sign-in and has not been captured. Keep claims to what the guide and the help centre state. Product features change often: describe a feature only as the help centre documents it, and build no item on a feature released after July 2026.

## Transcript location

`production/associate/transcripts/A<NN>-<slug>.md`, front matter as in `SERIES.md` with `episode: "A01"` and `series: "CCAO-F"`. Cards in `production/cards/A<NN>-<slug>.json`.

## Budget

About 140,000 characters across ten episodes, about 28,000 ElevenLabs credits. Render after the credit reset on 18 November 2026.
