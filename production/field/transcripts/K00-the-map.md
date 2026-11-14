---
episode: "K00"
series: "FIELD"
slug: the-map
title: "The map: six layers for comparing AI vendors"
description: "Six layers for comparing any AI vendor with Claude, how to read a benchmark and a market report without being fooled, which facts are safe to quote and which to check first, and the route through the series."
domain: "The field"
weight: ""
target_minutes: 12
---

## In this episode

SAM: Welcome to Know the Field, from Pass the Architect. This is episode zero: the map.

ALEX: What will I be able to do by the end?

SAM: Place any vendor's offering on six layers, so you compare like with like. Read a benchmark and know who ran it, what it measures and whether it still means anything. Read a market report and name its source. Tell a slow fact, safe to quote, from a fast one you check first. And you'll know the route through the next eight episodes.

ALEX: Bias declared: I build on Claude daily and use the others lightly.

SAM: Which makes you the right sparring partner. [sting]

## Cold open: the launch post

SAM: A manufacturing customer's C T O forwards you a rival lab's launch post. It says the new model beats Claude on a coding benchmark, from runs the lab did itself. The C T O asks whether to switch the team's coding agent. What do you do first? Option A, ask the lab for its harness and settings, and accept the result once disclosed. Option B, point to an independent leaderboard where Claude ranks higher. Option C, run both models on a small private eval built from the team's own repositories and tickets, comparing cost per task as well as score. Option D, tell the C T O vendor-reported numbers are marketing and can be ignored.

ALEX: B. Independent beats vendor-reported, and on the independent boards Claude is ahead.

SAM: Hold that. We come back to it at the end. [sting]

## The six layers

SAM: First, the map: six layers, named the same all series. One, the model. Two, the developer platform: the A P I and its tools. Three, the agent stack: frameworks and runtimes for agents. Four, the coding agent. Five, the enterprise wrapper: the chat product, admin, compliance and data controls. Six, the route to market: direct, a cloud marketplace, or a bundle such as Microsoft three sixty-five.

ALEX: Six is a lot. Customers ask which model is best. Why not stop there?

SAM: Because the model is rarely what they buy. They buy seats in a chat product, or spend a cloud budget they've already committed. The tell: when a customer says "better", ask "better at which layer?"

ALEX: Give me one real example per layer.

SAM: The model: DeepSeek publishes open weights anyone can run. But a model carries its provenance. A United States Homeland Security order removes DeepSeek products from federal civilian agencies, including products built on DeepSeek.

SAM: The developer platform: OpenAI's Responses A P I has built-in tools, among them web search, file search, a hosted shell, computer use and remote M C P servers. Compare them with Claude's tool by tool.

SAM: The agent stack: Google's Agent Development Kit, A D K. Open source under Apache two point oh, in five languages, and model-agnostic, with an adapter for Claude. It speaks both M C P and A to A.

ALEX: The coding agent has to be Cursor. A nice editor sitting on top of Claude.

SAM: That undersells it. Cursor builds its own models: Menlo Ventures, an Anthropic investor, reports its Composer two was built on Kimi, an open-weight model from Moonshot. And SpaceX completed its purchase of Cursor in August, so Cursor and Grok now share an owner. Check where data goes and which model is the default.

ALEX: Fair. Enterprise wrapper?

SAM: Microsoft three sixty-five Copilot. Claude runs inside it, with Anthropic as a Microsoft subprocessor, on by default in commercial tenants outside the E U, E F T A and the U K. Claude can win inside someone else's wrapper.

ALEX: And route to market?

SAM: Amazon Bedrock. It now sells OpenAI's models beside Claude, so a customer with an A W S commitment can buy either lab without a new contract.

SAM: Pause here and answer before we go on. For each item, name the layer. One: an admin setting that turns a model off for E U staff. Two: buying Claude in Microsoft Foundry to draw down an Azure commitment. Three: an open-source framework for multi-agent workflows. Four: web search built into the A P I. [pause]

ALEX: One, enterprise wrapper. Two, route to market. Three, agent stack. Four, developer platform.

SAM: All four. [sting]

## Reading a benchmark

SAM: Second skill: reading a benchmark. Four questions. Who ran it? What does it measure? Is it contaminated? Is it saturated?

ALEX: Who ran it is easy. Vendor-reported numbers come from the vendor's own harness, effort setting, and sometimes several attempts.

SAM: And check what they compared against. Google's launch posts cite partner benchmarks and never name Claude. That isn't lying; it's choosing the frame.

ALEX: So ignore vendor numbers.

SAM: No. Anthropic publishes launch numbers too. A vendor number is a claim to check, not a lie. Prefer independent runners, and say which kind you're quoting.

ALEX: And the independent ones all measure the same thing?

SAM: Far from it. Artificial Analysis runs a composite of about ten evaluations itself, with cost per task beside the score. Arena ranks models by human preference votes, not task success. Task boards such as Terminal-Bench test agents, where the harness matters about as much as the model: one model is listed several times under different agents.

ALEX: Contamination?

SAM: Test problems leaking into training data, or tests that are wrong. In February OpenAI stopped reporting S W E bench Verified, the old coding headline, citing contamination and tests that reject correct fixes. In July it withdrew its endorsement of S W E bench Pro, finding about three in ten tasks broken.

ALEX: And saturation is everyone scoring in the nineties.

SAM: Near the ceiling, gaps are noise. The A R C A G I two puzzle board is close to saturated; its interactive successor still separates the labs.

ALEX: Let me make the loyal case. As of November twenty twenty-six, Claude leads the Artificial Analysis index and Arena's agent board. That settles it.

SAM: It settles those two boards. Gemini leads Arena's text ranking, and OpenAI edges A R C A G I two. Nobody leads everywhere, and a customer who uses Gemini knows it. Lead with the board that matches their work.

SAM: Pause here and answer before we go on. For each statement, say true or false. One: Arena's text leaderboard measures which model completes tasks best. Two: S W E bench Verified is still the best public test of coding agents. Three: on an agent benchmark, one model can score differently under different harnesses. Four: a score a vendor publishes for its own model is independent evidence. [pause]

ALEX: False, false, true, false.

SAM: Right. One is preference. Two: OpenAI stopped reporting it. Four is vendor-reported, whoever the vendor. [sting]

## Reading a market report

SAM: Third skill: market reports. The one you'll hear quoted most is Menlo Ventures' twenty twenty-six enterprise A I report, which puts Anthropic first in enterprise A P I spend.

ALEX: Which ends the argument.

SAM: It's one input. When you cite it, say three things. Menlo is an Anthropic investor, and says so. It surveyed about four hundred United States decision-makers, so shares are estimates, not audited revenue. And it counts A P I spend only: Google's figure excludes Workspace and the Gemini app bundles.

ALEX: So Google's small A P I share might just mean Google sells through Workspace.

SAM: Partly; Menlo also says Google's spend leans to its cheaper Flash models. Read the method before the headline.

SAM: Pause here and answer before we go on. Choose two. A bank's board member quotes a market report showing Anthropic far ahead of Google in enterprise A I. Which two caveats should you raise? A, the publisher is an Anthropic investor. B, it counts A P I spend, not spend bundled into productivity suites. C, survey-based reports are made up and should never be cited. D, the lead proves Claude is the right model for the bank's use case. E, the report is unreliable because it is recent. [pause]

ALEX: A and B.

SAM: Yes. A is disclosure, B is scope. C overcorrects: a survey with a stated method is evidence, with limits. D confuses share with fit. E is backwards. [sting]

## Slow facts and fast facts

SAM: Fourth: slow facts and fast facts. Slow facts are architecture, licences, protocols, governance, business models and sales channels: quote them plainly. Fast facts are prices, benchmark ranks, context windows, version numbers and which models a cloud carries: check them first.

ALEX: A slow one?

SAM: M C P now sits in a Linux Foundation fund, the Agentic A I Foundation, beside OpenAI's AGENTS dot md and Google's A to A. That won't flip next month.

ALEX: Here's a slow fact I'd quote: Bedrock is Claude's home ground. Claude is the frontier model on A W S.

SAM: That's a fast fact dressed as a slow one. OpenAI's models went generally available on Bedrock this year, and Claude is in Microsoft Foundry. Both labs now sell through A W S and Azure, so the cloud no longer picks the lab. The tell: a fact that names a version or a list is fast.

SAM: Pause here and answer before we go on. A logistics company runs on A W S with a large committed spend. Procurement will not sign with a new vendor this year. The team wants Claude for document agents, and wants to trial an OpenAI model against it. What do you recommend? A, sign a direct contract with Anthropic and another with OpenAI. B, buy both through Amazon Bedrock on the existing commitment. C, self-host an open-weight model instead. D, wait for next year's procurement cycle. [pause]

ALEX: B. And it stings a little to recommend a channel that sells the competition.

SAM: It fits the constraint. A needs the contracts procurement ruled out. C swaps both models for one nobody asked for. D loses a year. Bedrock does lack some Claude features, Managed Agents among them; episode four covers what changes.

ALEX: So where does the series go from here?

SAM: One to three: OpenAI, Google, and Microsoft as competitor and channel. Four: Claude through other clouds. Five: open weights, xAI and sovereignty. Six: coding agents. Seven: ten customer objections. Eight holds the numbers, dated, and is re-recorded when they move. [sting]

## Cold open: the verdict

SAM: Back to the launch post. Alex, you picked B.

ALEX: Which answers a general question. The C T O asked about one team.

SAM: That's the core of it. The answer is C. A private eval measures the work they actually do, and cost per task catches a model that wins on score but costs far more per job. A still trusts the vendor's frame. B wins the argument and misses the question: a public board can't see their code. D dismisses evidence the C T O will keep hearing.

ALEX: The words that should have stopped me?

SAM: "Whether to switch the team's coding agent". A decision about their work needs a test on their work. [sting]

## Five to remember

SAM: Five to remember. One: six layers. Model, developer platform, agent stack, coding agent, enterprise wrapper, route to market. Compare like with like.

ALEX: Two: before trusting a benchmark, ask who ran it, what it measures, and whether it's contaminated or saturated.

SAM: Three: nobody leads everywhere. Name the board, and the kind of source: independent or vendor-reported.

ALEX: Four: when you cite Menlo, say Menlo invests in Anthropic, that it's a survey, and that it counts A P I spend only.

SAM: Five: quote slow facts plainly; check prices, ranks, versions and cloud line-ups first.

## Recap: conversation tells

SAM: Recall first. Pause and name the four skills from this episode, and the question each one makes you ask. [pause]

ALEX: Six layers: better at which layer? Benchmarks: who ran it, and what does it measure? Market reports: who published it, and what does it count? Slow and fast facts: true next month?

SAM: Now as conversation tells. If a customer says "their model is better", ask "better at which layer, for which job?"

ALEX: If a customer quotes a launch post, ask whose harness, against which version, and what it costs per task.

SAM: If they quote a leaderboard, ask whether it measures preference or task success, and whether the top is crowded near the ceiling.

ALEX: If someone quotes Menlo, in either direction, name the investor link and the A P I-only scope.

SAM: If a customer says their cloud decides, ask what's on their commitment. And if a fact has a version number in it, check it before you repeat it.

ALEX: Next, episode one: OpenAI, from the Responses A P I to Codex.
