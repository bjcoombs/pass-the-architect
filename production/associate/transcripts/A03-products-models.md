---
episode: "A03"
series: "CCAO-F"
slug: products-models
title: "Choosing the product and the model"
description: "When to use chat, a Project, research or an artifact; how Haiku, Sonnet and Opus trade cost, speed and quality; and when a long conversation should be restarted, summarised or persisted."
domain: "Product and Model Selection"
weight: "12%"
target_minutes: 16
---

## In this episode

SAM: Welcome to Pass the Architect, Associate Foundations. This is episode three: choosing the product and the model.

ALEX: What will I be able to do by the end?

SAM: Pick the right feature for a task: a plain chat, a Project, research, or an artifact. Match Haiku, Sonnet or Opus to what the task needs in cost, speed and quality. And decide, when a conversation gets long or goes stale, whether to restart it, summarise it, or move what matters somewhere it persists.

ALEX: Twelve percent, so about seven items. And the trap I fall into is reaching for the biggest model when the stem is really asking about a feature.

SAM: So we start with exactly that. [sting]

## Cold open: the vendor review

SAM: An operations lead is preparing a quarterly review of five logistics vendors. She needs a one-page comparison of each vendor's public announcements from the last three months, drawn from many current web sources, and her director will edit the page before it goes to the leadership team. Which approach fits best? Option A: a standard chat on Opus, the most capable model, asking it to list everything it knows about each vendor. Option B: turn on research, with web search, to investigate across sources, then have the comparison produced as an artifact she can edit and share. Option C: use Haiku for speed, pasting each vendor's home page into one long chat. Option D: create a Project, upload last year's vendor review as knowledge, and ask for this year's version.

ALEX: A. Opus is the strongest model, and quality matters when it goes to leadership.

SAM: Hold that. We come back to it at the end.

ALEX: Seven items. What do they cover?

SAM: Four objectives. Select the right product feature: Projects, research mode, chat and artifacts. Tell the model families apart: Haiku, Sonnet and Opus. Align the model with the task's cost, speed and quality needs. And manage context limits and memory: when to restart, summarise or persist. Every item in this domain asks the same thing underneath: what does this task actually need, and what is the smallest tool that meets it? [sting]

## Segment one: chat, Projects, research and artifacts

SAM: Start with the four features. A plain chat is for one-off work: a question, a quick draft, a rewrite. Nothing needs to carry over.

ALEX: And a Project is for work I come back to.

SAM: Right. The help centre describes a Project as a self-contained workspace with its own chat histories and knowledge base. You upload documents once, add instructions once, and every chat in that Project uses them. A consultant writing a weekly status report for the same client, with the same brand guide and engagement brief, should not be pasting those files in every Monday.

ALEX: Research?

SAM: Research is for questions that need investigating, not looking up. The help centre says Claude runs several linked searches, decides what to explore next from what it finds, and works through open questions one by one. It needs web search turned on, it is on paid plans, and it uses your limits faster than a normal chat.

ALEX: I would just leave research on all the time. It's more thorough, so why not?

SAM: Thoroughness is worth having, and for a market scan or a competitor review it is exactly right.

SAM: But the exam's answer style is proportionate. A quick fact check, a single figure, or a rewrite of your own paragraph gains nothing from a long multi-source investigation, and it spends time and usage. The tell is in the stem: "in depth", "many sources", "compare across", "current" point to research. "Quick", "one fact", "my own text" point to a plain chat.

ALEX: And artifacts?

SAM: The help centre's test is that an artifact is substantial and self-contained, typically over fifteen lines, and something you are likely to edit, iterate on or reuse outside the conversation. It opens beside the chat, where you can keep working on it. A policy draft, a one-page brief, a small dashboard: artifact. A two-line answer: inline.

SAM: Pause here and answer before we go on. A recruitment partner screens candidates every week for the same three roles. Each time, she opens a new chat and pastes in the three job descriptions and the company's interview guidelines, and some weeks she forgets one of the files. What should she do? A, keep one very long chat for all screening so the files stay in it. B, create a Project with the job descriptions and guidelines as knowledge, and instructions for how screening notes should look. C, turn on research so Claude finds the job descriptions itself. D, switch to Opus so Claude remembers the requirements better. [pause]

ALEX: I'm tempted by A. One chat, files pasted once, done.

SAM: That is the distractor that looks efficient. A long chat fills up and drifts, and every candidate's notes pile into the same conversation. The answer is B: knowledge and instructions set once, available in every chat in the Project. C sends research looking for internal documents that are not on the web. D is the bigger-model reflex: no model remembers files you did not give it. [sting]

## Segment two: Haiku, Sonnet and Opus

SAM: Now the models. Three families, three trade-offs. Haiku is the fastest and the lightest on your usage. Anthropic's guidance puts it on quick answers to simple questions, basic summaries, and high-volume, straightforward work.

ALEX: Sonnet is the middle.

SAM: Sonnet is the daily driver. The guidance says that if you are not sure which model to pick, start there: responsive enough for real-time work, capable enough that most problems will not outgrow it.

ALEX: And Opus for the hard stuff.

SAM: Opus is for deep research and complex reasoning that needs sustained thinking, and for problems where you tried Sonnet and it struggled. It uses more of your limits, so you reserve it for tasks that need it. The same logic applies to extended thinking: save the highest setting for your hardest problems, because deeper thinking takes longer and costs more of your limit.

ALEX: I'll push on this. If quality matters, and it always matters, why not just use Opus for everything? The cost is the company's problem.

SAM: Fair: Opus will rarely give you a worse answer, and for a board paper or a tangled contract question it may be the right call.

SAM: But the exam frames model choice as matching, not maximising. The guide's own wording is aligning model selection with task requirements: cost, speed and quality together. For two thousand short survey comments to tag by theme, Opus is slower and burns usage the team needs for harder work, with no gain in quality. The tell: "high volume", "short", "simple", "speed matters" points to a faster, lower-cost model. "Most capable" in an option, with no reasoning demand in the stem, is the overspend distractor.

ALEX: So Haiku whenever the budget is tight.

SAM: Careful, that rule just outran its scope. If a stem says "conflicting clauses across three contracts" or "nuanced judgement for a regulator", the cheapest model is the wrong economy. Budget is one constraint of three. Read what the task demands before you read what it costs.

ALEX: And if the output is wrong?

SAM: Then check why before you switch. A wrong citation is a validation problem from episode two, verified against the source. A missing document is a configuration problem. A bigger model fixes neither.

SAM: Pause here and answer before we go on. Choose two. Which two pairings of model and task fit the guidance? A, Haiku to tag two thousand customer survey comments by theme for a weekly dashboard. B, Opus to reformat a list of dates into a single style. C, Sonnet as the starting point for drafting a client proposal when you are unsure which model to use. D, Haiku for a multi-step analysis of conflicting obligations across three supplier contracts. E, Opus for every reply in a shared customer inbox, to maximise quality. [pause]

ALEX: A and C.

SAM: Both right. A is high-volume, simple work, Haiku's job. C follows the guidance to start with Sonnet when unsure. B spends the heaviest model on a mechanical edit. D puts the lightest model on multi-step reasoning across documents. E is the "maximise quality" overspend: the heaviest model on routine replies. [sting]

## Segment three: restart, summarise or persist

SAM: Last objective: context limits and memory. The context window is the material Claude can work with in one conversation: everything said, every file attached. It is large, but it is finite.

ALEX: What happens when a chat gets very long?

SAM: On paid plans with code execution enabled, the help centre says that as a conversation approaches the limit, Claude summarises earlier messages to make room, and your full chat history is kept. It also says longer conversations that trigger this use more of your usage limit.

ALEX: Then why would I ever restart? It handles it for me.

SAM: It does, and for one long piece of work that is often fine.

SAM: But a summary compresses. If the chat has drifted, if an early wrong figure keeps coming back, or if you are starting an unrelated task, the old material is now working against you. The exam gives you three moves. Restart: a new, unrelated task, or a conversation anchored on something wrong. Summarise: same work, chat grown long, so ask Claude for a summary of the decisions, figures and open questions, check it, and open a fresh chat with it. Persist: anything you need across many chats goes into a Project's knowledge or instructions.

ALEX: Why not just rely on memory for that?

SAM: Memory is real and useful. The help centre says Claude can remember things from your chats, you can view and edit what it remembers in settings, each project has its own memory, and incognito chats are not saved to memory at all. But memory holds what came up in conversation, in Claude's words. A rate card that must be quoted exactly belongs in the Project knowledge as the document itself. And note: the help centre says context is not shared across chats within a project unless it is added to the knowledge base.

ALEX: So the tell for persist?

SAM: "Every week", "every chat", "the whole team needs it". That points to Project knowledge or instructions, not to hoping the next chat remembers.

SAM: Pause here and answer before we go on. A finance analyst has spent three hours in one chat reworking a budget variance analysis. The figures changed twice. Claude now keeps quoting numbers from the first, superseded version. What is the best next step? A, switch to Opus in the same chat. B, keep going and restate the correct figures at the top of every message. C, ask Claude to summarise the agreed current figures and decisions, check that summary against her spreadsheet, and start a new chat with it. D, turn on research so Claude can find the right figures. [pause]

ALEX: C.

SAM: C. The chat is anchored on stale numbers, and the work continues, so summarise, verify and carry over. A is the bigger model again, still sitting on the same stale context. B fights the context every turn instead of clearing it. D searches the web for figures that live in her spreadsheet.

SAM: One more, in the dropdown style. Pause here and answer before we go on. For each situation, choose restart, summarise and carry over, or persist. One: an HR partner finishes a long chat on a pay review and now wants help with an unrelated team-offsite agenda. Two: a sales lead's proposal chat has run all afternoon and is near its limit, and she still needs the pricing section. Three: a consultant's team needs the same client glossary in every chat for the next six months. Four: a chat about a policy draft keeps returning to an assumption the user corrected an hour ago, and the draft is not yet finished. [pause]

ALEX: One, restart. Two, summarise and carry over. Three, persist. Four... restart?

SAM: Four is summarise and carry over. The work is unfinished, so you keep it, but you start clean with a checked summary that states the correction. Restart is for a new task. One is a new, unrelated task: restart. Two is the same work near the limit: summarise and carry over. Three is needed in every chat for months: persist it in the Project knowledge. [sting]

## Cold open: the verdict

SAM: Back to the vendor review. Alex, you picked A, a standard chat on Opus.

ALEX: And I can see it now. Opus can only tell her what it learned in training. She asked for the last three months, from current sources.

SAM: That is the miss: a model answer to a feature question. The answer is B. Research investigates across many current sources, and an artifact is the right home for a one-page comparison the director will edit and share. A gives a strong model no way to see recent news. C uses a fast model and manual pasting for work that needs investigation. D gives the Project last year's review, which is the wrong year.

ALEX: What should have stopped me?

SAM: "Many current web sources" and "will edit before it goes on". The first is research, the second an artifact. Neither is solved by a bigger model. [sting]

## Five to remember

SAM: One: chat for one-off work, a Project for repeated work with the same files and instructions, research for in-depth questions across many sources, an artifact for substantial content you will edit, reuse or share.

ALEX: Two: Haiku is the fastest and lightest, for high-volume, simple tasks. Sonnet is the daily driver and the place to start when unsure. Opus is for deep, sustained reasoning, and for work Sonnet struggled with.

SAM: Three: model choice is matching, not maximising. "Most capable" for a simple, high-volume job is the overspend distractor, and "cheapest" for multi-step reasoning is the false economy.

ALEX: Four: a long chat is summarised automatically on paid plans with code execution, but that uses more of your limit. Restart for a new task, summarise and carry over to continue the same work cleanly.

SAM: Five: anything needed across many chats goes into Project knowledge or instructions. Context is not shared between chats in a project unless it is in the knowledge base, and memory is no substitute for the document itself.

## Recap: the exam tells

SAM: Recall first. Pause and name the three things this episode taught you to choose between. [pause]

ALEX: Chat, Projects, research and artifacts. Haiku, Sonnet and Opus. And restart, summarise or persist.

SAM: Now as exam tells. If the stem says "every week" with the same files, think Project. If it says "in depth", "many sources" or "current", think research. If the output will be edited, reused or shared, think artifact.

ALEX: If it says "high volume", "short" or "speed matters", think a faster, lower-cost model. If it says "multi-step", "conflicting" or "nuanced", think Opus. If it says "not sure which model", think Sonnet.

SAM: If an option says "most capable model" and the task is simple, that is the overspend. If an option switches model to fix missing information, that is the bigger-model reflex.

ALEX: If a chat is anchored on old figures and the work goes on, summarise, check it, carry it over. If the next task is unrelated, restart. If everyone needs it every time, persist it in the Project.

SAM: Next, episode four: bringing Claude into a workflow, from requirements to redesign.
