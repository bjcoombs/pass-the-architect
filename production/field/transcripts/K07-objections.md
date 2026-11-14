---
episode: "K07"
series: "FIELD"
slug: objections
title: "The objections drill"
description: "Ten things customers say when Claude comes up, from \"we are a Microsoft shop\" to \"we need FedRAMP\", each argued out with a question to ask back. Plus model gateways, multi-model routing, and when to recommend a competitor."
domain: "Objections"
weight: ""
target_minutes: 20
---

## In this episode

SAM: Welcome to Know the Field, from Pass the Architect. This is episode seven: the objections drill.

ALEX: Ten things customers say when Claude comes up. What do I get by the end?

SAM: A reply to each that would survive a customer who has used the other product. You will turn "we are a Microsoft shop", "our commitment is elsewhere" and "our staff use ChatGPT" into a question about which layer they are buying. You will meet "Gemini is cheaper", "Claude is expensive" and "a benchmark says" with cost per finished task and the customer's own tests. You will handle self-hosting, lock-in and FedRAMP by naming the endpoint, not the logo, and set up a gateway that keeps the exit open. And you will know when to recommend a competitor, out loud.

ALEX: Fewer lectures, more drills.

SAM: Six drills, plus the opener. [sting]

## Cold open: the Azure-committed manufacturer

SAM: Here is your opening scenario. A manufacturer runs on Microsoft: Microsoft three sixty-five with Copilot, and a large Azure consumption commitment it is behind on. Procurement will approve new A I spend only if it runs through the Azure bill. Engineering wants Claude for an internal agent that answers questions over maintenance manuals, using the Messages A P I with tool calls. What do you advise? Option A, use Azure OpenAI instead, because a Microsoft shop should stay on Microsoft's models. Option B, sign directly with Anthropic, for the newest features on day one. Option C, deploy Claude through Microsoft Foundry, billed through the Azure Marketplace against the commitment, after checking that the features they need are supported there. Option D, tell them Microsoft three sixty-five Copilot already includes Claude, so nothing more is needed.

ALEX: B. Direct is where Claude is complete. Foundry lags, and they will want those features within a year.

SAM: Hold that. We come back to it at the end. [sting]

## Segment one: what the customer already owns

SAM: Segment one: what the customer already owns. First, "we are a Microsoft shop with Copilot."

ALEX: My reply: Copilot is a wrapper. Claude's own apps do more, so make the case for Claude Enterprise.

SAM: I would push back on that. In Microsoft three sixty-five Copilot, Anthropic is a Microsoft subprocessor, so Claude sits under Microsoft's product terms and data protection addendum. And Copilot Cowork, generally available since June, runs on Anthropic models that Microsoft names, with G P T in its Frontier programme.

ALEX: So the wrapper is carrying our model.

SAM: And doing two things better than a standalone purchase: it is already in every Office app, and its admin and data controls are ones the customer already runs. Microsoft also claims Copilot Cowork is thirty to forty percent cheaper per prompt than Claude Cowork. That comes from Microsoft's own internal test: vendor-reported until the customer measures it.

ALEX: Where does it stop?

SAM: At region and at layer. Claude in Copilot starts switched off in the E U, E F T A and the U K, sits outside the E U Data Boundary until a move Microsoft has announced for December, and is not offered in G C C High. And Copilot is the enterprise wrapper. Building agents is the developer platform layer, which in a Microsoft estate means Foundry.

ALEX: The tell?

SAM: "Microsoft shop" describes the route to market, not the model. Ask which layer they mean, and whether Claude is already on in their tenant.

ALEX: Second: "our cloud commitment is elsewhere."

SAM: That one has mostly dissolved. Claude is on Bedrock, on Google Cloud, and in Foundry, where its usage counts against an Azure commitment. And OpenAI's models are now generally available on Bedrock. A cloud commitment no longer decides between the two labs.

ALEX: So what differs is features per route.

SAM: Bedrock stays inside the A W S boundary but lacks Managed Agents, the batch A P I and Agent Skills. Claude Platform on A W S, operated by Anthropic and billed through A W S, has them, but processes data outside that boundary. Foundry lacks Managed Agents and batches. Ask which features they need, then pick the route that has them.

ALEX: Third: "our staff already use ChatGPT."

SAM: Personal accounts or a company plan? Personal accounts are a data-control problem whatever the vendor. A ChatGPT Enterprise rollout with real adoption is an asset, with provisioning, audit logs and a compliance A P I.

ALEX: I would still consolidate. One chat tool, Claude, everyone retrained.

SAM: One contract and one set of controls is a real gain. But adoption is the hardest thing to buy back, and the Stack Overflow twenty twenty-six developer survey found Claude and G P T usage neck and neck. Chat is one layer of six. Put Claude where the evidence favours it: coding agents, for one. In the same survey, Claude Code was the most used coding agent, at sixty-six percent of A I users against fifty-nine for GitHub Copilot. Independent, though a usage survey, not a contract count.

SAM: Pause here and answer before we go on. A law firm rolled out ChatGPT Enterprise last year, and partners use it daily. Its forty engineers trialled Codex and Claude Code on their own repositories and prefer Claude Code. What do you advise the C I O? A, replace ChatGPT Enterprise with Claude across the firm, for consistency. B, keep ChatGPT Enterprise, add Claude Code for the engineers, and govern both under one A I policy. C, block ChatGPT and mandate Claude. D, keep everyone on OpenAI, engineers on Codex, because one vendor is simpler. [pause]

ALEX: B.

SAM: B. It fits both stated facts: high adoption, and the engineers' own trial. A and C spend that adoption on tidiness. D overrides the engineers' evidence. And two vendors is normal: the same survey found twenty-seven percent of organisations already use different models for different work.

SAM: Pause here and answer before we go on. For each statement, say true or false. One: Claude bought in Microsoft Foundry draws down an Azure consumption commitment. Two: Claude usage billed through A W S also draws down a Microsoft commitment. Three: Claude Managed Agents are available in Foundry. Four: OpenAI's models are generally available on Amazon Bedrock. Five: an Azure subscription bought through a C S P partner can buy Claude in Foundry. [pause]

ALEX: True, false, false, true, true.

SAM: Four out of five. The fifth is false: Microsoft excludes C S P subscriptions, along with free trial and credit-based ones. Many mid-sized firms buy Azure through a partner, so ask before you promise the drawdown. [sting]

## Segment two: price and proof

SAM: Segment two: "Gemini is cheaper", "Claude is expensive", and "a benchmark says X is better". Ranks here are as of November twenty twenty-six; episode eight holds the numbers.

ALEX: Easy one first. Gemini four Carbon and Argon are on an introductory price that ends this month, and Flash prices double in January.

SAM: Price structure is worth teaching: promotions that end, implicit caching only on Gemini four, and Flash versions retired and rerouted within weeks. But that is not the whole answer. On Artificial Analysis's independent index, Gemini four Carbon ranks second, at about half the cost per task of Opus five point five. Google is genuinely strong on intelligence per dollar.

ALEX: Second to what?

SAM: Fable five point two, first on that index and, of the leaders, the most expensive per task by a wide margin. So "Claude is expensive" is often true at the top end. OpenAI's mid-tier Sol model ties Sonnet five point five on the same index at about an eighth of the cost per task.

ALEX: Then what is the reply?

SAM: Three questions. Per token, or per accepted result? Is caching on? Menlo Ventures, an Anthropic investor, reports that cache reads can be ninety-five percent or more of an agent's tokens, and Claude bills them at a tenth of the input price or less. And does every step need the top model, or can a frontier model plan while a smaller one does the bulk work?

ALEX: Benchmarks, then. Fable tops the independent index, Claude tops Arena's agent board. Done.

SAM: That is the customer's mistake from the other side: you picked the boards you win. Google leads Arena's text board; OpenAI leads Arc A G I two by a hair. Nobody leads everywhere.

ALEX: So which do I cite?

SAM: An independent one that resembles the job, and then none. Static coding benchmarks decay: OpenAI stopped reporting S W E bench Verified over flawed tests, then withdrew its endorsement of S W E bench Pro after finding about thirty percent of tasks broken. On agent boards the harness matters as much as the model. And Google's launch posts cite partner benchmarks without naming Claude. Vendor-reported is vendor-reported, Anthropic's included.

ALEX: The tell?

SAM: Which benchmark, run by whom, at what cost per task, and will you run your own tickets through both?

SAM: Pause here and answer before we go on. A media analytics firm on Google Cloud runs millions of short classification calls a day, and a research agent for hard multi-step questions. Its finance lead says Gemini is cheaper, so move everything. What do you advise? A, move everything to Claude, because agent quality matters most. B, move everything to Gemini, because price per token is lower. C, build an eval from their own data for each workload, compare cost per accepted result at the price after any promotion ends, and accept that the two may land on different models. D, pick whichever model leads Arena's text board. [pause]

ALEX: C. And I would bet the classification job lands on Google.

SAM: C, and that bet is fair: high-volume classification is where small, cheap models win, and Google's are strong. A and B apply one workload's logic to both. D uses a preference board for jobs it does not measure. Either way it all bills to Google Cloud, since Claude is there too. [sting]

## Segment three: control

SAM: Segment three: "we must self-host", "we do not want lock-in", and "we need FedRAMP or HIPAA".

ALEX: Self-hosting I would concede at once. Anthropic ships no open weights, so it is Gemma or Mistral or Kimi, and we walk.

SAM: That gives away too much. Ask what must stay where: the weights, the data, operator access, or the jurisdiction. Most "self-host" requirements are about the last three. Claude on Bedrock's native endpoint is operated by A W S, with no Anthropic operator access. Google-managed Claude keeps Google as the processor, with E U and U S endpoints.

ALEX: And when they really mean weights?

SAM: Say so plainly. Air-gapped sites, on-device work and self-tuned models need open weights, and Claude cannot be there. Gemma four is now Apache two point oh; Mistral publishes weights and sells E U inference. But warn them: the best open models sit level with mid-tier closed ones on the independent index, flagship open licences have reportedly drifted to custom terms, and frontier open models need multi-node G P U clusters. Self-hosting pays at sustained high volume or under a hard sovereignty rule, not as a cheap route to the frontier.

ALEX: And U S federal work?

SAM: A D H S order removes DeepSeek from federal civilian agencies, including products built on it. Keep a model bill of materials so a swap is a configuration change.

ALEX: Lock-in. M C P is open, Skills are open, so there is none.

SAM: The protocols are open. M C P now sits with the Linux Foundation's Agentic A I Foundation, whose members include OpenAI, Google and Microsoft, and Claude Code reads OpenAI's AGENTS dot md format when no CLAUDE dot md exists. But that portability makes leaving Claude easy too. Say so.

ALEX: Then where does lock-in live?

SAM: In stateful managed services: hosted agent runtimes, conversation state, vector stores. And in churn: this year OpenAI shut its Assistants A P I, and Google stopped serving Gemini C L I to most individuals. The defence works against any vendor: your own evals, tools behind M C P, and a gateway.

ALEX: Gateways, then.

SAM: The pattern is an alias. Applications call a logical name, say "coding default", and the gateway maps it to a pinned model version per environment. A swap becomes a configuration change plus an eval run. Never point production at a "latest" alias.

ALEX: And the gateway itself?

SAM: Tier-zero infrastructure. LiteLLM reportedly suffered a supply-chain attack in March through malicious package releases. Palo Alto Networks reportedly bought Portkey, and Stripe has agreed to buy OpenRouter. Pin versions, verify hashes, isolate its keys, and check who owns it this quarter.

ALEX: FedRAMP and HIPAA.

SAM: The authorisation belongs to the endpoint, not the logo. Anthropic's documentation points FedRAMP High and HIPAA workloads to Bedrock, and Google lists FedRAMP High for Claude on its agent platform. Claude Platform on A W S is not HIPAA-ready. And OpenAI lists FedRAMP twenty X on its trust portal, so it is a real option too.

SAM: Pause here and answer before we go on. A federal health contractor needs FedRAMP High and HIPAA coverage. It runs on A W S, and its Microsoft three sixty-five tenant is G C C High. It wants Claude to summarise case files. What fits? A, Claude Platform on A W S, for the native A P I and same-day features. B, Claude on Amazon Bedrock, inside the A W S boundary, building the agent loop themselves because Managed Agents is not offered there. C, Claude inside their Microsoft three sixty-five Copilot tenant. D, a DeepSeek-based fine-tune hosted in their own account, so no data leaves. [pause]

ALEX: A. It is still billed through A W S, and they get the full platform.

SAM: That is choosing the richer route over the stated constraint. Claude Platform on A W S is not HIPAA-ready, and data is processed outside the A W S boundary. The answer is B: Claude bought through a competitor's cloud, accepting the feature gap. C is not offered in G C C High. D puts a DeepSeek-derived component into federal work, which the D H S order excludes.

SAM: Pause here and answer before we go on. Choose two. A bank wants Claude, G P T and Gemini behind one gateway, so it can switch models without rewriting applications. Which two practices fit? A, applications call logical aliases mapped to pinned model versions per environment, with an eval run before each swap. B, point production at each vendor's "latest" alias, so it always gets the newest model. C, treat the gateway as tier-zero: pin its package versions, verify hashes, and isolate the keys it holds. D, choose an open-source gateway, because open-source packages cannot be compromised. E, route every request to the cheapest model the gateway lists. [pause]

ALEX: A and C.

SAM: A and C. B is the reverse problem: the model changes without an eval. D is contradicted by this year's LiteLLM attack. E routes by price alone, with no regard for the task. [sting]

## Segment four: when the answer is not Claude

SAM: Segment four, the last objection: "we need image or video generation." The reply is yes, and it is not Claude.

ALEX: Not yet, I would say.

SAM: Do not promise a roadmap you cannot see. Claude has no first-party image, video, music, speech or embedding models. Google holds the top three places on Arena's text-to-video board, and OpenAI the top five for text to image. For realtime voice, OpenAI offers a full-duplex voice A P I and Google's Live A P I has native bidirectional audio and video; Anthropic has no equivalent.

ALEX: So where does Claude fit in that project?

SAM: Perhaps as the writer, calling an image model as a tool behind the same gateway. Or not at all. A customer remembers who told them the truth about the part you do not sell.

ALEX: Then give me the list of when to recommend a competitor.

SAM: Image, video, music and realtime voice. Open weights, for air-gapped, on-device or self-tuned models. A working Copilot or ChatGPT Enterprise rollout, for employee chat. High-volume, simple work where a cheaper model passes the customer's eval. And any compliance boundary where Claude is not offered, such as Copilot in G C C High.

ALEX: And where do we hold the line?

SAM: Agentic coding and long-running agent work, where Claude leads the independent agent boards and the largest developer survey. Then let the customer's own eval confirm it.

SAM: Pause here and answer before we go on. A consumer brand on Google Cloud wants an assistant that drafts campaign copy and produces short product videos with sound. What do you advise? A, Claude for everything, generating the video through code execution. B, Google's video model through their Google Cloud account, with Claude or Gemini for the copy depending on their own eval, all billed to Google Cloud. C, wait for Anthropic to release a video model. D, a self-hosted open-weight pipeline, to avoid depending on any vendor. [pause]

ALEX: B. I was tempted by A, but code execution writes a script, not a film.

SAM: B. It fits the platform they have and the capability they need. A stretches a tool past what it does. C sells a roadmap nobody has published. D adds G P U operations to a marketing project with no requirement that calls for them. [sting]

## Cold open: the verdict

SAM: Back to the manufacturer. Alex, you picked B, direct.

ALEX: And procurement will only approve spend on the Azure bill. Direct is a separate contract, and it does nothing for the Azure commitment.

SAM: That is the core of it. The answer is C. Foundry bills against the commitment, and a Messages A P I agent with tool calls is supported there. The check matters: without Managed Agents or the batch A P I on Foundry, needing those would change the advice. And confirm they do not buy Azure through a C S P partner. A treats "Microsoft shop" as "Microsoft's models", which it no longer means. D confuses the enterprise wrapper with the developer platform: Copilot serves their staff; it does not host their agent.

ALEX: The words that should have stopped me?

SAM: "Only through the Azure bill" and "behind on the commitment". The constraint picks the route. [sting]

## Five to remember

SAM: Five to remember. One: "Microsoft shop" and "our commitment is elsewhere" are about the route to market. Pick the route that carries the features they need.

ALEX: Two: price means cost per accepted result, not per token. Caching, tiered routing and the price after a promotion ends all change the answer.

SAM: Three: no one leads every benchmark. Cite independent boards that resemble the job, and offer to run the customer's own tasks.

ALEX: Four: compliance belongs to the endpoint. FedRAMP High and HIPAA point to Bedrock; Claude Platform on A W S is not HIPAA-ready; Copilot in G C C High has no Claude.

SAM: Five: recommend a competitor for image, video, voice and open weights, and leave working chat rollouts alone. Keep the exit open with aliases, pinned versions, your own evals, and a gateway treated as tier-zero.

## Recap: the conversation tells

SAM: Recall first. Pause and name the ten objections, and the question you ask back for each. [pause]

ALEX: Microsoft shop: which layer? Commitment elsewhere: which features? ChatGPT already: personal or company plan? Gemini cheaper, and Claude expensive: per token or per result? Benchmark: whose, and at what cost? Self-host: what must stay where? Lock-in: where is the state? FedRAMP or HIPAA: which endpoint? Image or video: not us.

SAM: All ten. Now as conversation tells. If a customer says "we are a Microsoft shop", ask whether Claude is already on in their tenant.

ALEX: If they say "our money is on A W S", ask which features they need, then pick the route.

SAM: If they say "staff use ChatGPT", ask whether it is a governed rollout. If it is, leave it and put Claude where the work favours it.

ALEX: If they say "Gemini is cheaper" or "a benchmark says", ask for cost per accepted result on their own tasks.

SAM: If they say "we must self-host", ask whether they mean weights, data, operators or jurisdiction.

ALEX: If they say "no lock-in", show them aliases, pinned versions and their own evals.

SAM: If they say "FedRAMP or HIPAA", ask which endpoint holds the authorisation.

ALEX: And if they say "we need video or voice", recommend the competitor that does it.

SAM: Next, episode eight: the state of play for November twenty twenty-six, with every number we kept out of this one.
