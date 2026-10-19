---
episode: 12
slug: practice-gaps
title: "Practice Exam Gaps: thinking, retention, effort and injection"
description: "A short bonus episode on five platform facts a practice exam tested and the series had not covered: thinking block retention by model, append-only history on Fable 5.1, the scope of zero data retention, effort sweeps before orchestration, and keeping your own instructions out of tool results."
domain: "Cross-domain (Domains 1, 2, 4, 5)"
weight: "applied mechanics"
target_minutes: 12
---

## In this episode

SAM: Welcome to Pass the Architect. This is episode twelve, Practice Exam Gaps.

ALEX: Where does it take me?

SAM: By the end you'll know which models keep earlier thinking blocks and how to reclaim the space. Why rebuilding the system prompt breaks a Fable five point one conversation. What zero data retention does and does not cover. Why an effort sweep comes before an orchestrator. And why your own instructions do not belong inside a tool result.

ALEX: These came from a practice exam. Eighty-four percent, a pass, and every miss here was a platform fact, not judgement.

SAM: And half the misses were choose-two items with one right pick. So on every option tonight, read to the last word. [sting]

## Cold open: the swelling context

SAM: A legal research agent runs on Claude Opus five. Input tokens per request grow much faster than the documents it retrieves. The logs show every earlier assistant turn's thinking blocks are still in each request. What is going on, and what should the team do? Option A, this is the documented default for Opus five; use thinking block clearing through context editing if they need the space back. Option B, the A P I always strips old thinking server-side, so their client must be duplicating blocks; fix the serialiser. Option C, turn thinking off for the rest of the conversation. Option D, a client bug; delete every thinking block older than two turns before each request.

ALEX: B. I have seen exactly that bug, a history builder appending twice.

SAM: Hold that. We'll come back to it. [sting]

## Thinking blocks by model

SAM: Whether earlier thinking stays in context is per model. Two groups. Keep all prior turns: Opus four point five and later, Sonnet four point six and later, Haiku five point five, and the Fable and Mythos models.

ALEX: And the other group?

SAM: Keep the last turn only: earlier Opus and Sonnet models, and Haiku up to four point five. On those, the A P I strips older thinking for you. That is where Alex's instinct comes from.

ALEX: So on a keep-all model, the growth is just normal history.

SAM: Yes. Retained thinking counts as input like any other turn. The documented lever is thinking block clearing, part of context editing. Clearing restarts the cache from that point, which is the trade you accept.

ALEX: Why not prune by hand? I'm allowed to drop old thinking outside a tool loop.

SAM: You are, but it is not the documented fix, it also breaks the cache, and inside a tool-use turn you must pass thinking blocks back complete and unmodified. One more detail: on Opus five at x high or max effort, thinking cannot be turned off at all. A request that tries gets a four hundred error. [sting]

## Append-only history on Fable

SAM: Fable five point one binds each thinking block to everything sent before it: the system prompt, the tools, and the earlier messages. Change any of them and that block and every later one is invalid.

ALEX: And the symptom?

SAM: A four hundred error saying the block is bound to a different conversation. The patterns that cause it: rebuilding the system prompt or tools array between requests, editing or removing an earlier turn, or injecting a reminder into an old turn and deleting it next time.

ALEX: Which is also exactly what kills a cache.

SAM: Same root cause, same fix. Treat the conversation as append-only. Stable role and policy live in the system prompt. Per-request content, the document and the question, goes in the user turn. New instructions arrive as a mid-conversation system message, and trimming goes through server-side context editing or compaction, which do not count as edits.

SAM: Pause here and answer before we go on. A retailer's returns assistant on Fable five point one builds its system prompt fresh on every call: the role, the returns policy, then today's order details. Cache hits are near zero and follow-up turns fail with a binding error. What fixes both? Option A, keep the role and policy as a fixed system prompt and put each order's details in the user turn. Option B, set a one-hour cache time to live. Option C, strip all earlier thinking blocks before each request. Option D, move everything into the first user message and leave the system prompt empty. [pause]

ALEX: A. A fixed prefix caches, and the system prompt stops changing under the thinking blocks.

SAM: Right. B lengthens the life of a prefix that never matches. C dodges the error but leaves the cache cold and throws away reasoning. D still changes the first thing the model sees on every call. [sting]

## What zero data retention covers

SAM: Zero data retention, Z D R. Under it, Anthropic does not store prompts or responses at rest after the response returns. Now the four edges the exam tests.

ALEX: Go.

SAM: One, it is requested through sales and enabled per organisation. Each new organisation needs it enabled separately. Nothing extends automatically.

SAM: Two, it covers eligible features only. The Files A P I keeps files until you delete them or they expire. Batch processing keeps data twenty-nine days. Code execution, M C P connector and Managed Agents are outside it too.

ALEX: Surely the A P I stops me using those by accident.

SAM: Under Z D R, no. Using an ineligible feature is a choice to step outside the arrangement for that data. Blocking with a four hundred error is the HIPAA-ready behaviour, not the Z D R one. That is a favourite distractor.

SAM: Three, even with Z D R, content flagged by trust and safety systems may be kept for up to two years, and data can be held where the law requires it. Four, the Fable and Mythos models require thirty-day retention, so they are not available under Z D R unless Anthropic expressly authorises it.

SAM: Pause here and answer before we go on. Choose two. A clinic-scheduling vendor has Z D R and plans to tell auditors that Anthropic keeps nothing. They use the Messages A P I, the Files A P I for referral letters, and nightly batches. Which two statements correct the plan? Option A, files and batch jobs fall outside Z D R and follow their own retention. Option B, the A P I rejects ineligible features under Z D R, so the plan is safe. Option C, content flagged by trust and safety may still be kept for up to two years. Option D, Z D R switches on by default for paid organisations. Option E, a new organisation under the same account inherits Z D R. [pause]

ALEX: A and C. B is the HIPAA blocking rule wearing a Z D R badge.

SAM: Exactly. D and E both fail on the same fact: Z D R is requested, per organisation. [sting]

## Effort before orchestration

SAM: Next, cost. Anthropic's guidance is to tune one model before adding a second. Sweep two or three effort levels on a sample of your own traffic, each in its own session, and plot score against spend.

ALEX: Why separate sessions?

SAM: Changing effort mid-session starts a new cache prefix and distorts the comparison. That curve is the baseline any multi-model design has to beat.

ALEX: So when does an orchestrator with cheaper workers pay?

SAM: In the measurements, only two cases: routine work with a long cost tail, and work bigger than one context window, fanned out across independent pieces. When the job is one dependent chain that fits in one context, the orchestrator's model alone at lower effort came out ahead every time.

ALEX: And the advisor pattern, a cheap executor that consults a frontier model?

SAM: It can only help when the executor actually consults it, and only with capability the executor lacks. No sign of either in the stem, no advisor.

SAM: Pause here and answer before we go on. An insurer's claims-review agent reasons through one claim file in a single dependent chain, well inside one context window. The team wants a cheaper design. What does the guidance suggest first? Option A, a frontier planner with three cheaper workers. Option B, keep one model and sweep effort to find the cheapest level that holds quality. Option C, move to the Batch A P I and change nothing else. Option D, an advisor pattern with the cheapest model as executor. [pause]

ALEX: Last time I picked batch. This time, B.

SAM: B. C may save money, but it dodges the architecture question the stem asks. A and D add a second model the shape of the work does not justify. [sting]

## Instructions in tool results

SAM: Last gap: indirect prompt injection. The user is trusted. The attacker controls content Claude reads on their behalf: an email body, a web page, O C R from an upload, a tool result.

ALEX: Versus a jailbreak, where the user is the attacker.

SAM: Right, and the defences differ. For third-party content: deliver it inside tool results, say where it came from, state in the system prompt that tool content is untrusted data, JSON-encode it where you can, screen tool output with a small classifier, and keep privileges narrow.

ALEX: And the part I missed?

SAM: Because Claude treats tool-result content as untrusted, instructions you put there yourself may be ignored or flagged as a suspected injection. Send your own instructions in a user turn after the tool result, or in a mid-conversation system message.

SAM: Pause here and answer before we go on. Choose two. An accounts-payable agent reads supplier invoices and emails. Which two belong in the indirect-injection section of its threat model? Option A, a supplier email contains hidden text telling the agent to change the bank details on file. Option B, a user role-plays as an auditor across several turns to talk the model out of a refusal. Option C, the developer's formatting rules, placed inside the tool result, are ignored as possibly injected. Option D, one account trips the same content filter all week and is throttled. [pause]

ALEX: A and C. B and D are the user as adversary, which is the jailbreak model.

SAM: Correct. Ask who controls the text. If it is a third party, it is indirect. If it is the user, it is direct. [sting]

## Cold open: the verdict

SAM: Back to the research agent on Opus five. You said B.

ALEX: Wrong group. Opus five keeps every prior turn's thinking. It is A.

SAM: A. Retention is the default on keep-all models, and thinking block clearing is the documented way to reclaim space. B describes last-turn-only models. C loses the reasoning the agent needs and is rejected at x high and max effort. D treats documented behaviour as a bug and edits the prefix by hand. [sting]

## Five to remember

SAM: One: newer models keep all prior thinking, and it counts as input. Reclaim it with thinking block clearing.

ALEX: Two: on Fable five point one, history is append-only. Rebuild the system prompt and you get a binding error and a cold cache.

SAM: Three: Z D R is per organisation, eligible features only, not enforced by the A P I, and flagged content can still be kept for two years.

ALEX: Four: sweep effort on one model before you split the work. Orchestrate only for independent fan-out or more than one context.

SAM: Five: your own instructions go in the user turn, never inside a tool result.

## Recap: the exam tells

SAM: Before the last word, pause and name the five gaps without looking back. [pause]

ALEX: Thinking retention by model. Append-only history on Fable. The edges of Z D R. Effort before orchestration. And instructions out of tool results.

SAM: Now as exam tells. If context grows from old thinking on a current model, think keep-all default and thinking block clearing, not a client bug.

ALEX: If a stem says bound to a different conversation, or the cache never hits, look for a system prompt rebuilt per request.

SAM: If an option says Z D R covers everything, blocks ineligible features, or arrives automatically, it is wrong. Files and batch have their own retention.

ALEX: If the work is one dependent chain in one context, think a single model and an effort sweep, and treat batch as a dodge.

SAM: If the text came from a third party, think indirect injection. If the developer's own instruction sits in a tool result, expect it to be ignored.

ALEX: That's the gaps closed.

SAM: Now sleep. Good luck tomorrow.
