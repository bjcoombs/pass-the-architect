# OpenAI competitor fact sheet

As of 2026-11-14. Compiled for an Applied AI Architect advising enterprise customers. Every row carries a source and confidence.

**Legend**
- Confidence: **High** = read on a first-party page during this research. **Moderate** = first-party page seen only via search snippet or a consistent multi-source secondary report. **Low** = single secondary source, or sources conflict.
- **[1P]** first-party OpenAI (or partner cloud) fact. **[3P]** third-party claim or measurement. **[VR]** vendor-reported benchmark.
- **PERISHABLE** = likely to change before 2027-02-14.
- Access notes: openai.com and help.openai.com returned HTTP 403 to the fetch tool, so facts from those domains come via search-indexed copies (Moderate at best). developers.openai.com and learn.chatgpt.com fetched cleanly.

---

## 0. Headline changes since mid-2026 (read this first)

| Change | Date | Source | Conf |
|---|---|---|---|
| Model naming switched to codename tiers: Astra (top), Sol, Terra, Luna (cheapest). No more "mini/nano" or "o-series" in the current line | GPT-5.6 family 2026-07-09; GPT-6 Astra 2026-09-03 | https://developers.openai.com/api/docs/changelog | High [1P] |
| Assistants API shut down | 2026-08-26 | https://developers.openai.com/api/docs/deprecations | High [1P] |
| Agent Builder (the AgentKit visual canvas) and the Evals platform deprecated, gone 2026-11-30; Evals replacement named as Promptfoo | notice 2026-06-03 | https://developers.openai.com/api/docs/deprecations | High [1P] PERISHABLE |
| Agents API (managed Codex harness, hosted sandboxes) public beta: OpenAI's answer to Claude Managed Agents | 2026-09-10 | https://developers.openai.com/api/docs/changelog ; https://community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481 | High [1P] PERISHABLE |
| ChatGPT Work launched (Codex-based agent for knowledge workers; direct Cowork competitor); standalone Codex app folded into ChatGPT desktop app | 2026-07-09 | https://thenewstack.io/openai-codex-work-atlas/ ; https://reworked.co/digital-workplace/openai-debuts-direct-claude-cowork-competitor-chatgpt-work/ | Moderate [3P] |
| OpenAI models on Amazon Bedrock (GPT-5.4/5.5 from 2026-06-01; GPT-6 Astra GA 2026-09-08; GPT-6 Sol/Luna 2026-09-22; GPT-6.1 Sol 2026-09-29) | see dates | https://developers.openai.com/api/docs/changelog ; https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-astra-on-amazon-bedrock/ | High [1P] |
| OpenAI stopped reporting SWE-bench Verified (audit: at least 59.4% of audited problems had flawed tests); headline coding metric is now DeepSWE v1.1 and Terminal-Bench 4.0 | 2026-02-23 | https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ | Moderate [1P via snippet] |
| GPT-6 Astra is the first model OpenAI rates "Critical" for cybersecurity under its Preparedness Framework; top cyber capability gated to the "Daybreak Blue" trusted-defender programme | 2026-09-03 | https://the-decoder.com/gpt-6-astra-is-the-first-model-making-openai-willing-to-declare-the-agi-era/ ; https://rits.shanghai.nyu.edu/ai/openai-gpt-6-astra-critical-cyber/ | Moderate [3P] |

---

## 1. Model line-up

### 1a. Current flagship family (API)

All four: 1.05M context window, 128K max output. Source: https://developers.openai.com/api/docs/models (fetched 2026-11-14). Prices: https://developers.openai.com/api/docs/pricing (fetched 2026-11-14). Release dates: https://developers.openai.com/api/docs/changelog.

| Model | API ID | Role (OpenAI wording) | Released | Input / cached / output per 1M (short context) | Long context (>272K input) | Knowledge cutoff | Conf |
|---|---|---|---|---|---|---|---|
| GPT-6 Astra | `gpt-6-astra` | "Our most capable model for the most demanding work" | 2026-09-03 | $10.00 / $1.00 / $50.00 | $20 / $2 / $75 | 2026-04-30 | High [1P] PERISHABLE |
| GPT-6.1 Sol | `gpt-6.1-sol` | Mid-high tier; OpenAI claims near-Astra on DeepSWE at one-fifth the price | 2026-09-29 | $2.00 / $0.10 / $10.00 | $4 / $0.20 / $15 | 2026-04-30 | High [1P] PERISHABLE |
| GPT-6.1 Terra | `gpt-6.1-terra` | Mid tier | 2026-10-26 | $1.00 / $0.05 / $5.00 | $2 / $0.10 / $7.50 | 2026-06-01 | High [1P] PERISHABLE |
| GPT-6 Luna | `gpt-6-luna` | "Our most efficient model for focused, high-volume tasks" | 2026-09-22 | $0.10 / $0.01 / $0.50 | $0.20 / $0.02 / $0.75 | 2026-05-18 | High [1P] PERISHABLE |

Still-priced earlier generations (Standard tier, input / cached / output per 1M): `gpt-6-sol` $2 / $0.20 / $10 (2026-09-22); `gpt-5.6-sol` $4 / $0.40 / $20, `gpt-5.6-terra` $2 / $0.20 / $12, `gpt-5.6-luna` $0.20 / $0.02 / $1.20 (family released 2026-07-09); `gpt-5.5` $5 / $0.50 / $30 and `gpt-5.5-pro` $30 / $180 (2026-04-24); `gpt-5.4` $2.50 / $0.25 / $15 (2026-03-05); `gpt-5.4-mini` $0.75 / $4.50 and `gpt-5.4-nano` $0.20 / $1.25 (2026-03-17). High [1P], same pricing URL.

### 1b. Reasoning models

- There is no separate reasoning line any more. The GPT-5+ and GPT-6 models are reasoning models with an effort setting (Codex docs refer to `model_reasoning_effort`; Artificial Analysis lists "Max" and "High" variants). o3 / o3-pro remain priced but are scheduled for shutdown 2026-12-11. Source: https://developers.openai.com/api/docs/deprecations ; https://learn.chatgpt.com/codex/agent-configuration/subagents. High [1P].
- "Pro" models (gpt-5.5-pro, gpt-5.4-pro) remain at $30 / $180. High [1P].

### 1c. Open-weight

- Latest open-weight release is still gpt-oss-120b and gpt-oss-20b (Apache 2.0, August 2025). No 2026 open-weight entry in the API changelog; no gpt-oss successor found. Sources: https://developers.openai.com/api/docs/changelog ; https://www.theregister.com/2025/08/05/openai_open_gpt/. Moderate (absence of evidence).

### 1d. Specialised and voice models

| Item | Fact | Source | Conf |
|---|---|---|---|
| Cyber | `gpt-6-cyber` (2026-11-05), `gpt-5.6-cyber` (2026-08-07), via Daybreak Blue/Red access tiers | https://developers.openai.com/api/docs/changelog | High [1P] |
| Life sciences | GPT-Rosalind for approved organisations; GPT-6 Rosalind via trusted access 2026-10-30 | https://developers.openai.com/api/docs/models | High [1P] |
| Image | GPT-Image-2.6 Sunburst / Flare (2026-11-04) | changelog | High [1P] |
| Realtime | `gpt-realtime-2.1` and `-mini` (2026-07-06), `gpt-realtime-translate`, `gpt-realtime-whisper` | changelog | High [1P] |
| GPT-Live-1 | Full-duplex voice model, GA in API 2026-09-10, $0.05/minute billed per second plus backend model/tool usage; separate `/v1/live/sessions` endpoint; outbound SIP calling for all orgs 2026-11-02 | https://developers.openai.com/api/docs/models/gpt-live-1 ; changelog | High [1P] PERISHABLE |
| Transcription | `gpt-transcribe`, `gpt-live-transcribe` (2026-07-28); whisper-1 and gpt-4o-transcribe family shut down 2027-02-26 | changelog | High [1P] |

### 1e. Pricing tiers and multipliers

| Tier | Effect | Source | Conf |
|---|---|---|---|
| Batch | 50% off Standard | https://developers.openai.com/api/docs/pricing | High [1P] |
| Flex | 50% off Standard (slower, best-effort) | same | High [1P] |
| Fast (renamed from Priority on 2026-07-30) | 2x Standard | same | High [1P] |
| Ultrafast | 6x Standard; only gpt-6-astra and gpt-6.1-sol | same | High [1P] PERISHABLE |
| Long context | Roughly 2x input, 1.5x output above 272K input tokens | same | High [1P] |
| Data residency / FedRAMP endpoints | +10% for models released on or after 2026-03-05 | same | High [1P] |

Claude comparison point (first party, fetched 2026-11-14, https://platform.claude.com/docs/en/about-claude/models/overview): Fable 5.2 $8/$40, Opus 5.5 $4/$20, Sonnet 5.5 $2/$10, Haiku 5.5 from $0.10/$0.50; all 1M context, 128K output. So on list price GPT-6 Astra ($10/$50) costs more than Fable 5.2, GPT-6.1 Sol matches Sonnet 5.5, and GPT-6 Luna matches Haiku 5.5's floor. High.

---

## 2. Developer platform

| Topic | Fact | Source | Conf |
|---|---|---|---|
| Responses API | The primary API; built-in tools, Conversations API for state, WebSocket mode (2026-02-23), server-side compaction (2026-02-10) | https://developers.openai.com/api/docs/changelog | High [1P] |
| Chat Completions | Not deprecated; no notice on deprecations page. Changelog steers tool calling to Responses | https://developers.openai.com/api/docs/deprecations | High [1P] |
| Assistants API | Shut down 2026-08-26; replacement Responses + Conversations | same | High [1P] |
| Prompt objects (`/v1/prompts`) | Shut down 2026-11-30; move prompts into code | same | High [1P] PERISHABLE |
| Built-in tools (Responses) | Web search, file search, shell (hosted containers or local; succeeds Code Interpreter in pricing as "Hosted Shell and Code Interpreter"), computer use (built-in since 2026-03-05), image generation, remote MCP servers, tool search (gpt-5.4+), Skills (versioned bundles in hosted shell, since 2026-02-10), Programmatic Tool Calling (JS orchestration, 2026-07-09) | https://developers.openai.com/api/docs/guides/tools ; changelog | High [1P] |
| Tool prices | Web search $10/1k calls plus content tokens; file search $2.50/1k calls plus $0.10/GB-day storage (1 GB free); containers $0.03 (1 GB) to $1.92 (64 GB) per 20-minute session, 5-minute minimum | https://developers.openai.com/api/docs/pricing | High [1P] PERISHABLE |
| Structured outputs | JSON-schema structured outputs remain (not re-verified in this pass) | training knowledge | Low |
| Async tool calling, mid-turn steering | Shipped with GPT-6 Astra 2026-09-03; Azure does not yet support mid-turn steering | changelog ; https://azure.microsoft.com/en-us/blog/gpt-6-astra-frontier-intelligence-for-work-now-available-in-microsoft-foundry/ | High [1P] |
| Fine-tuning | Self-serve fine-tuning job creation restricted from 2027-01-06 | deprecations page | High [1P] PERISHABLE |

### Prompt caching (changed substantially in 2026)

Source: https://developers.openai.com/api/docs/guides/prompt-caching (fetched 2026-11-14). High [1P] unless noted. PERISHABLE.

- GPT-5.6 and later: implicit caching (automatic breakpoint at end of latest eligible message) plus optional explicit mode via `prompt_cache_options.mode = "explicit"` and `prompt_cache_breakpoint` on content blocks; up to 4 cache writes per request. This is now close to Anthropic's `cache_control` model.
- Minimum 1,024 visible input tokens (GPT-5.6+).
- TTL: `"30m"` default or `"12h"` (Responses only). Earlier models: `in_memory` (5-10 min, up to 1 h) or `24h`; `24h` is default for non-ZDR orgs since 2026-05-29.
- Reads: 0.1x input on GPT-5.6+, 0.05x on GPT-6.1 Sol and Terra ("discounted up to 95%").
- Writes: 1.25x input for 30m, 2.5x for 12h (12h introduced 2026-10-20). Earlier models: no write charge. Note: OpenAI used to have no write premium; it now charges one, like Anthropic.
- ZDR-compatible: cache holds encrypted KV tensors in GPU-local storage, max 24 h; not shared across orgs or residency boundaries.
- `prompt_cache_key` now optional on GPT-5.6+ (routing automatic); used for per-tenant accounting and to prevent cross-user cache probing.

Claude comparison: Anthropic cache reads are 0.1x base, 0.05x on Opus 5.5 / Sonnet 5.5, 0.025x on Fable 5.1/5.2 (https://platform.claude.com/docs/en/about-claude/models/overview). High.

### Realtime / voice
See 1d. Realtime beta header removed 2026-05-12. GPT-Live-1 is the flagship voice product. High [1P].

---

## 3. Agent stack

| Component | Fact | Source | Conf |
|---|---|---|---|
| Agents SDK (Python) | MIT. Concepts: agents, sandbox agents, realtime agents, voice agents, agents-as-tools and handoffs, tools incl. MCP, guardrails, human-in-the-loop, sessions, tracing. README: provider-agnostic, supports "100+ other LLMs" alongside Responses and Chat Completions. ~30.7k stars | https://github.com/openai/openai-agents-python (2026-11-14) | High [1P] |
| Agents SDK (TypeScript) | MIT. Same concept list. README wording: "provider-agnostic, supporting OpenAI APIs and more" (no "100+" figure). Node 22+, Deno, Bun. ~4.0k stars | https://github.com/openai/openai-agents-js (2026-11-14) | High [1P] |
| SDK 2026 changes | Sandboxes, harness customisation, memory controls (2026-04-15); TS parity (2026-05-06) | changelog | High [1P] |
| Agents API | Public beta 2026-09-10. Managed Codex harness: sessions, orchestration, compaction, recovery, multi-agent delegation, MCP, skills, artifact generation. Sandbox: OpenAI-hosted, self-hosted, or partner (Blaxel, Cloudflare, Daytona, DigitalOcean, E2B, Modal, Oracle, Runloop, Vercel). No API fee; pay tokens plus container rates. Later: computer use (09-29), sandbox prewarming and active-turn-only billing (10-09), skills in hosted sandboxes and Artifact SDK (10-16), scheduled automations tool (10-23), background compaction and "automatic review" (10-30) | changelog ; https://community.openai.com/t/introducing-the-agents-api-and-hosted-sandboxes/1396481 ; https://the-decoder.com/openais-new-agents-api-gives-developers-the-infrastructure-behind-codex-and-chatgpt/ | High [1P] PERISHABLE |
| Agents API limits | US data residency only; no Zero Data Retention, including with self-hosted sandbox. `/v1/agents` listed as not ZDR-eligible | Agents API beta FAQ https://help.openai.com/en/articles/20001551-agents-api-beta-faq (via snippet) ; https://developers.openai.com/api/docs/guides/your-data (fetched) | High (your-data page) / Moderate (FAQ) PERISHABLE |
| Choosing a runtime | OpenAI's guide: Agents API (they run the loop), Agents SDK (you run the loop), Responses (raw), ChatKit (embedded chat UI). Agent Builder no longer mentioned | https://developers.openai.com/api/docs/guides/agents | High [1P] |
| AgentKit | Launched Oct 2025 (Agent Builder, ChatKit, Connector Registry, Evals). Agent Builder and Evals wind down 2026-11-30. ChatKit still listed (ChatKit storage still priced at $0.10/GB-day) | deprecations page ; pricing page ; https://openai.com/index/introducing-agentkit/ | High [1P] PERISHABLE |
| Workspace Agents (ChatGPT) | Announced 2026-04-22, research preview on Business, Enterprise, Edu, Teachers; positioned as successor to custom GPTs; credit-priced (start date conflicts: May 6 vs July 6) | https://venturebeat.com/orchestration/openai-unveils-workspace-agents-a-successor-to-custom-gpts-for-enterprises-that-can-plug-directly-into-slack-salesforce-and-more ; https://www.kommunicate.io/blog/chatgpt-workspace-agents/ | Moderate [3P] |
| MCP client | Remote MCP servers as a Responses tool; MCP in Agents SDK, Agents API, Codex. Secure MCP Tunnel for private enterprise MCP servers (2026-05-19) | tools guide ; changelog | High [1P] |
| MCP in ChatGPT | "Connectors" renamed "Apps" (Dec 2025); custom MCP via Developer Mode; Enterprise/Edu apps off by default, admin and RBAC gated; full write-capable MCP for Business/Enterprise/Edu | https://help.openai.com/en/articles/12584461 (via snippet) | Moderate |
| MCP server | No evidence OpenAI ships its own platform MCP server beyond docs; not researched in depth | none | Low |
| Standards stance | OpenAI co-founded the Linux Foundation Agentic AI Foundation (AAIF, announced 2025-12-09) and donated AGENTS.md; Anthropic donated MCP, Block donated goose. One secondary source lists A2A, Agent Skills and "Open Responses" among AAIF projects as of Nov 2026; OpenAI's own A2A role not confirmed | https://tessl.io/blog/openai-anthropic-and-others-unite-behind-agentic-ai-foundation-for-open-standards/ ; https://intuitionlabs.ai/articles/agentic-ai-foundation-open-standards | Moderate (founding) / Low (A2A, project list) |

---

## 4. Coding: Codex

| Topic | Fact | Source | Conf |
|---|---|---|---|
| Surfaces | ChatGPT desktop app (Chat / Work / Codex modes), mobile, web, Codex CLI, IDE extension, Codex Cloud; integrations GitHub, GitLab (beta), Slack, Linear, Codex SDK, GitHub Action | https://learn.chatgpt.com/docs | High [1P] |
| Docs moved | developers.openai.com/codex redirects to learn.chatgpt.com | fetch redirect 2026-11-14 | High |
| Open source | `openai/codex`: Apache-2.0, ~135k stars, Rust core (`codex-rs`) | https://github.com/openai/codex | High [1P] |
| Config | AGENTS.md; `config.toml` and `requirements.toml` (admin-managed); `~/.codex/` and `<repo>/.codex/` layers | https://learn.chatgpt.com/codex/hooks | High [1P] |
| Sandbox | `read-only`, `workspace-write` (default), `danger-full-access`. macOS Seatbelt; Linux/WSL2 bubblewrap; native Windows sandbox | https://learn.chatgpt.com/codex/sandboxing | High [1P] |
| Approvals | `on-request`, `never` (`untrusted` no longer selectable). "Approve for me" auto-review: `approvals_reviewer = auto_review` routes prompts to a reviewer agent | same | High [1P] |
| Hooks | 14 events: SessionStart, SessionEnd, UserPromptSubmit, PreToolUse, PermissionRequest, PostToolUse, PreModelRequest, PostModelRequest, PreCompact, PostCompact, SubagentStart, SubagentStop, Stop, Interrupt. `hooks.json` or `[hooks]` in config.toml; command and mcp_tool handlers only; enabled by default; must be trusted via `/hooks` | https://learn.chatgpt.com/codex/hooks | High [1P] |
| Subagents | TOML files in `~/.codex/agents/` or `.codex/agents/` (name, description, developer_instructions, optional model/effort); built-ins default, worker, explorer; parallel spawn with `max_concurrent_threads_per_session`; inherit parent sandbox, cannot override | https://learn.chatgpt.com/codex/agent-configuration/subagents | High [1P] |
| Skills and plugins | Skills, plugins (can bundle hooks), MCP all documented | https://learn.chatgpt.com/docs | High [1P] |
| Plans | Free and Go ($8) get GPT-6 Luna in desktop app; Plus $20; Pro $100 / $200 / $500 (Ultrafast on $500, no 5-hour limit); Business $20/user/month annual or $25 monthly; Enterprise/Edu contact sales; API-key use at API rates with no cloud features | https://learn.chatgpt.com/codex/pricing | High [1P] PERISHABLE |
| Plus usage estimate | Per 5 hours: GPT-6 Astra 5-45 local messages, GPT-6.1 Sol 15-160, GPT-6 Luna 350-3,000 | same | High [1P] PERISHABLE |
| Recommended models | Docs suggest `gpt-6.1-sol` for demanding work, `gpt-6-luna` for narrow tasks | subagents page | High [1P] |
| Adoption claim | "More than 5 million" weekly Codex users, over 1 million for non-coding work | https://thenewstack.io/openai-codex-work-atlas/ | Moderate [VR] |

**Shape vs Claude Code.** The two have converged: project instruction file (AGENTS.md vs CLAUDE.md), layered user/project/managed config, OS-level sandbox, hook events with near-identical names (PreToolUse, PostToolUse, Stop, SubagentStop, PreCompact, SessionStart), subagents as files, skills, plugins, MCP. Differences worth naming: Codex makes the OS sandbox the default boundary (workspace-write) and layers approvals on top; Codex subagent files are TOML and cannot loosen the parent sandbox; Codex hooks support only command and mcp_tool handlers (prompt/agent handlers parsed but skipped); Codex ships inside the consumer ChatGPT app down to the Free tier. AGENTS.md is the AAIF standard, so it is read by many tools. Assessment, Moderate.

---

## 5. Enterprise

| Topic | Fact | Source | Conf |
|---|---|---|---|
| Plans | ChatGPT Business (formerly Team) $20/user/month annual or $25 monthly, 2+ seats, SAML SSO, MFA. Enterprise and Edu: contact sales; SCIM, EKM, RBAC, Compliance API, audit logs | https://learn.chatgpt.com/codex/pricing | High [1P] |
| Enterprise seat price | Not published; third parties estimate $45-75/seat | https://www.layer3labs.io/guides/chatgpt-enterprise-pricing | Low [3P] |
| ChatGPT Work | Codex-based agent for documents, spreadsheets, decks, web apps over connected data; scheduled cloud tasks; Sites (public URLs) in beta. Access by plan conflicts across sources | see section 0 | Moderate [3P] PERISHABLE |
| ChatGPT data residency | At-rest: Australia, Canada, Europe (EEA+CH), India, Japan, Singapore, South Korea, UAE, UK, US. In-region inference: Europe, US, UAE. Included at no extra cost for Enterprise/Edu | https://help.openai.com/en/articles/9903489-data-residency-and-regional-data-processing-for-chatgpt (via snippet) | Moderate PERISHABLE |
| API data residency | Storage and processing: US, EU, Australia, Japan, India, UAE (AU/JP/IN processing limited to `gpt-6-luna`; IN and UAE via sales). Storage only: Canada, Singapore, South Korea, UK. Region fixed at project creation; +10% price uplift | https://developers.openai.com/api/docs/guides/data-residency | High [1P] PERISHABLE |
| API retention | Abuse logs up to 30 days by default; no training on API data since 2023-03-01 unless opted in. ZDR and Modified Abuse Monitoring need OpenAI approval | https://developers.openai.com/api/docs/guides/your-data | High [1P] |
| Not ZDR-eligible | Conversations, ChatKit threads, Agents, Assistants/Threads, vector stores, files, fine-tuning, evals, batches | same | High [1P] |
| Certifications | SOC 2 Type 2 (API, ChatGPT Enterprise/Edu/Team), SOC 3, ISO 27001/27017/27018/27701, ISO 42001, CSA STAR, PCI DSS (payments components), TX-RAMP, FedRAMP 20x listed | https://trust.openai.com/ | High [1P] |
| HIPAA | Not on trust portal page; BAA reported available for API and ChatGPT Enterprise (and ChatGPT for Healthcare), not Business | https://www.gend.co/blog/chatgpt-for-business ; training knowledge | Low |
| Azure / Microsoft Foundry | GPT-6 Astra GA in Foundry 2026-09-03 (Global and US Data Zone, Standard and PTU); Sol, Luna, 6.1 Sol followed. Foundry lacks mid-turn steering for Astra | https://azure.microsoft.com/en-us/blog/gpt-6-astra-frontier-intelligence-for-work-now-available-in-microsoft-foundry/ | High [1P Microsoft] |
| Amazon Bedrock | GPT-6 Astra GA 2026-09-08 at OpenAI list prices, counts toward AWS commits; ChatGPT Work and Codex can be pointed at Bedrock | https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-astra-on-amazon-bedrock/ ; https://aboutamazon.com/news/aws/bedrock-openai-models | High [1P AWS] |

---

## 6. Learning and credentials

| Topic | Fact | Source | Conf |
|---|---|---|---|
| OpenAI Academy | Free. Four areas: Apply AI at Work, Build with AI (Codex or API), Lead AI Adoption, Teach and learn with AI | https://academy.openai.com/ | High [1P] |
| API learning path | Five courses: Scope AI Solutions; Evaluate AI Applications; Design and Build Agentic Systems; Build with Retrieval-Augmented Generation; Optimize AI Application Performance | https://help.openai.com/en/articles/20001270-openai-academy-courses (via snippet; direct fetch 403) | Moderate [1P] |
| Codex learning path | Three courses: Get Started with Codex; Extend Codex Workflows; Scale Codex Across Governed Teams and Systems | same | Moderate [1P] |
| Badges | Issued via Accredible on 80%+ assessment; completing a path earns a completion certificate. Badges are explicitly not OpenAI Certifications | same | Moderate [1P] |
| Live bootcamps | API Builder Bootcamp (5 sessions: API Foundations, Agents, Realtime, RAG, Production and Optimization); Codex Bootcamp | https://academy.openai.com/public/resources/api-builder-bootcamp-2026-08-19 | Moderate [1P] |
| OpenAI Certified | Coursera-powered app inside ChatGPT; for Enterprise and Edu workspaces, invite-only, enrol via account rep; admin enables, user needs Coursera account. No public price found | https://help.openai.com/en/articles/20001151-openai-certified-app (via snippet) | Moderate [1P] PERISHABLE |
| AI Foundations / Certification | Announced Sept 2025; pilots with employers (Walmart, John Deere, Lowe's, BCG, Accenture reported). Proctored certification still pilot-limited; exam guide, price, passing score not public | https://findskill.ai/blog/openai-certification-guide/ ; https://www.eweek.com/news/openai-chatgpt-training-certifications/ | Low [3P] |
| Unreliable claims | Pages quoting a 65-question exam or $399 fee conflict with pilot status; disregard | https://aiforanything.io/blog/openai-certification-exam-guide-2026 | Low |

There is no published OpenAI equivalent of an architect-level, publicly bookable, paid certification found as of 2026-11-14.

---

## 7. Strengths and weaknesses vs Claude

### Third-party measurements

| Benchmark | Result | Source (as of) | Conf |
|---|---|---|---|
| Artificial Analysis Intelligence Index | 1 Claude Fable 5.2 Max 65; 2 Gemini 4 Carbon 60; 3 Claude Opus 5.5 Max 59; 4 GPT-6 Astra Max 57; 5 GPT-6.1 Sol Max 55 (tied Claude Sonnet 5.5 Max 55); 8 GPT-6.1 Terra 51; GPT-6 Luna 28 vs Claude Haiku 5.5 36 | https://artificialanalysis.ai/leaderboards/models (2026-11-14) | High [3P] PERISHABLE |
| AA cost per task | GPT-6.1 Sol Max $1.27 vs Claude Sonnet 5.5 Max $10.02 at the same score of 55; GPT-6 Astra $6.24 vs Opus 5.5 $10.04 vs Fable 5.2 $26.54 | same | High [3P] PERISHABLE |
| Arena (formerly LMArena) Agent leaderboard | 1 Fable 5.2 30.5%; best OpenAI is GPT-6 Astra at #7, 14.6% | https://arena.ai/leaderboard (2026-11-14) | High [3P] PERISHABLE |
| Arena WebDev | #1 Claude Fable 5.2 (xHigh) | same | High [3P] PERISHABLE |
| Arena Text | Gemini 4 Carbon reported #1 (1528) in early Nov; OpenAI and Claude positions not confirmed | https://af.net/realtime/google-gemini-4-carbon-leads-lmarena-text-leaderboard-with-1528-score/ | Low [3P] |
| Terminal-Bench | Current board is 4.1; rows did not render, so no independent ranking captured | https://www.tbench.ai/leaderboard | n/a |

### Vendor-reported (OpenAI)

| Claim | Source | Conf |
|---|---|---|
| GPT-6 Astra: Terminal-Bench 4.0 57.9% vs Claude Fable 5.1 55.8% and GPT-5.6 Sol 37.3%; Terminal-Bench Science 64.6% vs Fable 5.1 52.6%; DeepSWE v1.1 74.1% (later tables show 74.8 high). One outlet reports 57.7% | https://thenewstack.io/openai-gpt6-astra-benchmarks/ ; https://www.deeplearning.ai/the-batch/gpt-6-astra-is-a-star | Moderate [VR] |
| GPT-6.1 Sol: DeepSWE v1.1 75.2 (high) vs Astra 74.8, "Astra-level at one-fifth the price" | https://propakistani.pk/2026/09/30/gpt-6-1-sol-brings-astra-level-performance-at-5x-lower-cost/ | Moderate [VR] |
| OpenAI publishes no SWE-bench Verified or Pro scores for GPT-6.x. Note Astra's comparison was against Fable 5.1, not the later Fable 5.2 | https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ | Moderate |

### Where OpenAI is genuinely stronger (as of 2026-11-14)

1. **Price-performance in the middle.** GPT-6.1 Sol matches Claude Sonnet 5.5 on the AA index at the same list price but about one-eighth the AA cost per task, and has 0.05x cache reads. High [3P].
2. **Voice.** GPT-Live-1 full-duplex at $0.05/min, Realtime 2.1, SIP calling. Anthropic has no equivalent first-party realtime voice API. Moderate.
3. **Distribution.** ChatGPT consumer reach, Codex and ChatGPT Work down to the Free tier; now on Azure, Bedrock and direct. Removes the old "Claude is the only frontier model on Bedrock" argument. High.
4. **Breadth of first-party modalities** (image, transcription, translation, voice) under one bill. High.
5. **Codex sandbox-by-default** and open-source Apache-2.0 CLI with 135k stars. High.

### Where Claude is stronger

1. **Top of the independent leaderboards.** Fable 5.2 leads AA (65 vs 57), Arena Agent (30.5% vs 14.6%) and Arena WebDev. Opus 5.5 also outranks GPT-6 Astra on AA. High [3P] PERISHABLE.
2. **Frontier price.** Fable 5.2 ($8/$40) is cheaper on list than GPT-6 Astra ($10/$50). High.
3. **Managed agents compliance.** OpenAI's Agents API is beta, US-only residency, no ZDR. Check Claude Managed Agents' own current terms before using this in a pitch. High for OpenAI side.
4. **Platform stability.** OpenAI retired Assistants, Agent Builder, Evals and prompt objects within about 15 months of promoting several of them; customers who built on AgentKit's canvas are migrating now. Anthropic publishes "not sooner than" retirement dates per model. High [1P both].
5. **Long-context parity, not advantage:** both offer about 1M tokens and 128K output. Do not claim a context lead.

### How customers choose (pattern, Moderate)
- Microsoft-centric estates default to Azure OpenAI / Foundry; that advantage now also cuts for Claude (Claude is in Foundry too).
- Voice and consumer-facing assistants lean OpenAI.
- Agentic coding and long-horizon agent work lean Claude on current independent evidence.
- Cost-sensitive high-volume mid-tier work is genuinely contested; GPT-6.1 Sol is the model to benchmark against.
- Regulated workloads should be decided on residency plus ZDR eligibility per endpoint, not on the logo: both vendors carve out stateful features.

---

## 8. Starter-note claims: verdicts

| Claim | Verdict | Evidence | Conf |
|---|---|---|---|
| "OpenAI Academy has five API courses (Scope, Evaluate, Agentic Systems, RAG, Optimise) and three Codex courses, badges via Accredible" | **True** (spelling is "Optimize"; full titles in section 6). Badges are not certifications | help.openai.com article 20001270 via search snippet | Moderate |
| "OpenAI Agents SDK is MIT-licensed, works with 100+ other LLMs, Python and TypeScript" | **True with a nuance**: MIT for both; Python and TypeScript both exist; the "100+ other LLMs" wording is in the Python README only, the TS README says "provider-agnostic, supporting OpenAI APIs and more" | GitHub READMEs | High |
| "OpenAI certification is invite-only" | **Mostly true**: the OpenAI Certified app is invite-only for ChatGPT Enterprise/Edu workspaces and the proctored certification is pilot-only; Academy courses and Accredible badges are open to anyone | help article 20001151 via snippet; third-party guides | Moderate |
| Tracker model name "GPT-6 Astra" | **True**: `gpt-6-astra`, released 2026-09-03, $10/$50 | developers.openai.com models, pricing, changelog | High |
| Tracker model name "GPT-5.6" | **True but incomplete**: GPT-5.6 is a family (Sol, Terra, Luna) released 2026-07-09; bare `gpt-5.6` is an alias for Sol. It is now a previous generation | changelog | High |

---

## 9. Open gaps

- Deprecations page lists a 2026-06-11 notice that names gpt-6.1-sol (released 2026-09-29) as a replacement; either the notice was revised or the fetch summary blended rows. Low confidence on that row's notice date.
- No independent Terminal-Bench 4.1 ranking captured.
- HIPAA BAA scope and ChatGPT Enterprise seat price not confirmed first-party.
- Workspace Agents credit pricing start date conflicts (May 6 vs July 6, 2026).
