---
episode: 6
slug: governance
title: "Governance, Safety & Risk Management"
description: "The layered safety stack and who owns each layer, guardrail placement and fail-closed design, risk assessment, review routing by stakes, compliance as control plus owner plus evidence, and fairness you can reconstruct."
domain: "Governance, Safety & Risk Management"
weight: "14%"
target_minutes: 23
---

## In this episode

SAM: Welcome to Pass the Architect. This is episode six, Governance, Safety and Risk Management.

ALEX: What will I be able to do by the end?

SAM: Name the four layers of the safety stack and who owns each one. Place a guardrail at the right control point and decide which way it fails. Walk a system's entry points to find the risks nobody covered. Route human review by stakes instead of sending everything to a person. Turn a regulation into a control, an owner and an evidence artifact. And trace an unfair outcome back to the place it entered.

ALEX: For the exam, this is fourteen percent, about nine items. The trap it fixes is trusting the model's safety training, or a line in the system prompt, to enforce a rule only your organisation has.

SAM: Which is exactly the trap in today's opener.

ALEX: Then let's hear it. [sting]

## Cold open: regional claims access

SAM: Here's your opener. A health insurer runs a claims assistant for its adjusters. Policy says an adjuster may only see claims from their own region. In testing, Claude refused every harmful prompt the red team tried. In production, an adjuster asks, politely, for a claim from another region, and gets it. Which change closes the gap? Option A, add the regional rule to the system prompt. Option B, enforce a deterministic authorization check in the retrieval tool, keyed to the adjuster's identity as injected by the server. Option C, add an output classifier that flags claim numbers from other regions. Option D, move to a larger model with stronger safety training.

ALEX: The rule was never written down anywhere Claude could see it. So I'll say A. Tell the model the policy and it follows the policy.

SAM: Noted. Hold that thought while we work through the domain.

ALEX: What's the weight?

SAM: Fourteen percent, so roughly nine items out of sixty-three. Five task statements: implement guardrails and safety controls, identify risks and failure modes, apply human-in-the-loop validation, ensure compliance with regulations like GDPR, HIPAA and FedRAMP, and address bias, fairness and transparency. The course hangs all five on one idea: safety is a stack of controls, each with a blind spot the next one has to catch, and the architect places every control and decides what happens when it fails.

ALEX: Start with the stack, then.

SAM: Four layers, from Claude outward. Layer one is trained behaviour. Anthropic trains Claude against a published constitution, so broad classes of harmful output are already reduced on every request with no configuration at all. Its blind spot is your domain: your policy, your data rules, your authorization model. Anthropic owns it.

ALEX: And the constitution has a priority order, if I remember right.

SAM: Broadly safe, then ethical, then compliant with Anthropic's guidelines, then genuinely helpful. The weighing is holistic rather than strict, so they're balanced together, not applied as a rigid sequence. Layer two is the system prompt: role, tone and stated constraints for one request. Its blind spot is anything an adversarial or unusual input can talk Claude out of, because an instruction is not enforcement. Layer three is runtime screening of inputs and outputs. It detects disallowed content, but it doesn't authorize side-effecting actions and it misses novel attacks the classifier wasn't built for. Layer four is authorization: is this action permitted for this caller in this context? Its blind spot is content quality and fairness.

ALEX: And layers two to four belong to the architect.

SAM: All three. The vendor owns one layer out of four. That's the most testable ownership fact in the domain.

ALEX: So the classic trap is the one from the cold open.

SAM: Mistaking trained refusals for a domain policy. A team watches Claude refuse every nasty prompt and concludes it will also refuse to leak another business unit's records. But a cross-unit request looks perfectly normal in general terms, so nothing in training flags it. The rule exists in no layer. Claude can't enforce a rule it was never given. Exam phrasing to watch for: "the model's safety training already handles this." For anything partner-specific, that option loses.

ALEX: I'll push on that. A previous client ran a public chatbot for two years on Claude's refusals alone and never had an incident. Why encode something the model already refuses?

SAM: For broad harm, they were right. Knowing what training already covers lets you skip duplicate controls for things like weapons synthesis or plainly hateful content. Every layer costs latency and engineering, and layers drift apart unless someone versions and tests them together.

ALEX: So where does "Claude already refuses that" stop working?

SAM: Where the rule belongs to the organisation. That chatbot had no regional policy and no business-unit boundary. A cross-unit request looks ordinary, so there's nothing for training to refuse.

ALEX: And the tell?

SAM: If the stem names a rule only this organisation has, the option leaning on safety training loses. If it's broad harm, don't build a duplicate. [sting]

## Guardrails and control points

ALEX: Guardrails next. Where do they sit?

SAM: Three decision points, each answering a different question. Input screening runs before the model call: should this request reach the model at all? Output screening runs before the response reaches the user: is this safe to return? Tool-call authorization runs before any side effect, such as an email, a database write or a refund: may this caller do this here? A control at one point does nothing for the other two.

ALEX: I'll defend the output filter, though. Every production team I've worked with ships one as the safety net. It's the last check before the customer sees anything.

SAM: And it earns its place. For toxicity or a forbidden field in the response, output screening is the right control.

ALEX: But?

SAM: Picture the trace. The model calls the refund tool, money moves, and only then does the output filter read the text and pass it. Output screening judges words, not actions. The irreversible step happened upstream of the only control.

ALEX: So it's a net for what Claude says, not what Claude does.

SAM: That's it. The tell: if the stem has a tool with a side effect, an email, a write, a refund, find the check that runs before execution. An option that reads or flags afterwards is a detective control dressed as a fix.

ALEX: Model-based or deterministic at each point?

SAM: Match the check to whether the decision must be interpreted or proven. Open-ended intent, like jailbreak or injection patterns at input, or toxicity at output, needs a model-based classifier or judge. Crisp rules, like a banned-term blocklist, a regex, a length limit, a forbidden field or a schema check, go deterministic: faster, predictable, and it can't be argued with. Authorization is almost always deterministic, an allowlist plus identity and scope, because you need a decision you can audit and replay.

ALEX: But model-based checks get evaded.

SAM: And deterministic rules are brittle: they miss what they didn't anticipate and over-block lookalikes. So you chain them in series and say explicitly which gap each one covers. Same model-versus-code split as graders in the evaluation domain, applied to controls.

ALEX: What about injection that doesn't come from the user?

SAM: Indirect prompt injection, through retrieved documents or tool outputs, is the dominant injection vector in enterprise systems with retrieval or tools. A poisoned document arrives after input screening has already passed the request. The fix is to screen retrieved content and tool results before they're appended to the context, with the same classifier you use on user input.

ALEX: And when the screening service itself falls over?

SAM: You choose fail open or fail closed. If you don't choose, the surrounding code usually passes traffic through. A guardrail that silently fails open is worse than none, because it looks like protection and provides nothing. Default your own screens and authorization to fail closed, and log every blocked or failed gate so an incident can be reconstructed.

ALEX: Then that's my exam rule. Every control in every layer fails closed, and any option that fails open is wrong.

SAM: I'll stop you there, because that's a new rule stretched past its scope. The course spells out that fail closed applies to controls your team builds. Anthropic's built-in safety controls aren't operator-configurable and don't fail open.

ALEX: So an option that offers to make the vendor's safety layer fail closed...

SAM: Is an invented feature. The tell: check who owns the control before you judge its fail direction. Yours, fail closed and log it. Anthropic's, not yours to set.

SAM: Pause here and answer before we go on. A retail support agent answers from a product knowledge base and can issue store credit through a tool. The design today is a toxicity judge on the final response. Which two additions most directly close the largest gaps? Choose two. A, a deterministic authorization check on caller identity and credit limit before the store-credit tool runs. B, screening retrieved knowledge-base passages for embedded instructions before they enter the context. C, a sentence in the system prompt telling Claude never to issue credit above fifty dollars. D, a second toxicity judge from a different vendor on the output. E, a weekly sampled review of credit transactions. [pause]

ALEX: A for sure. And I'd take C over B. It's one line, it costs nothing, and the fifty-dollar ceiling is explicit.

SAM: Cheap, yes, and it may help on ordinary traffic. But a credit limit has to hold every time, and a sentence in the system prompt is an instruction, not enforcement. A crafted input can talk the model past it. That's the distractor family called a probabilistic fix for a deterministic need, and A already enforces the limit provably.

ALEX: Then A and B.

SAM: Correct. A puts a provable gate in front of the only side effect. B covers the dominant injection vector, which the current design ignores entirely. D doubles up the one point that's already covered. E is a detective control: useful for monitoring, but the credit has already gone out by the time anyone samples it. [sting]

## Risks and human review

ALEX: Second task statement. Risks and failure modes.

SAM: Five recurring categories. Direct prompt injection, where the user overrides instructions. Indirect injection, through retrieved content or tool outputs. Token-budget exhaustion, where oversized or padded inputs truncate work or inflate cost. Tool and action abuse, where the model is induced to call a side-effecting tool outside policy. And data exposure, where sensitive fields land in the context or the logs, a leak that has nothing to do with model behaviour.

ALEX: Mitigations, quickly.

SAM: Injection: screen every input path, not just the user's. Budget exhaustion: chunking, input limits, budget monitoring. Tool abuse: authorization before execution, independent of what the model says. Data exposure: server-side redaction before anything reaches the call or the log. Recall from the integration episode: the context window is not a data-governance boundary, so necessity decides what goes in.

ALEX: How do I find the gaps?

SAM: Walk the request and data paths through every entry point: user input, retrieved content, tool outputs, the model's own output, and the logs. Anywhere a plausible attack meets no control is a finding. And the assessment is a written deliverable. Per risk: category, affected component, likelihood and impact, and the mitigation with an owner and an evidence artifact. That's what the security reviewer signs.

ALEX: Skills count as a risk too?

SAM: As a supply-chain risk. A third-party skill can run commands or phone home the moment it's invoked, and conversation screening never sees it. Audit the bundle against its stated purpose, sandbox it with least privilege, restrict sources to a vetted registry, and record a verdict: approve, reject, or remediate.

ALEX: Third statement, human in the loop.

SAM: Treat reviewer attention as a budget. Two variables set the stakes: reversibility and the cost of a wrong decision. Confidence sits on top. It doesn't change the stakes, it estimates how likely this output is to be wrong, and it only helps if it's calibrated. The rule: route to a person when the decision is low-confidence and either irreversible or high-cost. Let confident, reversible, cheap decisions through. When the variables disagree, weight cost and reversibility more heavily.

ALEX: Then where does the human sit?

SAM: Three placements, safer to faster. Pre-action approval: nothing takes effect until a person approves, at the cost of latency and staffing. Post-action audit: it runs now and gets reviewed later, so it only suits reversible, lower-cost decisions. Sampled review: monitors the system, doesn't guard individual outcomes.

ALEX: Here's where I'd dig in. In a regulated shop I'd put a human on everything to be safe. Nobody gets fired for too much review.

SAM: There's something right in that. Pre-action approval is the safest placement, and in front of an irreversible, high-cost action it's exactly what you want.

ALEX: So why not everywhere?

SAM: Because blanket review fails twice. Volume: four hundred items a day and the reviewer starts clicking approve to keep up. Context: if all they see is the output and an approve button, even a short queue can't be judged. Give the reviewer three things: the inputs, the output, and why it was flagged. Fix only one of the two failures and review still collapses. Anthropic's own research makes the same point about agents: sign-off on every step adds friction without real safety gain, and consent fatigue sets in. Move review to higher-value checkpoints like plan approval or exceptions, and put a hard gate in front of irreversible actions.

ALEX: So "review everything" is the safe-sounding distractor.

SAM: Over-engineering with a safety badge on it. The tell: when the stem gives you a reviewer capacity and a decision volume, the answer routes by stakes, and an option that sends everything to a person has ignored the numbers.

SAM: Pause here and answer before we go on. A field-service agent schedules technician visits, which customers can rebook freely, and also orders replacement parts above five thousand dollars, which can't be returned. Reviewers can handle about forty items a day; the agent makes two thousand decisions. Which routing design fits? A, route every decision below ninety percent confidence to review. B, route low-confidence part orders to pre-action approval, sample scheduling decisions, and show reviewers the inputs, output and flag reason. C, route by confidence alone with the threshold set low enough to fit forty items. D, post-action audit of all part orders. [pause]

ALEX: B. Stakes drive routing, confidence sets the volume.

SAM: Right. A routes on confidence alone, ignores stakes, and buries the reviewers in scheduling noise. C fits the queue, but the threshold is set by queue size rather than stakes, so a doubtful, non-returnable order that scores just above it goes through with no gate. D catches the bad order after the money is spent, which is exactly the case post-action audit doesn't suit. [sting]

## Compliance obligations

ALEX: Compliance. GDPR, HIPAA, FedRAMP.

SAM: Core idea: regulations state outcomes, not implementations. So each obligation becomes three things you own: a technical control, a named owner, and an evidence artifact showing it's live. The evidence artifact is the piece most often missed and the piece the reviewer checks first.

ALEX: Make it concrete for HIPAA.

SAM: Control: protected health data goes only through a HIPAA-ready Enterprise plan or a first-party API configuration under a signed Business Associate Agreement, with HIPAA compliance enabled and only eligible features in scope. Evidence: the signed BAA, the admin setting, and the eligible-feature list. Coverage attaches to the configuration and the feature, not to the vendor relationship. Beta features are generally outside a BAA unless explicitly listed, so a signed agreement alone isn't enough.

ALEX: FedRAMP?

SAM: The workload sets the impact level, and the route must be authorized at or above it. Control: deliver only through an Anthropic-documented authorized route. Evidence: that route's authorization record and proof the workload runs only there. Claude for Government runs in a FedRAMP High authorized environment and went generally available at the end of September. The cloud government regions are the other routes. A standard commercial Enterprise plan is not a substitute. And government regions get new models after the commercial release, so confirm which model the route actually offers.

ALEX: Data residency and GDPR. Every European client I've had says the same thing: we're GDPR, so everything stays in the EU. Isn't EU-only the safe pick?

SAM: Many of them have a contract or a strict residency rule behind that, and when such a rule applies, it governs the platform choice over latency and cost. But GDPR does not by itself require EU residency; cross-border transfers are lawful with a valid transfer mechanism.

ALEX: So EU-only, on GDPR alone, is me adding a requirement.

SAM: Importing a constraint the stem never stated. The tell: look for an explicit residency rule in the stem. If all it says is GDPR, the EU-only option is answering a question nobody asked.

ALEX: And when a residency rule is stated?

SAM: The control must cover every copy: logs, caches, monitoring, retention. Defaulting to a global endpoint is the most common way a cloud-mediated deployment breaks residency. Evidence is a data-flow record of where every copy lives. One more distinction: no training on your data and data retention are separate claims. Data can be excluded from training and still be retained for abuse monitoring or audit.

ALEX: And once the compliant route is picked, we're done?

SAM: That's the Watch Out. A compliant entry point is a prerequisite, not proof. The course story: residency pinned correctly at design, then months later a logging change starts writing request metadata to a second region. No owner, no artifact watching it, so it surfaces at audit. Revalidate the register on a schedule; as the stakeholder episode will stress, regulated checkpoints fire on a calendar, not a threshold. [sting]

## Bias, fairness and transparency

ALEX: Last statement. Bias, fairness, transparency.

SAM: Fairness isn't a single model attribute; it enters at four points you control. The retrieval corpus, which can over- or under-represent groups. The prompt framing, which can encode an assumption. The few-shot examples, which can carry the corpus's skew. And downstream routing, which can send some groups down different paths. The trap is "the vendor ran bias evaluations, so fairness is handled." The vendor never saw your corpus.

ALEX: Transparency to whom?

SAM: Three audiences. An affected user needs the inputs and the reason in terms they can act on. A regulator needs a durable, queryable record showing comparable cases were treated consistently. Your build team needs the full trace: prompt, retrieved context, output and every routing step. Build decision logging once; users, regulators, engineers, reviewers and the control register all draw on it. Two catches: an aggregate accuracy dashboard can hide harm concentrated in one subgroup, so break it down. And the decision log holds personal data, so it's in scope for the compliance register itself, with minimization, retention limits and access control. Transparency and minimization govern the same log; they don't conflict.

SAM: Pause here and answer before we go on. A bank's credit-support assistant is challenged by a regulator who asks whether similar applicants were treated comparably. The team logs final recommendations only. What's the most important change? A, ask the model vendor for its latest bias evaluation. B, log inputs, retrieved context, output and routing per decision, queryable and retained under the register's rules. C, add a system prompt instruction to treat all applicants equally. D, publish the overall approval rate. [pause]

ALEX: B.

SAM: Yes. A outsources a problem that entered through the bank's own corpus. C is an instruction with no evidence behind it. D is the aggregate metric that hides subgroup harm. Only B lets anyone reconstruct a decision or rule out a source.

ALEX: Back to the claims assistant. I said A, put the rule in the system prompt.

SAM: And A is the tempting distractor. It's better than nothing, but a system prompt steers; it doesn't enforce, and a well-phrased request can get past it. The answer is B: a deterministic authorization check in the retrieval tool, using identity injected by the server rather than claimed in the user's message. It removes the risk at its root, so the forbidden record never reaches the context. C is an output filter: it judges text after retrieval already exposed the data, and it's model-dependent for a rule that must be provable. D assumes training can learn a policy it has never seen. Bigger models don't fix missing layers. [sting]

## Five to remember

ALEX: Five to remember. First: the vendor owns trained behaviour; the architect owns system prompt, screening and authorization. Any partner-specific rule lives in a layer you build.

SAM: Second: three control points, input, output, authorization, each with its own check type and a deliberate fail direction. Your own guardrails fail closed, and retrieved content gets screened too.

ALEX: Third: route review by stakes. Low confidence plus irreversible or high cost goes to a person, with inputs, output and flag reason in front of them.

SAM: Fourth: every obligation is a control, an owner and a living evidence artifact. A compliant route is the prerequisite, never the proof.

ALEX: Fifth: fairness enters at corpus, framing, examples and routing. Log each decision so it can be reconstructed, and break metrics down by subgroup.

## Recap: the exam tells

SAM: Before the recap, your turn. Pause and name the five task statements from today, and the giveaway in a stem that points to each one. [pause]

ALEX: Guardrails and safety controls, risks and failure modes, human in the loop, compliance, and bias, fairness and transparency. Giveaways: a tool with a side effect, a poisoned document, a reviewer capacity, a named regulation, and one group doing worse.

SAM: Good. Now as exam tells. If a question says the model's safety training already handles a rule only this organisation has, think of a layer you build. The vendor owns one layer out of four.

ALEX: If the stem has a tool that sends an email, writes a record or issues a refund, think authorization before execution. An option that reads or flags afterwards is a detective control.

SAM: If an option offers to make Anthropic's built-in safety fail closed, think invented feature. Your own screens fail closed; the vendor's are not yours to set.

ALEX: If the stem mentions retrieved documents or tool outputs, think indirect injection, and screen that content before it enters the context.

SAM: If it gives you a reviewer capacity and a decision volume, think route by stakes: low confidence plus irreversible or high cost goes to a person, with the inputs, the output and the flag reason.

ALEX: If it says only GDPR, no residency rule was stated. If it says HIPAA, think signed business associate agreement plus the right configuration and eligible features, and ask where the evidence artifact is.

SAM: And if it shows a healthy overall metric and a complaint from one group, think the four entry points, corpus, framing, examples and routing, plus decision logging so the case can be reconstructed.

SAM: Next time, stakeholders: discovery, trade-off conversations, SLAs and the hand-off that this control register feeds straight into.
