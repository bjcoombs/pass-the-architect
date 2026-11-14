---
episode: "K02"
series: "FIELD"
slug: google
title: "Google"
description: "Gemini on six layers: the widest multimodal range in the field, two developer front doors, an open agent kit and the A to A protocol, Antigravity in place of Gemini CLI and Jules, and Gemini Enterprise with Claude switched on inside it."
domain: "Google"
weight: ""
target_minutes: 22
---

## In this episode

SAM: Welcome to Know the Field, from Pass the Architect. This is episode two: Google.

ALEX: What will I be able to do by the end?

SAM: Name the jobs where a Gemini model is the better pick today, and the ones where Claude is, with a reason a customer can check. Choose between Google's two developer front doors. Place Google's agent kit and the A to A protocol next to the Claude Agent S D K and M C P. Explain what replaced Gemini CLI and Jules, and what that means for a team using them. And advise a Workspace customer who wants Gemini for most staff and Claude for one team.

ALEX: Google is the vendor customers bring up when they already pay for Workspace or BigQuery. If I can't answer on its own ground, I lose the room.

SAM: Then we start on its ground. [sting]

## Cold open: the Workspace retailer

SAM: Here is your opening scenario. A retailer with eight thousand staff runs on Google Workspace and has a large Google Cloud commitment. IT wants one assistant for every employee across Gmail, Drive and Calendar, run from consoles they already manage, with data kept in the E U. The legal team insists on Claude for contract review. What do you recommend? Option A, Claude Enterprise seats for all eight thousand, so legal and everyone else share one product. Option B, Gemini Enterprise for all staff, with admins switching on Claude Opus five point five for the legal team, billed pay as you go. Option C, a custom assistant built on the Gemini A P I with A P I keys. Option D, Gemini Enterprise for everyone, and tell legal that Gemini tops the leaderboards so Claude isn't needed.

ALEX: A. Claude for everyone, one product, one vendor, and legal gets what it asked for.

SAM: Hold that. We come back to it at the end. [sting]

## Segment one: the models

SAM: Segment one, the model layer. Google's frontier line this autumn is Gemini four, in three models. Carbon is the strongest, and spends more tokens reasoning and checking its work. Argon is the default for most software and knowledge work. Hydrogen is the fast one, pitched as the everyday engine for agent workflows.

ALEX: And under those, the Flash models.

SAM: The Flash line is the cheap workhorse tier. Going by Google's own changelog, a new Flash point release lands every month or two, and older model names get rerouted to newer ones on set dates. A customer who pinned a version can find a different model answering.

ALEX: I'll be honest about my reflex. Gemini is the one that fell behind. Menlo's market report has Google a distant third in enterprise A P I spend.

SAM: Two corrections. Menlo Ventures is an Anthropic investor and says so. And its figure counts A P I spend only. It leaves out the Workspace and Gemini app bundles, and Menlo itself says Google's A P I spend leans to its cheaper Flash models.

SAM: And on independent boards Gemini is not behind. As of November twenty twenty-six, Gemini four holds the top two places on the Arena text board, which measures human preference. Carbon is second on the Artificial Analysis intelligence index, at about half the cost per task of Opus five point five.

ALEX: So where is Claude ahead, with evidence?

SAM: Agent and coding work. On those same independent boards Claude holds the top three places on Arena WebDev and the top two on the Arena agent board, with Carbon third. And note what Google publishes itself: its launch posts cite partner benchmarks, vendor-reported, and never name Claude.

ALEX: So the tell is which board the customer is quoting.

SAM: Yes. Text preference leans Gemini. Agentic coding leans Claude. Cost per task leans Google.

ALEX: Now the part I hear least about. Multimodal.

SAM: Google's widest lead, and the least contested. Video generation with native audio, where Google holds the top three on the Arena text-to-video board. Image generation and editing. Speech-to-text, text-to-speech in over a hundred languages, music, and embeddings that cover text, images, audio, video and P D F. And the Live A P I: real-time, two-way audio and video conversation.

ALEX: And Claude's answer to those?

SAM: Claude reads images and documents, but Anthropic has no first-party model for image, video or audio generation, speech, or embeddings. A Claude design that needs them brings in another vendor.

ALEX: Fine, but most of my customers do text and documents.

SAM: Many do, and for them this lead does not matter. The ones it does matter for are contact centres, media, and field service teams sending photos and video. Ask early whether the job needs a voice or a camera.

SAM: One more model fact. Gemma four, Google's open-weight family, moved to the Apache two point oh licence in April, with small edge sizes for on-device use. Anthropic has no open-weight model. When a customer needs to run offline or fine-tune on its own hardware, Gemma is a real answer.

SAM: Pause here and answer before we go on. A telecom on Google Cloud wants a contact-centre agent that holds spoken conversations with callers in real time. Its architect wants one managed service to handle the audio end to end, with no separate speech services chained in. Which model does it build on? Option A, Claude Sonnet five point five through Google's Model Garden, with prompts tuned for short replies. Option B, the Gemini Live A P I for the spoken conversation. Option C, Claude chained behind a third-party speech-to-text and text-to-speech service, because Claude leads the agent boards. Option D, Gemma four running on servers in each call centre. [pause]

ALEX: B. And it stings to say it.

SAM: B. The constraint is real-time speech, and the Live A P I is built for exactly that. A has no speech path at all. C chains in the separate speech services the architect ruled out, and agent boards don't measure spoken conversation. It suits a job where the hard part is reasoning. D trades the managed service for hardware the stem never asked for. [sting]

## Segment two: two front doors

SAM: Segment two, the developer platform. Google has two front doors. One is the Gemini A P I with Google A I Studio: an A P I key, quick to start, Gemini models only. The other is the Gemini Enterprise Agent Platform.

ALEX: Which is what?

SAM: Vertex A I, renamed at Cloud Next in April. Agent Engine became Agent Runtime in the same move.

ALEX: And the difference between the doors?

SAM: Agent Platform runs on Google Cloud identity and service accounts, publishes the regions where each model's processing happens, and adds V P C service controls, customer-managed encryption keys, audit logs and reserved throughput. Its Model Garden carries third-party models, Claude among them.

ALEX: So the key-based door is for prototypes.

SAM: Mostly. And a default to flag: since late October, new paid-tier Gemini A P I projects store generated content by default. Check that against the customer's data policy.

ALEX: What else does Google do well here?

SAM: Grounding with Google Search and Google Maps as built-in tools. Batch at half the standard rate. Structured output across current models.

ALEX: And caching. Gemini caches automatically. Nothing to set up. That beats marking breakpoints by hand.

SAM: Less work, and on by default. That part is right.

SAM: But Gemini four supports implicit caching only. You can't create a cache object, and in an agent loop it reuses the earlier request only when the new turn adds enough tokens, a threshold Google sets. On Claude you place the cache breakpoints, on every current model, so you decide what stays cached.

ALEX: The question to ask?

SAM: How much of your bill is a long agent loop re-reading the same context, and who controls what gets cached?

SAM: Pause here and answer before we go on. For each statement, say true or false. One: Gemini four lets you create and manage explicit cache objects. Two: Model Garden on Google's Agent Platform offers Claude alongside Gemini. Three: new paid-tier Gemini A P I projects now store generated content by default. Four: batch requests on Google's main Gemini text models cost half the standard rate. [pause]

ALEX: False, true, true, true.

SAM: All four right. Gemini four is implicit caching only. Claude is in Model Garden. The storage default changed in late October, so check it. And batch is half price, the same structure as Claude's batch discount. [sting]

## Segment three: the agent stack

SAM: Segment three, the agent stack. Google's agent kit is the A D K, the Agent Development Kit. Apache two point oh, in Python, TypeScript, Go, Java and Kotlin. Version two adds graph workflows with human input and retries, skills, and context compaction.

ALEX: That's Google lock-in. A Claude customer should build on the Claude Agent S D K.

SAM: Look again. The A D K is model-agnostic, with adapters for Claude, OpenAI and open models. It consumes M C P tools and can expose an agent as an M C P server. It deploys to Google's Agent Runtime, to Cloud Run, to G K E, or on your own servers. And the Claude Agent S D K is Python and TypeScript only.

ALEX: So for a Java shop the A D K is the more natural fit.

SAM: Among the vendors' own in-process agent frameworks, the A D K reportedly covers the most languages. Where the Agent S D K wins is the harness: it is Claude Code's loop as a library, with file and shell tools, compaction and subagents already built and tuned.

ALEX: And hosted agents?

SAM: Two pieces. Agent Runtime hosts agents on Google Cloud, with a memory bank. And since May the Gemini A P I has Managed Agents, in preview. One call provisions a Google-hosted Linux sandbox running the Antigravity agent harness, sessions resume with their files, and you customise it with AGENTS dot md and SKILL dot md files.

ALEX: SKILL dot md. That's Anthropic's skills format.

SAM: And AGENTS dot md came from OpenAI. Call it convergence. The closest analogue to Claude Managed Agents now reads both formats.

ALEX: Then protocols.

SAM: Google started A to A, the agent-to-agent protocol. Version one shipped in March, and in August it moved under the Linux Foundation's Agentic A I Foundation, the same home as M C P. Over a hundred and fifty organisations back it, and Microsoft Foundry and Amazon's AgentCore both host it.

ALEX: M C P for tools and data, A to A for one agent calling another.

SAM: That's the split. And on M C P, Google runs more than fifty managed M C P servers, for BigQuery, Spanner, Cloud SQL, G K E and Workspace mail, Drive and calendar, behind I A M deny policies and an agent registry. Google names Claude as a compatible client.

SAM: Pause here and answer before we go on. Choose two. An insurer's platform team on Google Cloud writes Java. It wants an agent framework it can run on G K E, with Claude as the model for the hardest reasoning step, and its agents must call a partner's claims agent, which the partner runs on a different stack. Which two fit? A, the A D K in Java, using its Claude adapter. B, the Claude Agent S D K in Java. C, A to A for the call to the partner's agent. D, ask the partner to rebuild its agent as an M C P tool inside the insurer's process. E, Gemini Enterprise seats for the platform team. [pause]

ALEX: B and C. Stay on Claude's own kit, and A to A for the partner.

SAM: C is right. B is a loyal answer to a constraint that rules it out: the Agent S D K has no Java version. The other answer is A, which keeps Claude as the model and gives the team its own language. D makes the partner give up control of its own agent. E is the employee product, the wrong layer for a platform team.

ALEX: So I picked the badge, not the brief.

SAM: The tell was "writes Java". The framework and the model are separate choices. [sting]

## Segment four: the coding agent

SAM: Segment four, the coding agent. Anything learned before this spring is out of date. At I O in May, Google made Antigravity its single coding harness: a desktop app that runs parallel agents and scheduled background tasks, a command-line tool, and an S D K.

ALEX: What happened to Gemini CLI?

SAM: From June it stopped serving free, A I Pro and A I Ultra users. The open-source repository remains, for Code Assist Standard and Enterprise customers and paid A P I keys, and its own readme says it is not tuned for Gemini four. Jules, the background coding agent, went read-only on the eleventh of November and shuts down at the end of December.

ALEX: Antigravity is a Claude Code copy. Skills, subagents, hooks, plugins.

SAM: The feature lists do line up. Antigravity reads SKILL dot md files and bundles plugins of skills, subagents, M C P and hooks. But Claude Code now reads AGENTS dot md when no CLAUDE dot md exists. Both sides borrowed. That's convergence, not copying.

ALEX: Then where do they differ?

SAM: Three places. Antigravity is multi-model: it pairs a Gemini planner with a fast Gemini executor, and on paid plans it also offers Claude Opus and Sonnet five point five. The Antigravity command-line tool is closed source, which reportedly angered developers who had contributed to Gemini CLI. And it is bundled into Google's consumer A I plans, where users have reported tight weekly quotas.

ALEX: And Claude Code's case?

SAM: Claude leads the independent agentic coding boards we named, and the Stack Overflow developer survey this year has Claude Code as the most-used coding agent, with Gemini a distant third among models.

ALEX: Which is my other point. Google kills things. Gemini CLI, Jules, Code Assist for individuals, Vertex as a name, Agentspace. I wouldn't tell a customer to bet on it.

SAM: The list is real, and it belongs in the risk register. But a rename is not an outage. The platform and its controls carried on under the new name. The churn sits at the developer-tool edge and in model versions, not in the cloud underneath.

ALEX: So the advice?

SAM: Put model names behind an alias, watch the changelog, and rerun your evals when a version moves. That works with any vendor.

SAM: Pause here and answer before we go on. A fintech's forty engineers use Jules for background pull requests and the Gemini CLI on personal A I Pro accounts. The head of engineering asks what to do before year end. Option A, nothing: paid users are unaffected. Option B, move everyone to the Gemini Code Assist I D E extensions on their personal A I Pro plans. Option C, export the Jules work, then run a short trial of Antigravity and Claude Code on the team's own repositories and tickets, and choose on the results. Option D, fork the Gemini CLI repository and keep running it on the personal accounts. [pause]

ALEX: C.

SAM: C. Jules is read-only and switches off at the end of December, and personal A I Pro accounts lost Gemini CLI in June. B fails for the same reason: the extensions stopped for individual A I Pro users. D keeps the code but not the service behind it. A trial on their own code beats any public board. [sting]

## Segment five: the enterprise wrapper

SAM: Segment five, the enterprise wrapper and the route to market. Gemini Enterprise is the employee product. It absorbed Agentspace, and comes in Business, Standard, Plus, Frontline and pay-as-you-go editions.

ALEX: With the controls I'd expect?

SAM: Data residency in the U S or the E U, V P C service controls, customer-managed keys, Access Transparency and audit logs. And Gemini is built into Workspace itself: Hydrogen now powers Gemini in Sheets on eligible business plans.

ALEX: And Claude's place in it?

SAM: Admins can switch on Claude Opus five point five and Sonnet five point five inside Gemini Enterprise. Claude usage is billed pay as you go; seat credits cover Gemini only. So budget it separately.

ALEX: And buying Claude on Google Cloud more generally?

SAM: Claude is in Model Garden, and there is also an Anthropic-run listing on the Google Cloud Marketplace. Both can draw down a Google commitment, and they differ in features and in who processes the data. Episode four takes that apart. [sting]

## Cold open: the verdict

SAM: Back to the retailer. Alex, you picked A, Claude Enterprise for all eight thousand.

ALEX: And now I see what I skipped. They asked for consoles they already manage, and they live in Workspace.

SAM: That's the constraint. The answer is B. Gemini Enterprise is Google's own employee product, managed alongside Workspace and Google Cloud, with data kept in the E U. Legal gets Claude Opus five point five inside the same product, on pay-as-you-go billing that seat credits don't cover. Before go-live, confirm where Claude's processing runs, because the E U rule covers legal too.

ALEX: And the others?

SAM: A is a strong product fighting the brief, a second console and a second contract. C is a build project, on the key-based front door that lacks the cloud's identity and regional controls. D overrules legal with a text preference board, which doesn't measure contract review.

ALEX: The words that should have stopped me?

SAM: "Consoles they already manage". When the customer names the platform, fit inside it, and bring Claude in where the team asks for it. [sting]

## Five to remember

SAM: Five to remember. One: Gemini's lead is multimodal. Live speech, video, image, audio and embeddings are first-party at Google and absent at Anthropic.

ALEX: Two: read which board a customer quotes. Text preference and cost per task lean Gemini; agentic coding leans Claude. Google's launch numbers are vendor-reported and never name Claude.

SAM: Three: Vertex is now Agent Platform, the door with I A M, regions and Claude in Model Garden. Gemini four caches implicitly only; Claude lets you place the breakpoints.

ALEX: Four: the A D K is open, model-agnostic and in five languages. A to A connects agents, M C P connects tools, and both now sit in the same foundation.

SAM: Five: Antigravity replaced Gemini CLI for most users, and Jules ends in December. Gemini Enterprise can switch on Claude Opus and Sonnet for the teams that want it.

## Recap: conversation tells

SAM: Recall first. Pause and name the five segments we walked through for Google, and one question to ask a customer at each. [pause]

ALEX: Models: does the job need voice or video? Platform: key or Agent Platform? Agents: which language, and whose agent are we calling? Coding: still on Gemini CLI or Jules? Enterprise: do they live in Workspace?

SAM: Now as conversation tells. If a customer says they need real-time voice, video or generated images, ask whether Google's media models belong in the design. Claude has no first-party answer.

ALEX: If they say it must run offline or be fine-tuned in house, ask about Gemma four under Apache two point oh.

SAM: If they say Gemini tops the leaderboard, ask which board. Text preference, or agentic coding.

ALEX: If they need regions, identity and private networking, ask why they are on an A P I key and not Agent Platform. And if their agent loops are costly, ask who controls the cache.

SAM: If their team writes Java or Go and wants Claude, ask whether the A D K with its Claude adapter fits better than the Agent S D K. If their agent must call another company's agent, think A to A.

ALEX: If they still run Gemini CLI on personal plans or Jules, ask about a trial on their own code before December.

SAM: And if they live in Workspace but one team wants Claude, ask whether Gemini Enterprise with Claude switched on solves it, before you sell a second product.

ALEX: Next, episode three: Microsoft, competitor and channel.
