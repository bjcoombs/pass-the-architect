---
episode: 2
slug: models-prompting
title: "Models, Prompting & Context Engineering"
description: "Model tiers chosen by eval rather than reflex, system prompts that hold at scale, when zero-shot, few-shot and chain-of-thought earn their tokens, context budgets, and prompt caching that actually hits."
domain: "Claude Models, Prompting & Context Engineering"
weight: "13%"
target_minutes: 23
---

## In this episode

SAM: Welcome to Pass the Architect. Episode two: Models, Prompting and Context Engineering.

ALEX: Where does it leave me?

SAM: By the end you'll be able to pick a model tier on eval evidence and know when extended thinking and fine-tuning are worth paying for. You'll write a system prompt whose guardrails hold, choose between zero-shot, few-shot and chain-of-thought, budget a context window and pick a context strategy, and build a prompt cache that actually hits, with Skills for procedures shared across teams.

ALEX: Thirteen percent, about eight items. And this is the domain where "use a bigger model" and blunt truncation turn up most as distractors, so it pays to know why they lose.

SAM: Then start with an item where every step already runs on the biggest model. [sting]

## Cold open: the claims pipeline

SAM: Here's the first item. An insurer runs a three-step claims pipeline: classify the incoming claim, summarise the supporting documents, then compose a note for the adjuster. Every step runs on the most capable model tier with extended thinking switched on. Monthly cost is five times the approved budget and median latency is well past the agreed target. What should the architect do first? Option A: move every step to the smallest tier. Option B: build an eval set for each step, set pass thresholds in advance, and move each step to the lowest tier that still passes. Option C: keep the top tier and truncate the supporting documents to cut input tokens. Option D: fine-tune a smaller model on the top tier's outputs.

ALEX: I'll say B. A feels reckless, and C throws away evidence the adjuster needs.

SAM: Hold that. We'll come back to it at the end.

SAM: This is Domain two, Models, Prompting and Context Engineering: thirteen percent, roughly eight of sixty-three items. The blueprint has five task statements: select models on trade-offs, design system prompts, templates and guardrails, apply zero-shot, few-shot and chain-of-thought, optimise context windows and token use, and implement prompt reuse through caching, modular prompts and Skills.

ALEX: Where does the exam make it hard?

SAM: In the distractors. "Use a bigger model" and blunt cuts like truncation that lose required content turn up here more than anywhere.

SAM: Model selection first. The course names three tiers: Haiku, Sonnet and Opus, each tuned for a different balance of cost, latency and capability. Opus is the most capable of the three. Where do you start?

ALEX: For a new build I'd start on Opus and tune down later.

SAM: That's the answer the exam wants you to drop. The course is explicit: start on Sonnet. Move up to Opus only when an eval set shows Sonnet misses your quality bar. Move down to Haiku only when an eval set confirms the quality loss is acceptable for that task. Measured, never reflexive.

ALEX: I'll argue it anyway. A wrong answer to a customer costs far more than the token bill. If quality matters more than cost, why not pay for the best?

SAM: Part of that holds. If the eval shows Sonnet misses the bar, Opus is the right call and the exam backs you.

SAM: But "the best" is a claim you haven't tested. Making no model decision is itself a decision, and it defaults to the most expensive option. Teams rarely come back to it, because downgrading a live system carries change-management cost.

ALEX: So the evidence decides, not the stakes.

SAM: Yes. The tell: an option that moves to a stronger tier without naming the measurement behind it is the bigger-model distractor. Pick the option that measures before it moves.

ALEX: So the eval set does more than gate a release.

SAM: It also makes the tier choice defensible in the design conversation. Three parts: a curated test set covering the real distribution of work, a grading function, and a threshold set before you run it. A threshold set afterwards isn't a standard, it's acceptance criteria written after the build.

ALEX: What does a well-run downgrade look like?

SAM: Picture a document-extraction pipeline at a bank. The cheaper tier scores fine on average, but two document types fall below the agreed threshold, which the average hid. So route those two types to the stronger tier through the existing classifier and send the rest to the cheaper one. That's what routing tiers means on this exam. Different steps, or different input classes, on different models, each choice backed by an eval.

ALEX: And latency? Does high volume push latency up?

SAM: The course ties latency to task complexity, model size and output length, not volume. Tier and output length are the levers.

ALEX: And extended thinking?

SAM: It's a cost and latency trade. Thinking tokens are billed as output tokens and add time to every call. The model reasons either way; you're choosing whether to pay for a separate reasoning pass. The rule: run evals without it, work on the prompt, and turn it on only when a measured accuracy gap remains.

ALEX: I'd still leave it on for anything customer-facing. If it catches one bad answer in a thousand, a second of latency is cheap.

SAM: On a genuinely multi-step task a measured gap can justify it, and then you're right to pay.

SAM: But one in a thousand is a hope, not a measurement. You pay the thinking tokens and the delay on every call, and "it can't hurt" is not evidence.

ALEX: So what in the item points me away from it?

SAM: The phrase "accuracy meets the target". Once the stem says that, thinking is a cost to remove, not a safeguard to keep.

ALEX: And fine-tuning, when prompting feels flaky?

SAM: Last step, not first. Most reliability problems are prompt problems. The order is: improve the prompt, add tools or retrieval, move to a stronger pattern, and only then consider fine-tuning. It earns a look at very high volume where inference cost is the binding constraint, where latency is critical and a smaller specialised model would win, or where a consistent format still fails after prompting. Otherwise it ties you to a fixed model version and narrows your options.

ALEX: Prompts are brittle, though. My last client spent weeks chasing format drift. A fine-tuned model would just have learned the shape.

SAM: A consistent format that still fails after prompting is one of the three cases the course names, so your client may well have earned it.

SAM: The question is whether the stem says they got there. Most reliability problems are prompt problems, and the exam assumes you start at the bottom of the ladder.

ALEX: And if it doesn't say?

SAM: Then the fine-tune is out of order. The tell: unless the stem says prompt work was tried and still fails, fine-tuning is a distractor, and the word "first" makes it certain.

ALEX: The real line-up changes every few months, though.

SAM: Faster than any exam. The course reasons in tiers, so do the same: ask where a tier sits on the cost, latency and capability trade, not which version number it has.

SAM: Pause here and answer before we go on. A retail bank's support router sorts incoming messages into one of six queues. It runs on a mid tier with extended thinking enabled. Accuracy meets the target, but the router adds noticeable latency to every conversation. What's the best change? Option A: move the router to the top tier so it finishes its reasoning faster. Option B: disable extended thinking on the router and confirm on the eval set that accuracy holds. Option C: add three worked examples per queue to the prompt. Option D: cache the router's responses for a day. [pause]

ALEX: B.

SAM: Correct. A router that needs no reasoning gains nothing from a thinking pass but pays its latency and cost on every request. Turn it off, then confirm with the eval, because configuration changes are behaviour changes. A is "bigger model" and makes cost worse. C adds input tokens to a task that's already accurate. D caches outputs, and every customer message is different, so nothing would match. [sting]

## System prompts and guardrails

SAM: Second task statement: system prompts, templates and guardrails. A system prompt that hundreds of requests a day depend on is an asset you design, not a sentence you type. What does it need?

ALEX: A role, some rules, an output format?

SAM: Close. Role and scope: what's in bounds and what's out. Constraints: what it must never do and must always do. And an output contract naming the exact shape of the response. At scale, ambiguity is a defect repeated on every request.

ALEX: And templates?

SAM: A template is that system prompt with parameterised slots inside fixed scaffolding. The design rule: the scaffolding carries the consistency and safety guarantees, so filling a slot can never remove a constraint.

ALEX: What's the failure the exam probes here?

SAM: Underspecification. Where the prompt is silent, the model fills the gap with its own assumption, differently each run. The diagnosis is to take each requirement the output must meet and ask whether the prompt states it or only hopes for it. Then make the implicit explicit, and restate the goal beside the instruction, since the model can follow the letter and miss the intent.

ALEX: Concrete example?

SAM: An extraction prompt says "always include all fields, even if empty". The model reads it as "fill every field" and invents values. The intent, an empty value, was never stated.

ALEX: How do you make a guardrail hold?

SAM: Build it into the output contract, not just the role text. Picture a public-sector benefits assistant that must never promise a payment date. Put that sentence in the role text and the model can drift past it. Make the response format require it structurally and it can't be quietly ignored. The course's line is that an underspecified guardrail is worse than a missing one, because it looks like a control without being one.

ALEX: My last client put "never promise a payment date" in capitals in the role text. Months in production, no complaints.

SAM: Role text often does hold on ordinary traffic. I won't pretend it never works.

SAM: But no complaints only means nobody noticed. An unusual input can talk the model past a sentence; it can't skip a field the response format requires.

ALEX: So the stem tells me which one it wants?

SAM: Watch for "must never" or "guarantee". A must-never needs a structural answer in the output contract, not a firmer sentence.

ALEX: That links to governance.

SAM: It does, and it's worth carrying into Domain five. A system prompt shapes behaviour inside a request, but it isn't enforcement. An unusual or hostile input can talk the model out of it, so policy that matters also needs runtime controls: screening, authorisation and review. Same with precision: for anything needing exact logic or high-stakes numbers, use structured outputs and code execution, not free text. [sting]

## Choosing a prompting technique

SAM: Third task statement: techniques. Zero-shot, few-shot and chain-of-thought. Before I explain, which do you reach for first?

ALEX: Few-shot. Examples always seem to help.

SAM: That's the habit the exam punishes. Zero-shot is the default for a well-specified task the model already handles: classifying tickets into named categories, or summarising a short product description. Few-shot is for when the format or judgment is easier to show than to describe: pulling fields from receipts with wildly varied layouts. Chain-of-thought is for multi-step reasoning, where the path decides the answer: whether a contract clause creates liability under three conditions that interact.

ALEX: And the rule for choosing?

SAM: The lightest technique that meets the requirement. Each step up costs tokens and latency on every call. Chain-of-thought on a summarisation task is a recurring tax for no gain.

ALEX: Does the choice change across models?

SAM: Yes. A more capable model usually needs less scaffolding to reach the same quality, so a prompt tuned for one model is only a starting point for another. The thing you ship is the prompt and model pairing, which is why a model swap gets an eval like any release.

ALEX: And bias?

SAM: Leading phrasing, example sets showing only one kind of case, and prompts that presume the answer. Bias shows up only in aggregate, so neutral phrasing and balanced examples are requirements, not polish. And stale few-shot examples quietly steer the model wrong as the task changes.

SAM: Pause here and answer before we go on. This one is choose two. A field-service company's ticket triage prompt assigns priority by business impact. Engineers notice that angrily worded feature requests keep getting top priority. Which two changes address the root cause? Option A: add a few-shot example showing an urgently worded feature request correctly assigned the lowest priority. Option B: add an explicit rubric instruction to judge priority by impact and ignore tone. Option C: move the prompt to a larger model tier. Option D: enable extended thinking. Option E: add a dashboard tracking the distribution of priorities each day. [pause]

ALEX: B for certain, the rubric never says to ignore tone. For the second I'll take E. We just said the lightest technique that works, an example is a step up in tokens, and E tells you whether B worked.

SAM: Wanting to check the fix is sound. In production you'd build that dashboard.

SAM: But you've stretched "lightest technique" past its scope. That rule stops you adding scaffolding a task doesn't need. Here the judgment is easier to show than describe, which is exactly where few-shot earns its place. That's the over-applied rule, one of your miss patterns.

SAM: The answer is A and B. The rubric defines severity by impact but never tells the model to ignore tone, so urgent wording inflates priority. B closes that gap directly. Without an example to the contrary, the model maps urgent language to high priority, and A shows it the counter-case. C and D spend money without diagnosing why the prompt fails. E is a detective control dressed as a fix. It might tell you the problem exists, but it fixes nothing. [sting]

## Context windows and tokens

SAM: Fourth task statement: context windows and tokens. Four terms the course insists you keep apart. The context window is the model's active attention space and resets between calls. Retrieval fetches external knowledge at query time and adds to the window rather than replacing it. Persistent application state, like an order status or an account balance, lives in your system and needs a tool call. And memory layers are continuity your application stores and passes back. The model has no native memory between calls.

ALEX: How much of the window should I plan to use?

SAM: Not all of it. The window is a ceiling, not a target. Budget for the largest realistic conversation, plus retrieved context, plus the system prompt, plus working space, plus margin for growth. Measure rather than estimate: every response reports actual token counts in its usage field, and a token-counting endpoint works before you send.

ALEX: What happens at the edge?

SAM: Two failures people conflate. A request already too large is rejected before generation. A request that fits but whose output hits the ceiling stops early, truncated, with a stop reason saying the window ran out. And attention can degrade on very long contexts well short of the limit.

ALEX: Then strategy. Monolithic or progressive?

SAM: Monolithic loads everything at once. It suits bounded tasks, stable prefixes you can cache, and reasoning that needs all the material together. It breaks when context piles up: a conversation starting at four thousand tokens can carry eighty thousand by turn thirty, with per-call cost climbing silently until the bill arrives. Progressive loads only what the next step needs and is the right default for most production workloads. Between them sit retrieval, for corpora too big to fit or sources that change faster than you redeploy, and compaction, which summarises accumulated context.

ALEX: Compaction sounds like the free fix.

SAM: It's largely one-way. A summary that drops an exact identifier, a figure or a prior decision can't get it back. And real systems combine all four by phase: a stable cached prefix at the start, recent state while working, retrieval on demand, compaction when the window fills. Strategy and sizing are separate decisions. Treating them as one is where most designs go wrong.

ALEX: And cost modelling?

SAM: Model the token distribution, not the average. Most requests are short, but a tail of long ones can take a large share of spend, and an average-based model can understate cost two or three times. Domain four uses the same logic when it prefers p ninety-five latency to the median. [sting]

## Prompt reuse and caching

SAM: Last task statement: prompt reuse. Caching first. The cache matches on a stable prefix. Order is tools, then system, then messages, and any byte-level change invalidates everything after it. So what goes first?

ALEX: The static material. Instructions and reference documents first, per-request content last.

SAM: Yes. Static before dynamic, always, with the cache breakpoint marked at the boundary. On the Anthropic API caching is explicit: you mark segments with cache control markers, and savings aren't automatic. Writing to the cache costs more than normal input; reads cost a fraction of it. The course's worked example uses reads at ten percent of the input rate, and it tells you to check current pricing. Hits also cut time to first token.

ALEX: So switch it on everywhere?

SAM: No. The default cache lifetime is five minutes. A prompt called less often, or with a small fixed portion, may never pay back the write. Prefixes below a per-model minimum length silently aren't cached at all, so verify hits with the cache-read token count in the usage field. And if the cached content has to reflect live state, caching opens a consistency window.

ALEX: If a fixed block is that expensive, why not cut it? Most of a long policy document is clauses nobody's question ever touches.

SAM: Loading only what the next step needs is the progressive default, so dropping material that's genuinely unused is fair.

SAM: Truncation is blind, though. It removes whatever falls past the line, and the clause the model needs is as likely to be there as anywhere. If the stem says the content is required, cutting it fixes the cost by breaking the task. Caching fixes the same cost and keeps the content.

ALEX: So the tell is the word "required"?

SAM: That, plus a cost or latency complaint about a fixed block. The pairing points to caching, and truncate or summarise is the blunt cut.

SAM: Pause here and answer before we go on. A field-service assistant builds every request as follows: the current timestamp and the technician's ID, then a six-thousand-token equipment manual and safety rules, then the technician's question. Calls arrive every few seconds. Caching is enabled, but the cache-read token count is always zero. What's the best fix? Option A: lengthen the cache lifetime. Option B: move the timestamp and technician ID after the manual and safety rules so the fixed block becomes the prefix. Option C: switch to a smaller model tier. Option D: summarise the manual down to five hundred tokens. [pause]

ALEX: B. The timestamp changes on every call, so the prefix never matches.

SAM: Exactly. A doesn't help, because the entry never matches in the first place, and calls every few seconds sit well inside five minutes anyway. C changes the price per token but never produces a hit. D is the blunt cut: it discards safety content the technician needs, and could push the prefix towards the minimum length. Reorder, then confirm hits in the usage field.

ALEX: Now modular prompts versus Skills.

SAM: A modular prompt library is shared fragments and templates engineers assemble in their own code, fine within one team. A Skill is a versioned, self-contained unit, a SKILL dot md file packaging the instructions plus optional scripts, travelling as one governed artifact. Choose a Skill when the same procedure runs the same way every time, is distributed across teams or products, and needs versioning, approval and rollback.

ALEX: And without one?

SAM: A prompt copied across teams drifts into many slightly different versions. Versioned reuse is the control.

SAM: Back to the cold open. The claims pipeline on the top tier with thinking on, five times over budget. You said B.

ALEX: B. Per-step evals, thresholds set first, lowest passing tier for each step.

SAM: Correct. A is the reflex in reverse: a downgrade without evidence risks quality on the step that needs it, probably the adjuster note. C is the blunt cut that drops evidence and leaves thinking on the classifier. D jumps to fine-tuning before prompting and tier selection, and ties you to one model version. When this pattern plays out, the usual end state is the classifier on the small tier, summarisation in the middle, the top tier kept for final composition, and cost down sharply with quality unchanged. [sting]

## Five to remember

SAM: Five to remember. One: start on Sonnet, and move up or down only on eval evidence, with the threshold set before you run it.

ALEX: Two: the lightest technique that works. Zero-shot by default, few-shot when it's easier to show, chain-of-thought when the path decides the answer.

SAM: Three: guardrails belong in the output contract and runtime controls, not just in role text. A guardrail the model can route around isn't a guardrail.

ALEX: Four: the context window is a ceiling, not a target. Default to progressive, combine strategies by phase, and model the token tail, not the average.

SAM: Five: static before dynamic. Caching keys off a stable prefix; verify hits in the usage field, and use a Skill when a procedure must be versioned and shared across teams.

## Recap: the exam tells

SAM: Before the tease, a test. Pause and name the five task statements we covered, or the giveaway for each. [pause]

ALEX: Model selection. System prompts and guardrails. Zero-shot, few-shot and chain-of-thought. Context windows and tokens. And prompt reuse: caching, modular prompts and Skills.

SAM: Now as exam tells. If an option moves to a stronger tier without naming a measurement, think bigger-model distractor. If the stem says accuracy meets the target and thinking is on, think turn it off and confirm on the eval.

ALEX: If fine-tuning shows up and the stem never says prompt work was tried and still fails, think out of order.

SAM: If the stem says "must never" or "guarantee", think a structural answer in the output contract, not a firmer sentence in the role text.

ALEX: If the judgment is easier to show than describe, think few-shot. If the path decides the answer, chain-of-thought. Otherwise zero-shot.

SAM: If a conversation's cost climbs turn after turn, or a cost model rests on the average, think progressive context and the token tail.

ALEX: If caching is on but the cache-read count is zero, look for something volatile sitting before the fixed block.

SAM: And if a fixed block is called required and cost or latency is the complaint, think caching, never truncation. If a prompt is copied across teams and drifting, think Skill.

ALEX: Next time: Integration, part one. Protocols, capability bloat, identity and auth, and progressive discovery, in the heaviest domain on the exam.
