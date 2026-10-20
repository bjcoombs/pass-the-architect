# Pass the Architect - CCAR-F retake series bible

A companion series for resitting Claude Certified Architect - Foundations (exam code CCAR-F) after the 25 September 2026 attempt (661 against a pass mark of 720, about four or five answers short). Hosts, transcript format, learning-design rules and accuracy rules are those in `SERIES.md` (same folder); this file overrides only what differs.

## Exam facts (official exam guide, v1.0, July 2026)

- 60 items, 120 minutes, scaled pass mark 720 on 100-1,000, percent correct by domain on the score report.
- Multiple-choice AND multiple-response items; each item states how many to select.
- Four scenarios drawn at random from six. Each scenario frames a set of items:
  1. Customer Support Resolution Agent (Agent SDK, MCP tools get_customer, lookup_order, process_refund, escalate_to_human; 80%+ first-contact resolution while knowing when to escalate).
  2. Code Generation with Claude Code (slash commands, CLAUDE.md, plan mode vs direct execution).
  3. Multi-Agent Research System (coordinator with search, document analysis, synthesis and report subagents; cited reports).
  4. Developer Productivity with Claude (Agent SDK, built-in tools Read, Write, Bash, Grep, Glob, MCP servers).
  5. Claude Code for Continuous Integration (automated review, test generation, actionable feedback, minimal false positives).
  6. Structured Data Extraction (JSON schemas, validation, edge cases, downstream integration).
- Domain weights: Agentic Architecture & Orchestration 27%, Tool Design & MCP Integration 18%, Claude Code Configuration & Workflows 20%, Prompt Engineering & Structured Output 20%, Context Management & Reliability 15%.
- The guide lists 30 task statements (1.1-1.7, 2.1-2.5, 3.1-3.6, 4.1-4.6, 5.1-5.6), each with "knowledge of" and "skills in" bullets, including named anti-patterns. Items are written against those bullets. Teach every bullet in an episode's task statements.

## What differs from the CCAR-P series

- Every drill is set inside one of the six named scenarios, and says which one.
- The previous attempt lost marks on applied configuration and API mechanics tested as scenarios. Teach through symptoms ("formatting keeps drifting, what do you change?"), never recall.
- Pushback is built in from the start: five to seven exchanges per episode where ALEX argues a strong practitioner case for a distractor, SAM concedes what is right about it, explains why the exam's answer differs from the guide's own wording, and ends on the tell (the word or pattern in the item that points to the exam's answer). At least once per episode ALEX argues a wrong option after the pause and SAM names the miss pattern. Sometimes SAM pushes back when ALEX over-applies a rule.
- At least one multiple-response ("choose two") drill per episode.
- The guide's anti-patterns are gold: wherever a task statement names one ("parsing natural language signals to determine loop termination", "arbitrary iteration caps as the primary stopping mechanism"), turn it into a distractor.

## Episodes

Reused unchanged from the CCAR-P series: 10 Your Five Miss Patterns, 11 Closing the Foundations Gaps. New episodes must not repeat episode 11's drills.

| # | Slug | Title | Task statements | Min | Words |
|---|------|-------|-----------------|-----|-------|
| F00 | game-plan | Foundations game plan | Format, scenarios, sample questions | 12 | 1,700-2,000 |
| F01 | agentic-loop | The agentic loop and enforced workflows | 1.1, 1.4, 5.3 | 22 | 3,100-3,600 |
| F02 | coordinators | Coordinators, subagents and decomposition | 1.2, 1.3, 1.6 | 22 | 3,100-3,600 |
| F03 | hooks-sessions | Hooks, sessions and escalation | 1.5, 1.7, 5.2 | 20 | 2,900-3,400 |
| F04 | claude-code-config | Claude Code configuration | 3.1, 3.2, 3.3, 2.4 | 22 | 3,100-3,600 |
| F05 | claude-code-workflows | Plan mode, refinement and CI | 3.4, 3.5, 3.6 | 20 | 2,900-3,400 |
| F06 | structured-output | Prompts and structured output | 4.1, 4.2, 4.3, 4.4, 4.5, 4.6 | 24 | 3,400-3,900 |
| F07 | tools-mcp | Tool design and built-in tools | 2.1, 2.2, 2.3, 2.5 | 20 | 2,900-3,400 |
| F08 | context-reliability | Context, review and provenance | 5.1, 5.4, 5.5, 5.6 | 20 | 2,900-3,400 |
| F09 | scenarios | The six scenarios | All, per scenario | 22 | 3,100-3,600 |
| F10 | final-drill | Foundations final drill | All | 20 | 2,700-3,100 |

Listening order: F00, 10, F04, F05, F06, F01, F02, F03, F07, F08, 11, F09, then F10 the night before and F11 (exam day) the morning of the exam. Published files are numbered 00 to 12 by that position, and the hosts say the position aloud ("This is episode two" for F04); `tools/renumber_retake.py` made the spoken numbers match. File IDs such as F04 stay in the repository only.

## Sources (paths relative to `~/dev/github.com/forgd-ai/`, private forgd repositories)

- Official exam guide text: the official exam guide PDF converted with pdftotext (`f-guide.txt`, not committed: Anthropic's document). Authoritative for task statements, scenarios, sample questions (section 9) and preparation exercises (section 8). Sample questions may be discussed in F00 only; all other drills are original.
- Listener profile (gap table, miss patterns, exam interface): `~/.cache/pass-the-architect/listener-profile.md`, kept outside the repository (structure in `listener-profile.template.md`).
- `cca-f-study-pack/cca-f-study-pack-main/`: exam domains, technical and blind-spot guides, anti-patterns, scenario coverage map.
- `ccf-a-exam-app/ccf-a-exam-app-main/app/questions.json`: 186 domain-tagged questions with explanations, for scenario shapes.
- `cca-f-study-examples/cca-f-study-examples-main/`: runnable examples per topic.
- `claude-kb/claude-kb-main/`: verify every flag, file name, hook event, settings scope and API value before it goes into a script; describe in words anything unverified. Where current product behaviour differs from the July 2026 guide, teach the guide's answer and do not mention the newer behaviour.

## Transcript location

`podcast/foundations/transcripts/F<NN>-<slug>.md`, front matter as in `SERIES.md` with `episode: "F01"` and `series: "CCAR-F retake"`.

## Budget

About 200,000 characters across eleven new episodes, about 44,000 ElevenLabs credits at the measured Turbo v2.5 rate; about 82,000 remain this month.
