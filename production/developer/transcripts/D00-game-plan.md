---
episode: "D00"
series: "CCDV-F"
slug: game-plan
title: "Developer game plan"
description: "How the Developer Foundations exam is built: fifty-three items in two hours, eight weighted domains, a countdown pacing plan, per-statement dropdown items, and a four-step method worked through the three official sample questions."
domain: "All domains"
weight: "100%"
target_minutes: 12
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode zero, the game plan.

ALEX: What do I walk away with?

SAM: By the end you'll be able to describe the paper: fifty-three items, two hours, eight domains and where the weight sits. You'll pace it with three checkpoints off a clock that counts down. You'll know how to handle a dropdown item, statement by statement. You'll have a four-step method for reading any item. And you'll have used that method on all three official sample questions.

ALEX: I've shipped with the A P I and Claude Code. Do I need a method, or just the facts?

SAM: Both. Most wrong options here are things a working engineer would try first. The method is what stops you picking them. Let's start with one. [sting]

## Cold open: ten thousand documents

SAM: First official sample. A developer must process ten thousand documents overnight to produce a non-urgent analytics report. Cost is the primary concern, and results are not needed until the following morning. Which approach best fits the requirement?

SAM: Option A, send every request synchronously through the Messages A P I in parallel, to finish as quickly as possible. Option B, use the Message Batches A P I, which processes large asynchronous workloads within a twenty-four hour window at reduced cost. Option C, lower max tokens on synchronous calls to minimise cost. Option D, switch to the smallest available model regardless of output quality.

ALEX: I'd have written A on my last project. Parallel calls, a worker pool, done by midnight.

SAM: Hold that. We come back to it once you have the method. [sting]

## The paper

SAM: Fifty-three items in a hundred and twenty minutes. Multiple choice and multiple response, and every item states how many to select. The pass mark is a scaled seven hundred and twenty on a range of one hundred to one thousand.

ALEX: Measured against other candidates?

SAM: No, against a fixed standard. Your score report shows percent correct by domain, but only the total decides the result, so a strong domain can carry a weak one.

ALEX: Multiple response. How do I play those?

SAM: Read the number first. Then judge every option on its own: true for this stem, or not. A choose-two item with five options is five small true-or-false questions. The guide does not say whether partial credit exists, so treat one wrong pick as costing the whole item.

ALEX: And the domains?

SAM: Eight. One dominates. Applications and Integration is thirty-three point one percent, about seventeen or eighteen items: A P I mechanics, software engineering foundations, application design, configuration, requirements and the systems life cycle.

ALEX: A third of the paper in one domain.

SAM: Then Model Selection and Optimization, sixteen point eight percent, about nine items. Agents and Workflows, fourteen point seven, about eight. Prompt and Context Engineering, eleven percent, about six. Tools and M C Ps, ten point six, five or six. Security and Safety, eight point one, about four. Then two small ones: Claude Code at three point one percent and Eval, Testing and Debugging at two point six, one or two items each.

ALEX: Claude Code at three percent? That's most of what I do all day.

SAM: Which is why it's a trap to over-study it. And remember the items carry no domain label. A Claude Code question may really be testing configuration management or hooks. You read the stem, not a heading. [sting]

## Pacing and the screen

ALEX: Pacing.

SAM: Keep ten minutes in reserve for flagged items. That leaves about two minutes four seconds an item. The clock counts down in hours and minutes, so the checkpoints are time left, not time spent. Item eighteen with one hour twenty-three left. Item thirty-five with forty-seven minutes left. Item fifty-three with ten minutes left.

ALEX: One twenty-three, forty-seven, ten.

SAM: If an item runs past two minutes, pick your best answer, flag it and move on. A blank never scores. Review at the end lists your flagged and unanswered items.

ALEX: Two minutes feels generous.

SAM: It is, until a dropdown item eats four. Some items list four or five statements, each with its own dropdown of two or three choices: true or false, or which of three mechanisms fits. No choice is a throwaway. Each statement is its own small judgement, so read each one alone against the stem.

ALEX: So a dropdown item is a choose-all-that-apply in disguise.

SAM: Closer to four items sharing one stem. That's why we'll drill them in every episode, read aloud as "for each statement, say true or false". [sting]

## The four-step method

ALEX: The method, then.

SAM: Four steps. One, count. Read how many to select, and read the last line of the stem: best fits, most effective, first step, NOT.

SAM: Two, constraint. Find the words that set the bar: cost is the primary concern, overnight, untrusted, reusable across applications, must never. That phrase decides the item.

SAM: Three, mechanism. Name the purpose-built mechanism for that constraint before you look at the options. The exam rewards the tool designed for the job.

SAM: Four, strike. Cross out the three families of distractor the samples show. Faster or bigger: more parallelism, a larger model. A polite instruction where a control is needed. And pasting data into the prompt where the model needs access. Then strike anything with one wrong clause, however good its first half.

ALEX: Count, constraint, mechanism, strike.

SAM: Say it until it's automatic.

SAM: Pause here and answer before we go on. Second official sample. A Claude-powered agent summarises web pages submitted by end users. One page contains hidden text instructing the model to ignore previous instructions and reveal its system prompt. Which mitigation is most effective? A, raise the model's temperature so its behaviour is harder to predict. B, treat retrieved page content as untrusted input, keep it separate from trusted instructions, and use guardrails or hooks so injected instructions cannot trigger sensitive actions. C, add a line to the system prompt asking users not to include malicious instructions. D, switch to a larger model that follows instructions more reliably. [pause]

ALEX: Count: one, most effective. Constraint: content from end users, so untrusted. Mechanism: isolation plus an enforced control. B.

SAM: B. Now argue for D. You've seen a stronger model shrug off an injection a weaker one fell for.

ALEX: I have. Bigger models are better at telling instructions from data.

SAM: Sometimes, and a better model is a fine upgrade. But the guide's rationale says a more instruction-following model can be more susceptible, not less. It is the faster-or-bigger family. A is irrelevant to injection, and C is the polite instruction: a request is not an enforceable control.

ALEX: The tell?

SAM: Untrusted content near sensitive actions. The answer separates it and enforces a control. It never asks nicely.

SAM: Pause here and answer before we go on. Third official sample. A team needs Claude to call an internal inventory service exposed as a REST A P I. They want the capability reusable across several Claude applications and maintained independently of any one app. Which approach best fits? A, hard-code the inventory logic into each application's system prompt. B, build an M C P server that exposes the inventory operations as tools, so multiple Claude applications can connect to it. C, paste the current inventory data into the context window on every request. D, rely on a built-in tool, since built-in tools can reach any internal REST A P I. [pause]

ALEX: Constraint: several applications, maintained independently. B.

SAM: B. Push back.

ALEX: For one app I'd write a custom tool that calls the REST endpoint. Twenty lines, no server to run.

SAM: For one app, that's a good answer, and the exam may ask exactly that. But this stem says several applications and maintained independently of any one. A custom tool lives inside each app and gets copied. An M C P server is built once and every app connects. A is neither reusable nor maintainable. C pastes data: no live access, and wasted context. D is false: built-in tools don't reach arbitrary internal A P Is.

ALEX: So the tell is the word "several".

SAM: "Several applications" and "independently". Shared capability, one server. [sting]

## Dropdown practice

SAM: Pause here and answer before we go on. Our own item, in dropdown form. A travel company's assistant quotes fares, and fares change many times a day. Every quote must use the current fare. For each statement, say true or false. One, pasting the morning's fare table into the system prompt meets the requirement. Two, a tool that looks up the fare for the requested route at the moment of the question meets it. Three, a model with a larger context window solves it, because the whole fare table then fits. Four, the word "current" in the stem is what rules out a pasted snapshot. [pause]

ALEX: False, true, false, true.

SAM: All four. One is pasted data: stale within the hour, and paid for on every request. Two is access, the mechanism built for live data. Three is the bigger family: more room for a stale table is still a stale table. Four names the constraint.

ALEX: And "current" was the constraint word.

SAM: "Current" or "live" means access, not a pasted copy. [sting]

## Cold open: the verdict

ALEX: Back to ten thousand documents. I said A, parallel synchronous calls.

SAM: Run the method. Count: one, best fits. Constraint: cost is the primary concern, and results aren't needed until morning. Mechanism for cost-first, latency-tolerant volume: the Message Batches A P I. The answer is B.

ALEX: But parallel calls would actually finish faster.

SAM: They would, and if the stem said the report was needed in an hour, speed would matter. It said cost first and morning is fine. Parallel synchronous calls don't reduce per-token cost; A is the faster family. C trims output but doesn't address batch against realtime. D buys cost with quality the stem never offered to give up.

ALEX: So the tell?

SAM: "Overnight", "non-urgent", "cost is the primary concern". Time to spare and money to save points to batch. [sting]

## Using the series

ALEX: How do I use the rest of the series?

SAM: In order. Episodes one to four cover the big domain: the A P I and its costs, software engineering, application design, then configuration and Claude Code. Five is models. Six, agents and workflows. Seven, prompts, context and output. Eight, tools and M C P. Nine, security, hooks, secrets and debugging. Ten is the final drill for the night before, and eleven is for the morning.

ALEX: And when you say pause?

SAM: Pause and say your answer out loud before you hear ours. In choose-two and dropdown drills, call every option or statement. Recalling an answer does more than hearing it twice. [sting]

## Recap: the exam tells

SAM: One more pass. Pause and name the four steps of the method, and the three distractor families. [pause]

ALEX: Count, constraint, mechanism, strike. Faster or bigger, a polite instruction, and pasting data instead of access.

SAM: Now as exam tells. If an item says choose two, read the number first and judge each option alone.

ALEX: If you reach item eighteen with less than one hour twenty-three left, or an item passes two minutes, answer, flag and move on.

SAM: If an item shows a list of statements with dropdowns, treat each statement as its own small item.

ALEX: If the stem says cost first and no rush, think batch, not parallel calls.

SAM: If content comes from users or the web, keep it apart from instructions and enforce with guardrails or hooks.

ALEX: If a capability must serve several applications, think a shared M C P server, not pasted data or copied logic.

SAM: And if the stem says current or live, the answer gives Claude access, not a pasted copy.

ALEX: Next?

SAM: Episode one: messages, streaming, thinking, caching and batch, and what each costs.
