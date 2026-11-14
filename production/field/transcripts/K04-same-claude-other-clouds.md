---
episode: "K04"
series: "FIELD"
slug: same-claude-other-clouds
title: "Same Claude, different cloud"
description: "Buying Claude through Amazon Bedrock, Claude Platform on AWS, Google Cloud or Microsoft Foundry instead of direct: who operates each, which features it carries, where the data goes, and which commitment it draws down. Plus AWS's own stack: Nova, AgentCore, Strands and Kiro."
domain: "Claude on AWS, Google Cloud and Azure"
weight: ""
target_minutes: 20
---

## In this episode

SAM: Welcome to Know the Field, from Pass the Architect. This is episode four: same Claude, different cloud.

ALEX: An odd title for a series about competitors.

SAM: Because the clouds are both. They resell Claude, and they sell what competes with Anthropic's own platform. By the end you'll be able to rebuild one table in your head: for each way of buying Claude, who operates it, which features it carries, where the data goes, and which commitment the spend draws down. You'll know the two doors on A W S, the two on Google Cloud and the two on Azure. And you'll place A W S's own stack, Nova, Agent Core, Strands and Kiro, on the six layers from episode zero.

ALEX: So this is the route to market episode. The model stays the same; the developer platform around it doesn't.

SAM: That gap is where customers get surprised. [sting]

## Cold open: the health insurer

SAM: A U S health insurer runs everything on A W S and has a large A W S spending commitment to burn down. It wants Claude to summarise claims files containing patient data, and compliance says the workload must stay inside the A W S boundary under its HIPAA programme. Which route fits? Option A, the Claude A P I direct, with U S-only inference switched on. Option B, Claude Platform on A W S, the native Claude A P I billed through A W S Marketplace. Option C, Claude in Amazon Bedrock. Option D, Claude in Microsoft Foundry, hosted on Azure, because prompts stay inside the cloud there too.

ALEX: B. It's the real Claude A P I with every feature, and it lands on the A W S bill.

SAM: Hold that. We come back to it at the end. [sting]

## Segment one: two questions

SAM: Counting each hosting option separately, there are seven doors to Claude. Direct. On A W S, Bedrock and Claude Platform on A W S. On Google Cloud, Google-managed and Anthropic-managed. On Azure, Foundry hosted on Azure, or hosted on Anthropic.

ALEX: Too many to memorise.

SAM: So ask two questions. Who operates the service? That decides the features and who processes the data. Whose bill does it land on? That decides which commitment it burns. Who runs it decides what it does; whose bill decides what it burns.

ALEX: Why does the operator decide the features?

SAM: When the cloud operates Claude, as on Bedrock or Google-managed, you get the model and the core of the Messages A P I: prompt caching, extended thinking, tool use, citations, structured outputs, the long context window. You don't get Anthropic's server-side platform: the Files A P I, Agent Skills, code execution, the M C P connector, the Message Batches A P I, Managed Agents. Those are services Anthropic runs. That comes from Anthropic's own documentation, which lists what each door doesn't support.

ALEX: And when Anthropic operates it, but you buy through the cloud?

SAM: Claude Platform on A W S and Anthropic-managed Google carry most of that platform, Managed Agents included. The trade is the boundary: Anthropic processes the data, and on A W S the documentation says plainly it's processed outside the A W S security boundary.

ALEX: A year ago, "we're an A W S shop" was half an argument for Claude.

SAM: Not any more. OpenAI's models are generally available on Bedrock, and Claude is generally available in Foundry. The cloud no longer picks the lab. It picks the door. [sting]

## Segment two: the A W S doors

SAM: Door one, Amazon Bedrock. A W S operates it, and Anthropic has no operator access. It has a newer endpoint that speaks the native Messages shape and an older Invoke Model path. As of November twenty twenty-six, only the older path serves Fable five point two and Mythos five point two, so check the model against the endpoint.

ALEX: Bedrock is the second-class Claude, though. Models late, features never.

SAM: Half of that is wrong. According to A W S, Opus five point five was on Bedrock the day Anthropic announced it. And Bedrock beats direct on two things. Regulated work: Anthropic's own documentation points FedRAMP High, I L four and five, and HIPAA workloads to Bedrock. And it's native A W S: I A M, quotas raised through A W S without asking Anthropic, spend against the A W S commitment.

ALEX: And the half that's right?

SAM: Features. No Files, no Skills, no server-side tools, no Batches A P I, no Managed Agents. Bedrock has its own batch inference instead. So the question for the customer: do you need the boundary, or the platform?

SAM: Door two, Claude Platform on A W S, generally available since May. The native Claude A P I, operated by Anthropic, signed with A W S I A M, logged in Cloud Trail, billed through A W S Marketplace in Claude Consumption Units. It carries Files, Batches, Skills, code execution, the Compliance A P I, customer-managed keys and Managed Agents, and Anthropic describes feature access as typically same-day.

ALEX: Then that's my default for A W S customers.

SAM: Read the gaps first. Not HIPAA-ready. No fast mode. Zero data retention is opt-in. And signing up creates a new Anthropic organisation; your existing one isn't converted.

ALEX: Why does that matter?

SAM: Commercially. Private offers don't transfer between Bedrock and Claude Platform on A W S, or from an old organisation to the new one, and discounts don't apply backwards. On whether Platform spend counts toward the A W S commitment: reportedly yes, and Anthropic's documentation talks about retiring A W S commitments, but get A W S's own wording before a customer plans a drawdown around it.

ALEX: Then my case for skipping both. Direct gets every feature on day zero.

SAM: On features, right. But the constraint often isn't features. If procurement only approves spend on an existing commitment, or legal only signs the cloud's data terms, direct loses before features come up. Ask what the customer must keep, then pick the door.

SAM: One more quirk: partner clouds set their own retirement dates. Opus four point one and Sonnet four are retired on the Claude A P I and still served on Bedrock.

SAM: Pause here and answer before we go on. For each statement, say true or false. One: on Bedrock, Anthropic staff can operate the serving infrastructure. Two: signing up for Claude Platform on A W S converts your existing Anthropic organisation in place. Three: a private-offer discount agreed for Bedrock carries over to Claude Platform on A W S. Four: a model retired on the Claude A P I can still be served on Bedrock. Five: prompt caching works on Bedrock. [pause]

ALEX: False, false, false. Four, false: retired is retired. Five, true.

SAM: Four out of five. Four is true: the partner sets the lifecycle. One, A W S operates Bedrock with no Anthropic operator access. Two, it's a new organisation. Three, private offers don't transfer. Five, caching is part of the core Bedrock carries. [sting]

## Segment three: Google Cloud and Azure

SAM: Google Cloud has the same split under different names. Google-managed Claude lives in Model Garden on what was Vertex A I, renamed this year as Gemini Enterprise Agent Platform. Google operates it, processes the data and bills it. Features look like Bedrock's, with web search added, and Google lists FedRAMP High through Agent Platform.

SAM: The Anthropic-managed offer comes through Google Cloud Marketplace. Anthropic operates it and sets the limits, and it carries Skills, batch, code execution, Files, the M C P connector in beta, and Managed Agents. Some trust and safety processing happens outside Google Cloud. Spend draws down a Google Cloud commitment like other Marketplace purchases.

ALEX: So a Google-committed customer no longer has to accept the feature gap.

SAM: That's the headline. Gemini Enterprise switching on Opus for employees, from episode two, is a different layer: the enterprise wrapper.

SAM: Azure breaks the pattern. Foundry has two hosting options, and Anthropic operates both. Hosted on Azure runs on Azure infrastructure: prompts and completions stay in Azure, and only usage metadata and safety-flagged content go to Anthropic. Hosted on Anthropic runs on Anthropic's infrastructure, and data may leave the Azure geography you chose.

ALEX: Then Hosted on Anthropic is the direct A P I with an Azure invoice.

SAM: Closer, not close. Neither option has Managed Agents, the Message Batches A P I or the Compliance A P I. Hosted on Azure is narrower again: Microsoft sums it up as messages and token counting, and calls for Files, Skills or code execution return an error.

SAM: Azure's upside is the bill, and the boundary on Hosted on Azure. Spend goes through Azure Marketplace in consumption units and counts toward the Microsoft Azure Consumption Commitment, the M A C C, under either option. Microsoft states the reverse just as plainly: units billed by another cloud don't touch your M A C C. One trap: subscriptions bought through a Cloud Solution Provider partner can't buy Claude.

SAM: And under both options Anthropic, not Microsoft, is the data processor. That differs from Claude inside Microsoft three sixty-five Copilot, from episode three, where Anthropic is a Microsoft subprocessor.

SAM: Pause here and answer before we go on. Choose two. A manufacturer runs on Azure with a large M A C C, and its data policy says prompts and completions must stay in Azure. Which two statements are true? A, Foundry hosted on Azure keeps prompts and completions in Azure. B, Foundry spend draws down the M A C C under either hosting option. C, the Message Batches A P I is available if they choose Hosted on Anthropic. D, buying through Claude Platform on A W S would also count against the M A C C, because both bill in consumption units. E, Hosted on Azure supports Agent Skills and the Files A P I. [pause]

ALEX: A and C. Hosted on Anthropic is Anthropic's own infrastructure, so batch should be there.

SAM: A is right. C is the near miss: Batches isn't on Foundry under either option. The second answer is B. D is the reverse rule Microsoft writes down. E returns an error on Hosted on Azure. So, A and B, and if their overnight job needs batch, raise it before the design. [sting]

## Segment four: the table in your head

SAM: Build the table one row at a time. Columns: who operates it, which features, residency and compliance, which commitment.

ALEX: Row one, direct. Anthropic operates. Every feature, day zero. An Anthropic contract.

SAM: Row two, cloud-operated: Bedrock and Google-managed. The cloud operates. Model and core Messages features. The cloud's boundary, the regulated-workload answer, with regional pinning at a premium. The cloud's own commitment.

ALEX: Row three, Anthropic-operated on a marketplace: Claude Platform on A W S and Anthropic-managed Google. Anthropic operates. Nearly the full platform. Anthropic processes the data, at least partly outside the cloud's boundary. The cloud commitment, in consumption units.

SAM: Row four, Azure. Anthropic operates both options. Core features on Hosted on Azure, more on Hosted on Anthropic, Managed Agents and Batches on neither. A U S data zone, no E U data zone listed. The M A C C either way.

ALEX: Short version?

SAM: Cloud-run: core model, cloud boundary. Anthropic-run: full platform, cloud bill. Azure: M A C C either way, Managed Agents neither way.

ALEX: Residency, then. A customer says E U. Pick the E U region and move on.

SAM: That instinct bites. It depends on the door and the model. Bedrock has an E U inference profile. Google-managed has an E U multi-region, but its single-region endpoints only serve older models, Sonnet four point six and earlier. Foundry lists no E U data zone. And on Claude Platform on A W S, the region you call doesn't pin where processing happens.

ALEX: So "E U" is a question, not a checkbox.

SAM: Per door and per model. And lag splits the same way: model lag is small, feature lag is structural. On cloud-run doors, Anthropic's server-side features aren't late, they aren't on the list.

SAM: Pause here and answer before we go on. A retailer has a large Google Cloud commitment and wants a returns agent built on Claude Managed Agents with Agent Skills, with every dollar on the Google Cloud bill. Which route? A, Claude in Model Garden, Google-managed. B, the Anthropic-managed Claude offer on Google Cloud Marketplace. C, the Claude A P I direct, with a separate Anthropic invoice. D, Gemini Enterprise with Claude Opus switched on for staff. [pause]

ALEX: B.

SAM: B. Anthropic operates it, so Managed Agents and Skills are there, and spend draws down the Google commitment. A is on the bill but has neither feature. C has both features and misses the bill. D is an employee product, not a platform for a returns agent, and its seat credits cover Gemini models only. [sting]

## Segment five: A W S's own stack

SAM: A W S doesn't only resell. On the six layers it has a model family, an agent stack and a coding agent of its own.

ALEX: Model first. Nova.

SAM: The Nova two family: Lite, Pro, Sonic and Omni, with Pro and Omni reportedly still in preview this summer. Two pieces stand out: Nova Forge, an annual subscription for organisations building their own models, and Nova Act, for browser agents, priced per agent-hour rather than per token.

ALEX: A cheaper model for bulk work, then. Not a rival at the top.

SAM: Episode eight holds the rankings. The structural point: Nova sits on Bedrock beside Claude, so bulk work can move without a new contract.

SAM: The agent stack is where A W S is strongest. Bedrock Agent Core is a set of managed services: Runtime, Memory, Gateway, Identity, Browser, Policy, Registry, even Payments, though the page doesn't say which are generally available. Runtime is framework- and model-agnostic: it names Strands, Lang Graph, Crew A I, Google's A D K and the OpenAI Agents S D K, with models from Anthropic, Google and OpenAI. It speaks M C P and A to A, and Gateway turns A P Is and Lambda functions into M C P tools.

ALEX: Managed Agents does the hosting job with Claude's own harness. I'd take that every time.

SAM: That's the loyal answer, and it underrates Agent Core. Managed Agents runs Anthropic's harness for Claude. Agent Core runs any of those frameworks and models, with identity, policy and a registry around them. For an estate with three frameworks and two labs, it does a job Managed Agents doesn't try to do.

ALEX: Then where does Managed Agents win?

SAM: A Claude-first team that wants the harness tuned to the model, features the day Anthropic ships them, and no runtime to assemble. The question: one lab or several?

ALEX: And Strands?

SAM: A W S's open-source agent S D K, Apache two point oh, in Python and TypeScript. It supports Bedrock, Anthropic, OpenAI and Gemini, with M C P built in and A to A support. Same layer as the Claude Agent S D K, but model-agnostic. And Bedrock Agents has reportedly been renamed Agents Classic and closed to new customers, so new builds go to Agent Core.

ALEX: Kiro last. A Claude Code look-alike.

SAM: That undersells it. Kiro is built around spec-driven development, with an I D E and a C L I, and it's where A W S is moving Amazon Q Developer users: Q Developer's I D E plugins and paid subscriptions reach end of support on the thirtieth of April twenty twenty-seven. Kiro serves Claude models itself, and A W S launched its managed M C P server with a demo in Claude Code.

ALEX: So when does Kiro win?

SAM: For a team leaving Q Developer that wants a spec-first workflow from A W S. Claude Code wins on the first-party harness: skills, hooks, subagents, plugins, features on the day they ship. Before recommending Kiro, check the Claude model the team wants is on Kiro's current list.

SAM: Pause here and answer before we go on. A logistics company on A W S has agents built in Lang Graph and Strands. Some call Claude, some call OpenAI models on Bedrock. It wants one managed runtime with agent identity, a gateway exposing its Lambda functions as M C P tools, and a policy layer, all on the A W S bill. What fits? A, Claude Managed Agents. B, Amazon Bedrock Agent Core. C, Bedrock Agents Classic. D, Kiro. [pause]

ALEX: B. An hour ago I'd have said A.

SAM: B. Two frameworks, two labs, Lambda as M C P tools, identity and policy: that's Agent Core's job description. A runs Anthropic's harness for Claude, not their Lang Graph agents or OpenAI calls. C is reportedly closed to new customers. D is a coding agent, a different layer. [sting]

## Cold open: the verdict

SAM: Back to the health insurer. Alex, you picked B, Claude Platform on A W S.

ALEX: And now I can see it lose. Anthropic operates it, the data is processed outside the A W S boundary, and it isn't HIPAA-ready.

SAM: So the answer is C, Bedrock. A W S operates it with no Anthropic operator access, Anthropic's documentation points HIPAA workloads there, and spend lands on the A W S commitment. Summarising claims needs the model and the Messages A P I, which Bedrock has. A fixes neither the boundary nor the bill. B is the right door for a customer who needs Managed Agents more than the boundary. D is the wrong cloud: Foundry draws down Azure's commitment.

ALEX: The words that should have stopped me?

SAM: "Must stay inside the A W S boundary." A boundary requirement picks the cloud-operated door. [sting]

## Five to remember

SAM: Five to remember. One: two questions place any door. The operator decides the features and the processor. The bill decides the commitment.

ALEX: Two: the cloud-operated doors, Bedrock and Google-managed, carry the model and core Messages features inside the cloud's boundary, but not Files, Skills, code execution, Batches or Managed Agents.

SAM: Three: the Anthropic-operated marketplace doors, Claude Platform on A W S and Anthropic-managed Google, carry nearly the full platform on the cloud bill, with Anthropic as processor, at least partly outside the cloud's boundary.

ALEX: Four: Foundry draws down the M A C C under either hosting option, and neither has Managed Agents or Batches.

SAM: Five: A W S competes on the agent stack. Agent Core runs any framework and model, Strands is its open-source S D K, Kiro its coding agent, and Nova sits beside Claude on Bedrock.

## Recap: conversation tells

SAM: Recall first. Pause and name the five segments, and the question you'd ask the customer in each. [pause]

ALEX: Two questions, the A W S doors, Google and Azure, the table, A W S's own stack. Ask: who operates and who bills; boundary or platform; which commitment; which region; one lab or several.

SAM: Now as conversation tells. If a customer says "we're an A W S shop", ask whether the data must stay inside the A W S boundary or whether they need Managed Agents. The first is Bedrock, the second Claude Platform on A W S.

ALEX: If they say HIPAA or FedRAMP High, start with the cloud-operated door.

SAM: If a Google customer has accepted the old Vertex feature gap, tell them the Anthropic-managed offer carries the platform and burns the same commitment.

ALEX: If an Azure customer wants Managed Agents or batch on the M A C C, say early that Foundry has neither today.

ALEX: If they say "E U", ask which door and which model.

SAM: If they run several frameworks and labs on A W S, look at Agent Core before Managed Agents. If they're leaving Q Developer, Kiro is the default; make Claude Code's case on the harness.

ALEX: Next, episode five: open weights, xAI and sovereignty.
