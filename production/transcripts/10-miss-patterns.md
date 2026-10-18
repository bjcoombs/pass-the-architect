---
episode: 10
slug: miss-patterns
title: "Your Five Miss Patterns"
description: "A bonus episode on the five answering habits that cost marks at Foundations, with a one-line self-check and a trap-built drill for each, the guide's thesis, and a pacing plan for the Pearson VUE interface."
domain: "All domains"
weight: "100%"
target_minutes: 20
---

## In this episode

SAM: Welcome to Pass the Architect. This one is Your Five Miss Patterns.

ALEX: What's the payoff?

SAM: By the end you'll be able to catch yourself in each of the five habits that cost marks: trusting real-world instinct over the answer key, accepting an option with one wrong clause, misreading what the stem asks, stretching a rule past its scope, and importing a constraint the stem never stated. You'll have a one-line self-check for each, a three-word filter for every option, and a pacing plan for the exam interface.

ALEX: And this is where the marks are. They go on habits, not on missing knowledge, so fixing a habit is worth more than any new fact.

SAM: And Alex walks into every trap first, on purpose.

ALEX: Thanks for that. Let's begin. [sting]

## Pattern one: real-world instinct

SAM: This one is for you specifically. Foundations was lost by four or five answers. Not by a missing domain, not by a gap in understanding. Four or five items where you knew the material and still picked the wrong option.

ALEX: How close was it?

SAM: Six hundred and sixty-one against a pass mark of seven hundred and twenty, after one evening of flashcards. The principles were there. The misses came when a principle was tested as an applied scenario, the "formatting keeps drifting, what do you change" kind of item.

ALEX: So the marks went somewhere other than knowledge.

SAM: They went to habits. Five of them, and they are consistent enough to name. Each gets a segment: what it looks like, why it pulls, a one-line self-check to run in the exam, and a drill built to trigger that exact habit.

ALEX: And I fall for each trap first.

SAM: You do. That is the point. A trap you have felt is easier to spot on Tuesday than one you have only heard described.

SAM: Pattern one. Your real-world instinct overrides the guide's answer. You read the options, one of them is what you would actually ship on a Friday afternoon, and you pick it.

ALEX: Because it is defensible. I have done it, it worked.

SAM: That is why it is tempting. Your experience is real, but the exam marks against the course's model of a good architect, and that model is often stricter than a busy team. The self-check: would the answer key pick this, or would my last team?

SAM: Pause here and answer before we go on. A field-service scheduling assistant passed its pilot and goes to production in three weeks. The tech lead says retries and fallbacks can wait until the first incident shows where they are needed, and building them now is gold-plating.

SAM: What should the architect do? Option A, agree, launch lean and add reliability controls once incidents show where they belong. Option B, build exponential-backoff retries, a fallback chain and a circuit breaker into the initial design, each at its own layer. Option C, add a status page and on-call alerting so outages are spotted quickly. Option D, move to a more capable model tier to reduce failures. [pause]

ALEX: A. Ship it, learn from production, don't build for problems you haven't had.

SAM: That is pattern one, word for word. The course says the opposite: retries, fallbacks and circuit breakers are much harder to add to a system not designed for them, so build them in from the start. Without them the primary endpoint is a single point of failure, and at peak load the whole workflow goes down instead of degrading.

ALEX: And the layers?

SAM: Retries close to the API call, circuit breakers at the service boundary, fallback chains in the orchestration layer. C is a detective control: it tells you faster that you are down. D is scale instead of structure: a bigger model does nothing for a rate limit or an outage. The answer is B. [sting]

## Pattern two: one wrong clause

SAM: Pattern two. You accept an option with one correct clause and one wrong clause. The first half matches what you were looking for, you feel recognition, and you stop reading.

ALEX: Recognition feels like being right.

SAM: And the exam writers know it. On choose-two items especially, an option is only true if every clause in it is true for this scenario. The self-check: is every clause of this option true here, read to the last word?

SAM: Pause here and answer before we go on. A public-sector benefits assistant sends the same long policy system prompt on every request. Requests arrive every few seconds through the working day, and the monthly cost is about to breach its ceiling.

SAM: Choose two. Which belong in the plan? Option A, mark the stable policy prefix for caching, and put the current date and time at the top of the system prompt so answers stay current. Option B, place the stable policy first and the user's message after it, and enable prompt caching on that prefix. Option C, enable caching and budget every request, including the first, at the cache read rate. Option D, project cost at production volume using the cache read rate for cached tokens plus the higher write cost on first use, then compare it to the ceiling. Option E, switch to the smallest model tier to cut cost, and build the eval set later. [pause]

ALEX: A and B. Caching is the lever, and both of them say cache the policy.

SAM: You stopped reading A halfway. A timestamp at the top changes the prefix on every call, so the cache never hits. That second clause kills the first. The answer is B and D.

ALEX: C sounds close to D.

SAM: Same trick. Enabling caching is right; budgeting the first request at the read rate is wrong, because cache writes cost more than standard input. E pairs a possible move with a forbidden one: you change model tier on eval evidence, never before the eval exists. One more detail in the stem: a request every few seconds sits well inside the default five-minute cache lifetime, so caching will actually pay. [sting]

## Pattern three: misreading the stem

SAM: Pattern three. You misread the stem. Two variants: a NOT or EXCEPT question answered as if it asked for the true option, and "first step" answered as if it said "most effective".

ALEX: Because by the time I reach the options, I have already decided what the question is.

SAM: You have decided what a typical question would be. The self-check: reread the last line of the stem, and say what it asks: NOT, first, or most?

SAM: Pause here and answer before we go on. A bank wants to validate a new prompt version for its statement-summary feature. Which of the following is NOT a reason to prefer shadow testing over a live A B split? Option A, a single bad output carries too much risk. Option B, traffic is too low to power a live split before the change is needed. Option C, regulation may not allow customers to see an unvalidated change. Option D, the team needs real downstream user behaviour to score the change. [pause]

ALEX: A. Too much risk per output is the textbook reason for shadow testing.

SAM: It is, which is why it is wrong here. The question says NOT. A, B and C are all reasons the course gives for shadow testing. D is the cost of shadow testing: no user sees the shadow output, so scoring relies on an offline rubric or golden answers. The answer is D.

SAM: Now a pair. Same scenario, two questions. Pause here and answer before we go on. A benefits triage system has a healthy overall accuracy dashboard. An advocacy group reports that applicants from one region go to manual review far more often. There is no per-region breakdown and no decision-level log.

SAM: What is the first step? Option A, rebalance the retrieval corpus. Option B, add a system-prompt instruction to treat every region equally. Option C, break the outcome down by region and add decision-level logging, capturing inputs, retrieved context, output and routing, to find which entry point introduced the skew. Option D, request the model provider's bias evaluation results. [pause]

ALEX: A. A skewed corpus is the classic cause, so fix it.

SAM: That answers "most effective", and it guesses. Unequal outcomes can enter at four points: the corpus, the prompt framing, the few-shot examples and the downstream routing. With no breakdown and no log, you cannot say which. First you instrument, so C. B is a probabilistic fix for a deterministic need. D treats fairness as the vendor's problem, which the course calls out by name.

SAM: Second question. The logs now show a routing rule sends any application with a non-standard address format to manual review, and that format is common in the affected region. What is the most effective fix? Option A, change the routing rule at its source and recheck the per-region breakdown. Option B, add a second reviewer for every manual-review case from that region. Option C, a more capable model that parses addresses better. Option D, a prompt line telling the model to ignore address format. [pause]

ALEX: A. The rule is the cause, fix the rule.

SAM: Right. B is a compensating control that leaves the skew in place. C and D blame the model, and the model is not the component that did this; the routing is. Notice the same scenario had different right answers for "first" and "most effective". That is the whole pattern. [sting]

## Pattern four: rules beyond scope

SAM: Pattern four. You learn a rule and then apply it beyond its scope. At Foundations it was "retrying is always wrong". The real rule was narrower.

ALEX: Retrying is wrong when the same input will fail the same way.

SAM: Exactly. A permission denial, a business-rule rejection, a malformed request: retrying unchanged just repeats the failure. A transient error is different. Rules this series has given you have the same risk: "bigger model is a distractor" holds when nothing points at model capability, not when an eval says the default tier misses the bar. The self-check: does the reason behind this rule apply to this case?

SAM: Pause here and answer before we go on. A retail order-tracking assistant gets intermittent rate-limit errors, four twenty-nines, at peak hours. Requests are otherwise well formed and succeed off-peak. What should the design do? Option A, never retry; return the error to the user immediately and log it. Option B, retry with exponentially longer delays, a cap on attempts and total wait, and a fallback to another model tier or a cached response once retries run out. Option C, retry immediately in a loop until the call succeeds. Option D, move every request to the most capable model. [pause]

ALEX: A. I have it drilled in: retrying is the trap.

SAM: That is pattern four. A rate limit at peak is transient, the textbook case for exponential backoff. The longer delays stop a flood of retries from turning a short hiccup into an outage, and the cap reflects how much delay the use case can tolerate. C is the flood the backoff exists to prevent. D is scale instead of structure. A sounds principled and fails users who would have succeeded seconds later. The answer is B. [sting]

## Pattern five: imported constraints

SAM: Pattern five. You import constraints the stem never stated. Compliance, residency, a manager who might need access one day. The option that satisfies your invented constraint starts to look best.

ALEX: Because in real enterprises those constraints are nearly always there.

SAM: In real enterprises, yes. On the exam, if a constraint matters, the stem states it. The self-check: can I point to the words in the stem that make this matter?

SAM: Pause here and answer before we go on. A retailer is building an internal assistant that answers store staff questions about the returns policy. The brief says the policy changes monthly and the team wants new model features as soon as they ship. Nothing else is specified.

SAM: Choose two. Option A, build on the direct Anthropic API. Option B, route through a cloud provider in a fixed region, because company data must stay in-region. Option C, keep the policy as a versioned document retrieved at call time, so a monthly change needs no prompt rewrite. Option D, send every answer to human review before staff see it, because retail AI output is regulated. Option E, sign a business associate agreement before launch. [pause]

ALEX: C, and B. A retailer that size will have residency rules.

SAM: Find the words. The brief never mentions residency. The course treats the direct API as the default, newest features first, unless a procurement or residency rule points elsewhere, and here none does. D invents a regulation and a review burden. E imports HIPAA into a returns policy. The answer is A and C.

ALEX: And C earns its place from the words "changes monthly".

SAM: Exactly the test. C has words in the stem behind it; B has only your memory of other clients behind it. If the stem had said "data must stay in the E U", B would be in contention and A would need checking. It did not, so B is a distractor, however sensible it sounds. [sting]

## Thesis, interface and pacing

SAM: All five patterns break against one sentence, the thesis behind every answer key: fix the root cause with the smallest mechanism that guarantees the outcome.

ALEX: Root cause, smallest, guarantees.

SAM: Each word answers a pattern. "Root cause" beats your real-world workaround. "Smallest" kills the option that bolts on an invented constraint. "Guarantees" rules out the instruction that only usually works. Read an option against all three words before you commit.

ALEX: So the thesis is a filter, not a slogan.

SAM: Yes. And five distractor types each fail one of those words. Probabilistic fix for a deterministic need: a system-prompt line saying "never refund over five hundred" where a tool-call authorization check belongs.

ALEX: Over-engineering: an M C P server for a tool that only one product will ever call.

SAM: Blaming the wrong layer: cache hits collapse after someone adds a date to the system prompt, and the option blames the model tier.

ALEX: Invented features: an option that turns on a setting or parameter that does not exist, like a "guaranteed accuracy" mode. If you have never heard of it in the course, distrust it.

SAM: Scale instead of structure: a bigger model or a bigger context window for a skewed corpus or an underspecified prompt. Then the interface, which you saw at Foundations on Pearson VUE. Expect the same layout on Tuesday.

ALEX: Two columns.

SAM: The left column holds the scenario frame. It rarely changes, so at Foundations you stopped reading it, and that probably cost marks. Whenever it changes, reread it in full before the question. The constraint you need is often on the left.

ALEX: Right column is the question and options.

SAM: Left-click selects. Right-click strikes an option out, so use it: every option you eliminate, strike it. On choose-two items that leaves a visible short list, and you judge each survivor clause by clause. There is a separate flag control.

ALEX: And Review?

SAM: Bottom left. It lists every item, keeps your answers, and jumps to flagged or unanswered ones. Always choose an answer before you flag. A blank never scores.

ALEX: Pacing. I felt short of time and used every minute.

SAM: Then fix checkpoints in advance. Sixty-three items, and you keep the last ten minutes for flags, so one minute forty-five an item. Item twenty-one by thirty-seven minutes. Item forty-two by seventy-three. Item sixty-three by a hundred and ten. If you hide the clock in the top right, show it at each checkpoint, and if you are behind, take your best answer and flag rather than grinding.

ALEX: And the late slump.

SAM: Your concentration dipped late last time. Eat a proper breakfast before nine, and bring water. Items fifty to sixty-three count as much as the first ten, and those are where pattern two and pattern three hit hardest. [sting]

## The five checks

ALEX: Give me the five checks, tight.

SAM: One: would the answer key pick this, or my last team?

ALEX: Two: is every clause true here, read to the last word?

SAM: Three: reread the last line. NOT, first, or most?

ALEX: Four: does the reason behind this rule apply to this case?

SAM: Five: can I point to the words in the stem that make this matter?

ALEX: And over all of them, root cause, smallest mechanism, guaranteed outcome.

## Recap: the exam tells

SAM: Before the last word, pause and name the five patterns without looking back, and the drill that caught Alex on each. [pause]

ALEX: Instinct over the key, the launch-lean reliability item. One wrong clause, the timestamp in the caching option. Misreading the stem, the NOT question and the first-versus-most pair. A rule past its scope, never retrying a rate limit. And an imported constraint, residency for a returns assistant.

SAM: Now as exam tells. If an option is what a busy team would ship on a Friday afternoon, like adding retries after the first incident, ask what the course says to build in from the start.

ALEX: If the first half of an option matches what you wanted, read to the last word. A timestamp at the top of a cached prefix kills the whole option.

SAM: If the last line says NOT, first, or most, answer that question. First, with no breakdown and no log, means instrument before you fix.

ALEX: If you feel a rule firing, like retrying is the trap, ask whether its reason applies. A transient rate limit at peak is the textbook case for backoff.

SAM: If an option protects you from residency, a regulation or HIPAA, find the words in the stem. No words, no constraint.

ALEX: If an option is an instruction where a guarantee is needed, or a setting you never met in the course, the thesis rules it out: root cause, smallest, guarantees.

SAM: And on the interface, if the left column changes, reread it, strike out what you eliminate, and answer before you flag.

SAM: Four or five answers. You already know enough to get them. Run the checks, and they are yours.
