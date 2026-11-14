# The field beyond Claude: fact sheet

Compiled 2026-11-14. Every fact carries a source URL, an as-of date and a confidence tag.

- **Confidence**: **H** = primary source read directly, or several independent outlets agree. **M** = one primary source via secondary coverage, or secondary sources that agree. **L** = one secondary or aggregator source, or sources that conflict.
- **1P** = first-party (vendor, standards body, regulator, or the benchmark owner). **3P** = third party (press, analysts, aggregators).
- **PERISHABLE** = likely to change within three months.
- Model names in this sheet (Fable, Opus 5.5, GPT-6 Astra, Gemini 4 Carbon and so on) are taken from the sources as of today. Several post-date my training data, so I checked each one against at least one live leaderboard or vendor page.

---

## 0. Context: the frontier as of mid-November 2026

| Lab | Current flagship(s) | Evidence | Conf |
|---|---|---|---|
| Anthropic | Claude Fable 5.2 (released 2026-11-09), Opus 5.5, Sonnet 5.5, Haiku 5.5; Mythos 5.2 restricted | AA index and ARC leaderboards list them (1P benchmark owners, read 2026-11-14). Fable 5.2 at $8/$40 per M tokens, 20% below Fable 5.1 (3P: https://techenclave.com/news/items/anthropic-releases-claude-fable-5-2-at-lower-api-prices) | H for existence, M for price |
| OpenAI | GPT-6 Astra (2026-09-03), GPT-6.1 Sol/Terra, GPT-6 Luna | GPT-6 Astra GA on Bedrock 2026-09-08 (1P: https://aws.amazon.com/about-aws/whats-new/2026/09/openai-gpt-6-astra-on-amazon-bedrock/). Astra list price $10/$50 is 3P-reported (https://www.yottalabs.ai/post/gpt-6-astra-pricing-api-cost-2026). Menlo cites $10/$60 | H existence, L price |
| Google | Gemini 4 Carbon (on ARC 2026-11-10; preliminary on Arena), Gemini 4 Argon (API 2026-10-13), Gemini 4 Hydrogen | Arena and ARC leaderboards (1P). Argon introductory price $2/$10 until 2026-11-30, then $4/$20 (3P: https://letsdatascience.com/news/gemini-4-argon-undercuts-claude-on-price-73027210) **PERISHABLE** | H existence, M price |
| Meta | Muse Wonder (closed), Muse Spark 1.x (closed), Muse Spark Open (open weights) | Arena Text #3 is Muse Wonder (1P) | H |
| xAI (now SpaceXAI) | Grok 4.7 | See section 1 | H |

---

## 1. xAI Grok

### Models and API prices (1P: https://docs.x.ai/docs/models, read 2026-11-14) - H, PERISHABLE

| Model | Context | Input $/M | Cached $/M | Output $/M |
|---|---|---|---|---|
| grok-4.7 (recommended for code and chat) | 500k | 2.00 (4.00 at 200k or more) | 0.50 | 6.00 (12.00 at 200k or more) |
| grok-4.6 / 4.5 | 500k | 2.00 | 0.50 / 0.30 | 6.00 |
| grok-4.3, grok-4.20 family (incl. multi-agent) | 1M | 1.25 | 0.20 | 2.50 |
| grok-build-0.1 (coding) | 256k | 1.00 | 0.20 | 2.00 |

- The 200k long-context rule reprices **the whole request** once the prompt passes 200k tokens. Grok 4.7's knowledge cut-off is May 2026. `logprobs` is silently ignored on 4.20 and later. (1P, same page) H
- Grok 4.7 launched 2026-09-21 at the same price as 4.6. Available in Cursor and GitHub Copilot at launch. xAI's own CursorBench 4.0 score: 46.3% (4.6: 40.4%). Launch came after at least five slips from late July. The announcement came from the @SpaceXAI handle, which replaced @xai. (3P: https://decrypt.co/378824/xai-launches-grok-4-7, https://www.crowdfundinsider.com/2026/09/312007-xai-launches-grok-4-7-for-longer-coding-and-knowledge-work/) M
- Independent standing: Grok 4.7 Xhigh scores **35** on the Artificial Analysis Intelligence Index, rank 15, against 65 for Fable 5.2 and 46 for the best open model (Kimi K3.1 Pro). The cost per AA task is $7.77, more than GPT-6.1 Sol Max at $1.27. (1P: https://artificialanalysis.ai/leaderboards/models, 2026-11-14) H, PERISHABLE
- Grok 5: no release. Musk's targets slipped from late 2025 to Q1 and then Q2 2026. (3P: https://www.nxcode.io/resources/news/grok-5-release-date-latest-news-2026, mid-2026) M

### Corporate status
- SpaceX acquired xAI in an all-stock deal reported at about $1.25T combined (early 2026). (3P: https://www.datacenterknowledge.com/business/musk-merges-xai-spacex-in-1-25t-ai-power-play-outlines-space-goals) M
- SpaceX closed its ~$60B all-stock purchase of **Cursor** (Anysphere) on about 2026-08-14. Cursor now sits in a SpaceXAI division. An SEC 8-K shows conversion into about 389.3M SpaceX Class A shares. The Information reported that staff were told the Cursor brand could be phased out; this is unconfirmed. (3P: https://thenextweb.com/news/spacex-cursor-acquisition-completed-gpu-fleet, https://www.vktr.com/ai-market/spacex-completes-60-billion-cursor-acquisition/) H for the close, L for the brand claim
- **Advisory point**: an enterprise that standardises on Cursor now buys from the same corporate group as Grok. Check where Cursor routes data, the sub-processor list and the model defaults after the acquisition.

### Enterprise offer
- Grok Business is $30/seat/month, self-serve from 2025-12-30. Grok Enterprise and "Enterprise Vault" (isolated data plane, customer-managed keys) are priced on request. (3P: https://venturebeat.com/ai/musks-xai-launches-grok-business-and-enterprise-with-compelling-vault-amid) M
- Compliance claims (SOC 2 Type II, GDPR, CCPA, no training on business data) are vendor-stated. I did not read an xAI trust page directly. L, verify under NDA
- US federal: GSA OneGov deal makes Grok 4 and Grok 4 Fast available to agencies at $0.42 per agency for 18 months, through March 2027. (3P: https://www.nextgov.com/acquisition/2025/09/gsa-inks-onegov-deal-grok-ai/408334/, 2025-09) H

### Controversies relevant to enterprise risk
- **2025 conduct incidents**: "white genocide" insertions (May 2025, blamed on an unauthorised employee change) and antisemitic, Hitler-praising output (July 2025, blamed on an upstream code change that reactivated old instructions). That makes three "technical glitch" explanations in 2025. (3P: https://www.eweek.com/news/grok-ai-chatbot-hate-speech-xai-apologizes/) H
- **2026 sexual-deepfake scandal**: Grok image generation produced non-consensual sexual images, including of minors. Ofcom opened an Online Safety Act investigation on 2026-01-12 (fines up to 10% of qualifying worldwide revenue). The European Commission opened a formal DSA investigation on 2026-01-26 (up to 6% of global turnover). French police raided X's Paris office in February 2026 in a criminal CSAM probe. xAI restricted image generation to paid X subscribers on 2026-01-09. (3P: https://www.rpclegal.com/snapshots/technology-digital/spring-2026/online-safety-regulators-investigate-x-over-grok-ai-chatbot-images/, https://www.crowdfundinsider.com/2026/01/258335-grok-targeted-by-eu-for-possible-dsa-transgressions/, https://wtop.com/national/2026/01/what-you-need-to-know-about-grok-and-the-controversies-surrounding-it/) H. I found no final outcome for either probe. **PERISHABLE**
- **Risk framing for a customer**: the investigations target the consumer and X-integrated product, not the API. The governance question carries over to the API: system-prompt changes reached production without control on at least two occasions. Ask for change-management evidence and model-version pinning (xAI supports dated model IDs, per the 1P docs above).

---

## 2. Open-weight models

### Headline numbers (Menlo Ventures, 2026-11-03, 1P report: https://menlovc.com/wp-content/uploads/2026/11/menlo_ventures_enterprise_ai_report-2026-110326.pdf) - H
- Open source accounts for **19% of enterprise tokens but 4% of spend**. Its token share rose from 11% and its spend share fell from 6% as the average open token price dropped 3.3x to $0.13/M. The blended closed-model price is $0.70/M.
- **Chinese models are 89% of open-source spend**: Kimi 61%, DeepSeek 15%, GLM 11%, Qwen 3%. Llama, the top Western open model, has 7%.
- Grok 4.7 and open models (Kimi K3, DeepSeek V4, GLM-5.3) "approach frontier performance at a fraction of the price, yet together hold just under 5% of LLM API spend."
- Cursor built **Composer 2 on Kimi K2.5**, with Fireworks running the RL rollouts.
- Caveat: Menlo is an Anthropic investor. The survey covered about 400 US enterprise decision-makers and was fielded by Morning Consult on 2026-09-08 to 26.

### Independent capability check
- AA Intelligence Index, top open-weight models: **Kimi K3.1 Pro 46**, DeepSeek V4.1 Flash 1017 33, GLM-5.3 32. The top closed models score 65 (Fable 5.2), 60 (Gemini 4 Carbon) and 59 (Opus 5.5). Kimi is about 20 points behind the leader and level with mid-tier closed models such as GPT-6.1 Terra (51) and Gemini 4 Argon (50). (1P: https://artificialanalysis.ai/leaderboards/models, 2026-11-14) H, PERISHABLE
- LMArena Text: the top open-weight entry is GLM-5.3 at #28 (1482, MIT-listed). Kimi K3 (custom licence) is #20. (1P: https://arena.ai/leaderboard/text, as of 2026-11-11) H
- OpenRouter usage, trailing 30 days to 2026-11-13: #1 DeepSeek V4.1 Flash 1017 (185T tokens), #3 GLM 5.3 Flash. By request share, DeepSeek is the top author at 31.8% and Anthropic is 5th at 5.8%. OpenRouter skews to cost-sensitive developers and agents, not enterprise spend. (1P: https://openrouter.ai/rankings) H, PERISHABLE

### Per family

| Family | Current (as of) | Licence | Price (hosted, $/M in/out) | Conf |
|---|---|---|---|---|
| **Meta** | Llama is no longer the forward line. Muse Spark launched closed. Muse Glimmer (30B, Apache 2.0, Aug 2026). **Muse Spark Open** weights 2026-10-15: 816B MoE, 42B active, 1M context | Custom "Muse Model License": free use, "Built with Muse Spark Open" notice, separate deal for MaaS providers over $20M revenue. Not OSI-approved | Various hosts | M (3P: https://thenewstack.io/meta-muse-spark-open/, https://www.deeplearning.ai/the-batch/with-muse-spark-meta-pivots-away-from-its-open-weights-llama-strategy). Muse Spark 1.1 leads SWE-bench Pro (61.5%, 1P Scale) |
| **Mistral** (France) | **Mistral Large 4** weights 2026-10-29: about 1.05T MoE, about 52B active (one source says 49B), 1M context, multimodal. Medium 3.5 (Apr 2026, 128B dense, merges Magistral and Devstral 2) | Large 4: modified MIT, with a separate agreement required for MaaS resellers. Medium 3.5: modified MIT | Sources conflict: $0.70 or $1.36 input, $4.18 output | M (3P: https://letsdatascience.com/blog/mistral-large-4-weights-out-resellers-need-license, https://www.digitalapplied.com/blog/mistral-large-4-open-weights-price-comparison) |
| **DeepSeek** | **V4.1 Flash** (2026-09-10), refreshed as V4.1-Flash-1017 (2026-10-17): 552B MoE, 1M context. No V4.1 Pro | MIT | First-party $0.30/$1.20 peak, $0.15/$0.60 off-peak. Same on Fireworks and Together | M (3P: https://techstrong.ai/articles/deepseek-unveils-v4-1-flash-model-with-architectural-upgrades-price-cuts-ahead-of-shanghai-ipo/, https://pricepertoken.com/endpoints/compare/fireworks-vs-together) |
| **Qwen** (Alibaba) | Qwen3.8 line (Aug 2026): 27B under Apache 2.0, a 2.4T flagship under a custom licence with revenue conditions. Earlier 3.5 and 3.6 releases were Apache 2.0 | **Licences are diverging**: small models Apache, flagship custom, Flash-Next under the "Qwen Community License 1.0" | n/a | M (3P: https://www.eweek.com/news/alibaba-qwen3-8-27b-license-apac-china/, https://www.alibabacloud.com/blog/alibaba-unveils-qwen3-8-27b-and-releases-weights-of-qwen3-8-flagship-model_603463) |
| **Kimi** (Moonshot) | **Kimi K3.1 Pro**: API 2026-10-23, weights on Hugging Face 2026-11-04. Reported at 2.8T MoE, about 1.56TB MXFP4 checkpoint | Custom Kimi licence. K3's licence needs a separate agreement for cloud resale above $20M revenue; internal use is free | $2/$10 (Moonshot, Together, Fireworks); Highspeed $4/$20 | M (3P: https://www.buildmvpfast.com/blog/kimi-k3-1-pro-open-model-coding-pricing-2026, https://interconnected.blog/kimis-tightrope-openness-and-revenue-at-once-but-new-us-ban-risks/). **PERISHABLE** |
| **GLM** (Zhipu / Z.ai) | GLM-5.3 (Aug to Sep 2026), GLM-5.3-Flash (320B multimodal MoE) | Flagship: **dropped MIT** for a custom licence that requires a security review for operators above $10B revenue. Flash: MIT | Flagship $1.40/$4.40 (Together); Flash $0.15/$0.50 | M (3P: https://thenewstack.io/zai-glm-weights-license/) |
| **OpenAI gpt-oss** | Still gpt-oss-120b and 20b (Aug 2025). No successor found | Apache 2.0 | Widely hosted, including Bedrock | M (1P: https://openai.com/index/introducing-gpt-oss/; absence of a successor is L) |
| **Gemma** (Google) | Gemma 4 (2026-04-02): E2B, E4B, 26B MoE, 31B dense, 256K context; a 12B was added later | **Moved to Apache 2.0**, dropping the custom Gemma terms | Self-host and laptop class | H (3P, many: https://www.theregister.com/2026/04/02/googles_gemma_4_open_weights/) |

Other open families showing up on usage boards: Tencent Hy4 (AA index 35, #2 on OpenRouter weekly), StepFun Step 5, Xiaomi MiMo-V2.6-Flash, MiniMax. (1P OpenRouter and AA, 2026-11-14) H

### Enterprise considerations
- **Licence drift is the 2026 story.** The headline Western and Chinese flagships (Muse Spark Open, Kimi K3.x, GLM-5.3, Qwen3.8 flagship, Mistral Large 4) all moved to custom licences that restrict large-scale resale. The permissive tier is now the small and mid models: Gemma 4, Qwen 27B, GLM Flash, DeepSeek V4.1 Flash (MIT), gpt-oss. Internal self-hosting is generally allowed. Reselling inference often is not. Confidence M, because licence texts were read via press, not on Hugging Face.
- **Self-hosting cost.** Frontier open models are multi-node. Third-party sizing for Kimi K3.1 Pro: about 19 x 80GB GPUs at INT4, and a single 8-GPU node is not enough. (3P: https://www.spheron.network/blog/deploy-kimi-k3-1-pro-on-gpu-cloud-2-8t-moe-setup-guide-2026/) L. Menlo finds 91% of companies that post-train use outside partners (Fireworks, Modal, Mercor). H. Self-hosting pays off at sustained high volume or under a hard sovereignty requirement, not as a cheaper way to reach frontier quality.
- **US procurement and provenance (Chinese weights).**
  - DHS issued a Federal Register order (reported 2026-10-20) that removes DeepSeek products from federal civilian agencies, **including third-party products built on DeepSeek technology**. Exceptions can be requested. It does not restrict non-government use. (3P: https://techcrunch.com/2026/10/20/us-orders-federal-agencies-to-remove-chinas-deepseek-ai-from-their-systems/; CRS: https://www.everycrsreport.com/reports/IF13336.html) H
  - A December 2025 law already restricted DeepSeek in intelligence and national security systems. (same TechCrunch) M
  - Under discussion but not enacted: contractor bans (Sen. Cotton letter), procurement rules, Entity List threats aimed at Kimi K3. Commerce's ICTS rule could apply where Kimi's licence forces US inference providers into contracts with Moonshot. (3P: https://www.semafor.com/article/07/30/2026/republican-urges-trump-administration-to-ban-chinese-ai-for-contractors, https://interconnected.blog/kimis-tightrope-openness-and-revenue-at-once-but-new-us-ban-risks/) M, **PERISHABLE**
  - A September 2026 report accused DeepSeek and five other Chinese labs, Alibaba and Moonshot among them, of distilling US models. (3P, TechCrunch above) M
  - **Advice**: for US federal work and federal contractors, treat DeepSeek-derived components (including fine-tunes) as excluded now, and others as at risk. Keep a model bill of materials so a swap can happen without re-architecture.
- **EU sovereignty (Mistral).** Mistral Compute targets up to 1 GW by 2030, sold through multi-year "European Compute Units"; first external customers came in March 2026. Regional endpoints let customers choose EU or US inference. (1P: https://mistral.ai/news/regional-inference-open-models-new-compute/) H. Le Chat Enterprise went GA in May 2025 with custom pricing (3P: TechCrunch). Le Chat was reportedly renamed **Mistral Vibe** in 2026 (3P: https://en.wikipedia.org/wiki/Mistral_AI) L. Counterpoint for the podcast: Claude in Microsoft Foundry (GA 2026-06-29) is outside the EU data-residency scope that Bedrock and Vertex offer (3P: https://infoq.com/news/2026/07/claude-foundry-ga-europe/) M.

---

## 3. Coding agents market

### Spend (Menlo 2026, 1P report above) - H, Menlo is an Anthropic investor
- Coding is a **$34.0B** application market, up 7.7x. **Claude Code and Codex together take $24.0B (70%)**, up from about $1B a year earlier. The rest of the market (Cursor, Cognition, Factory, Lovable) grew 2.9x to $10.1B.
- AI-native vendors hold 96% of coding spend. Menlo says challengers beat incumbent GitHub Copilot on "product velocity".
- Menlo does not split Claude Code from Codex.

### Developer usage (Stack Overflow 2026 survey, published 2026-10-06, 1P: https://stackoverflow.blog/2026/10/06/the-results-of-the-2026-developer-survey-are-here/) - H
- More than 30,000 participants. **Claude Code is the leading coding agent, used by 66% of AI users; GitHub Copilot is used by 59%.** The blog post does not mention Cursor, Codex or Windsurf. The full results site has more detail; I did not open it.
- Claude and GPT usage is "neck and neck", with Anthropic slightly ahead on "want to keep using". Gemini is a "distant third".
- 73% of AI-assistant users use one daily. 31% use AI tools for 4 or more hours a day.
- Cost controls in organisations: 38% set usage limits, **27% use different models for different work**, 25% limit who can use AI.
- 2025 baseline for comparison: Cursor 17.9%, Claude Code 9.7%, Windsurf 4.9% among AI dev tools. (1P: https://stackoverflow.blog/2026/10/01/a-look-back-before-we-look-forward-a-developer-survey-retrospective/)

### Per tool

| Tool | State as of Nov 2026 | Source | Conf |
|---|---|---|---|
| **Claude Code** | Latest official run-rate figure is above $2.5B (2026-02-12); no newer product-level figure found. #2 app on OpenRouter by daily tokens (1.75T). Reads AGENTS.md when no CLAUDE.md exists, from v2.1.277 (2026-09-18) | 1P Anthropic via https://feeds.simonwillison.net/2026/Feb/12/anthropic/; 1P OpenRouter; https://simonwillison.net/2026/Sep/18/thariq-shihipar/ | H |
| **Cursor** (now SpaceX) | Cursor 3 (2026-04-02) is agent-first. Own models: Composer 2 (2026-03-19, built on Kimi K2.5), Composer 2.5 (May 2026). Composer 3 is unannounced as of the latest sources. ARR reported at about $2B (Feb 2026) and about $4B (mid-2026, Sacra estimate) | https://codersera.com/blog/cursor-3-composer-2-walkthrough-2026/, https://sacra.com/c/cursor | M (ARR L) |
| **GitHub Copilot** | About 50M users, including the free tier; appears in about one in three GitHub PRs; revenue up more than 60% quarter on quarter after the move to usage-based billing (Microsoft FY26 Q4, late July 2026). Multi-model: offers Claude, GPT and Grok 4.7 | 3P reporting Microsoft earnings: https://windowsreport.com/microsoft-revenue-hits-90-billion-as-ai-growth-accelerates/ | M |
| **Codex** (OpenAI) | About 4M weekly active developers (April 2026). Codex plus ChatGPT Work together about 10M WAU (2026-07-21). GA on Amazon Bedrock since 2026-06-01. Codex with GPT-5.5 topped the Terminal-Bench 2.0 snapshot at 82.0% (April 2026) | https://www.digitalapplied.com/blog/openai-codex-4m-weekly-developers-growth-data; 1P AWS: https://aws.amazon.com/about-aws/whats-new/2026/06/amazon-bedrock-openai-models-codex-generally-available/ | M |
| **Cognition** (Devin + Windsurf) | $492M ARR and $26B post-money valuation (May 2026). About $900M ARR reported in August 2026 with about $800M planned burn. Devin Desktop (June 2026) is built on Windsurf | https://cryptobriefing.com/cognition-900m-arr-800m-cash-burn/ | M for May, L for August |
| **Gemini CLI to Antigravity** | Google deprecated Gemini CLI and the Code Assist IDE extensions on 2026-05-19 in favour of **Antigravity CLI**. The personal tier was cut off on 2026-06-18; paid API keys still work. "No 1:1 feature parity" at launch | 1P: https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/ | H |
| **Kiro** (AWS) | GA 2026-05-07; spec-driven IDE. Successor to Amazon Q Developer: new Q Developer sign-ups closed 2026-05-15, end of support 2027-04-30. Tiers from Free up to "Power"; reported prices conflict ($19 or $20 Pro, up to $200) | https://rywalker.com/research/kiro; 1P billing docs https://kiro.dev/docs/enterprise/billing/ | M |
| **Cline / Roo / Kilo** | **Roo Code shut down** (announced 2026-04-21, repo archived May 2026); users pointed to Cline or Kilo Code. Kilo Code is #3 on OpenRouter apps by tokens | https://rywalker.com/research/ai-coding-assistants; 1P OpenRouter | M |
| **Amp** | Spun out of Sourcegraph as Amp, Inc. (Dec 2025). Amp Labs for enterprise (May 2026) | https://rywalker.com/research/amp-sourcegraph | L |
| **OpenCode** | MIT, by Anomaly (formerly SST). About 156k GitHub stars (May 2026). Sells hosted tiers (Zen/Go) | https://codersera.com/blog/ai-coding-agents-complete-guide-2026/ | L |

**Where Claude Code sits**: it leads developer usage in the largest survey (66% vs Copilot 59%). With Codex it takes most coding spend. Its main structural rivals are now Codex, distributed through Bedrock and Azure as well as OpenAI, and Copilot, which has distribution, multi-model choice and a usage-based billing pivot. Cursor is a strong product but its ownership changed. Open-source harnesses (Kilo, OpenCode, Hermes Agent, pi) run large token volumes on cheap Chinese models through OpenRouter.

---

## 4. Enterprise LLM market share

**Menlo Ventures, "2026: The State of Enterprise AI", 2026-11-03 (1P PDF above)** - H for what it says. Methodological caveats are listed below the table.

| Metric | 2025 | 2026 |
|---|---|---|
| Anthropic share of enterprise LLM API spend | 40% | **55%** |
| OpenAI | 27% | **31%** |
| Google | 21% | **9%** |
| Anthropic + OpenAI combined | 67% | **86%** |
| Open-source share of spend / tokens | 6% / 11% | **4% / 19%** |
| Enterprise AI deployment spend (run rate) | $33B | **$176.8B** (Sept 2026) |
| Frontier-lab share of all deployment dollars | 50% | **69%** ($122.7B) |
| Coding app market | ~$4.4B | **$34.0B**; Claude Code + Codex = $24.0B (70%) |

- Menlo's explanations: Google "hasn't matched Anthropic's and OpenAI's flagship models since" Gemini 3 Pro (November 2025), and its API spend skews to Flash. OpenAI gained in the second half from GPT-5.6 (July) and GPT-6 (September).
- Most popular models a year ago: Sonnet 4.5 ($3/$15) and GPT-5 ($1.25/$10). Today: **Opus 5.5 ($4/$20) and GPT-6 Astra (listed by Menlo at $10/$60)**. Buyers are trading up. Small-model prices fell 80% or more, yet small closed models lost token share (29% to 13%) to open source.
- Agents produce 80% of OpenRouter tokens (130.9T/week). Agent traffic overtook human traffic in February 2026.
- Cache reads can be 95% or more of an agent's tokens. At Opus 5.5 rates ($0.20 cache read), an agent session averages about $0.70/M tokens.
- **Caveats**: (1) Menlo is an Anthropic investor and says so. (2) About 400 US respondents; shares are survey-weighted estimates of production API usage, not audited revenue. (3) Google's 9% excludes Workspace and Gemini app bundles and covers API spend only. (4) Menlo's 2025 usage-based figures (Anthropic 32%, OpenAI 25%) are not comparable.
- Corroborating signal (3P, L): reports cite an Anthropic SEC filing (S-1 Amendment No. 2, 2026-11-10) with a run rate of about $81B at 2026-10-31. Single secondary source: https://fourweekmba.com/ai-anthropics-run-rate-hit-81b-october-added-2-2x-2025-sales/. Verify against EDGAR before using on air. **PERISHABLE**
- Distribution shift (1P AWS): **OpenAI models are GA on Amazon Bedrock**: GPT-5.5, 5.4 and Codex (2026-06-01), GPT-5.6 Sol/Terra/Luna (July), GPT-6 Astra (2026-09-08), plus GovCloud. Claude is GA in Microsoft Foundry (2026-06-29, 3P). Enterprises can now buy both leading labs on their existing cloud commitment, which weakens cloud as a reason to pick one. H

---

## 5. Benchmarks: current leaders and how to read them

| Benchmark | Leader now | Notes | Source / as-of | Conf |
|---|---|---|---|---|
| **AA Intelligence Index** | Claude Fable 5.2 Max **65**; Gemini 4 Carbon High 60; Opus 5.5 59; GPT-6 Astra Max 57 | Composite of about 10 evals, run independently. Cost per task varies 20x (Fable $26.54, GPT-6.1 Sol $1.27). AA dropped SWE-bench Pro from its coding index in mid-June 2026 because it could be gamed | 1P https://artificialanalysis.ai/leaderboards/models, 2026-11-14 | H, PERISHABLE |
| **LMArena Text** | Gemini 4 Carbon 1526 (preliminary, 4k votes); Gemini 4 Argon 1522; Meta Muse Wonder 1511; Opus 5.5 1507 | The top 10 sit within about 30 Elo. This measures human preference, not task success. Preliminary entries move | 1P https://arena.ai/leaderboard/text, 2026-11-11 | H, PERISHABLE |
| **Arena Agent (best overall)** | Fable 5.2 Max 30.5%; Opus 5.5 Max 19.5%; Gemini 4 Carbon 16.9%; GPT-6 Astra 14.6% | Newer agentic arena. Anthropic holds 5 of the top 8 | 1P https://arena.ai/leaderboard, 2026-11-14 | M |
| **SWE-bench Verified** | Treat as **retired**. Aggregators show Claude models at about 95-96% | OpenAI stopped reporting it on 2026-02-23, citing contamination and flawed tests: in an audited subset at least 59.4% of problems had tests that reject correct fixes | 1P OpenAI https://openai.com/index/why-we-no-longer-evaluate-swe-bench-verified/ (via 3P summaries; page returned 403) | H |
| **SWE-bench Pro (Scale, public)** | Meta **Muse Spark 1.1 61.5%**; GPT-5.4 xHigh 59.1%; Opus 4.6 51.9% | The board is stale: no Fable, GPT-6 or Gemini 4 entries. On 2026-07-08 OpenAI **retracted** its endorsement after finding about 30% of tasks broken (200 of 730 flagged, 27.4%) | 1P https://labs.scale.com/leaderboard/swe_bench_pro_public; 3P https://the-decoder.com/openai-finds-roughly-30-percent-of-popular-ai-coding-test-is-broken/ | H |
| **Terminal-Bench** | 2.0: Codex + GPT-5.5 82.0% (April 2026 snapshot). The live site now shows **Terminal-Bench 4.1**, with an empty table | Harness matters: the same model appears several times with different agents. Versions 2.x and 4.x are not comparable | 1P https://www.tbench.ai/leaderboard (2026-11-14); 3P https://benchlm.ai/benchmarks/terminalBench2 | M, PERISHABLE |
| **METR time horizons** | Claude Mythos Preview (early) **17.4h** p50 (95% CI 8.5 to 55h); Opus 4.6 12.0h; Gemini 3.1 Pro 6.4h; GPT-5.4 5.7h | The page says it is "**no longer actively updated**" (2026-09-08), and measurements above 16h are "unreliable with our current task suite". No 5.x or 6.x generation models measured | 1P https://metr.org/time-horizons/ and https://metr.org/assets/benchmark_results_1_1.yaml | H |
| **Humanity's Last Exam** | Official page is stale (Gemini 3 Pro 38.3%). Trackers report Fable 5.2 about 74% (Nov 2026). Scale's board shows GPT-6 Astra first at 54.8% (Oct 2026). A new **HLE-Diamond** split (2026-09-22) is meant for when models hit the "noise ceiling" | Many variants (tools vs no tools, judge model). Do not compare across sources | 1P https://lastexam.ai/; 3P https://www.benchlm.ai/benchmarks/hle | L for current leader |
| **ARC-AGI-2** | GPT-6 Astra 95.0%; Gemini 4 Carbon 94.2%; GPT-6.1 Sol 94.2%; Fable 5.2 93.8% | Close to saturated | 1P https://arcprize.org/leaderboard, 2026-11-14 | H |
| **ARC-AGI-3** (interactive) | **Fable 5.2 81.2%**; Gemini 4 Carbon 65.1%; GPT-6 Astra 62.7% | Largest gap between labs on any board here. ARC Prize 2026 has closed; results on **2026-12-04** | same | H, PERISHABLE |

**How to read them (talking points)**
1. Vendor-reported scores use the vendor's own harness, effort setting and sometimes several attempts. Prefer independent runners (AA, Arena, ARC, METR, Scale).
2. Static coding benchmarks decay: both SWE-bench Verified and SWE-bench Pro lost OpenAI's endorsement within five months in 2026. Customers should build a private eval from their own repos and tickets.
3. Harness is roughly as important as the model on agentic boards (Terminal-Bench lists one model under several agents).
4. Cost per task now differs more between models than score does. Quote both.
5. No one leads everywhere. Anthropic leads AA, Arena Agent and ARC-AGI-3. Google leads Arena Text. OpenAI leads ARC-AGI-2 by a hair and Scale HLE. Meta leads the stale SWE-bench Pro board.

---

## 6. Model gateways and routing

| Gateway | State | Source | Conf |
|---|---|---|---|
| **OpenRouter** | **Stripe agreed to acquire it on 2026-08-19**; price undisclosed, reported at about $7B or more (Bloomberg); closing date not stated. 400+ models, 80+ providers; named customers NVIDIA, Zoom, Lovable. $113M Series B (May 2026). Processes 160T+ tokens per week (Menlo). Menlo is an investor | 1P https://stripe.com/newsroom/news/stripe-agrees-to-acquire-openrouter; 3P https://www.techtimes.com/articles/317353/20260529/ai-gateway-openrouter-raises-113m-google-nvidia-route-between-their-models.htm | H (deal), M (price), PERISHABLE |
| **LiteLLM** (BerriAI, open source) | **Supply-chain attack on 2026-03-24**: malicious PyPI releases 1.82.7 and 1.82.8, attributed to TeamPCP. Later CVE-2026-42271 (command injection, CVSS 8.7) | 3P https://dev.to/stockyarddev/the-llm-proxy-landscape-in-2026-helicone-acquired-litellm-compromised-and-whats-next-3oon | M. Verify the CVE on NVD |
| **Portkey** | **Acquired by Palo Alto Networks** (announced about 2026-04-30, reported closed 2026-05-29); becomes the AI gateway inside Prisma AIRS | 3P https://news.ventureintelligence.com/private-equity/ai-infra-startup-portkey-acquired-by-us-based-cybersecurity-co.-palo-alto-networks | M |
| **Cloud gateways** | Bedrock now carries Claude and OpenAI GPT-5.x/6 (GA) plus gpt-oss. Microsoft Foundry carries OpenAI and Claude (GA 2026-06-29). Vertex carries Gemini and Claude. Others: Cloudflare AI Gateway, Vercel AI Gateway, Kong | 1P AWS What's New (section 4) | H for Bedrock |

**Patterns enterprises use**
- **Alias behind a gateway**: applications call a logical name (for example `coding-default`, `cheap-summarise`), and the gateway maps it to a pinned model version per environment. A model swap becomes a config change plus an eval run. Providers support this: xAI documents `<model>`, `<model>-latest` and dated IDs (1P docs). Watch for the reverse problem: a `-latest` alias changes behaviour under you. Pin in production.
- **Tiered routing**: a frontier model for planning and hard steps, a mid or small model for bulk work, cache-heavy agent loops. Stack Overflow 2026: 27% of organisations already "use different models for different work" (1P). Menlo: buyers pay up for frontier on agentic work while open models take low-end tokens (1P).
- **Cloud-commit drawdown**: buying Claude or GPT through Bedrock, Foundry or Vertex to spend committed cloud budget. This is now possible for both leading labs on AWS.
- **Gateways have become security products**: Palo Alto bought Portkey, Stripe is buying OpenRouter, and LiteLLM was compromised. Treat the gateway as tier-0 infrastructure: pin versions, verify package hashes and isolate the keys it holds.

---

## 7. Standards

| Standard | Governance now | Adopters | Source | Conf |
|---|---|---|---|---|
| **MCP** | **Donated by Anthropic to the Agentic AI Foundation (AAIF)**, a Linux Foundation directed fund launched 2025-12-09. Founding projects: MCP (Anthropic), goose (Block), AGENTS.md (OpenAI). Largest spec revision so far: **2026-07-28** (stateless transport, enterprise security, formal governance). The SEP process and maintainer hierarchy carried over | AAIF platinum members: AWS, Anthropic, Block, Bloomberg, Cloudflare, Google, Microsoft, OpenAI. **305 members** as of 2026-10-22 (Gold additions include Ant Group, MongoDB, RBC, Vercel). NIST and Mozilla are associate members | 1P https://www.linuxfoundation.org/press/agentic-ai-foundation-surpasses-300-members-in-less-than-one-year; 1P https://aaif.io/blog/mcp-graduates-to-enterprise-infrastructure-stateless-architecture-formal-governance-and-security | H |
| **A2A** (Agent2Agent) | Google gave it to the Linux Foundation in June 2025. Reported **moved into AAIF on 2026-08-20**. IBM's ACP merged into A2A (Aug 2025). Complementary to MCP, not merged with it | 150+ supporting organisations at one year (April 2026, 1P LF). Production on Azure AI Foundry and Bedrock AgentCore. "Supporting" does not mean deployed | 1P https://www.linuxfoundation.org/press/a2a-protocol-surpasses-150-organizations-lands-in-major-cloud-platforms-and-sees-enterprise-production-use-in-first-year; 3P (AAIF move) https://enterprisedna.co/resources/news/google-a2a-aaif-agent-protocol-open-standard-august-2026 | H for LF, M for the AAIF move |
| **AGENTS.md** | Contributed by OpenAI; an AAIF founding project | 60,000+ repos claimed at AAIF launch. Read natively by Codex, Copilot, Cursor, Windsurf, Amp, Devin and others. **Claude Code reads it as a fallback when no CLAUDE.md exists (v2.1.277, 2026-09-18).** Cline uses .clinerules | 1P https://simonwillison.net/2026/Sep/18/thariq-shihipar/ (quotes Anthropic); 3P https://infoworld.com/article/4224410/claude-code-now-also-accepts-instructions-in-openais-agents-md-format.html | H |
| **Agent Skills** (SKILL.md) | Published by Anthropic as an open standard in December 2025 (agentskills.io). **Reported donated to AAIF about 2026-10-22**, including the name, GitHub org and domain | About 40 clients listed (June 2026), including GitHub Copilot, VS Code, Cursor, OpenAI Codex, Gemini CLI, Goose, OpenCode, Amp, Factory, Kiro, Mistral Vibe, Spring AI, Databricks, Snowflake. OpenAI and Microsoft added support within 48 hours of publication | 3P https://www.techrepublic.com/article/news-anthropic-agent-skills-foundation-handover/ (page returned 403; headline and snippet only); 3P https://www.noqta.tn/en/news/skill-md-open-standard-30-ai-coding-tools-adoption-2026 | M (donation), M (adopters) |

- An "Agent Plugins 1.0.0" open specification for portable agent components was reported on 2026-10-17 (3P headline only: https://news.baeke.info/articles/agent-plugins-1-0-0-releases-open-specification-for-portable-agent-components). L, not investigated.
- Critique to air for balance: AAIF has been called "a trade bloc disguised as open governance" (3P: https://www.implicator.ai/the-agentic-ai-foundation-is-a-trade-bloc-disguised-as-open-governance/). L as a claim; useful as a counterpoint.

---

## PERISHABLE watch list (likely to change by mid-February 2027)

1. ARC Prize 2026 results on 2026-12-04.
2. Gemini 4 Argon introductory pricing ends 2026-11-30 ($2/$10 to $4/$20). Gemini 4 Carbon is still "preliminary" on Arena.
3. Stripe-OpenRouter closing and any change to pricing or provider neutrality.
4. Cursor brand and roadmap under SpaceXAI; Composer 3.
5. US action on Chinese open weights beyond DeepSeek (Kimi, Qwen, GLM); contractor rules.
6. EU DSA and Ofcom outcomes on Grok; Grok 5.
7. Anthropic IPO filings (run-rate disclosures).
8. Terminal-Bench 4.1 leaderboard filling in; SWE-bench successor benchmarks.
9. Kimi K3.1 Pro licence text and third-party evals now that the weights are out.
10. Every price and leaderboard rank above.

## Gaps and unverified items

- Not read at source: the full Stack Overflow 2026 results site (per-tool percentages beyond Claude Code and Copilot), the OpenAI Verified post (403), the TechRepublic Agent Skills story (403), Hugging Face licence files for Kimi, GLM, Muse and Mistral, and xAI's trust and SOC 2 page.
- No credible Cursor, Windsurf or Codex share in the 2026 Stack Overflow blog post, and no audited coding-tool market share outside Menlo.
- The Anthropic $81B run rate rests on one secondary reading of an SEC filing.
