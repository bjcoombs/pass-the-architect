---
episode: 5
slug: evaluation
title: "Evaluation, Testing & Optimization"
description: "Evals as acceptance criteria, the grading ladder, A/B tests that don't overclaim, diagnosing the component the trigger touched, the demo-cost trap, and observability that catches slow decay. Domain four, sixteen percent of the exam."
domain: "Evaluation, Testing & Optimization"
weight: "16%"
target_minutes: 25
---

## In this episode

SAM: Welcome to Pass the Architect. Episode five: Evaluation, Testing and Optimization.

ALEX: What will I walk away able to do?

SAM: Write evals as acceptance criteria with thresholds taken from the business, and choose code, a judge or a human for each check. Run an A/B test that doesn't overclaim, and know when shadow testing is the only option. Classify a failure by the component its trigger touched. Model cost at production volume and pick the right levers. And monitor for wrong answers that never throw an error.

ALEX: It's sixteen percent, about ten items, and the traps are testing after the build, trusting a small sample, and reaching for a bigger model before diagnosing anything.

SAM: Then start with a suite that passes and a system that doesn't. [sting]

## Cold open: the passing suite

SAM: Opening item. A health insurer's claims team revises its extraction prompt. The eval suite passes at ninety-nine percent. A week later, adjusters report missing incident dates on scanned, partly handwritten forms. The model version is pinned and latency hasn't moved. Most likely root cause? Option A, the model's behaviour changed under the pinned version. Option B, the golden dataset predates the prompt change and holds few or no scanned, handwritten forms. Option C, the judge model grading the extractions is too lenient. Option D, the temperature is too high.

ALEX: C. A ninety-nine percent pass that doesn't match production smells like a lenient grader.

SAM: Hold that. We'll come back to it.

SAM: This is domain four, Evaluation, Testing and Optimization, sixteen percent of the exam, roughly ten items. Six task statements: define metrics across accuracy, latency, cost, safety and security. Design datasets and test frameworks with mixed methods. Run A/B tests and iterate. Diagnose prompt failure, hallucination and model mismatch. Optimize tokens, latency and cost-performance. And monitor with logging and observability.

ALEX: Where does the course put its weight?

SAM: Evals as acceptance criteria, and experiments that don't overclaim. Those two ideas sit under almost every item here.

ALEX: My instinct is build the thing, then write tests once it works.

SAM: Make the case for it.

ALEX: Early on I don't know what good looks like. The prompt changes daily, the output shape shifts, and any eval I write on day one gets rewritten by day five. Tests against a moving target are wasted effort.

SAM: Part of that holds. A prototype is how you learn what the system can do, and a suite written against a format you then abandon does get rewritten. But the exam treats the eval suite as acceptance criteria, written before production code, not bolted on as a QA step. Writing it first forces you to state success in measurable terms, exposes design assumptions while they're cheap to change, and gives you a gate for every later change.

ALEX: And if I wait until it works?

SAM: Then "works" means whatever the prototype happened to do. If you can't write an eval for a behaviour, you have no reliable way to know it's there, so no change to it is verifiable. The tell: any option that runs evals after the build, or as a final QA pass, is the distractor. Listen for "before production code" and "acceptance criteria".

ALEX: How do I get from a business requirement to a threshold?

SAM: Four moves. Take "summarize claims accurately". Make it specific: extract the filer's name, claim number, incident date and claimed amount. Set the threshold from the business requirement, not from whatever the first prototype hit. The course's example: one hundred percent on structured fields, under two percent hallucination, schema compliance ninety-nine point five percent. List the failure modes, a fabricated claim number, a missing date, a value from the wrong claim, and give each its own dataset category. Then add adversarial inputs: missing fields, handwriting, odd layouts.

ALEX: So "the POC got ninety-two percent, make that the bar" is the distractor.

SAM: Yes. A threshold anchored to the prototype measures the prototype, not the need. Now the five metric dimensions. The course's exercise is an insurer: extract fields, summarize the narrative, flag possible fraud, respond in seconds, stay under a per-claim cost, never leak one claimant's data into another's summary, never auto-deny.

ALEX: Field accuracy is code, because the expected values are known.

SAM: Right. Latency is code: P ninety-five against a target. Cost is code: it comes from input tokens, output tokens, model tier and whether caching applies. Security is the interesting one.

ALEX: Cross-claimant leakage is high-stakes. I'd want a judge, or a human.

SAM: That's the trap. Stakes don't pick the method; the nature of the check does. Scan each summary for identifiers from any other claim in the batch. Deterministic, so code. Safety splits: no auto-deny is binary, so code, while summary faithfulness needs interpretation, so a judge.

ALEX: When a dimension bundles an action with a judgment, split it into two checks.

SAM: Yes. That's the grading ladder, climbed from the bottom. Code wherever the behaviour allows: schema, exact match, length, presence. Milliseconds, almost free, never drifts. Then a model-based judge with a rubric, for tone, reasoning, appropriateness, faithfulness. Then human review, for high-stakes or novel behaviour where neither code nor a calibrated judge is trustworthy yet. Slowest, dearest, and humans bring their own inconsistency.

ALEX: And watch for checks that sound interpretive but aren't, like confirming the extracted claim number matches the source.

SAM: If the expected value is known, it's a comparison, so code. Making a judge rigorous: a detailed rubric, constrained verdicts from a small fixed set of labels, reasoning alongside the score so you can see borderline inconsistency, a different model from the one being graded to avoid self-preference, and calibration against human-labelled examples before you trust it. An uncalibrated judge gives confident scores that look trustworthy and aren't, which the course calls worse than no automated grade.

ALEX: Then why not one judge for everything? One pipeline, one rubric, and a judge can confirm a claim number matches as well as code can.

SAM: One mechanism is easier to run, and a judge would usually get the claim number right. Usually is the problem. Code is milliseconds, almost free, and never drifts. A judge needs a rubric, a different model, and calibration against human labels before you can trust it.

ALEX: So the simplicity is borrowed.

SAM: It moves the work into calibration, to buy a probabilistic answer to a deterministic question. The tell: when the check is "matches", "contains", "present" or "within a limit", the answer is code, and an option routing it to a judge is a probabilistic fix for a deterministic need.

ALEX: Judge calls cost money, though.

SAM: Cost is a secondary constraint. Size the dataset for confidence; an undersized suite that lets a breaking change through costs far more. And favour volume over perfection: many automatically graded cases beat a handful of hand-graded ones, because they catch more regressions and run on every change. For chat systems, multi-turn evals are a separate category with their own golden dataset of full conversations, checking that context holds across turns and follow-ups don't invent details.

SAM: Pause here and answer before we go on. Choose two. A retailer's returns assistant reads an order, approves or routes the return, and drafts a reply. Which two checks should be code-based? Option A, the refund amount in the reply matches the order system. Option B, the reply's tone is empathetic and on-brand. Option C, the reply contains no order number belonging to another customer. Option D, the reply correctly captures why the customer is returning the item. Option E, escalation was the right call on an ambiguous, partly damaged item. [pause]

ALEX: A and C. A is a known-value comparison. C is the identifier scan.

SAM: Correct. B is tone, so a judge. D is about meaning, also a judge. E is a judgment on an ambiguous case, judge or even human territory. A and C are each independently true, so both and only both. [sting]

## Suite pitfalls and A/B tests

ALEX: What goes wrong once the suite exists?

SAM: Three things. A dataset built from convenient inputs rather than a representative sample; the course's composite is a contract assistant tested on ten familiar contracts that failed on non-standard obligation structures. A stale suite: the prompt changes, the golden dataset doesn't, and the suite keeps passing on behaviour the system no longer produces. The course calls that the highest-risk moment for a regression. And manual spot checks treated as a substitute, when you can only spot-check inputs you thought of.

ALEX: And if a score is low, I don't edit the grader.

SAM: Never. Fix the system, not the test data or scoring. Read the per-category breakdown, because a higher mean can hide degraded edge cases. Confirm any tuned change on a held-out set you never tuned against. And run every change through the suite: model swap, prompt revision, context strategy, retrieval configuration.

ALEX: That's offline. How do I test on live traffic?

SAM: A structured A/B test has four parts. A specific, falsifiable hypothesis naming the treatment, the primary metric, the success threshold and constraints on secondary metrics. Random assignment, consistent per user or session. One primary metric chosen before the run. And a sample size calculated from the minimum detectable effect, the baseline and the confidence you need.

ALEX: Harder with LLMs?

SAM: Outputs are probabilistic, so results are noisier and you need bigger samples than for deterministic software. And a prompt that helps typical inputs can hurt rare edge cases that become common later, say in a seasonal spike, so the test period has to resemble future traffic. In the course's worked example, a seventy percent baseline and a five-point target needs roughly fifteen hundred sessions per group, about four days at eight hundred requests a day. The habit is converting sample size into duration before you start.

ALEX: And reading the result?

SAM: Without overclaiming. Statistical significance means probably not chance; it doesn't mean the gain justifies shipping and maintaining the new version. Check secondary metrics too: a success gain that adds thirty percent to cost may not be a net win.

ALEX: What if no user can see a worse version?

SAM: Shadow testing. Send the new version a copy of live traffic, serve everyone the current version, and score the shadow outputs offline against a rubric or golden answers. You lose downstream signal, like whether the user accepted the answer. Use it when one bad output costs too much or traffic is too thin; in regulated settings it's often the only acceptable option. And the confidence you need is set by the consequence of a wrong call, not the expected effect size. A small tweak to a medical intake summarizer still needs high confidence.

SAM: Pause here and answer before we go on. A state benefits agency tests a revised prompt on its eligibility chatbot. Sixty sessions per version give task success of seventy-one percent against sixty-four. The product owner wants to ship today. Best next step? Option A, ship, because seven points is large. Option B, pre-specify the primary metric and secondary constraints, calculate sample size from baseline and minimum detectable effect, assign sessions randomly and consistently, and run to that size. Option C, move to a more capable model first. Option D, keep the test running and stop as soon as the gap reaches significance. [pause]

ALEX: I'm drawn to A. Seven points is a big gap, and a team I worked with shipped on a smaller sample than this and the gain held.

SAM: Sometimes it does hold, and that's what makes A dangerous: you remember the times it held. Sixty a side is a confirmation check, not a test. The course's composite had a six-point gain at fifty sessions that vanished within two weeks. And the stem says nothing about how sessions were assigned or whether the metric was fixed in advance.

ALEX: So B.

SAM: B. A treats noise as signal; it's the underpowered-test distractor, and it lands when a past success outranks the method. C changes a different variable and fixes nothing about the experiment. D is the subtle one: run until you see what you want and you'll find it, real or not. Underpowering, an uncontrolled input mix, and choosing the metric afterwards each invalidate a result on their own. The tell: a small session count sitting next to "ship today". [sting]

## Diagnosing failures

ALEX: Diagnosis. Where do I start?

SAM: Classify before you fix. Prompt failure: the instruction was ambiguous and the model filled the gap, so fix the prompt. Hallucination: confident content not grounded in the input, so fix it with grounding, meaning retrieval, tool use or verification; a stronger instruction won't do it. Model mismatch: wrong tier, or swapped without re-evaluation, so re-select, gated by an eval. And retrieval: the model can reason faithfully over bad context.

ALEX: Same rule as the sample items: investigate the component the trigger touched.

SAM: Yes. The course maps symptoms to suspects. Latency spikes: context grew, a tool slowed, or a cache stopped hitting, so check tokens per request, the slowest span and cache behaviour. Cost rises on flat usage: the tier crept up or caching regressed. Quality slides with no code change: a model or prompt change, or retrieval drift from a growing corpus, so compare against the eval set. Intermittent tool failures: authorization, rate limits or an unhandled error path. One trap here: disabling caching to cure "stale content". Prompt caching only hits on an exact prefix match, so it can't serve changed content; you add cost and latency and miss the cause.

ALEX: And "use a bigger model" is the evergreen distractor. I strike it on sight.

SAM: Careful, that's the rule stretched past its scope. A bigger model won't fix a drifted index, and most of the time it is the trap. But model mismatch is one of the four classes. Wrong tier, or a swap without re-evaluation, and re-selecting is the fix.

ALEX: How do I tell them apart against the clock?

SAM: Read what the stem has already cleared. Running the eval on a larger model is a fair test of a capability limit, once prompts, tools and routing check out. The tell: "use a bigger model" as a reflex is the distractor; "re-select, gated by an eval" after the other components are cleared is the answer.

ALEX: The method itself?

SAM: Record the reporter's own words. Name three hypotheses before looking. Gather the system prompts, tool descriptions and execution traces. Evidence must point at a specific line. Change one thing at a time and re-measure; if the metric doesn't move, that wasn't the fix. Run cases repeatedly, since one run proves nothing. In multi-agent systems, read the coordinator's instructions first, then follow a shared trace ID across orchestrator and subagents, because a dropped subagent can fail silently at synthesis.

SAM: Pause here and answer before we go on. A retailer's product assistant tells a customer a blender has a five-year warranty. The trace shows the right product page was retrieved, and it says two years. Best fix? Option A, add "never make up warranty terms" to the system prompt. Option B, move to the most capable tier. Option C, require each warranty claim to cite a retrieved passage and verify the term against it before replying. Option D, lower the temperature. [pause]

ALEX: Retrieval worked, so it isn't rag. The model asserted something not in its context. Hallucination, so C.

SAM: Correct. Grounding plus verification removes the failure at the root. A is the stronger-instruction trap, B the bigger-model trap, and D guarantees nothing about grounding. [sting]

## Optimization and cost

ALEX: Optimization. The demo-cost trap.

SAM: A POC runs ten to fifty requests a day and the bill is negligible. The course's post-launch composite has three compounding failures: the cost model was built at demo volume, the token distribution was assumed uniform when long documents ate eighty percent of spend, and with no fallback one overload error at peak took the workflow down. The POC proved capability and was mistaken for a cost and reliability model.

ALEX: So I model cost before choosing the architecture.

SAM: From call volume, supplied by the business owner, token budget per request split into input and output, and model tier. Model the distribution, not the average, which can understate cost two- or threefold. Design to P ninety-five under concurrent load, not a single-request median. Run sensitivity: volume doubles, the tail grows. And measure the business metric on the POC sample, because a system inside budget that doesn't move it has still failed.

ALEX: That's a lot of modelling for a bill that was negligible. The POC numbers are real data. I'd take cost per request, multiply by forecast volume, add a margin and move on.

SAM: The per-request figure is real, and multiplying it out is a fair first sketch. It fails on shape, not size. The composite assumed a uniform token distribution, and long documents ate eighty percent of spend. A margin on the average doesn't fix the wrong shape, and it says nothing about P ninety-five at peak.

ALEX: So the demo cost isn't the cost.

SAM: It's a capability result, not a cost model. The tell: an option that extrapolates from demo volume or an average token count is the trap; the answer models the full distribution at production volume.

ALEX: Which levers matter most?

SAM: Prompt caching when a long, stable prefix repeats: stable content first, volatile after. Cache writes cost more than standard input and the default lifetime is five minutes, so sparse traffic won't save consistently. Routing across tiers: cheap for routine work, stronger for hard calls. Batch API at a discount for work whose SLA allows asynchronous processing. Max tokens as a hard ceiling sized to the output; raising it only adds cost and latency. Cut needless serial round trips. Stream user-facing replies: time to first token governs perceived speed, time to completion governs duration and cost.

ALEX: The guardrail on all of it?

SAM: Gate every optimization on an accuracy check. And a cost ceiling and a latency target must both hold at once; slack on one buys nothing on the other.

SAM: Pause here and answer before we go on. Choose two. A field service dispatch assistant takes sixty thousand calls a month with a six-thousand-token system prompt that rarely changes. It's over its cost ceiling and its latency target is tight. It also generates nightly work-order summaries needed by morning. Which two changes close the gap without losing required content? Option A, put the stable system prompt first, volatile content after, and enable prompt caching. Option B, raise the max tokens cap. Option C, move every call to the most capable tier. Option D, send the nightly summaries through the Batch API. Option E, cut the system prompt in half. [pause]

ALEX: A and D.

SAM: Right. A attacks the dominant input cost and helps latency. D moves work that can wait onto discounted pricing. B raises cost and latency. C pushes cost the wrong way. E is the blunt cut that loses required content. [sting]

## Monitoring in production

ALEX: Last one. Monitoring.

SAM: An LLM system doesn't crash when it fails; it gives a subtly wrong answer. Log four things. The request: model version, input tokens, prompt identifier. The response: output tokens, latency, stop reason. The context: user role, session ID, whether caching applied. The outcome: did the downstream system accept it.

ALEX: I'd keep it leaner. Log errors, alert on the error rate, and dig in when it spikes.

SAM: Error alerts earn their place; intermittent tool failures and overload errors show up exactly there. But the failure this domain cares about throws no error. The request succeeds, the answer is subtly wrong, and the dashboard stays green.

ALEX: So a threshold never fires.

SAM: Not for model drift. Behaviour shifting on stable inputs is caught by periodic distribution comparison, not thresholds. The tell: "no errors" or "all requests succeed" in a stem that also reports worse answers points away from error-rate alerts and toward outcome logging and distribution comparison.

ALEX: And above the logs?

SAM: Layers for four questions: what is it doing, how well, when did it change, why. Request traces including tool calls. Aggregates like cost per request, P fifty and P ninety-five, task success and errors by type, decomposed per request, because aggregates can look healthy while a few requests burn the budget. Alerts, for example cost above one hundred and fifty percent of the seven-day average, or P ninety-five crossing the SLA. Then change attribution: model drift, which we just covered. Data drift is the inputs changing. A model update effect is a new version behaving differently. Different fixes for each. Pin versions and keep an update runbook.

ALEX: And the business view?

SAM: A translation layer built at design time, mapping task success to first-contact resolution and latency to handle time. Classify outputs as acceptable, needs revision or needs override, and feed that back into the evals. And from domain three: security teams treat a trustworthy audit trail as the precondition for letting agents act, so an unlogged agentic action can't be approved. Reliability controls sit in layers, retries near the API call, circuit breakers at the service boundary, fallbacks in orchestration, and the fallback gets tested in the eval suite.

SAM: Back to the opening item. Prompt revised, suite passes, handwritten forms lose incident dates, model pinned, latency flat. You said C.

ALEX: Wrong, and I see why. Incident-date extraction is a known-value check, so it belongs in code, not with a judge. And the failures cluster on one input class.

SAM: The answer is B. The trigger was a prompt change, and the suite kept passing because the golden dataset predates it and lacks the failing input class: stale and unrepresentative at once. A is ruled out by the pinned version. C fails because the check is deterministic and nothing in the stem mentions a judge. D wouldn't single out scanned forms after a prompt revision. The fix: update the dataset to the new prompt, add handwritten forms as their own category, re-run before shipping. [sting]

## Five to remember

SAM: Five to remember. One: evals before code, thresholds from the business requirement, and a stale golden dataset gives false confidence.

ALEX: Two: climb the grading ladder from the bottom. Code wherever the answer is known or binary, however high the stakes. A calibrated judge for interpretation. Humans last.

SAM: Three: hypothesis, random consistent assignment, a primary metric fixed in advance, a calculated sample size. Significant isn't the same as worth shipping, and shadow testing covers the cases where no user may see a worse version.

ALEX: Four: diagnose the component the trigger touched. Prompt failure means fix the prompt, hallucination means grounding, mismatch means re-select with an eval. A bigger model is almost never the answer.

SAM: Five: model cost at production volume on the full token distribution, lean on caching, tier routing and batch, gate every optimization on accuracy, and log enough to tell model drift from data drift from a version change.

## Recap: the exam tells

SAM: Before the tease, a test. Pause and name the main segments, or the giveaway for each. [pause]

ALEX: Evals as acceptance criteria. Metrics and the grading ladder. A/B and shadow testing. Diagnosis. Optimization and the demo-cost trap. Monitoring.

SAM: Now as exam tells. If an option writes evals after the build, or sets the bar at what the prototype scored, think acceptance criteria before code, with thresholds from the business.

ALEX: If the check is "matches", "contains", "present" or "within a limit", think code, however high the stakes.

SAM: If the suite passes but production fails on one input class after a prompt change, think a stale, unrepresentative golden dataset.

ALEX: If a small session count sits next to "ship today", think underpowered test. If no user may see a worse version, think shadow testing.

SAM: If the right passage was retrieved and the model still asserted something else, think hallucination: grounding and verification, not a stronger instruction.

ALEX: If cost is extrapolated from demo volume or an average token count, think the full distribution at production volume. If work can wait until morning, think Batch API.

SAM: And if the stem says no errors but answers got worse, think outcome logging and periodic distribution comparison, not error-rate alerts. The failure this domain cares about keeps the dashboard green.

ALEX: Next time, domain five: guardrails, human-in-the-loop, and the regulations that rule out options before you design anything.
