# Pass the Architect - CCDV-F series bible

A two-host study series for Claude Certified Developer - Foundations (exam code CCDV-F), written for a first attempt. Hosts, transcript format, learning-design rules and accuracy rules are those in `SERIES.md` (same folder); this file overrides only what differs.

## Exam facts (official exam guide, v1.0, July 2026)

- 53 items in 120 minutes. Multiple-choice and multiple-response items; each item states how many to select.
- Scaled pass mark 720 on 100-1,000; the score report shows percent correct by domain, but only the total decides the result.
- The candidate is a hands-on engineer with one to five years of software experience and six months with Claude or a comparable LLM, fluent in Python or TypeScript, REST and CLIs.
- Domain weights, with each skill's share of the whole exam:

| # | Domain | Weight | Skills (share of exam) |
|---|--------|--------|------------------------|
| 1 | Agents and Workflows | 14.7% | Agent architecture 4.5; agent construction with Claude 5.3; agent patterns and frameworks 4.9 |
| 2 | Applications and Integration | 33.1% | Understanding requirements 3.4; systems life cycle 2.8; Claude API mechanics 6.8; software engineering foundations 7.4; Claude application design 8.6; configuration management 4.1 |
| 3 | Claude Code | 3.1% | Claude Code operation 3.1 |
| 4 | Eval, Testing, and Debugging | 2.6% | Debugging and error handling 2.6 |
| 5 | Model Selection and Optimization | 16.8% | LLM fundamentals 5.2; technical fundamentals 6.1; model selection and trade-offs 2.7; cost and token management 2.8 |
| 6 | Prompt and Context Engineering | 11.0% | Context engineering 3.8; prompt engineering 4.6; output handling 2.6 |
| 7 | Security and Safety | 8.1% | AI application security 3.2; guardrails and safe deployment 2.3; Claude hooks 1.0; identity, secrets and key management 1.6 |
| 8 | Tools and MCPs | 10.6% | Tool implementation 4.4; MCP server development 2.1; agentic customization 4.1 |

- The skill descriptions in section 6 of the guide are what items are written against. Teach every named element of each skill in its episode.
- Three official sample items (section 8): batch for an overnight, cost-first job; untrusted web content kept apart from instructions with guardrails or hooks; an MCP server for a capability shared by several applications. They show the house style: the answer matches the stated constraint with the purpose-built mechanism, and the distractors are "faster or bigger", a polite instruction instead of a control, and pasting data instead of giving access.

## Exam interface (Pearson VUE, from the listener's Architect sittings)

- The clock counts down in hours and minutes. Pace at about two minutes four seconds an item with a ten-minute flag reserve: item 18 at one hour twenty-three left, item 35 at forty-seven minutes left, item 53 at ten minutes left.
- Some items list four or five statements, each with its own dropdown of two or three choices. No option is a throwaway; each statement is its own small judgement.
- Items do not show their domain. Drills must not lean on a domain label to cue the answer.

## Hosts for this series

ALEX is a capable engineer who has shipped with the Claude API and Claude Code and is sitting this exam for the first time. Competent, a little rusty on the exact mechanics, quick to argue for what worked on the last project. SAM knows how the exam is written. No retake storyline: this is first-attempt preparation.

## Episode structure

As in `SERIES.md` (preview, cold open, why this matters, core segments, pause-and-answer drills, cold open resolved, five to remember, retrieval prompt, recap as exam tells), with these rules built in from the first draft rather than added in later passes:
- Five to seven pushback exchanges per episode, as in `briefs/pushback-brief.md`: ALEX argues a strong practitioner case for a distractor, SAM concedes what is right, explains why the exam's answer differs, and ends on the tell.
- The three-pass shape in `briefs/intro-outro-brief.md`: preview, body, then retrieval prompt and a recap framed as exam tells.
- At least four drills per core episode, at least one choose-two, and at least one per-statement dropdown item read aloud as "For each statement, say true or false" or the three-way equivalent.
- Every drill is original. The three official sample items may be discussed in D00 only.
- `## ` chapter headings before the first turn and after every `[sting]`.

## Episodes

| # | Slug | Title | Skills | Min | Words |
|---|------|-------|--------|-----|-------|
| D00 | game-plan | Developer game plan | Format, weights, method, the three sample items | 12 | 1,700-2,000 |
| D01 | api-mechanics | The Claude API: messages, streaming, thinking, caching and batch | 2: Claude API mechanics; 5: cost and token management | 22 | 3,100-3,500 |
| D02 | engineering-foundations | Software engineering for Claude applications | 2: software engineering foundations; 5: technical fundamentals | 22 | 3,100-3,500 |
| D03 | application-design | Designing Claude applications | 2: Claude application design, understanding requirements, systems life cycle | 22 | 3,100-3,500 |
| D04 | configuration-claude-code | Configuration and Claude Code | 2: configuration management; 3: Claude Code operation | 16 | 2,200-2,600 |
| D05 | models | LLM fundamentals and choosing a model | 5: LLM fundamentals, model selection and trade-offs | 18 | 2,500-2,900 |
| D06 | agents | Agents and workflows | 1: all three skills | 20 | 2,800-3,200 |
| D07 | prompt-context | Prompts, context and output handling | 6: all three skills | 18 | 2,500-2,900 |
| D08 | tools-mcp | Tools, MCP servers and choosing a customization | 8: all three skills | 18 | 2,500-2,900 |
| D09 | security-debugging | Security, hooks, secrets and debugging | 7: all four skills; 4: debugging and error handling | 18 | 2,500-2,900 |
| D10 | final-drill | Developer final drill | All, weighted by the blueprint | 18 | 2,500-2,900 |
| D11 | exam-day | Exam day | Logistics, noteboard, countdown pacing | 6 | 800-1,000 |

Listening order is D00 to D11. Files are numbered by position, so the spoken number matches the ID ("This is episode four" for D04). D10 is for the night before; D11 for the morning.

## Sources

- Exam guide text: `~/.cache/pass-the-architect/guides/developer.txt` (pdftotext of the official PDF; not committed, because it is Anthropic's document). Authoritative for skills, weights and sample items.
- Official documentation, fetched as needed: platform.claude.com/docs (API, models, prompt engineering, tool use, caching, batch, streaming, thinking, structured outputs, guardrails), code.claude.com/docs (Claude Code, hooks, settings, skills, plugins, subagents, Agent SDK), modelcontextprotocol.io (MCP).
- `~/dev/github.com/forgd-ai/claude-kb/claude-kb-main/` and `~/dev/github.com/forgd-ai/factoid_data/factoid_data-main/factoids/`: Anthropic-grounded notes for checking product claims.
- The free prep course on Anthropic Partner Academy is behind a sign-in and has not been captured. Where the course and these sources might differ, teach the exam guide's framing, and keep claims to what the documentation states.
- Where current product behaviour is newer than the July 2026 guide, teach the guide's answer and the stable documented behaviour; do not build an item on a feature released after July 2026.

## Transcript location

`production/developer/transcripts/D<NN>-<slug>.md`, front matter as in `SERIES.md` with `episode: "D01"` and `series: "CCDV-F"`. Cards in `production/cards/D<NN>-<slug>.json`.

## Budget

About 195,000 characters across twelve episodes, about 39,000 ElevenLabs credits at the measured rate. Render after the credit reset on 18 November 2026.
