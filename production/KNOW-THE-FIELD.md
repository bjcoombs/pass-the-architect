# Know the Field - series bible

A two-host series on the companies Claude competes with: OpenAI, Google, Microsoft, AWS, xAI and the open-weight labs. It is written for an architect who knows Claude well and has to advise enterprise customers who are also looking at the alternatives. There is no exam behind this series. The goal is a straight answer when a customer asks "why Claude and not X?", and knowing when X really is the better choice.

Hosts, transcript format and the accuracy discipline are those in `SERIES.md` (same folder). This file overrides what differs.

## What the listener should be able to do after the series

- Place any vendor's offering on six layers and compare like with like: model, developer platform, agent stack, coding agent, enterprise wrapper, route to market.
- Say where each major competitor is truly stronger than Claude today, and where Claude is, with a checkable reason for each.
- Advise on buying Claude through Bedrock, Vertex AI or Foundry rather than direct, and what that changes.
- Handle the common customer objections without running a competitor down.
- Tell a slow-moving fact (architecture, licence, protocol, business model) from a fast-moving one (price, benchmark rank, model version), and check the fast ones before quoting them.

## Hosts for this series

- **ALEX** knows Claude deeply: the API, Claude Code, the Agent SDK, MCP, skills. ALEX has used the other vendors' tools only lightly and leans towards Claude by habit. ALEX makes the case a loyal Claude user would make, and is sometimes wrong in the way a partisan is wrong.
- **SAM** has delivered on several stacks and sits on the customer's side of the table. SAM gives each competitor fair credit, names where Claude wins with evidence, and says "it depends" only when followed by what it depends on.

Neither host sells. The test for every claim: would it survive a customer who has used the competitor's product?

## Episode structure

Same three-pass shape as `SERIES.md` and `briefs/intro-outro-brief.md`: preview, body, then retrieval prompt and a recap. The recap is framed as conversation tells ("If a customer says X, ask Y") instead of exam tells. Specifically:

1. **Preview** (120-180 words): what the listener will be able to do by the end.
2. **Cold open**: SAM reads a customer scenario with four options, ALEX commits, the answer comes late.
3. **Core segments** (three to five), each covering the six layers that matter for this vendor. For each: what it is, where it is truly strong, where Claude differs, and the question to ask the customer.
4. **Pushback**: five to seven exchanges as in `briefs/pushback-brief.md`, turned round. ALEX defends Claude by reflex, SAM concedes what is right and corrects what is not. At least twice, SAM pushes back the other way when ALEX underrates a competitor.
5. **Pause-and-answer drills**: at least four per core episode, written as customer scenarios ("A retail customer runs on Google Workspace and BigQuery and wants..."). At least one choose-two. At least one per-statement item read aloud as "For each statement, say true or false". Right answers fit the customer's stated constraint, not the most loyal reply.
6. **Five to remember**, retrieval prompt, recap as conversation tells, one-line tease.

## Facts that change fast

Prices, benchmark scores and ranks, context-window sizes, model version numbers, and lists of which models a cloud offers all change month to month.
- In K00 to K07, avoid them where the argument does not depend on them. Where one is needed, say it once with "as of November twenty twenty-six", and teach the reason behind it (pricing structure, not the price).
- K08 holds the numbers. It is the one episode meant to be re-recorded when they move, and its title carries the month.
- Slow-moving facts can be stated plainly: architecture, licences, protocols, governance, business models, sales channels.

## Episodes

| # | Slug | Title | Scope | Min | Words |
|---|------|-------|-------|-----|-------|
| K00 | the-map | The map: six layers for comparing AI vendors | The frame, how to read benchmarks and vendor claims, the listener's route through the series | 12 | 1,700-2,000 |
| K01 | openai | OpenAI | Models, Responses API and built-in tools, Agents SDK and agent tooling, Codex, ChatGPT Enterprise, the Microsoft relationship | 22 | 3,000-3,400 |
| K02 | google | Google | Gemini models and multimodal reach, AI Studio vs Vertex AI, ADK and Agent Engine, A2A, Gemini CLI and coding tools, Gemini Enterprise and Workspace | 22 | 3,000-3,400 |
| K03 | microsoft | Microsoft: competitor and channel | Foundry and Azure OpenAI, Agent Framework, Microsoft 365 Copilot and Copilot Studio, GitHub Copilot, Claude inside the Microsoft estate | 20 | 2,800-3,200 |
| K04 | same-claude-other-clouds | Same Claude, different cloud | Claude via Bedrock, Vertex AI and Foundry vs the Claude API: feature parity and lag, data residency, committed-spend drawdown, quotas; AWS's own stack (Nova, AgentCore, Strands, Kiro) | 20 | 2,800-3,200 |
| K05 | open-weights | Open weights, xAI and sovereignty | Llama, Mistral, DeepSeek, Qwen, Kimi, GLM, gpt-oss, Gemma; self-hosting cost; provenance and procurement; xAI Grok and enterprise risk | 20 | 2,800-3,200 |
| K06 | coding-agents | Coding agents: Claude Code and the field | Codex, Gemini CLI, GitHub Copilot, Cursor, Kiro, Devin and the open-source agents; shared standards (MCP, AGENTS.md, skills); what customers actually adopt | 20 | 2,800-3,200 |
| K07 | objections | The objections drill | Ten customer objections, each argued out; model gateways and multi-model strategy; when to recommend a competitor | 20 | 2,800-3,200 |
| K08 | state-of-play-2026-11 | State of play, November 2026 | Current line-ups, list prices, benchmark leaders and how to read them, market-share reports; dated throughout | 16 | 2,200-2,600 |

Listening order is K00 to K08. The spoken number matches the ID ("This is episode four" for K04).

## Sources

- Research fact sheets in `field/research/` (same folder as this file): one per vendor group, every fact with a source URL, an as-of date and a confidence mark. These are the primary source. Teach High-confidence facts plainly, hedge Moderate ones, leave Low ones out unless the point is that the claim is unverified.
- For Claude-side claims: platform.claude.com/docs, code.claude.com/docs, modelcontextprotocol.io, and `~/dev/github.com/forgd-ai/claude-kb/claude-kb-main/`.
- A competitor fact that is not in the fact sheets must be checked against the vendor's own documentation before it is used. Vendor-reported benchmark numbers are named as vendor-reported.

## Transcript location

`production/field/transcripts/K<NN>-<slug>.md`, front matter as in `SERIES.md` with `episode: "K01"`, `series: "FIELD"`, `domain` naming the vendor or theme, and `weight: ""`. Cards in `production/cards/K<NN>-<slug>.json`.
