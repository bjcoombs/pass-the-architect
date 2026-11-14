---
episode: "K03"
series: "FIELD"
slug: microsoft
title: "Microsoft: competitor and channel"
description: "Microsoft sells against Claude and sells Claude: the two ways to host Claude in Foundry, Microsoft Agent Framework, Claude inside Microsoft 365 Copilot and Copilot Cowork, and GitHub Copilot against Claude Code."
domain: "Microsoft"
weight: ""
target_minutes: 20
---

## In this episode

SAM: Welcome to Know the Field, from Pass the Architect. This is episode three: Microsoft, competitor and channel.

ALEX: Competitor and channel. That is an odd pair.

SAM: It is the whole episode. Microsoft sells G P T models against Claude, and it also sells Claude. By the end you will be able to place Microsoft on the six layers from episode zero. You will choose between the two ways to run Claude in Foundry, and know what each one leaves out. You will say when Microsoft Agent Framework is the right agent stack, even for a Claude project. You will explain how Claude reaches Microsoft three sixty-five Copilot and Copilot Cowork, and who processes the data when it does. And you will advise a GitHub customer on Copilot versus Claude Code without picking a side by habit.

ALEX: And I will defend Claude at every turn.

SAM: You will. Some of the time you will be right. [sting]

## Cold open: the Azure commitment

SAM: Here is the customer. A logistics company runs on Azure and has a large Azure consumption commitment it has to spend. It wants an internal service that summarises shipping disputes with Claude. Security sets two hard rules: prompts and completions stay inside Azure, and the spend must count against the Azure commitment. The team also mentions it might try Claude Managed Agents next year. Which route do you recommend? Option A, Claude in Microsoft Foundry, hosted on Azure. Option B, Claude in Microsoft Foundry, hosted on Anthropic. Option C, the Claude A P I, bought direct from Anthropic. Option D, buy Claude through the company's Microsoft cloud solution provider partner, so it lands on the partner's Azure invoice.

ALEX: B. Hosted on Anthropic sounds closest to the real platform, so they keep the features, Managed Agents included, and it is still bought through Azure.

SAM: Hold that. We come back to it at the end.

SAM: First, the map. At the model layer, the models in this episode are mostly other labs': OpenAI's and Anthropic's. The developer platform is Foundry. The agent stack is Agent Framework and Foundry Agent Service. The coding agent is GitHub Copilot. The enterprise wrapper is Microsoft three sixty-five Copilot, Copilot Studio and Agent three sixty-five. And the route to market is where Microsoft is strongest: the Azure bill and the Microsoft three sixty-five bundle.

ALEX: So at almost every layer, Claude can sit inside the Microsoft product as well as against it.

SAM: Which makes "why Claude and not Microsoft?" the wrong question. The useful one is "which door into Claude, and what does that door leave out?" [sting]

## Segment one: Foundry, two ways to host Claude

SAM: Segment one, Foundry. It is Microsoft's model platform. It carries OpenAI's G P T models, the old Azure OpenAI service, and since the end of June twenty twenty-six, according to press reports, Claude as generally available.

ALEX: And Claude in Foundry speaks the normal Messages A P I?

SAM: It does. Same request shape, Anthropic's own S D Ks have Foundry clients, and you authenticate with an A P I key or Entra I D. The decision that matters is the hosting option, and there are two.

ALEX: Go on.

SAM: Hosted on Azure: Anthropic operates it, on Azure infrastructure. Prompts and completions stay in Azure; only usage metadata and content flagged by safety systems go to Anthropic. Hosted on Anthropic: it runs on Anthropic's infrastructure, and data may be processed outside the Azure geography you selected.

ALEX: Why would anyone pick the second?

SAM: Models and features. Some models, the Fable class among them, are served only hosted on Anthropic. And hosted on Azure carries a smaller feature set. As of November twenty twenty-six, it lacks the Files A P I, Agent Skills, code execution, programmatic tool calling and the newer web search and fetch tools. Microsoft sums up its Azure-hosted support as messages and token counting.

ALEX: And under both options?

SAM: Neither has Claude Managed Agents, the Message Batches A P I, the Admin A P I or the Compliance A P I.

ALEX: Then Foundry is a second-class way to buy Claude. If a customer wants Claude, I send them to the Claude A P I and skip the lag.

SAM: The lag is real, and for an agent-heavy build it can settle the matter. But judge Foundry as the customer's finance team would. Claude in Foundry is billed through Azure Marketplace in Claude Consumption Units, and that spend draws down the Azure consumption commitment. For a company sitting on a large unspent commitment, that can outweigh every missing feature.

ALEX: Fair. What else changes?

SAM: Three things people miss. One, Anthropic is still the seller of record, the data processor and the provider of the service level agreement, and Microsoft provides support. Two, some subscriptions cannot buy Claude at all, including free trials and cloud solution provider subscriptions, so partner-resold Azure is out. Three, Claude units billed on another cloud do not draw down the Azure commitment.

ALEX: And the question to ask the customer?

SAM: "Must the data stay inside Azure, and which Claude features do you need in the next year?" The first answer picks the hosting option. The second tells you whether Foundry can carry the build at all.

SAM: Pause here and answer before we go on. Choose two. A retailer runs Claude in Foundry, hosted on Azure. Its developers are trying five things. Which two will fail on this hosting option? A, Messages A P I calls authenticated with Entra I D. B, uploading product catalogues through the Files A P I. C, counting tokens before a request. D, submitting a nightly job through the Message Batches A P I. E, Messages A P I calls authenticated with an A P I key. [pause]

ALEX: B and D.

SAM: B and D. The Files A P I is missing when hosted on Azure, and Batches is missing on Foundry under either option. A, C and E are the core that works. [sting]

## Segment two: Agent Framework and Foundry Agent Service

SAM: Segment two, the agent stack. Microsoft Agent Framework is the direct successor to Semantic Kernel and AutoGen, built by the same teams. It takes AutoGen's agent abstractions and Semantic Kernel's state, type safety, middleware and telemetry, and adds graph-based workflows.

ALEX: That sounds like Semantic Kernel with a new label. Microsoft renames things.

SAM: It is more than a rename, and underrating it will cost you with Microsoft customers. Look at the languages: dot net, Python, and Go in public preview. The Claude Agent S D K is Python and TypeScript. For a bank whose engineers write C sharp, that alone can decide it.

ALEX: What would I recognise in it?

SAM: Five orchestration patterns by name: sequential, concurrent, handoff, group chat, and Magentic, where a manager agent coordinates specialists. Human approval works through tool approval. It ships M C P clients, A to A hosting samples, and a harness agent with planning, context compaction, file access, memory and tool approval. The licence is M I T.

ALEX: Planning, compaction, tool approval. That is the Claude Code harness feature list.

SAM: It is convergence, and fine to say so. And Agent Framework ships an Anthropic model provider, so a C sharp team can run Claude inside it.

ALEX: And Foundry Agent Service?

SAM: The hosted runtime. Prompt agents are declarative, and Foundry runs them. Hosted agents are your own container, built with Agent Framework, LangGraph, the Claude Agent S D K or your own code. Toolboxes expose a curated tool set as one managed M C P endpoint. A to A version one is generally available, and agents publish to Teams and Microsoft three sixty-five Copilot.

ALEX: Can a Claude deployment back a prompt agent?

SAM: Unconfirmed. Microsoft's own sources conflict, so check the model catalogue before you promise it. A Claude Agent S D K container as a hosted agent is the documented path.

ALEX: Where is Claude ahead here?

SAM: On the hosted side. Anthropic will run the agent loop and sandbox for you through Claude Managed Agents, and Foundry does not offer them under either hosting option. That is a documented limit, not a benchmark.

SAM: Pause here and answer before we go on. An insurer's platform team writes everything in C sharp on dot net and has years of Semantic Kernel code. It wants multi-agent workflows with handoff between a triage agent and specialist agents, and Claude as the model for two of them. What do you recommend? A, rewrite the agents in Python on the Claude Agent S D K. B, Microsoft Agent Framework in C sharp, with its Anthropic model provider for the Claude agents. C, stay on AutoGen, since the patterns started there. D, write a custom agent loop in C sharp from scratch. [pause]

ALEX: A. The Agent S D K is the best harness for Claude, and a rewrite is a one-off cost.

SAM: That is the loyal answer, and it ignores both constraints. The answer is B. The team works in C sharp, its code is Semantic Kernel, and Agent Framework is that code's successor, with handoff built in and Claude through the Anthropic provider. A throws away the language and the code base. C is the predecessor. D rebuilds what the framework already ships.

ALEX: So the tell is the language.

SAM: The language and the existing code. "Dot net" or "Semantic Kernel": start from Agent Framework and put Claude inside it. [sting]

## Segment three: Claude inside Microsoft 365 Copilot

SAM: Segment three, the enterprise wrapper. Claude is now a model inside Microsoft three sixty-five Copilot. It appears in Microsoft Copilot, Researcher, Copilot Studio, Power Platform and Copilot in the Microsoft three sixty-five apps.

ALEX: Under whose terms?

SAM: That is the question that matters. Here Anthropic is a Microsoft subprocessor. Claude in Microsoft three sixty-five Copilot is covered by Microsoft's Product Terms and data protection addendum, Enterprise Data Protection and the Customer Copyright Commitment.

ALEX: Notice the flip. In Foundry, Anthropic is the data processor. In Copilot, it is Microsoft's subprocessor.

SAM: Same model, different contract, depending on the door. Now the defaults. In the commercial cloud, Claude is on by default, except in the E U, the E F T A countries and the U K, where the default is no users. And Claude in Copilot is currently outside the E U Data Boundary and in-country processing commitments. A Microsoft message centre notice says processing moves inside that boundary in early December, and that Claude turns on by default for E U and E F T A tenants from the ninth of December, unless admins opt out first.

ALEX: Good. So every Microsoft three sixty-five customer already has Claude, and I can tell them so.

SAM: Not quite, and saying so would mislead a U K customer. Government clouds such as G C C High and D O D do not get it at all. And the frontier classes differ. Fable-class and Mythos-class models may come as Anthropic models with data retention: off by default everywhere, and when enabled, Anthropic is an independent processor under its own terms and keeps inputs and outputs for up to thirty days, longer for flagged content.

ALEX: So the first question is not "do you want Claude". It is which tenant, which region, which model class.

SAM: That is the question to ask. In Copilot Studio, Microsoft says makers choose the model per agent, and admins get a second control. And the bundle: Microsoft three sixty-five E seven packages Microsoft three sixty-five Copilot with Agent three sixty-five, the Entra Suite and E five. That is the route-to-market layer as one line item.

ALEX: And Copilot Cowork?

SAM: Generally available since June, after a preview from March. It runs on Anthropic models; Microsoft names Opus and Sonnet, with G P T in its Frontier programme and a Microsoft model called Cowork One announced as coming. It needs the Microsoft three sixty-five Copilot licence. Microsoft says more than half the Fortune five hundred use it.

ALEX: So Copilot Cowork is Claude Cowork with a Microsoft badge. And Microsoft claims it is thirty to forty percent cheaper per prompt than Claude Cowork. That is marketing.

SAM: Half right. The cost figure is vendor-reported: Microsoft's own internal test, a hundred and twenty-five runs over twelve prompts, both on the same Opus model. Treat it as a claim until a customer tests it. But "a badge" undersells it. It lives in the customer's Microsoft three sixty-five tenant, under the identity, licence and data terms they have already signed. For a Microsoft three sixty-five customer, that is a real advantage.

ALEX: And Cowork One?

SAM: The one to watch. If Microsoft's own model takes over Cowork, Claude's share inside it could shrink. For now, the models Microsoft names for it are Anthropic's.

SAM: Pause here and answer before we go on. For each statement, say true or false. One: in a U K tenant today, Claude is on by default in Microsoft three sixty-five Copilot. Two: Claude in Microsoft three sixty-five Copilot, under subprocessor terms, is covered by Microsoft's Product Terms and data protection addendum. Three: today, Claude in Copilot is inside the E U Data Boundary. Four: if an admin enables a Fable-class model with data retention, Anthropic becomes an independent processor and may keep inputs and outputs for up to thirty days. [pause]

ALEX: False, true, false, true.

SAM: All four. One: the U K default is no users. Two: that is the subprocessor arrangement. Three: currently excluded, with a move announced for December. Four: with data retention, the frontier classes come under Anthropic's own terms, and they are off by default everywhere. [sting]

## Segment four: GitHub Copilot and Claude Code

SAM: Segment four, the coding agent. GitHub Copilot is now a multi-agent, multi-model marketplace. It offers Claude models from Haiku up to Fable, alongside G P T and Grok. And through Agent H Q it hosts the Claude and Codex coding agents themselves, in public preview on every paid plan since February.

ALEX: So GitHub resells Claude models and hosts the Claude agent.

SAM: Yes. Billing moved to usage in June: premium requests became GitHub A I Credits, metered on tokens at each model's A P I rates. The Agent Control Plane is generally available, security validation for third-party agents went generally available in June, and Copilot code review gained agent skills and M C P in July.

ALEX: Agent skills. That is our format.

SAM: Anthropic published it as an open standard, and GitHub Copilot reads it. Convergence again: a skill written for Claude Code can travel.

ALEX: Here I hold my ground. Claude Code leads. The Stack Overflow twenty twenty-six survey has Claude Code used by sixty-six percent of A I users and Copilot by fifty-nine.

SAM: That survey is independent, with more than thirty thousand developers, so cite it. But both numbers are above half, so many developers use both. It measures use, not who pays. And when you quote the Menlo Ventures report saying challengers beat Copilot on product velocity, say that Menlo is an Anthropic investor.

ALEX: Then where is Claude Code ahead in a way a Copilot user would accept?

SAM: Two checkable points. It is Anthropic's own harness, so Claude features land there first, while GitHub's changelog lists the Claude agent in Copilot as a public preview. And it carries the full harness in one tool: skills, hooks, subagents and plugins. Copilot sells something else: one seat, one bill, central governance, and a choice of models and agents. When the constraint is consolidation, Copilot with Claude inside it is often the right answer.

SAM: Pause here and answer before we go on. A software company with two thousand developers has standardised on GitHub Enterprise. Security wants one control plane for every coding agent, one bill, and central control of which models are enabled. Developers have asked for Claude models and the Claude coding agent. What do you recommend? A, replace GitHub Copilot with Claude Code for all two thousand developers. B, keep GitHub Copilot, enable the Claude models, and use the Claude coding agent through Agent H Q. C, tell them Copilot cannot run Claude, so they need two tools. D, build an in-house coding agent on the Claude Agent S D K. [pause]

ALEX: B. Every constraint they stated is about consolidation, and Copilot meets it with Claude inside.

SAM: B. A answers a question nobody asked and breaks the one-bill rule. C is false. D builds a product when they asked to govern one. If a platform team later needs hooks and custom subagents, Claude Code can sit beside Copilot for that team. [sting]

## Cold open: the verdict

SAM: Back to the logistics company. Alex, you picked B, hosted on Anthropic.

ALEX: And segment one undid it. Hosted on Anthropic may process data outside the Azure geography, which breaks the first rule. And it does not bring Managed Agents either: neither Foundry option has them.

SAM: So the answer is A, hosted on Azure. Prompts and completions stay in Azure, and the spend draws down the commitment. C fails the commitment rule. D fails on a fact: cloud solution provider subscriptions cannot buy Claude in Foundry.

ALEX: And the Managed Agents line?

SAM: It is a "might, next year". Do not trade a hard rule for a maybe. Tell them now that Managed Agents is not on Foundry.

ALEX: The words that should have stopped me?

SAM: "Stay inside Azure" and "count against the commitment". Two hard rules, one option that meets both. [sting]

## Five to remember

SAM: Five to remember. One: Microsoft is a competitor and a channel. Ask which door into Claude the customer is using, and what that door leaves out.

ALEX: Two: hosted on Azure keeps prompts and completions in Azure, with a core feature set. Hosted on Anthropic has more models and features, but data may leave the Azure geography. Neither has Managed Agents or Batches; both draw down the Azure commitment.

SAM: Three: Microsoft Agent Framework succeeds Semantic Kernel and AutoGen, runs on dot net, Python, and Go in preview, has five orchestration patterns, and can run Claude. For a C sharp team, it is the stack to start from.

ALEX: Four: in Microsoft three sixty-five Copilot, Anthropic is Microsoft's subprocessor under Microsoft's terms. Off by default in the E U, E F T A and U K, outside the E U Data Boundary for now, and Fable-class models with data retention come under Anthropic's own terms.

SAM: Five: GitHub Copilot resells Claude models and hosts the Claude agent. Copilot sells consolidation and governance; Claude Code sells the full harness and Claude features first. Match the customer's constraint, not your habit.

## Recap: the conversation tells

SAM: Recall first. Pause and name the four segments, and the question you would ask the customer in each. [pause]

ALEX: Foundry: must data stay in Azure, and which features next year. Agent Framework: what language does the team write. Microsoft three sixty-five Copilot: which tenant, which region, which model class. GitHub Copilot: is the constraint consolidation or the full harness.

SAM: Now as conversation tells. If a customer says "we have to burn down our Azure commitment", ask whether Claude in Foundry covers the features they need.

ALEX: If they say "data never leaves Azure", ask which hosting option. Hosted on Azure, not hosted on Anthropic.

SAM: If they say "we buy Azure through a partner", check the subscription type, because cloud solution provider subscriptions cannot buy Claude.

ALEX: If they say "we are a dot net shop", ask about Agent Framework with Claude inside it before you pitch the Agent S D K.

SAM: If they say "we already have Claude in Copilot", ask which region, and whether it runs under Microsoft's terms or Anthropic's.

SAM: And if they say "one bill for every developer", ask whether Copilot with Claude inside it already does the job.

ALEX: Next, episode four: same Claude, different cloud. Bedrock, Vertex and Foundry side by side, and what each one changes.
