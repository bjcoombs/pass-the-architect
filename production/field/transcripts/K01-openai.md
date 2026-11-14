---
episode: "K01"
series: "FIELD"
slug: openai
title: "OpenAI"
description: "OpenAI on all six layers: the Astra-to-Luna model tiers, the Responses API and agent stack, Codex and ChatGPT Work, ChatGPT Enterprise, and its models on Azure and Bedrock. Where OpenAI is stronger than Claude, where Claude leads, and the questions to ask a customer."
domain: "OpenAI"
weight: ""
target_minutes: 22
---

## In this episode

SAM: Welcome to Know the Field, from Pass the Architect. This is episode one: OpenAI.

ALEX: The rival I get asked about most. What will I be able to do by the end?

SAM: Place OpenAI on all six layers, from the model to the route to market. Map its agent stack onto Claude's, piece by piece. Compare Codex with Claude Code without calling either a copy. Answer a regulated customer's data questions endpoint by endpoint. And name what OpenAI does better than Claude today, with the evidence, as well as where Claude leads.

ALEX: And the Microsoft question?

SAM: That too: who sells OpenAI's models now, and whose cloud commitment the spend draws down. We start with a phone call. [sting]

## Cold open: the phone line

SAM: Here is your opening scenario. A utility runs Claude for its back office: billing disputes, account letters, internal agents. Now it wants an assistant that answers customer phone calls, talks naturally, and copes when callers interrupt mid-sentence. The contact-centre lead asks what to use for the voice layer. Option A, OpenAI's full-duplex voice model for the phone channel, with Claude kept on the back-office work. Option B, build it on Claude by wrapping separate speech-to-text and text-to-speech services around the Messages A P I, so everything stays with one model vendor. Option C, move the whole estate to OpenAI, so one vendor covers voice and back office. Option D, run the phone line on Claude Managed Agents, because it handles long sessions.

ALEX: B. They already trust Claude, the back office is on Claude, and speech services are a solved problem. One model vendor, one contract.

SAM: Hold that. We come back to it at the end. [sting]

## The model

SAM: Layer one, the model. OpenAI renamed its line this year. The current family uses codename tiers: Astra at the top, then Sol, then Terra, then Luna, the cheapest. G P T six Astra is the flagship. The mini and nano names and the separate o-series are gone from the current line.

ALEX: So where did the reasoning models go?

SAM: Into everything. The current models are all reasoning models with an effort setting, and o three is scheduled for shutdown in December.

SAM: Beyond text, OpenAI covers more modalities first-party than Anthropic does: image generation, transcription, translation and realtime voice, including a full-duplex voice model that can place phone calls. For open weights there is G P T oss, Apache licensed, still the twenty twenty-five release, with no successor the research could find.

ALEX: And quality? This is where I expect Claude to win.

SAM: Here one dated line earns its place. As of November twenty twenty-six, on Artificial Analysis's independent index, Claude Fable five point two leads, and Opus five point five sits above G P T six Astra. On Arena's agent leaderboard, also independent, Fable scores roughly double OpenAI's best.

SAM: The middle tier tells a different story. On that same index, G P T six point one Sol scores level with Sonnet five point five, at roughly one-eighth of the cost per task.

ALEX: One-eighth. That is not a rounding error.

SAM: No. It is the first thing OpenAI does better today: price-performance in the middle tier.

SAM: Two habits for reading OpenAI's own numbers. Its launch table for Astra reportedly compared it against Fable five point one, not the newer five point two, and those figures are vendor-reported. And OpenAI stopped reporting S W E bench Verified in February, after its own audit found flawed tests. Its headline coding numbers now come from newer benchmarks, so never line them up against an old Claude S W E bench score.

ALEX: Context window?

SAM: Parity at the top tiers. Do not pitch a context lead; there isn't one.

SAM: The question to ask the customer: which tier are you comparing? Astra against Fable is one conversation. Sol against Sonnet is another, and much closer. [sting]

## Platform and agent stack

SAM: Layers two and three. The developer platform is the Responses A P I: one endpoint with built-in tools for web search, file search, a hosted shell, computer use, image generation, remote M C P servers, tool search, and skills. Chat Completions still works and carries no deprecation notice, but OpenAI steers tool calling to Responses.

ALEX: Skills? As in our skills?

SAM: Versioned bundles that run in the hosted shell. And caching has converged too. OpenAI's newer models offer explicit cache breakpoints and charge a premium on cache writes, which is close to Anthropic's model. A year ago OpenAI had no write premium.

ALEX: So caching mechanics are no longer a Claude talking point.

SAM: Not the mechanism. Compare effective rates on the customer's own traffic instead.

SAM: Now the agent stack. OpenAI's own guide offers four choices. The Agents A P I, where OpenAI runs the loop. The Agents S D K, where you run it. Raw Responses. And ChatKit, an embeddable chat interface.

ALEX: That maps straight across. Agents A P I is Managed Agents, Agents S D K is the Claude Agent S D K, Responses is the Messages A P I.

SAM: Close, with differences worth knowing. The Agents S D K is M I T licensed, in Python and TypeScript, with handoffs, guardrails, sessions, tracing and voice agents. It is provider-agnostic: the Python readme claims support for over a hundred other models. The Claude Agent S D K is Claude Code's harness as a library, built for Claude. One is a portable framework; the other is a coding-grade harness for one model family.

SAM: The Agents A P I went into public beta in September. It is the managed Codex harness: sessions, compaction, multi-agent delegation, M C P and skills, with sandboxes that OpenAI hosts, you host, or a partner hosts. There is no separate fee; you pay for tokens and container time.

ALEX: Here is where I'd warn people off. OpenAI shut down the Assistants A P I in August. Agent Builder, the visual canvas, and its Evals platform go at the end of this month. Stored prompt objects too. Why build on that?

SAM: The retirements are real, and a customer who built on the Agent Builder canvas is migrating right now. Anthropic's docs publish not-sooner-than retirement dates per model, and that is a fair point to make.

SAM: But look at what went: a canvas, a hosted eval tool, stored prompts, an older assistants layer. The Responses A P I and the open-source Agents S D K are where OpenAI pointed people, and they are still there.

ALEX: So the tell?

SAM: Ask which layer they built on. Primitives and an open-source S D K, low risk. A hosted canvas or a beta service, plan the exit before you build.

SAM: One more fact before a drill. The Agents A P I beta keeps data in the United States only and is not eligible for zero data retention, even with a self-hosted sandbox. OpenAI also lists its stateful features as not eligible: conversations, ChatKit threads, agents, vector stores, files and batches. And zero data retention itself needs OpenAI's approval.

SAM: Pause here and answer before we go on. A European insurer has OpenAI's approval for zero data retention and must keep it on everything its claims agent touches. Processing must happen in the E U, and the team wants to save engineering time. What fits? A, the Agents A P I with OpenAI-hosted sandboxes. B, the Agents A P I with a self-hosted sandbox in the insurer's own E U cloud. C, run the loop itself with the Agents S D K on its own infrastructure, call an E U data residency project, keep conversation state in its own store, and check zero data retention eligibility for each endpoint it calls. D, keep the loop simple and store state in OpenAI's Conversations A P I. [pause]

ALEX: B. The sandbox sits in their cloud, the data stays home, and OpenAI still runs the loop. That saves the engineering.

SAM: That is the trap. A self-hosted sandbox moves tool execution, not the A P I's terms: the Agents A P I is still United States only and still outside zero data retention. A fails for the same reasons. D puts state in a store on the not-eligible list. C is right: the insurer runs the loop, owns the state, and checks every endpoint. It costs engineering, and that is the price of the constraint. [sting]

## Codex and ChatGPT Work

SAM: Layer four, the coding agent. Codex runs in the Chat G P T desktop app, on the web and mobile, as a C L I, an I D E extension and a cloud service, with GitHub, Slack and Linear integrations. The C L I is open source under Apache two point oh, with a Rust core.

ALEX: I've read the config docs. A project instruction file, layered user, project and admin config, hooks called Pre Tool Use and Post Tool Use and Stop, subagents as files, skills, plugins, M C P. It is Claude Code with a different logo.

SAM: Careful. The shapes have converged, and convergence runs both ways. The project file is AGENTS dot md, which OpenAI contributed to the Linux Foundation's Agentic A I Foundation, the same foundation Anthropic gave M C P to. Since September, Claude Code reads AGENTS dot md when a repository has no CLAUDE dot md.

SAM: Call Codex a clone in front of a developer who uses both, and you lose the room.

ALEX: Fair. So what is actually different?

SAM: Three things. Codex makes the operating-system sandbox the default boundary, with workspace writes allowed, and layers approvals on top. Its subagents inherit the parent's sandbox and cannot loosen it. And its hooks run only command and M C P tool handlers; prompt-based handlers are parsed but skipped.

SAM: Then distribution, the second thing OpenAI does better. Codex ships inside the consumer Chat G P T app, down to the free tier, and OpenAI's models are sold direct, on Azure and on Bedrock. Many of a customer's developers have tried Codex before procurement has heard of it.

ALEX: And Chat G P T Work?

SAM: Reportedly a Codex-based agent for knowledge workers, launched in July: documents, spreadsheets, decks and small web apps over connected data, with scheduled tasks. It is aimed squarely at Cowork. Sources disagree on which plans get it, so check before quoting.

SAM: On market size, Menlo Ventures' November enterprise report, and Menlo is an Anthropic investor, puts Claude Code and Codex together at most of the spend on coding tools. It does not split the two. Treat coding as a two-way race, not a Claude lock.

SAM: The question to ask the customer: which of your developers already use Codex, and what must your sandbox and approval policy be?

SAM: Pause here and answer before we go on. For each statement, say true or false. One: the Codex C L I is open source under Apache two point oh. Two: a Codex subagent can be given a looser sandbox than its parent when a task needs more access. Three: Claude Code reads AGENTS dot md when a repository has no CLAUDE dot md. Four: Codex hooks run prompt-based handlers as well as command handlers. [pause]

ALEX: True, false, true, false.

SAM: All four. Subagents inherit the parent's sandbox and cannot override it. And Codex parses prompt handlers but skips them; it runs command and M C P tool handlers only. [sting]

## Enterprise and the clouds

SAM: Layers five and six. The enterprise wrapper is Chat G P T Business, formerly Team, and Chat G P T Enterprise. Enterprise adds automated user provisioning, customer-managed encryption keys, role-based access, a Compliance A P I and audit logs. OpenAI's trust portal lists S O C two Type two, a set of I S O certificates including the A I management standard, and a FedRAMP twenty X listing.

ALEX: Data residency?

SAM: On the A P I, storage and processing in the United States, the E U, Australia, Japan, India and the U A E, though some of those regions process only the cheapest model. The region is fixed when a project is created, and residency carries a price uplift.

ALEX: "Fixed when a project is created." That one bites.

SAM: So ask in the first meeting. On H I P A A, a business associate agreement is reported for the A P I and Enterprise, but the research could not confirm it first-party. Have the customer get it in writing.

SAM: Now the route to market, and the Microsoft relationship. OpenAI's models are sold through Microsoft Foundry, where Azure OpenAI now lives. G P T six Astra was generally available in Foundry on its launch day, in global and United States data zone deployments, with standard and provisioned throughput.

ALEX: So Azure is the OpenAI cloud.

SAM: It was the obvious one. Two things changed this year. Since June, OpenAI's models and Codex are on Amazon Bedrock, at OpenAI's list prices, counting toward A W S commitments, and Codex and Chat G P T Work can be pointed at Bedrock. And Microsoft hedged too: Claude is now in Foundry, billed through Azure Marketplace and eligible for the customer's Azure consumption commitment. Microsoft's Copilot Cowork runs on Anthropic models, with G P T in its early-access programme.

ALEX: Same model, different cloud. Is it the same product?

SAM: Not quite. At Astra's launch, Foundry lacked mid-turn steering, which OpenAI's own A P I had. Same lesson as Claude on other clouds: the model arrives fast, features can lag. Check the feature, not the logo.

SAM: The frameworks travel as well. The OpenAI Agents S D K runs as a hosted agent in Foundry, next to the Claude Agent S D K, and on Bedrock AgentCore.

SAM: The question to ask: whose cloud commitment does this spend need to draw down?

SAM: Pause here and answer before we go on. A retailer has a large A W S spending commitment. Its developers want Codex and G P T models. Procurement says the spend must draw down the A W S commitment, and no new vendor contract is allowed this year. What do you recommend? A, Chat G P T Enterprise bought direct from OpenAI. B, OpenAI's models on Amazon Bedrock, with Codex pointed at Bedrock. C, Claude on Bedrock instead, because Claude is the only leading lab's model there. D, OpenAI's models through Microsoft Foundry. [pause]

ALEX: B. Through gritted teeth, but B.

SAM: B. It meets both constraints with the product the developers asked for. A is a new contract and misses the commitment. C rests on a claim that stopped being true in June, and ignores what they asked for. D draws down the wrong cloud's commitment. If they later want Claude for agentic work, it sits on the same bill. [sting]

## Pushback

SAM: Pushback round. Make the loyal case, Alex.

ALEX: Claude leads the independent leaderboards. That should end the conversation.

SAM: It leads the boards that matter most for agentic work today, and that is a fair opening. But no one leads everywhere: OpenAI narrowly tops at least one other independent board, and ranks move monthly.

SAM: The tell: when a customer quotes a leaderboard, ask for an eval on their own tasks, and offer to help build it.

ALEX: Then price. A cheaper mid tier is a race to the bottom. Customers pay for quality.

SAM: That underrates them. Sol scored level with Sonnet on an independent index at a fraction of the cost per task. That is quality held and cost cut. Call the middle tier contested, and benchmark Sol before you defend Sonnet.

ALEX: Compliance, then. Claude is the safe enterprise pick. OpenAI's Agents A P I cannot even do zero data retention.

SAM: True of that beta, and worth saying. But both vendors draw lines around stateful features. Before you claim an advantage, put Claude Managed Agents through the same two questions: where does the data live, and is it eligible for zero data retention?

SAM: Decide per endpoint, not per logo.

ALEX: Last one. Microsoft shops default to Azure OpenAI. We cannot win there.

SAM: Too gloomy. Claude is in Foundry, on the same Azure bill and commitment. The catch: Claude in Foundry lacks Managed Agents and the batch A P I today. Episode three covers that in full.

SAM: Pause here and answer before we go on. Choose two. A bank's C T O asks where OpenAI is genuinely stronger than Claude today. Which two claims survive a customer who has used both? A, price-performance in the middle tier. B, reach: Codex in the consumer app down to the free tier, and models sold direct, on Azure and on Bedrock. C, the top of the independent agentic leaderboards. D, a longer context window. E, a more stable platform with fewer retirements. [pause]

ALEX: A and B. C is where Claude leads.

SAM: A and B. C is Claude's, on Artificial Analysis and Arena's agent board. D is parity, so neither side should claim it. E runs the other way: Assistants, Agent Builder and Evals were all retired within about fifteen months. [sting]

## Cold open: the verdict

SAM: Back to the utility's phone line. Alex, you picked B: wrap Claude in speech services.

ALEX: The loyal answer. One model vendor.

SAM: A reasonable instinct, but the constraint is natural conversation with interruptions. OpenAI ships a full-duplex voice model built for exactly that, along with realtime models and phone calling. As far as the research found, Anthropic has no first-party realtime voice equivalent.

SAM: So the answer is A: OpenAI for the phone channel, Claude where it already works. B makes the customer build and tune a voice pipeline it never asked to own. C throws away a working back office to save one contract. D answers a different question: Managed Agents runs long agent sessions, not voice.

ALEX: And the words that should have stopped me?

SAM: "Talks naturally" and "interrupt mid-sentence". When the constraint is a modality, check who ships it first-party. [sting]

## Five to remember

SAM: Five to remember. One: OpenAI's tiers are Astra, Sol, Terra and Luna, all reasoning models with an effort setting. Compare tier to tier: Astra with Fable, Sol with Sonnet.

ALEX: Two: OpenAI is stronger today on mid-tier price-performance, first-party voice, and reach. Claude leads the independent agentic leaderboards. Say both, and name the source.

SAM: Three: the stacks map across. Agents A P I to Managed Agents, Agents S D K to the Claude Agent S D K, Responses to the Messages A P I. Build on primitives; the canvas and evals tool were the parts retired.

ALEX: Four: Codex and Claude Code have converged, and AGENTS dot md is shared ground. Codex differs on sandbox by default, subagents that cannot loosen it, and a free-tier reach.

SAM: Five: OpenAI is on Azure and Bedrock, so the cloud no longer picks the lab. For regulated work, check residency and zero data retention per endpoint, on both vendors.

## Recap: the conversation tells

SAM: Recall first. Pause and name the four segments, and the question to ask the customer in each. [pause]

ALEX: The model; platform and agent stack; Codex and Chat G P T Work; enterprise and the clouds. Which tier are you comparing; which layer did you build on; who already uses Codex; whose commitment does the spend draw down.

SAM: Now as conversation tells. If a customer says G P T six beats Claude, ask which tier against which, and whose benchmark.

ALEX: If they say OpenAI is cheaper, ask for cost per task on their own traffic, not the list price.

SAM: If they built on Assistants or Agent Builder, they are migrating now. Offer the primitives route, whichever model they pick.

ALEX: If they need zero data retention, ask which endpoints. OpenAI's Agents A P I and stateful features sit outside it.

SAM: If they call Codex a Claude Code clone, correct it: converged, sharing AGENTS dot md, with a different sandbox default.

ALEX: If they need phone calls with natural interruption, look at OpenAI's voice stack first.

SAM: If procurement says A W S commitment only, both labs are on Bedrock now. If it says Azure, both are in Foundry.

ALEX: Next, episode two: Google.
