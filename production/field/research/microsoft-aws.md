# Microsoft and AWS: competitor and channel fact sheet

As of 2026-11-14. Every row carries a source, the date it was checked or the page date, and a confidence rating.

**Key**
- **Confidence:** H = primary vendor page read directly, M = primary source partly read or one vendor page plus consistent press, L = third-party only or sources conflict.
- **Source type:** 1P = first-party (Anthropic, Microsoft, AWS, GitHub docs and blogs). 3P = press, trackers, training vendors.
- **PERISHABLE** = likely to change before mid-February 2027.
- Model names (Opus 5.5, Fable 5.2, Mythos and so on) are as they appear on the vendor pages on 2026-11-14.

---

## Part A - Microsoft

### A1. Claude in Microsoft Foundry

| # | Fact | Conf | Source (type, as-of) |
|---|------|------|------|
| A1.1 | Claude reached GA in Foundry on 29 June 2026 (3P reports). Hosted-on-Azure launched first with Opus 4.8 and Haiku 4.5. | M | [Redmond Mag 2026-07-02](https://redmondmag.com/articles/2026/07/02/anthropic-claude-goes-ga-in-microsoft-foundry.aspx), [InfoQ](https://infoq.com/news/2026/07/claude-foundry-ga-europe/) (3P) |
| A1.2 | There are **two hosting options**. "Hosted on Azure" is Anthropic-operated and runs on Azure infrastructure. Prompts and completions stay in Azure; only usage metadata and content flagged by safety systems go to Anthropic. "Hosted on Anthropic" runs on Anthropic infrastructure, and data may be processed outside the selected Azure geography. | H | [Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/claude-in-microsoft-foundry) (1P, 2026-11-14); [MS Learn hosting comparison](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-hosting-comparison) (1P, page 2026-09-21) |
| A1.3 | **Hosted on Azure** serves Opus 5.5, Opus 5, Opus 4.8, Sonnet 5.5, Sonnet 5, Haiku 5.5 and Haiku 4.5. **Hosted on Anthropic only** serves Fable 5 / 5.1 / 5.2, Mythos 5 / 5.1 / 5.2 (limited availability, Entra ID auth required), Opus 4.5-4.7 and Sonnet 4.5-4.6. PERISHABLE | H | Anthropic docs (1P, 2026-11-14) |
| A1.4 | Endpoint: `https://{resource}.services.ai.azure.com/anthropic/v1/messages`. It speaks the native Messages API shape. Auth is an API key or Entra ID. SDKs: `AnthropicFoundry` (Python), `@anthropic-ai/foundry-sdk`, `Anthropic.Foundry` (C#), plus Go, Java, PHP and Ruby. | H | Anthropic docs (1P) |
| A1.5 | **Not supported on Foundry under either hosting option:** Admin API, Advisor tool, **Claude Managed Agents**, Compliance API, Models API, **Message Batches API**, server-side fallback, user profiles. | H | Anthropic docs (1P, 2026-11-14) |
| A1.6 | **Also missing when Hosted on Azure:** code execution, web search and web fetch beyond the basic `20250305`/`20250910` versions, **Agent Skills**, programmatic tool calling and the **Files API**. These calls return a 400. Microsoft summarises Azure-hosted support as "Messages, Token counting" only. Claude Code detects Azure hosting and adapts. | H | Anthropic docs; MS Learn hosting comparison (1P) |
| A1.7 | Deployment types: Global Standard, or US Data Zone Standard (Azure-hosted only). US Data Zone is priced at **1.1x**, the same as `inference_geo: "us"` on the first-party API. **No EU Data Zone** is listed. | H | [Anthropic pricing](https://platform.claude.com/docs/en/about-claude/pricing) (1P) |
| A1.8 | Billing goes through Azure Marketplace in **Claude Consumption Units (CCU)**, at $0.01 per CCU. Usage is rated at Anthropic list prices, the private-offer discount is applied, and the result is metered hourly and invoiced monthly in arrears. There is no prepaid balance. | H | Anthropic pricing; [MS Learn CCU billing](https://learn.microsoft.com/en-us/azure/foundry/foundry-models/concepts/claude-models-billing) (1P, page 2026-10-22) |
| A1.9 | **CCU is MACC-eligible.** Spend decrements the Microsoft Azure Consumption Commitment. "CCU billed by other cloud providers doesn't decrement your MACC." | H | MS Learn CCU billing (1P) |
| A1.10 | Subscription types that **cannot** buy Claude: free trial, student, credit-based, Enterprise accounts in South Korea, and **CSP subscriptions**. The CSP exclusion matters for partner-resold Azure. | H | MS Learn hosting comparison (1P) |
| A1.11 | Under both hosting options, Anthropic is seller of record, data processor and SLA provider, and Microsoft provides support. Claude is a "Non-Microsoft Product" under the Product Terms. | H | MS Learn hosting comparison (1P) |
| A1.12 | Foundry does not return Anthropic rate-limit headers. Quota goes through the Azure quota form. | H | Anthropic docs (1P) |
| A1.13 | Fast mode is available on Foundry for Opus 5.5 (Azure-hosted) and Fable 5.2 (Anthropic-hosted). | H | Anthropic pricing (1P) |

### A2. Rest of Foundry: Azure OpenAI and Foundry Agent Service

| # | Fact | Conf | Source |
|---|------|------|------|
| A2.1 | GPT-5.5 has been GA in Foundry since spring 2026 (model version 2026-04-24). Region and quota gaps were reported on Microsoft Q&A. PERISHABLE | M | [Azure blog](https://azure.microsoft.com/en-us/blog/openais-gpt-5-5-in-microsoft-foundry-frontier-intelligence-on-an-enterprise-ready-platform) (1P); MS Q&A (1P community) |
| A2.2 | Foundry Agent Service offers three agent types: **prompt agents** (declarative, Foundry runs them), **voice-based prompt agents** (preview parts) and **hosted agents** (your container or .zip). Hosted agents can be built with Agent Framework, LangGraph, the OpenAI Agents SDK, the "Anthropic Agent SDK", the Copilot SDK or custom code. | H | [MS Learn Agent Service overview](https://learn.microsoft.com/en-us/azure/foundry/agents/overview) (1P, page 2026-10-26) |
| A2.3 | **Toolboxes** expose a curated tool set as one managed MCP endpoint. Agents can connect to remote MCP servers using key, Entra managed identity, OAuth OBO or no auth. | H | Same (1P) |
| A2.4 | **A2A v1.0 is GA** in Foundry Agent Service; v0.3 stays in preview. Agents publish to Teams, Microsoft 365 Copilot and the Entra Agent Registry. | H | Same (1P) |
| A2.5 | Prompt agents can opt into a "Microsoft Copilot harness" (preview) for multi-step tool, skill, file and command workflows. | H | Same (1P) |
| A2.6 | It is not confirmed whether Claude deployments can back a Foundry *prompt* agent. A community Q&A says no for the classic create_agent API, while 2025 Microsoft posts listed Claude in Agent Service. Check the `agentsv2` filter in the model catalog. | L | [MS Q&A](https://learn.microsoft.com/en-us/answers/questions/5861158/) (1P community); [Tech Community 2025](https://techcommunity.microsoft.com/blog/azure-ai-foundry-blog/expanded-models-available-in-microsoft-foundry-agent-service/4471180) |
| A2.7 | Hosted agents GA: a Message Center notice dated 2 June 2026 says GA, but a 7 July devblog recap treats GA as still pending. | L | [AZ563596](https://mc.merill.net/message/AZ563596) (1P mirror); [devblogs June recap](https://devblogs.microsoft.com/foundry/whats-new-in-microsoft-foundry-june-2026/) |

### A3. Microsoft Agent Framework

| # | Fact | Conf | Source |
|---|------|------|------|
| A3.1 | It is the **direct successor to Semantic Kernel and AutoGen**, built by the same teams. It combines AutoGen's agent abstractions with SK's state, type safety, middleware and telemetry, and adds graph-based workflows. | H | [MS Learn overview](https://learn.microsoft.com/en-us/agent-framework/overview/) (1P, page 2026-10-23) |
| A3.2 | **Languages: .NET (C#), Python and Go.** Go is in **public preview**, needs Go 1.26+ and lacks declarative agents, CodeAct and functional workflows. The Go preview was announced on 10 July 2026. | H | MS Learn overview (1P); [Go devblog](https://devblogs.microsoft.com/go/microsoft-agent-framework-for-go-public-preview/) (1P) |
| A3.3 | **Licence: MIT.** The repo has about 14.7k stars. The Go SDK lives in a separate repo, `microsoft/agent-framework-go`. | H | [GitHub](https://github.com/microsoft/agent-framework) (1P, 2026-11-14) |
| A3.4 | **Five orchestration patterns:** Sequential, Concurrent, Handoff, Group Chat and Magentic (a manager agent coordinates specialists). Human-in-the-loop works through tool approval. | H | [MS Learn orchestrations](https://learn.microsoft.com/en-us/agent-framework/workflows/orchestrations/) (1P) |
| A3.5 | 1.0 GA for .NET and Python landed in early April 2026 (3P sources disagree between 2 and 3 April). Orchestrations reached 1.0 in both languages later. | M | [Visual Studio Magazine 2026-04-06](https://visualstudiomagazine.com/articles/2026/04/06/microsoft-ships-production-ready-agent-framework-1-0-for-net-and-python.aspx) (3P) |
| A3.6 | It ships MCP clients, A2A hosting samples, a "Harness Agent" (planning and todos, context compaction, file access and memory, tool approval) and an Anthropic model provider. | H | MS Learn overview; GitHub (1P) |
| A3.7 | 3P reports say Build 2026 (2-3 June) moved the Harness and the **Claude Agent SDK and GitHub Copilot SDK connectors** to stable. | L | [InfoQ 2026-08](https://infoq.com/news/2026/08/agent-framework-harness-ga) (3P) |

**Verify: "Microsoft Agent Framework supports .NET, Python and Go (preview), five orchestration patterns, MIT"** - **CONFIRMED** (H).

### A4. Copilot stack

| # | Fact | Conf | Source |
|---|------|------|------|
| A4.1 | **Anthropic is a Microsoft subprocessor.** Under it, Claude in Microsoft 365 Copilot is covered by the Microsoft Product Terms and DPA, Enterprise Data Protection and the Customer Copyright Commitment. | H | [MS Learn: Claude in Microsoft Online Services](https://learn.microsoft.com/en-us/copilot/microsoft-365/connect-to-ai-subprocessor) (1P, page 2026-11-04) |
| A4.2 | Claude is **on by default** in commercial cloud **except EU/EFTA and UK**, where the default is "No users". Surfaces: Microsoft Copilot, Researcher, Copilot Studio, Power Platform and Copilot in Microsoft 365 apps. | H | Same (1P) |
| A4.3 | Claude in Copilot is **currently excluded from the EU Data Boundary** and from in-country processing commitments. | H | Same (1P) |
| A4.4 | Message Center MC1546438 says processing moves into the EU Data Boundary in early December 2026, and Claude becomes **on by default for EU/EFTA tenants from 9 Dec 2026**. Admins can opt out before that date. PERISHABLE | M | [MC1546438 mirror](https://mc.merill.net/message/MC1546438) (1P via 3P mirror) |
| A4.5 | GCC non-federal customers got a Claude opt-in on 22 July 2026. Claude is not available to GCC federal, GCC High, DoD or sovereign clouds. | H | MS Learn subprocessor page (1P) |
| A4.6 | **Fable-class and Mythos-class models** may come as "Anthropic models with Data Retention". These are off by default everywhere. When enabled, Anthropic is an independent processor under its own terms and retains inputs and outputs for up to 30 days (longer for flagged content). Fable 5.1 is available under subprocessor terms for some organisations. | H | Same (1P) |
| A4.7 | **Copilot Cowork** reached GA on 16 June 2026 after a Frontier preview that started 30 March 2026. It runs on **Anthropic models (Opus 4.8, Sonnet 4.6 named)**, with GPT 5.5 in Frontier and a Microsoft "Cowork 1" model announced as coming. It requires the Microsoft 365 Copilot licence and is billed in Copilot Credits at $0.01 each. Microsoft says more than half of the Fortune 500 use it. | H | [Microsoft Copilot blog 2026-06-16](https://www.microsoft.com/en-us/copilot/blog/2026/06/16/copilot-cowork-is-now-generally-available/) (1P) |
| A4.8 | Microsoft claims Copilot Cowork was **30-40% cheaper per prompt than Claude Cowork** with its Microsoft 365 connector. The test was internal: 125 runs, 12 prompts, both on Opus 4.8. Treat this as vendor marketing. | H (that Microsoft claims it) | Same (1P) |
| A4.9 | **Microsoft 365 E7** costs $99/user/month on annual billing ($90.45 without Teams). It bundles Microsoft 365 Copilot, Agent 365, Entra Suite and E5, and went on sale 1 May 2026. Agent 365 standalone is $15/user/month. | H | [MS enterprise plans](https://www.microsoft.com/en-us/security/pricing/enterprise-plans); [Agent 365 GA blog 2026-05-01](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) (1P) |
| A4.10 | In Copilot Studio, makers choose the model per agent, and Power Platform admin center adds a second control layer. MCP is GA in Copilot Studio (date not confirmed). | M | MS Learn subprocessor page; [Copilot Studio MCP GA blog](https://www.microsoft.com/en-us/microsoft-copilot/blog/copilot-studio/model-context-protocol-mcp-is-now-generally-available-in-microsoft-copilot-studio) (1P) |

### A5. GitHub Copilot vs Claude Code

| # | Fact | Conf | Source |
|---|------|------|------|
| A5.1 | Claude models listed GA in GitHub Copilot: Fable 5 / 5.1 / 5.2, Opus 5.5, Opus 5, Opus 4.8 (plus a fast-mode preview), Sonnet 5.5, Sonnet 5, Sonnet 4.6, Haiku 5.5 and Haiku 4.5. Fable models need an admin to enable them, and Anthropic retains data by default. ZDR is available only under a time-bound exemption to end-2026. The 1M context window works only in VS Code and Copilot CLI. PERISHABLE | M | [GitHub docs: supported models](https://docs.github.com/en/copilot/reference/ai-models/supported-models) (1P, read 2026-11-14, first 100k chars) |
| A5.2 | **Usage-based billing started 1 June 2026.** Premium requests were replaced by GitHub AI Credits, metered on tokens at each model's API rates. Included credits equal the plan price: Pro $10, Pro+ $39, Business $19/user, Enterprise $39/user. Completions and Next Edit stay free. Annual Pro and Pro+ plans stay on premium requests until renewal. | H | [GitHub blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) (1P) |
| A5.3 | **Agent HQ:** Claude and Codex coding agents reached public preview for Pro+ and Enterprise on 4 Feb 2026, then Business and Pro on 26 Feb 2026. The Agent Control Plane is GA. Security validation for third-party agents went GA on 9 June 2026. Claude became an agent provider preview in JetBrains IDEs on 22 June 2026. | H | [Changelog 02-04](https://github.blog/changelog/2026-02-04-claude-and-codex-are-now-available-in-public-preview-on-github/), [02-26](https://github.blog/changelog/2026-02-26-claude-and-codex-now-available-for-copilot-business-pro-users/), [06-09](https://github.blog/changelog/2026-06-09-security-validation-for-third-party-coding-agents/), [06-22](https://github.blog/changelog/2026-06-22-new-features-and-claude-as-agent-provider-preview-in-jetbrains-ides/) (1P) |
| A5.4 | Copilot code review added agent skills and MCP (GA 29 July 2026). | H | [Changelog](https://github.blog/changelog/2026-07-29-copilot-code-review-agent-skills-and-mcp-now-generally-available/) (1P) |
| A5.5 | Framing: GitHub Copilot is now a **multi-agent, multi-model marketplace** that resells Claude models and hosts the Claude agent. Claude Code is the first-party harness. Copilot sells governance and seat consolidation. Claude Code sells same-day features and the full harness (Skills, hooks, subagents, plugins). | - | Analysis |

### A6. Microsoft credentials

| # | Fact | Conf | Source |
|---|------|------|------|
| A6.1 | **AI-103: "Developing AI Apps and Agents on Azure"** leads to **Microsoft Certified: Azure AI Apps and Agents Developer Associate**. It is 120 minutes, pass mark 700, Python-based, and offered in 10 languages. | H | [MS Learn cert page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/) (1P, updated 2026-11-05) |
| A6.2 | AI-103 skills measured (as of 16 April 2026): Plan and manage an Azure AI solution 25-30%; **Implement generative AI and agentic solutions 30-35%**; Computer vision 10-15%; Text analysis 10-15%; Information extraction 10-15%. | H | [AI-103 study guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ai-103) (1P) |
| A6.3 | **AI-103 price $165 (US).** Microsoft's page says only "price based on country". $165 is the standard US associate price per 3P sources. A beta price of about $99 is also reported. | M | 3P: [Udemy blog](https://blog.udemy.com/ai-103-certification-guide/), [mscertquiz](https://mscertquiz.com/blog/microsoft-certification-exam-cost-2026) |
| A6.4 | **AI-103 prep paths total 30 h 26 min**: 4 learning paths, 31 modules, 1,826 minutes. Generative AI apps 412 min, AI agents 642 min, natural language 346 min, visual data 426 min. The instructor-led course AI-103T00-A is 4 days. | H | MS Learn catalog API, `learn.microsoft.com/api/catalog` (1P, queried 2026-11-14); [AI-103T00](https://learn.microsoft.com/en-us/training/courses/ai-103t00) |
| A6.5 | **AI-102 retired 30 June 2026.** | H | [MS Learn retired exams](https://learn.microsoft.com/certifications/retired-certification-exams) (1P, updated 2026-11-13) |
| A6.6 | **AI-900 also retired 30 June 2026.** The Azure AI Fundamentals cert continues through **AI-901 "Microsoft Azure AI Fundamentals"** (retirement: none). Domains: Identify AI concepts 40-45%; **Implement AI solutions using Microsoft Foundry 55-60%**. Python syntax is expected. Fundamentals exams are typically $99 US (3P). | H (price M) | Retired exams page; [AI-901 page](https://learn.microsoft.com/en-us/credentials/certifications/exams/ai-901/) (1P) |
| A6.7 | **Agent-specific cert: AB-100 "Agentic AI Business Solutions Architect"** (expert level). It covers multi-agent design across Microsoft 365 Copilot, Copilot Studio and Foundry, and requires an active associate cert from a list of 11. Related exams: AB-900, AB-730, AB-731. | M | [AB-100 cert page](https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/), [study guide](https://learn.microsoft.com/credentials/certifications/resources/study-guides/ab-100) (1P) |
| A6.8 | Retired Applied Skills: "Create agents in Microsoft Copilot Studio" (8 July 2026), "Create an AI agent" (28 May 2026), "Develop generative AI apps with Azure OpenAI and Semantic Kernel" (15 April 2026). AZ-204 retired 31 July 2026. | H | Retired exams page (1P) |
| A6.9 | Microsoft partners keep partner credit for retired certs for one year after retirement. | H | Same (1P) |

**Verify results:**
- "AI-102 retired 30 June 2026": **CONFIRMED** (H).
- "AI-103 $165": **LIKELY** (M; Microsoft does not print it, 3P agree).
- "AI-103 prep paths total 30 h 26 min": **CONFIRMED** (H, exactly 1,826 min).

---

## Part B - AWS

### B1. Three ways to buy Claude on AWS (a change in 2026)

| # | Fact | Conf | Source |
|---|------|------|------|
| B1.1 | **Claude Platform on AWS** went GA on 11 May 2026. It is the native Claude API, **operated by Anthropic**, reached through an AWS account (IAM/SigV4, CloudTrail) and billed through AWS Marketplace in CCUs at $0.01. AWS calls itself "the first cloud provider to offer access to the native Claude Platform experience". It launched in 17 regions. "Customer data is processed outside the AWS security boundary." | H | [AWS What's New 2026-05](https://aws.amazon.com/about-aws/whats-new/2026/05/claude-platform-aws/) (1P); [Anthropic docs](https://platform.claude.com/docs/en/build-with-claude/claude-platform-on-aws) (1P) |
| B1.2 | Claude Platform on AWS supports Messages, Files, Batches, Skills, code execution, the Compliance API, KMS CMEK and **Claude Managed Agents**. Managed Agents differences: autonomous sessions re-auth after 6 hours, and self-hosted environments cannot attach memory stores. Anthropic describes feature access as "typically same-day". | H | Anthropic docs (1P) |
| B1.3 | Claude Platform on AWS does **not** support HIPAA readiness, most Admin API endpoints, the Claude Code workspace, OAuth, **fast mode**, OpenAI-compatible endpoints, or MCP tunnels except to public servers. ZDR is **opt-in** (unlike Bedrock). Signing up creates a **new Anthropic org**; there is no in-place conversion. | H | Anthropic docs (1P) |
| B1.4 | **Amazon Bedrock `bedrock-mantle`** ("Claude in Amazon Bedrock") serves the native Messages API at `/anthropic/v1/messages`. It is **AWS-operated with zero Anthropic operator access**. Default quota is 2M input TPM, raisable to 5M input / 500k output TPM without Anthropic approval. | H | [Anthropic docs: Claude in Amazon Bedrock](https://platform.claude.com/docs/en/build-with-claude/claude-in-amazon-bedrock) (1P) |
| B1.5 | **Amazon Bedrock `bedrock-runtime`** (InvokeModel/Converse, the legacy path) is the only Bedrock endpoint serving **Fable 5.2 and Mythos 5.2**. The latest SDK defaults to API version `2026-10-21`, which models numbered 4.6 and lower on Bedrock reject with a 400, so SDK versions need pinning. | H | [Anthropic docs: bedrock-runtime](https://platform.claude.com/docs/en/build-with-claude/claude-on-amazon-bedrock-legacy) (1P) |
| B1.6 | **Bedrock does not support (both endpoints):** Files API and URL sources, server-side tools (code execution, web search, web fetch, advisor), **Agent Skills, MCP connector**, programmatic tool calling, **Message Batches API** (Bedrock has its own batch inference instead), Models/Admin/Compliance/Usage APIs, **Claude Managed Agents**, server-side fallback. bedrock-runtime also lacks automatic prompt caching (explicit breakpoints still work). | H | Anthropic docs (1P) |
| B1.7 | **Bedrock does support:** prompt caching, thinking, tool use (bash, computer use, memory, text editor; browser use on mantle), **citations**, structured outputs, PDF and the 1M context window on current models. Payloads are capped at 20 MB. | H | Anthropic docs (1P) |
| B1.8 | **Cross-region inference:** the global endpoint has no premium. Regional and geo inference profiles (US, EU, JP, AU/APAC) carry a **10% premium** for Sonnet 4.5 and later. Newer models require an inference profile ID, not the base model ID. | H | Anthropic docs (1P) |
| B1.9 | AWS Bedrock batch inference is **50% off** on-demand for select models including Anthropic. Priority tier is +75% and Flex is -50% (footnotes for other providers; Anthropic tier prices not shown). Sonnet 5.5 cache-read price was cut 50% from 7 Oct 2026. | M | [AWS Bedrock pricing](https://aws.amazon.com/bedrock/pricing/) (1P, partly rendered) |
| B1.10 | **Release timing:** Opus 5.5 was on Bedrock the same day Anthropic announced it (22 Sept 2026). Endpoint coverage is uneven, though: Fable 5.2 and Mythos 5.2 are absent from mantle. | M | [AWS ML blog](https://aws.amazon.com/blogs/machine-learning/claude-opus-5-5-is-now-available-on-aws/) (1P); [classmethod](https://dev.classmethod.jp/en/articles/bedrock-claude-opus-5-5/) (3P) |
| B1.11 | Lifecycle dates on partner platforms are set by the partner. Opus 4.1 and Sonnet 4 are retired on the Claude API but still served on Bedrock. | H | Anthropic pricing and docs (1P) |

### B2. Amazon Nova

| # | Fact | Conf | Source |
|---|------|------|------|
| B2.1 | The Nova 2 family (Lite, Pro, Sonic, Omni), Nova Forge and Nova Act launched at re:Invent in December 2025. Nova 2 Pro and Omni were reported still in preview in mid-2026. | M | [Amazon press 2025-12](https://press.aboutamazon.com/2025/12/amazon-introduces-four-new-frontier-nova-models-a-pioneering-nova-forge-service-for-organizations-to-build-their-own-models-and-nova-act-for-building-reliable-browser-agents) (1P) |
| B2.2 | Nova Act costs **$4.75 per agent-hour**. Nova Forge is an annual subscription (amount not published). | H | [AWS Nova pricing](https://aws.amazon.com/nova/pricing/) (1P) |
| B2.3 | Nova 2 Lite costs about $0.30 input / $2.50 output per MTok (base ID) and about $0.33 / $2.75 on us./eu. profiles, with a 1M context window. The AWS pricing tables did not render, so these figures are unverified. PERISHABLE | L | 3P trackers ([cloudprice](https://cloudprice.net/models/amazon.nova-2-lite-v1:0), getmaxim) |

### B3. Agents on AWS

| # | Fact | Conf | Source |
|---|------|------|------|
| B3.1 | **Bedrock AgentCore services listed today:** Harness (a managed agent loop running in a per-session microVM), Runtime, Memory, Gateway (turns APIs and Lambda into MCP tools and fronts existing MCP servers), Identity, Code Interpreter, Browser, Observability (OTEL), **Payments** (x402 and MPP), Evaluations, **Optimization** (A/B testing), Policy (Dogwood, Cedar-compatible) and **Registry** (agents, MCP servers, skills). That is 13 entries. GA or preview status per service is not shown on the page. PERISHABLE | H (list) / L (status) | [AgentCore docs](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/what-is-bedrock-agentcore.html) (1P, 2026-11-14) |
| B3.2 | AgentCore Runtime is framework- and model-agnostic. Named frameworks: Strands, LangGraph, CrewAI, LlamaIndex, Google ADK and OpenAI Agents SDK. Named models include Claude, Gemini and OpenAI models. Protocols: MCP and A2A. A2A servers run on port 9000. The Harness names Bedrock, OpenAI and Gemini model providers. | H | Same; [A2A contract](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/runtime-a2a-protocol-contract.html) (1P) |
| B3.3 | AgentCore pricing is consumption-based: vCPU-hours and GB-hours for Runtime, Browser and Code Interpreter, per-unit for the others, and CloudWatch rates for observability. Model tokens are billed separately. AgentCore went GA in October 2025 (3P). | M | [AgentCore pricing](https://aws.amazon.com/bedrock/agentcore/pricing/) (1P); 3P guides |
| B3.4 | **Bedrock Agents was renamed "Agents Classic"** and closed to new customers on 30 July 2026. Existing agents keep running, the model catalog is frozen and no new features are planned. | L-M | 3P ([Enterprise DNA](https://enterprisedna.co/resources/news/amazon-bedrock-agents-classic-agentcore-enterprise-july-2026/), [byteiota](https://byteiota.com/aws-agentcore-is-here-what-to-do-before-classic-locks-you-out/)); AWS [migration blog](https://aws.amazon.com/blogs/migration-and-modernization/mass-migrating-ai-agents-to-amazon-bedrock-agentcore/) |
| B3.5 | **Strands Agents SDK:** Apache 2.0, Python (about 9.2k stars) and TypeScript (1.0 released; runs in Node and the browser). It supports Bedrock, Anthropic, OpenAI and Gemini. MCP is built in, and A2A is supported in the Python 1.0 docs and the TS SDK. | H | [GitHub sdk-python](https://github.com/strands-agents/sdk-python) (1P); [Strands TS 1.0 blog](https://strandsagents.com/blog/strands-agents-typescript-v1/) (1P) |
| B3.6 | **AWS MCP Server** (managed, remote) went GA on 6 May 2026 at no extra charge. Launch regions: us-east-1 and eu-central-1. AWS's own demo used Claude Code. | H | [AWS What's New](https://aws.amazon.com/about-aws/whats-new/2026/05/aws-mcp-server/) (1P) |

### B4. Kiro and Amazon Q Developer vs Claude Code

| # | Fact | Conf | Source |
|---|------|------|------|
| B4.1 | **Amazon Q Developer IDE plugins and paid subscriptions reach end of support on 30 April 2027** (announced 30 April 2026). New signups have been blocked since 15 May 2026. Q in the Console, docs, mobile app and Slack/Teams continue. | H | [AWS DevOps blog](https://aws.amazon.com/blogs/devops/amazon-q-developer-end-of-support-announcement/) (1P) |
| B4.2 | Opus 4.6 was removed from Q Developer Pro on 29 May 2026. The newest models (Opus 4.7 and later) are **Kiro-only**. | H | Same (1P) |
| B4.3 | **Kiro plans:** Free $0 (50 credits, open-weight models and Sonnet 4.5); Pro $20 (1,000 credits); Pro+ $40 (2,000); Pro Max $100 (5,000); Power $200 (10,000). Overage is $0.04/credit. Teams pooling is $20/seat with 500 credits per seat. GovCloud is about 20% higher. Listed Claude models: Opus 5, Opus 4.8, Sonnet 5, Sonnet 4.6, Sonnet 4.5, Haiku 4.5. Opus 5.5 is absent from that FAQ. PERISHABLE | H | [kiro.dev/pricing](https://kiro.dev/pricing/) (1P, read 2026-11-14) |
| B4.4 | Kiro positions on spec-driven development and has an IDE and a CLI. It is the AWS successor for Q Developer users. | H | AWS DevOps blog (1P) |

### B5. AWS credentials

| # | Fact | Conf | Source |
|---|------|------|------|
| B5.1 | **AWS Certified AI Practitioner (AIF-C01):** $100, 90 minutes, 65 questions. | H | [AWS cert page](https://aws.amazon.com/certification/certified-ai-practitioner/) (1P) |
| B5.2 | **AWS Certified Machine Learning Engineer - Associate:** MLA-C01 is $150, 130 minutes, 65 questions. The updated beta, exam code shown as ME1-C02 on the page, is $75 beta price, 170 minutes, 85 questions, with no new domains. PERISHABLE | H | [AWS cert page](https://aws.amazon.com/certification/certified-machine-learning-engineer-associate/) (1P) |
| B5.3 | **AWS Certified Generative AI Developer - Professional (AIP-C01 per URLs):** $300, 180 minutes, 75 questions. | H | [AWS cert page](https://aws.amazon.com/certification/certified-generative-ai-developer-professional/) (1P) |
| B5.4 | ML Specialty (MLS-C01): the last exam date was 31 March 2026. | M | [AWS T&C blog](https://aws.amazon.com/ko/blogs/training-and-certification/big-news-aws-expands-ai-certification-portfolio-and-updates-security-certification/) (1P) and 3P |

---

## Part C - Cross-cutting

### C1. MCP and A2A

| Vendor | MCP client | MCP server | A2A | Conf |
|---|---|---|---|---|
| Microsoft | Agent Framework (.NET, Python, Go); Foundry Agent Service (remote MCP, Toolboxes); Copilot Studio (GA); GitHub Copilot and code review | Azure MCP Server; Azure DevOps remote MCP (GA Aug 2026); Azure Language and Speech MCP servers (used in AI-103 paths); Toolbox-as-MCP endpoint | Foundry Agent Service **A2A v1.0 GA**; Agent Framework A2A hosting; AI-103 path module "Discover Foundry agents with A2A" | H for Foundry and Agent Framework; M for Azure MCP Server version and GA date |
| AWS | Strands (built-in); AgentCore Harness (remote MCP); Kiro | **AWS MCP Server GA 6 May 2026**; AgentCore Gateway (APIs and Lambda to MCP); AgentCore Registry catalogs MCP servers | AgentCore Runtime A2A (port 9000); Strands A2A | H |

Sources: MS Learn Agent Service overview; Agent Framework overview; AWS AgentCore docs; AWS What's New (all 1P, 2026-11-14). Azure MCP Server version history conflicts between sources (L): [AZ578662](https://mc.merill.net/message/AZ578662).

### C2. "Same Claude, different cloud"

Six ways to buy Claude now exist. The table compares them on 2026-11-14 (all 1P Anthropic docs unless marked).

| Dimension | Claude API (1P) | Claude Platform on AWS | Bedrock (mantle / runtime) | Google Cloud, Anthropic managed | Google Cloud, Google managed (Vertex) | Foundry, Hosted on Azure | Foundry, Hosted on Anthropic |
|---|---|---|---|---|---|---|---|
| Operator | Anthropic | Anthropic | AWS (no Anthropic operator access) | Anthropic | Google | Anthropic, on Azure infra | Anthropic |
| Data processor | Anthropic | Anthropic | AWS | Anthropic | Google | Anthropic (independent processor) | Anthropic |
| Managed Agents | Yes | Yes (with limits) | No | Yes | Not checked | No | No |
| Batches API | Yes | Yes | No (AWS batch at -50% instead) | Yes | Not checked | No | No |
| Files / Skills / code exec | Yes | Yes | No | Yes | Not checked | No | Yes |
| MCP connector | Yes | Yes (beta) | No | Yes (beta) | Not checked | Not listed | Not listed |
| Fast mode | Yes | **No** | n/a | Opus 5.5 | n/a | Opus 5.5 | Fable 5.2 |
| US-only inference | `inference_geo` 1.1x | 1.1x | Regional profile +10% | 1.1x | Regional +10% | US Data Zone 1.1x | No |
| EU residency | `inference_geo` options (not verified here) | Not pinned by region | EU profile +10% | Not verified | EU multi-region +10% | No EU Data Zone listed | No |
| Commit drawdown | Anthropic contract | AWS commitments incl. EDP (3P says yes; Anthropic doc says "AWS commitment retirement" unchanged) | AWS EDP (standard Bedrock) | Google commit "like other Marketplace purchases" | Google commit | **MACC-eligible** | **MACC-eligible** |
| Billing unit | USD/MTok | CCU $0.01 | AWS per-token | CCU $0.01 | Google per-token | CCU $0.01 | CCU $0.01 |
| New features | Day 0 | "Typically same-day" | Model day 0 seen (Opus 5.5); server tools absent | Close to 1P | Not checked | Lags (core set only) | Close to 1P |
| Quotas | Anthropic tiers | Start/Build/Scale tiers | AWS: 2M input TPM default, 5M self-serve | Anthropic | Google | Azure quota form | Azure quota form |
| Regulated workloads | - | Not HIPAA-ready; Bedrock recommended for FedRAMP High, IL4/5, HIPAA | Yes (AWS boundary) | - | - | - | - |

Notes:
- **CCU is the common denominator.** Anthropic-operated marketplace offers on AWS, Google and Azure all bill CCU at $0.01, rated at Anthropic list price after discount. CCU billed on one cloud does not decrement another cloud's commit (MS Learn, explicit).
- **Private offers do not transfer** between Bedrock and Claude Platform on AWS, or between an existing Anthropic org and the cloud-created org. Discounts cannot be applied retroactively (Anthropic docs, 1P, H).
- **Advisory heuristic:** pick the AWS- or Google-operated endpoint when the cloud must be the sole data processor or a FedRAMP/HIPAA boundary matters. Pick the Anthropic-operated marketplace offer when the customer needs Managed Agents, Skills, Files, Batches or server tools and wants the spend on the cloud bill. On Azure today, neither Foundry option offers Managed Agents or Batches.

---

## PERISHABLE watchlist (next three months)

1. Claude in Copilot moves into the EU Data Boundary and becomes on by default for EU/EFTA tenants on **9 Dec 2026** (A4.4).
2. Which models are Azure-hosted vs Anthropic-hosted in Foundry; Fable and Mythos availability on every cloud (A1.3, B1.5).
3. GitHub Copilot model list, and the Fable ZDR exemption ending at end-2026 (A5.1).
4. Kiro model list and credit multipliers (B4.3).
5. AgentCore service GA status (B3.1); Foundry hosted agents GA (A2.7).
6. MLA-C02 beta becoming GA, and the MLA-C01 cutover date (B5.2).
7. Bedrock Anthropic tier prices; Nova prices (B1.9, B2.3).
8. Microsoft "Cowork 1" model (A4.7) - could reduce Claude's share inside Copilot Cowork.
9. Q Developer IDE end of support, 30 April 2027 (outside the window, but migrations happen now).

## Open gaps (not verified)

- Whether Claude can back a Foundry *prompt* agent today (A2.6).
- Official AWS wording on Claude Platform on AWS and EDP drawdown. 3P says yes; the Anthropic doc's commercial section talks about private offers, not EDP.
- Feature list for Google managed (Vertex) Claude. Not fetched; this sheet covers the Anthropic-managed Google offer.
- AWS official price tables for Nova and Claude tiers (the page did not render).
