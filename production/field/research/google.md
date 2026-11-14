# Google (Gemini) - competitor fact sheet

As of: 2026-11-14. All URLs read on that date unless stated.

Legend:
- Confidence: **H** (primary source read directly), **M** (primary source partial, or several consistent secondaries), **L** (single secondary, conflicting, or inferred).
- **1P** = Google's own claim. **3P** = independent third party. **A** = Anthropic doc.
- **PERISHABLE** = likely to change by mid-February 2027.

---

## 0. What changed since mid-2026 (read this first)

| Change | Date | Source | Conf |
|---|---|---|---|
| Vertex AI renamed **Gemini Enterprise Agent Platform**; Agent Engine now **Agent Runtime**; Agentspace folded into **Gemini Enterprise** | 2026-04-22 (Cloud Next '26) | https://www.hpcwire.com/aiwire/2026/04/23/google-unveils-gemini-enterprise-agent-platform/ (3P); Anthropic docs now say "Agent Platform" https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed (A) | H |
| New **Gemini 4** family: Argon (announced 2026-09-30, GA 2026-10-13), Carbon (GA 2026-11-10), Hydrogen (GA 2026-11-12). The "Pro" brand is not used for Gemini 4 | Sep-Nov 2026 | https://aistudio.google.com/docs/changelog (1P) | H |
| **Gemini CLI** stopped serving free, AI Pro and AI Ultra users; replaced by closed-source **Antigravity CLI** (`agy`) | Announced 2026-05-19, cutoff 2026-06-18 | https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ (1P) | H |
| **Jules** shutting down: read-only from 2026-11-11, off 2026-12-31 | Notice 2026-10-29 | https://jules.google/docs/changelog/ (1P) | H |
| **Managed Agents** in the Gemini API (Antigravity harness, remote Linux sandbox, AGENTS.md + SKILL.md) | Preview 2026-05-19 | https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api (1P) | H |
| **A2A** moved under the Linux Foundation's Agentic AI Foundation (AAIF), alongside MCP | 2026-08-17 | https://aaif.io/blog/a2a-joins-aaif (3P, foundation) | H |
| New cert: **Professional Agentic Architect** ($200, exam + labs) | Announced 2026-11-11 | https://cloud.google.com/learn/certification/agentic-architect (1P) | H |

Practical consequence for the podcast: anything recorded from memory about "Gemini 2.5/3 Pro", "Vertex AI Agent Engine", "Gemini CLI as Google's Claude Code" or "Jules" is now out of date.

---

## 1. Model line-up

### 1a. Gemini 4 (frontier) - all PERISHABLE (prices change 2026-12-01)

| Model | API name | GA (Gemini API) | Context / output | List price per 1M tokens (in / out) | Positioning (1P) | Conf |
|---|---|---|---|---|---|---|
| Gemini 4 Carbon | `gemini-4-carbon` | 2026-11-10 | 1M shared in+out; long-decode up to 1M out | $2 / $10 intro until 2026-11-30, then **$4 / $20** | "Strongest model"; spends more tokens to reason and verify; hardest coding and science | H |
| Gemini 4 Argon | `gemini-4-argon` | 2026-10-13 (announced 2026-09-30) | 1,048,576 shared; streaming segment 65,536 | $2 / $10 intro, then **$4 / $20**; invite-only "Contributor tier" $1 / $5 that uses your data for training | Default for "the majority of software engineering and knowledge work" | H |
| Gemini 4 Hydrogen | `gemini-4-hydrogen` | 2026-11-12 | 1M | **$1.50 / $7.50 flat across 1M**; free tier exists | "Daily driver for agentic workflows"; fast executor alongside Carbon/Argon | H |

Sources: pricing https://aistudio.google.com/docs/pricing ; Argon post https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-argon/ ; Carbon post https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-4-carbon-now-available/ ; Hydrogen post https://blog.google/innovation-and-ai/models-and-research/gemini-models/introducing-gemini-4-hydrogen/ ; Argon model card https://docs.cloud.google.com/gemini-enterprise-agent-platform/models/gemini/4-argon (all 1P).

Notes:
- Argon output limit rose to 1M tokens from 64K (1P blog). H.
- Cached input on Gemini 4 is 95% off input price (1P blog, Argon). H.
- Gemini 4 supports **implicit caching only**; no explicit cache objects (1P caching doc https://aistudio.google.com/docs/caching ; Argon model card). H.
- Gemini 4 Argon on Agent Platform: no Live API; batch, grounding, structured output supported. ML processing in `us`, `eu`, `europe-west2`, `asia-southeast1` (1P model card). H.
- Argon was first released to cyber defenders "without cyber guardrails" via the **Fairwind Program**; Carbon "for cyber" also Fairwind-gated (1P). H.
- Consumer: Carbon in the Gemini app for AI Ultra; Hydrogen in the app dropdown and auto-routed for free users (1P). H.

### 1b. Gemini 3.x (current workhorse tier)

| Model | API name | Status / date | Price per 1M (in / out) | Conf |
|---|---|---|---|---|
| Gemini 3.8 Flash | `gemini-3.8-flash` | GA 2026-09-02; 1,048,576 ctx, 65,536 out | $0.75 / $3.75 promo until 2026-12-31, then **$1.50 / $7.50** from 2027-01-01 | H |
| Gemini 3.6 Flash | `gemini-3.6-flash` | GA 2026-07-21 | same as 3.8 Flash, same 2027 doubling | H |
| Gemini 3.5 Flash-Lite | `gemini-3.5-flash-lite` | GA 2026-07-21 | $0.30 / $2.50 | H |
| Gemini 3.1 Flash-Lite | `gemini-3.1-flash-lite` | GA 2026-05-07 | $0.25 / $1.50 (audio in $0.50) | H |
| Gemini 3.1 Pro | `gemini-3.1-pro-preview` | still preview-named | $2 / $12 up to 200K; $4 / $18 above 200K | H |
| Gemini 3 Flash | `gemini-3-flash-preview` | preview | $0.50 / $3.00 | H |
| Gemini 2.5 Flash-Lite | `gemini-2.5-flash-lite` | served "until further notice" | $0.10 / $0.40 (cheapest text model) | H |

Deprecations (PERISHABLE): `gemini-2.5-pro` reroutes to `gemini-3.8-flash` and `gemini-2.5-flash` to `gemini-3.5-flash-lite` on **2026-12-01**; 3.7 Flash and 3.5 Flash already deprecated (2026-10-08). Source: https://aistudio.google.com/docs/changelog (1P). H.

Pattern worth saying on air: Google ships a new Flash point release roughly every 4-6 weeks (3.5 May, 3.6 Jul, 3.7 Aug, 3.8 Sep) and retires the previous one within weeks. Customers on pinned versions get silently rerouted. Inferred from the 1P changelog. M.

### 1c. Deep Think

- No Gemini 4 Deep Think found. Latest confirmed is **Gemini 3 Deep Think** (update Feb 2026): AI Ultra in the Gemini app; API only via early-access for selected researchers and enterprises. https://itbrief.co.uk/story/google-expands-gemini-deep-think-for-research-apis (3P). M.
- Carbon's "uses more tokens to reason and verify" positioning looks like Deep Think's role moving into the main model line. Inference. L.

### 1d. Multimodal and specialised models (1P: https://aistudio.google.com/docs/models , pricing page)

| Capability | Model (API name) | Price | Conf |
|---|---|---|---|
| Video generation with native audio (up to 15 s) and video editing | Gemini Omni 1.2 Flash `gemini-omni-1.2-flash` (GA 2026-11-05); Veo 2/3.0 shut down June 2026 | $1.50 in; $12 per 1M video-out tokens | H |
| Image generation/editing | Nano Banana 2.1 `gemini-nano-banana-2.1` (GA 2026-10-06); Nano Banana Pro `gemini-3-pro-image` (4K); Nano Banana 2 Lite. Imagen 4 shut down | 2.1: about $0.034 per 1K image; Pro about $0.134 per 1K/2K, $0.24 per 4K | H |
| Real-time voice agents | Gemini 3.8 Live `gemini-3.8-live`, plus Extended Thinking variant (GA 2026-09-15) | $3 per 1M audio in (about $0.005/min), $12 per 1M audio out (about $0.018/min) | H |
| Speech translation | `gemini-3.5-live-translate-preview`, 70+ languages | $0.0053/min in, $0.0315/min out | H |
| TTS | `gemini-3.8-flash-tts` (130 languages), Flash-Lite TTS (101) | doubles 2027-01-01 | H |
| Speech-to-text | `gemini-3.5-transcribe`, `-live` (GA 2026-08-26) | $0.003/min in | H |
| Music | Lyria 3.5 `lyria-3.5` (full songs) | $0.08 per song | H |
| Multimodal embeddings | `gemini-embedding-2` (text, image, audio, video, PDF) | $0.20 per 1M text | H |
| Classifier-style decisions | Gemini Decision 1 + Decisions API (2026-11-11) | $0.10 per 1M in, no output tokens | H |
| Robotics | Gemini Robotics ER 2 (preview) | - | H |
| Long-video understanding | Argon LVBench 91.7% (1P claim); "agentic video understanding" cuts long-video input tokens up to 88% (1P) | - | H (as 1P claim) |

Claude has no first-party image, video, audio-generation, speech or embedding models. This is Google's widest, least-contested lead. H.

### 1e. Gemma (open weights)

- **Gemma 4**, released 2026-04-02, **Apache 2.0** (first time; earlier Gemma used a custom licence). Sizes: E2B, E4B (edge), 26B MoE (about 3.8B active), 31B dense. 31B was #3 open model on Arena text at launch (1P). https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/ ; https://9to5google.com/2026/04/02/google-gemma-4/ (3P). M (context window figure of 256K unverified, L).
- No later Gemma generation found as of 2026-11-14. M.
- Anthropic has no open-weights model; Gemma is the answer for on-device, air-gapped or fine-tune-yourself requirements. H.

---

## 2. Developer platform

### 2a. Two front doors (1P)

| | Gemini API / Google AI Studio | Gemini Enterprise Agent Platform (ex-Vertex AI) |
|---|---|---|
| Auth | API key | GCP IAM, service accounts |
| Data residency | No regional control | ML processing pinned to `us`, `eu`, specific regions per model card |
| Enterprise controls | Paid tier: data not used for training; free tier and Argon Contributor tier may be | VPC-SC, CMEK, Access Transparency, audit logs, provisioned throughput, Priority PayGo |
| Third-party models | Gemini only | Model Garden: 200+ models incl. Claude |
| Agents | Managed Agents (preview), Interactions API | Agent Runtime, Agent Studio, Memory Bank, Agent Registry |

Sources: model cards above; https://pasqualepillitteri.it/en/news/1311/gemini-enterprise-agent-platform-google-next-2026 and https://www.bain.com/insights/google_cloud_next_2026_the_agentic_enterprise_control_plane_comes_into_view/ (3P). M.

New default to flag: "Generate Content storage" turned **on by default for new paid-tier projects** on 2026-10-26 (1P changelog). Worth checking against customer data-handling policies. H. PERISHABLE.

### 2b. Context caching (1P: https://aistudio.google.com/docs/caching , pricing page)

- **Implicit caching**: on by default for Gemini 2.5 and newer; savings passed through automatically. Minimum 4,096 tokens for Gemini 4, 3.8/3.6 Flash, 3.1 Pro; 2,048 for 2.5. Gemini 4 agent loops cache the full prior request only if the new request adds at least 2,050 tokens. H.
- **Explicit caching**: create/manage cache objects, pay storage per hour (for example 3.8 Flash $0.50 per 1M tokens per hour, 3.1 Pro $4.50). **Not available for Gemini 4 or in the Interactions API.** H.
- Discount: cached reads are 90% off on Gemini 3.x (for example 3.8 Flash $0.075 vs $0.75) and 95% off on Gemini 4 per the Argon post ($0.10 vs $2.00). H.
- Compare Claude: explicit `cache_control` breakpoints, 90% read discount, write premium; no storage-per-hour fee. (A; general knowledge, verify with the claude-api skill before quoting.) M.

### 2c. Batch, tiers, grounding, tools (1P pricing page)

- **Batch**: 50% off standard on all main text models. H.
- **Grounding with Google Search** (Gemini 3 and newer): 5,000 prompts/month free, then **$14 per 1,000** queries; daily cap 1,500. Google Maps grounding same rate. Agent Platform 3.8 Flash also offers Parallel Web Search and Exa as grounding sources (1P model card). H.
- Code execution: no tool fee, billed as tokens. URL context and File Search: tokens plus embedding cost. H.
- Managed Agents / Antigravity Agent: model tokens at list price; **sandbox compute not billed during preview** (PERISHABLE). H.
- Webhooks for batch and long-running operations (2026-05-04). H.
- Interactions API is Google's "primary interface" for models and agents; breaking schema change in May 2026 (`outputs` to `steps`, `response_format`). https://blog.google/innovation-and-ai/technology/developers-tools/interactions-api-general-availability (1P). M.
- Structured output: supported across Gemini 4 and 3.x (model cards). H.

### 2d. Live API

Gemini 3.8 Live is GA with a thinking-level setting (2026-09-15). Native bidirectional audio and video. Claude has no equivalent realtime speech-to-speech API. H.

---

## 3. Agent stack

### 3a. Agent Development Kit (ADK)

- Languages (1P https://adk.dev/): **Python, TypeScript, Go, Java, Kotlin**. ADK TypeScript 2.0 GA announced on the docs home. H.
- Licence: **Apache 2.0** (https://github.com/google/adk-python , 22.2k stars). H.
- ADK 2.0 adds graph workflows (routes, human input, retries, dynamic workflows), Skills for agents, an Agents CLI, context compaction, model context caching (1P). H.
- Model-agnostic: adapters for Claude, OpenAI, Ollama, vLLM, LiteLLM, Gemma, Apigee AI Gateway (1P). H.
- MCP: consume MCP tools and expose an agent as an MCP server. A2A: expose and consume agents in Python, Go, Java, Kotlin (1P). H.
- Deploy: Agent Runtime, Cloud Run, GKE, or self-host (1P). H.
- Scale claim: ADK processes 6 trillion+ tokens/month on Gemini (1P via Bain, 3P). M.

### 3b. Agent Runtime (ex-Vertex AI Agent Engine) - PERISHABLE

- About **$0.085 per vCPU-hour** and **$0.009 per GiB-hour**; free tier about 50 vCPU-hours and 100 GiB-hours/month; idle time between turns not billed; Memory Bank storage $0.30 per GiB-month. Official pricing page too large to fetch; figures from a Google-hosted PDF and secondaries: https://services.google.com/fh/files/emails/b_502770571_gemini_enterprise_agent_platform_pricing.pdf , https://www.beri.net/article/agentcore-vs-agent-engine-vs-foundry-agent-service-pricing-runtime-memory-tools-2026 . M.
- Billing changes during 2026 (SKU consolidation 2026-06-17; "Semantic Governance" charge from 2026-08-01) reported by secondaries only. L.

### 3c. Managed Agents in the Gemini API (closest analogue to Claude Managed Agents)

- Preview since 2026-05-19. One Interactions API call provisions a Google-hosted Linux sandbox running the **Antigravity agent harness**; sessions resume with files intact; customise with **AGENTS.md and SKILL.md**. Current agent ID `antigravity-preview-09-2026` (changed tool names in Sept). Also in preview on Agent Platform. 1P: https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api ; https://aistudio.google.com/docs/changelog . H.
- Note the convergence: Google adopted SKILL.md (Anthropic's Agent Skills format) and AGENTS.md (OpenAI-originated, now AAIF). H.

### 3d. Gemini Enterprise (ex-Agentspace) - the employee-facing agent product

- Editions: Business (1-500 users, no GCP console needed), Standard, Plus, **Pay-as-you-go**, Frontline (needs 150+ Standard/Plus seats). https://docs.cloud.google.com/gemini/enterprise/docs/editions (1P). H.
- Prices are not on Google's docs page. Launch price (Oct 2025) $30/seat/month for Standard and Plus; Business about $21. 3P only: https://techcrunch.com/2025/10/09/google-ramps-up-its-ai-in-the-workplace-ambitions-with-gemini-enterprise , https://dupple.com/learn/gemini-enterprise-pricing . A UK G-Cloud document (Jan 2026) lists Business $25, Standard $35, Frontline $15. L. PERISHABLE.
- Pay-as-you-go with project spend caps and 50/80/100% alerts; 10% / 20% discount for 1-year / 3-year spend commits (2026-08). https://www.shopifreaks.com/google-adds-pay-as-you-go-pricing-and-project-spend-caps-to-gemini-enterprise-as-agent-workloads-outrun-seat-based-budgets/ (3P). M.
- **Claude inside Gemini Enterprise**: admins can enable **Claude Opus 5.5 and Claude Sonnet 5.5**, billed pay-as-you-go; seat credits apply only to Gemini models (1P editions page). H.
- Data residency `us`, `eu`, `global`; VPC-SC, CMEK, Access Transparency, Cloud Audit Logs (1P). H.

### 3e. Protocols

- **A2A**: v1.0 shipped March 2026 (multi-protocol bindings, version negotiation, multi-tenancy, signed agent cards). Joined **AAIF (Linux Foundation)** 2026-08-17, sitting next to MCP, AGENTS.md, goose. 150+ backing orgs; IBM's ACP merged in Aug 2025. https://aaif.io/blog/a2a-joins-aaif ; https://axios.com/2026/08/17/a2a-agentic-ai-foundation-open-ai-standards (3P). H.
- **MCP**: 50+ Google-managed remote MCP servers GA or preview (BigQuery, Spanner, AlloyDB, Cloud SQL, GKE, Cloud Run, Logging, Workspace Gmail/Drive/Calendar/Chat, Maps, Security Operations), with IAM Deny policies, Model Armor, OpenTelemetry and **Agent Registry**. Google names Claude as a compatible client. https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone (1P, 2026-04-29). H.
- **AP2 (Agent Payments Protocol)**: launched Sep 2025; Google donated it to the **FIDO Alliance** (reported 2026-04-30); v0.2 adds autonomous purchases. https://www.paymentsjournal.com/google-donates-its-agentic-payments-protocol-to-the-fido-alliance/ (3P). M. Relevance to most enterprise Claude conversations: low.

---

## 4. Coding tools

| Product | Status as of 2026-11-14 | Source | Conf |
|---|---|---|---|
| **Antigravity** (2.0 desktop app, Antigravity CLI `agy`, Antigravity SDK, Antigravity in Agent Platform) | Google's single coding harness since I/O 2026-05-19. Desktop app runs parallel agents, dynamic subagents, scheduled background tasks | https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/ (1P) | H |
| **Gemini CLI** | Apache 2.0 repo remains; only for Code Assist Standard/Enterprise, Code Assist for GitHub on GCP, and paid API keys. README says not tuned for Gemini 4+ | https://github.com/google-gemini/gemini-cli (1P) | H |
| **Jules** | Read-only since 2026-11-11, shut down 2026-12-31; export via Jules Tools | https://jules.google/docs/changelog/ (1P) | H |
| **Gemini Code Assist** IDE extensions | Stopped for AI Pro/Ultra and free individuals 2026-06-18; Standard/Enterprise continue. List price Standard $19 (annual) / $22.80 (monthly); Enterprise $45 / $54 per user/month | Developers Blog (1P); price via search of cloud.google.com/products/gemini/pricing (page not fully fetched) | H / M |

### Antigravity vs Claude Code - shape comparison

| Concern | Antigravity CLI / 2.0 | Claude Code |
|---|---|---|
| Context file | AGENTS.md (priority) and GEMINI.md both read; workspace config moved `.gemini/` to `.agents/` (3P guides, conflicting) | CLAUDE.md |
| Skills | `.agents/skills/` SKILL.md (1P plugins doc) | `.claude/skills/` SKILL.md |
| Extensions | "Plugins" bundle skills, subagents, rules, MCP, hooks (1P https://www.antigravity.google/docs/cli/plugins); `agy` imports Gemini CLI extensions | Plugins bundle skills, agents, hooks, MCP |
| Subagents | Yes; `/agents` panel to view/approve (1P) | Yes |
| Hooks | Yes (1P transition post) | Yes |
| Sandboxing | Gemini CLI had container `--sandbox`; Antigravity CLI sandbox details not found | OS-level sandbox, permission modes |
| Models | Gemini 4 Carbon/Argon/Hydrogen, 3.8 Flash; **Claude Opus 5.5 and Sonnet 5.5 (Thinking)** on AI Pro (non-trial), Ultra, Enterprise; GPT-OSS-120b. "Orchestrator" pairs Carbon/Argon planner with Hydrogen executor | Claude models only |
| Open source | Antigravity CLI **not open source** (The Register 2026-05-20) | Not open source |
| Pricing | Bundled in Google AI plans: AI Pro about $20; AI Ultra $100 (5x Pro) and $200 (20x Pro) from 2026-05-19; overage credits $25 per 2,500 | Claude Pro/Max/Team/Enterprise or API |

Sources: models table https://antigravity.google/docs/models (1P, undated; Claude 4.6 and GPT-OSS removal set for 2026-11-18, PERISHABLE); pricing https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/ (1P, $100 tier) and https://www.theregister.com/2026/03/12/users_protest_as_google_antigravity/ (3P); open-source status https://www.theregister.com/ai-ml/2026/05/20/bye-bye-gemini-cli-google-nudges-devs-toward-antigravity/5243605 (3P). Config-path details M/L.

Customer friction (3P): quota complaints ("weekly quota after a couple of requests") on the Antigravity CLI tracker; community anger that open-source Gemini CLI contributions fed a closed product (The Register). M.

---

## 5. Enterprise

### 5a. Claude on Google Cloud - two offerings (A, H)

| | Google managed (Model Garden, `AnthropicVertex`) | Anthropic managed (Marketplace, `AnthropicGoogleCloud`, `claude.googleapis.com`) |
|---|---|---|
| Operator / processor | Google | Anthropic (some trust-and-safety processing outside GCP) |
| Billing | GCP, as Agent Platform usage | GCP Marketplace |
| Rate limits | Google | Anthropic |
| Endpoints | Global; multi-region `us`/`eu`; regional. **Regional and multi-region cost 10% more**; regional endpoints only serve **Sonnet 4.6 and earlier** | `global` location; `inference_geo: "us"` for US-only inference |
| Not supported | Files API, URL image/doc sources, **code execution, web fetch, advisor tool, Agent Skills, MCP connector, programmatic tool calling, Message Batches, Models/Admin/Usage APIs, Claude Managed Agents**, server-side fallback | Pre-built self-hosted sandbox workers only |
| Supported | Messages, prompt caching, thinking, tool use (bash, browser use, computer use, memory, text editor, web search), citations, structured outputs, fast mode, 1M context on current models | Skills, batch, code execution, Files, MCP connector (beta), **Claude Managed Agents** (beta features), data residency, OpenTelemetry |
| Compliance note | FedRAMP High via Agent Platform (Google page) | ZDR on request |

Models on Google managed (A): Fable 5.2 / 5.1 / 5; Mythos 5.2 / 5.1 / 5 (limited availability); Opus 5.5, 5, 4.8, 4.7, 4.6, 4.5; Sonnet 5.5, 5, 4.6; Haiku 5.5, 4.5; plus deprecated 4.x. 30 MB request payload limit. Sources: https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/google-managed ; https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/overview ; https://platform.claude.com/docs/en/build-with-claude/claude-models-on-google-cloud/anthropic-managed ; https://docs.cloud.google.com/vertex-ai/generative-ai/docs/partner-models/claude . PERISHABLE (feature lists move monthly).

Advisor message: a GCP-committed customer no longer has to accept the old Vertex feature gap. The Anthropic-managed Marketplace offering burns down GCP commit and carries Skills, Files, batch, code execution and Managed Agents. H.

### 5b. Workspace with Gemini

- Gemini folded into Workspace business plans in 2025 with price rises (Business Standard about $14/user/month annual). 3P: https://www.constellationr.com/insights/news/google-workspace-drops-gemini-add-charge-raises-business-enterprise-plan-prices . M.
- **AI Expanded Access** add-on (Feb 2026) raises Gemini app, NotebookLM and Flow limits for Business/Enterprise Standard and Plus. https://workspaceupdates.googleblog.com/2026/02/google-workspace-ai-expanded-access.html (1P). M (price not found).
- Hydrogen powers Gemini in Sheets for eligible business plans (1P Hydrogen post). H.

---

## 6. Learning and credentials

| Item | Facts | Source | Conf |
|---|---|---|---|
| Generative AI Leader | **$99, 90 min, 50-60 MCQ**, English/Japanese/Spanish, valid 3 years, no prerequisites, "for anyone in any job role, with or without hands-on technical experience" | https://cloud.google.com/learn/certification/generative-ai-leader (1P) | H |
| Professional ML Engineer | **$200, 2 hours, 50-60 MCQ/multi-select**, English/Japanese, 3+ years experience recommended; exam guide v3.1 includes gen AI with Model Garden and Agent Builder | https://cloud.google.com/learn/certification/machine-learning-engineer (1P) | H |
| **Professional Agentic Architect** (new) | **$200, 2 h, 50-60 MCQ**, then hands-on Google Skills labs for those who pass; English; **valid 1 year**; 3+ years cloud plus 1+ year building agents on GCP recommended. Announced 2026-11-11 (beta reportedly from 2026-09-08, L) | https://cloud.google.com/learn/certification/agentic-architect ; https://blog.google/innovation-and-ai/infrastructure-and-cloud/google-cloud/professional-agentic-architect (1P) | H |
| GEAR (Gemini Enterprise Agent Ready) | Launched 2026-02-11 inside the Google Developer Program; free to join; **35 learning credits per month** on Google Skills; paths "Introduction to Agents" and "Develop Agents with ADK"; "Get Certified" cohort for customers; partner specialist track | https://cloud.google.com/blog/products/ai-machine-learning/gear-program-now-available ; https://developers.google.com/program/gear (1P) | H |
| "Develop Agents with Agent Development Kit (ADK)" path | Path page says **8 activities**; covers setup, agent logic, tools, memory, MCP; skill badge lab "Engineer AI Agents with ADK". Activity list did not render; a dedicated MCP lab not confirmed. Related separate course "Build Collaborative Multi-Agent Systems with ADK & MCP" (30 min) | https://www.skills.google/paths/3545 (1P) | M |

Cloud Skills Boost is now branded **Google Skills** (skills.google). H.

### Starter-note claims

| Claim | Verdict | Evidence |
|---|---|---|
| "Google GEAR programme gives 35 free monthly credits" | **True** | GEAR page and Google Cloud blog: 35 monthly learning credits, free to join. H |
| "ADK path has eight activities, a skill badge, an MCP lab" | **Mostly true; MCP lab unverified** | 8 activities and a skill-badge lab confirmed on the path page; MCP is a covered topic, but a lab specifically on MCP could not be confirmed (one search snippet said 7 activities; path updated about 3 weeks ago). M |
| "Generative AI Leader $99, 90 min, non-technical" | **True** | $99, 90 min; "with or without hands-on technical experience". H |
| "Professional ML Engineer $200, 2 h" | **True** | $200, two hours. H |
| "ADK has the widest language range among agent SDKs" | **True among first-party vendor agent SDKs, with caveats** | ADK: Python, TS, Go, Java, Kotlin (5). Claude Agent SDK: Python, TS. OpenAI Agents SDK: Python, TS. Microsoft Agent Framework: .NET, Python, Go (preview). Community frameworks (LangChain/LangGraph Python+JS; Spring AI Java) are narrower individually. Claude's *client* SDKs cover more languages, and Claude Managed Agents is reachable from all client-SDK languages via REST, so "widest" holds only for in-process agent frameworks. M |

---

## 7. Benchmarks and honest comparison

### 7a. Third-party (3P)

| Board | Result | Source / date | Conf |
|---|---|---|---|
| Artificial Analysis Intelligence Index | 1 Claude Fable 5.2 Max 65; **2 Gemini 4 Carbon High 60**; 3 Claude Opus 5.5 Max 59; 4 GPT-6 Astra 57; 6 Sonnet 5.5 Max 55; 7 Hydrogen xhigh 54; 9 Argon High 50; 3.8 Flash 31 | https://artificialanalysis.ai/leaderboards/models (2026-11-14) | H |
| Artificial Analysis cost per task | Carbon $5.48 vs Opus 5.5 $10.04 vs Fable 5.2 $26.54; Hydrogen $3.16 | same | H |
| Arena (ex-LMArena) Text | **1 Gemini 4 Carbon 1526 (preliminary), 2 Argon 1522**; Claude Opus 5.5 4th 1507 | https://arena.ai/leaderboard/text (2026-11-11) | H |
| Arena WebDev | 1 Claude Fable 5.2 1838, 2 Opus 5.5 1815, 3 Sonnet 5.5 1772, **4 Carbon 1768**; Argon 13th | https://arena.ai/leaderboard/webdev (2026-11-11) | H |
| Arena Agent | 1 Fable 5.2 30.5%, 2 Opus 5.5 19.5%, **3 Carbon 16.9%**, 5 Hydrogen 14.8%; Claude holds 5 of top 10 | https://arena.ai/leaderboard | H |
| Arena Text-to-Video | **Google top 3 (Omni 1.2/1.1/Flash)**; Veo 3.1 now 14th | https://arena.ai/leaderboard/video/text-to-video (2026-11-08) | H |
| Arena Text-to-Image | OpenAI top 5; **Nano Banana 2.1 7th** | https://arena.ai/leaderboard/text-to-image (2026-11-12) | H |
| Terminal-Bench 4.0 | Opus 5.5 64.8%, Sonnet 5.5 61.8% top; no Gemini entries in mirror; official tbench.ai table did not render | https://www.developersdigest.tech/benchmarks/terminal-bench (as of 2026-10-17) | L |
| SWE-bench Verified | Saturated (top scores 95-97%, all Claude); Vals stopped running it; Google does not report it for Gemini 4 | https://www.vals.ai/benchmarks/swebench-2025-09-24 ; https://llm-stats.com/benchmarks/swe-bench | M |

### 7b. Google-reported (1P, unverified)

- Argon: DeepSWE v1.1 77.9%; AutomationBench 51.3% (#1); LVBench 91.7%; CWE-bench v1 68%. No Claude comparisons named.
- Carbon: #1 CursorBench 4.0, Perplexity WANDR, Zapier AutomationBench at ">2X lower cost per task than the next best external model"; per-attempt breach rate 0.8% vs Argon 3.1%.
- Hydrogen: AA Index 51 at high (54 xhigh); Terminal-Bench 4.1 57% vs 18.2% for 3.8 Flash; HLE-Diamond 58.8%; 5x fewer fabricated claims than 3.8 Flash.
- Pattern: Google cites partner/vertical benchmarks (Cursor, Zapier, Vals, Harvey, Hebbia) and never names Claude. Say so on air.

### 7c. Where Google is genuinely stronger

1. **Multimodal breadth** - video gen (Arena #1-3), realtime voice (Live API), TTS, STT, music, multimodal embeddings, long-video understanding. Claude has none of these as first-party APIs. H.
2. **Price per unit of intelligence** - Carbon second on AA Index at about half Opus 5.5's cost per task; Hydrogen $1.50/$7.50 flat to 1M. But note 2x price rises on 2026-12-01 and 2027-01-01. H. PERISHABLE.
3. **Text Arena preference** - Gemini 4 holds #1 and #2. H.
4. **Platform gravity** - Workspace, BigQuery, 50+ managed MCP servers, Search/Maps grounding, data residency per model, TPU capacity. M.
5. **Open weights** - Gemma 4 under Apache 2.0. H.
6. **Breadth of agent SDK languages** - ADK in five languages. H.

### 7d. Where Claude is stronger

1. **Agentic coding and agent tasks** - Claude holds #1-3 on Arena WebDev and #1-2 on Arena Agent; tops AA Index (Fable 5.2); tops available Terminal-Bench 4.0 mirror. H/M.
2. **Product stability** - Google killed or rebranded Gemini CLI (for most users), Jules, Code Assist individual, Vertex AI, Agentspace, Imagen and Veo within 2026; Flash versions reroute every 1-2 months. Inferred from 1P changelog and notices. H on facts, opinion is ours.
3. **Context engineering control** - explicit prompt caching works on every current Claude model; Gemini 4 drops explicit caching. H.
4. **Harness maturity and openness of format** - Google adopted SKILL.md and AGENTS.md; Antigravity offers Claude Opus/Sonnet 5.5 inside Google's own coding tool. H.
5. **Multi-cloud** - Claude on AWS, Google Cloud (two ways) and Azure; Gemini only on Google. M (Azure/AWS not re-verified here).

### 7e. How customers actually choose (synthesis; M)

- GCP-committed + Workspace shop: Gemini Enterprise for employees, Claude for coding and hard agent work via Model Garden or the Anthropic-managed Marketplace listing (both burn GCP commit). Gemini Enterprise itself can expose Opus/Sonnet 5.5.
- Media, voice, video, contact-centre: Gemini Live / Omni / TTS lead; Claude needs third-party speech.
- Cost-sensitive high-volume extraction: Flash-Lite tiers ($0.10-$0.30 input) vs Haiku; check the 2027 Flash price doubling.
- Regulated, needs data residency per region: Agent Platform model cards publish ML-processing regions; Claude-on-Google regional endpoints only reach Sonnet 4.6 and older.

---

## 8. PERISHABLE watch list (next three months)

| Date | Event |
|---|---|
| 2026-11-18 | Claude 4.6 models and GPT-OSS-120b removed from Antigravity |
| 2026-11-30 / 12-01 | Gemini 4 Carbon and Argon intro pricing ends; list doubles to $4/$20. 2.5 Pro/Flash reroute |
| 2026-12-03 | Omni 1.1 Flash reroutes to 1.2 |
| 2026-12-31 | Jules shut down; 3.8/3.6 Flash and TTS promo prices end |
| 2027-01-01 | 3.8/3.6 Flash to $1.50/$7.50; TTS prices double |
| Ongoing | Managed Agents sandbox compute free during preview; Gemini Enterprise seat prices unpublished; Agent Runtime pricing consolidation; Arena preliminary scores for Carbon/Hydrogen |
