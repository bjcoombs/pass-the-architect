---
episode: 7
slug: stakeholders
title: "Stakeholder Communication & Lifecycle Management"
description: "Discovery that finds the hidden constraint, tradeoffs framed with reversal cost, feedback loops and SLAs that decide rather than display, documentation that survives the handoff, and the lifecycle gates between them."
domain: "Stakeholder Communication & Lifecycle Management"
weight: "14%"
target_minutes: 23
---

## In this episode

SAM: Welcome to Pass the Architect. This is episode seven, Stakeholder Communication and Lifecycle Management.

ALEX: So what do I walk away able to do?

SAM: Turn a stakeholder's vague word into a testable constraint, and spot the unknowns that block a feasibility verdict. Present a tradeoff with its reversal cost so the decision is actually informed. Build a feedback loop and an SLA that decide something rather than just display it. Write documentation a successor can act on. And name the artefact that gates each lifecycle phase.

ALEX: Fourteen percent, about nine items, and every option will sound reasonable. The trap it fixes is picking whatever feels productive in the room, like committing early or adding a dashboard, over the answer that removes the risk at its root.

SAM: Starting with a delighted sponsor who wants a date today.

ALEX: Let's hear it. [sting]

## Cold open: the go-live date

SAM: Here is your opening item. A retail chain's head of operations has just watched your prototype summarise supplier contracts. She is delighted. She asks: can you commit today to a six-week build and a go-live date? You do not yet know how many contracts arrive per day, how long the longest ones are, or how fast results must come back. What is the best next action? Option A: commit to six weeks to keep momentum, and refine scope in the first sprint. Option B: issue a provisional feasibility verdict based on the prototype, clearly labelled as provisional. Option C: before committing, gather the daily volume, the input size range and the latency requirement, then give a verdict with its constraints and write the boundary conditions into the statement of work. Option D: propose the largest model tier so there is headroom for whatever volume turns up.

ALEX: B is tempting because it sounds honest. But I think C.

SAM: Hold that. We come back to it at the end.

ALEX: So this is domain six. Fourteen percent, the same weight as governance.

SAM: About nine items on a sixty-three item paper. Five task statements: run structured discovery, communicate architectural decisions and tradeoffs, manage feedback loops and expectations including SLAs, document architectures and give implementation guidance, and support the lifecycle phases.

ALEX: These feel like soft-skills questions. Can I just pick the most reasonable-sounding answer?

SAM: Every option will sound reasonable. The right one removes the risk at its root, at the earliest point in the lifecycle. The distractors feel productive in the room: committing early, sketching early, adding a dashboard, getting a yes.

ALEX: Start with discovery.

SAM: The course calls a discovery call structured elicitation, not a conversation. Three steps: listen, translate, write down. Write before the conversation moves on, because anything unrecorded becomes an assumption the design silently inherits.

ALEX: Translate meaning what?

SAM: A stakeholder speaks in preferences. Designs are built against constraints. If someone says "we want this to feel seamless", seamless is not a requirement. It is a signal that more questions are needed. Treat any experience word that way: seamless, easy, fast, simple, intuitive.

ALEX: And the follow-up questions?

SAM: What would break that experience. What the user must never notice. What must still be true when something goes wrong. Seamless might become a p ninety-five latency target and a failure state that never exposes system internals. Testable, bounded constraints.

ALEX: The course has four buckets, right?

SAM: Must do, must not do, must cost, must prove. Must do separates what Claude owns from what stays with an existing system or a human. Must not do covers boundaries and cases that route to a human; stakeholders rarely volunteer those, so you ask. Must cost is a latency target, a per-interaction cost ceiling, a volume forecast. Must prove is the evidence obligation, far cheaper to find in discovery than in a legal review weeks later.

ALEX: And it all goes in a table.

SAM: A translation table. One row per item: the statement as said, the implied constraint, the decision it forces, and any assumption awaiting confirmation. A healthcare stakeholder saying "clinicians will review it anyway" becomes a row: a licensed human must authorise output before it reaches the record, so human authorisation is a mandatory gate, with an assumption to confirm authority and timing.

ALEX: What is the classic failure?

SAM: The call that turns into a design session. The architect hears two sentences, proposes a clean augmented pattern, and the stakeholder agrees because it sounds competent. The "quick review step" was really a licensed authorisation gate, and the dictation contained protected health information. Both surfaced in a compliance review two weeks later. A stakeholder who sees a confident sketch assumes the questions have been answered.

ALEX: And the scoping version of that is the cold open.

SAM: Yes. Scoping runs requirement to capability list, to architecture sketch, to boundary conditions, into the statement of work. A feasibility verdict has three states: feasible as scoped, feasible with constraints, not feasible. And a verdict is only sound with the constraints that make it true.

ALEX: What are the constraints you cannot skip?

SAM: Call volume, from the business owner, not a sample dataset. Input size, because whether the longest document fits in one call depends on the model tier's context window. And latency. The failure pattern: an architect answers "can Claude do this", commits a build length, and learns two weeks in about hundreds of documents a day, some hundreds of pages long, with a hard response-time limit. Capability was a necessary first check, not the last.

ALEX: Here is where I would push. Skip the questionnaire and run a quick prototype on a sample of their real contracts. Two days, and feasibility is answered with evidence instead of opinions.

SAM: A prototype is good evidence for one thing: whether Claude can do the task at all. That is the capability check, and it matters.

ALEX: But?

SAM: It is the first check, not the last. A sample shows you expected inputs. It cannot tell you daily volume, which comes from the business owner, or whether the longest document fits the context window, or whether the round trip fits the latency budget. The tell: when the stem lists what you do not yet know, volume, size, latency, the answer gathers those. An option that builds or tests something answers only the capability question.

ALEX: That "can Claude do this" check is the four properties from domain one, isn't it?

SAM: It is. Knowledge, for instance: live market data means a tool call to a live feed, and whether that round trip fits the latency budget must be tested before any verdict.

ALEX: Test me.

SAM: Pause here and answer before we go on. A public-sector benefits agency briefs you. The requirements you drafted say: caseworkers approve every eligibility decision; responses must feel instant; applicants' uploaded documents are retained for twelve months. Reviewing your notes, nobody mentioned retention. What is the best next action? A: delete the retention item, since it was not requested. B: keep it, because twelve months is standard practice. C: label it an assumption, assign an owner, and raise the retention question directly with the agency's compliance lead. D: leave it in and let the legal review catch any problem. [pause]

ALEX: Let me argue B. Twelve months is what every agency I have worked with keeps. Asking compliance makes you look new to the domain.

SAM: Your number may well be right. But nobody in this stem said it, so it is an assumption dressed as a fact. That is miss pattern five: importing a constraint the stem never stated.

ALEX: So C.

SAM: C. Retention in a citizen-data workflow is a must-prove constraint, and an assumption that traces to no statement is the most dangerous kind, because nobody remembers deciding it. A throws away a real obligation; you still need a retention rule. D moves discovery to the most expensive point in the lifecycle. The tell is "nobody mentioned": once a stem says that, the answer labels it, gives it an owner and asks. [sting]

## Communicating tradeoffs

ALEX: Second task statement. Communicating decisions and tradeoffs.

SAM: The course's line is that your job is not to resolve the tradeoff before the meeting. It is to make an informed decision possible. Every tradeoff gets three elements: what you gain, what you give up, and what reversal costs once the system is built around the choice. In regulated settings, add a fourth: what it does to compliance posture.

ALEX: Which element do people drop?

SAM: Reversal cost, and it is the one that changes the meeting, from "what is the better technical answer" to "what is the better business choice". The failure pattern: an architect recommends keeping a full policy document in context on every call. A C T O asks the per-call cost, gets an accurate answer, approves. Six weeks later the invoice shows a five-figure monthly line. The note back says: I approved a direction, not a number.

ALEX: And the context was static, so caching was sitting right there.

SAM: Domain two again: evaluate prompt caching before treating per-call cost as fixed. But the exam point is false alignment. The presentation was accurate, the room felt aligned, and the stakeholder still did not make an informed choice.

ALEX: How does the message change by audience? The exam guide talks about security, legal and executive conversations, and engineers need it too.

SAM: One method, different emphasis. Present a package: options considered, criteria, recommendation, remaining risks. Lead with the business outcome, not the architecture. For an executive, the question is what happens to the business if this is the wrong choice, so translate per-call figures into monthly cost at forecast volume and name the reversal cost. For security, state limits honestly; a security stakeholder trusts a system whose limits are clearly stated. For security and legal reviewers, bring evidence, not assertions: a signed agreement, a configuration screen, an authorisation record, a returned log query. That is the control register from domain five. For engineers, give the rejected alternatives and the tradeoff each resolved.

ALEX: I would go lighter for the executive. Every senior reader I have briefed wants one page and a recommendation. Per-call figures and reversal costs lose them.

SAM: Half right. Lead with the outcome and cut the architecture; no C F O needs chunk sizes.

ALEX: Which half is wrong?

SAM: The cost. Remember the C T O who approved a direction, not a number. What you cut for an executive is technical depth, never the monthly figure at forecast volume or the reversal cost. The tell: an option that simplifies the briefing by dropping cost or reversal is the false-alignment distractor.

ALEX: And they all need to repeat it upstairs.

SAM: The stakeholder is accepting a decision they must defend to their own leadership, so they leave with that justification in hand. For a design-choice objection, explain the tradeoff and what the alternative would have cost. If they ask "why not just use a better model?", answer with cost and quality numbers from actually testing that swap.

ALEX: Give me one on that.

SAM: Pause here and answer before we go on. Choose two. A bank's chief operating officer must approve keeping long policy documents in full context rather than building retrieval. Your draft covers the simpler design and the per-call cost. Which two additions most improve the chance of an informed decision? A: the projected monthly cost at forecast production volume, with caching evaluated. B: what it would cost to move to retrieval after the system is built around full context. C: a detailed explanation of chunk sizes and embedding choices. D: a recommendation to defer the decision until after launch. E: the latency p ninety-nine distribution from the prototype. [pause]

ALEX: A and B.

SAM: Right. A turns a per-call rate into the number the executive actually owns. B is the reversal cost, the missing third element. C is technical depth for the wrong audience. D avoids the decision and lets the system get built around it anyway. E is a real metric, but the decision in front of this executive is cost and reversibility. [sting]

## Feedback loops and SLAs

ALEX: Third task statement. Feedback loops and SLAs.

SAM: Observability gives you signals. A feedback loop decides which signals change behaviour, and whose. The course sequence: signals, triage, decide, act, review. The artefact is a governance table built before launch, mapping each signal to a trigger, an owner and an action.

ALEX: Why isn't a good alerting stack enough?

SAM: Because slow drift does not fire hard alerts. In the course trace, eval scores drift down for weeks while error rate stays flat, nothing fires, and a quarterly review finally catches what a quality-drift trigger would have caught seven weeks earlier. Every metric was collected. Nothing decided it mattered.

ALEX: And the SLA?

SAM: Three things: what is measured, what counts as a breach, what happens on a breach. Thresholds must trace to a tangible source. Latency to the user-experience expectation from discovery. Availability to how critical the deployment is. Quality to the eval acceptance criteria from domain four. A number that traces to none of those is a target someone liked.

ALEX: What expectation breaks most after launch?

SAM: Cost. Production volume routinely runs one to two orders of magnitude above the pilot. Give a consumption forecast at production volume and name the spend controls, such as caching, model tiering and budget alerts, before the first invoice.

ALEX: And regulated deployments?

SAM: Some reviews fire on a schedule, not a threshold. A periodic output audit against a documentation standard, a scheduled data-residency confirmation. They run even when every metric is green, and are wired in before launch. For triage, the test is whether a signal crosses a line someone agreed to and changes a decision they own. A budget breach goes to stakeholder review. A p ninety-nine blip inside budget stays in internal monitoring. A retry that succeeded is noise.

ALEX: Drill me.

SAM: Pause here and answer before we go on. A field-service company's repair-guidance assistant has seen its eval score fall for four straight weeks. Error rate is flat, no alert has fired, and a regional manager says answers feel weaker. What is the best next action? A: add more dashboards so the drift is easier to see. B: raise it at the next scheduled quarterly review. C: move to a larger model tier. D: diagnose whether the cause is prompt, data or model drift, add a quality-drift trigger with an owner to the governance table, and escalate to a stakeholder review once the diagnosis is confirmed. [pause]

ALEX: B. Nothing has breached. If I escalated every soft dip to stakeholders, I would be the architect who cries wolf.

SAM: That instinct is sound for noise. Triage exists so a p ninety-nine blip inside budget stays in internal monitoring. But four straight weeks of falling eval scores plus a user report is not a blip. It is the slow drift that never fires a hard alert.

ALEX: So B is real-world instinct winning, miss pattern one.

SAM: Yes. D. The signal already exists; the decision layer is missing, so you fix the loop and the cause. A is a detective control dressed as a fix. B is how this pattern burns seven weeks. C is "use a bigger model" before anyone knows whether the cause is a prompt change or stale data, and that diagnosis also decides whether you iterate or re-architect. The tell is "four straight weeks" next to "no alert has fired": the data is there, and nothing is deciding.

ALEX: So the rule is, a bigger model is always wrong.

SAM: Careful, that is miss pattern four. If someone asks "why not a better model?", the course answer is cost and quality numbers from actually testing that swap. A model change can be the right call.

ALEX: Then when does it lose?

SAM: When it comes before the diagnosis or before the volume is known. The tell is sequence: a bigger tier offered before anyone knows the cause or the load. [sting]

## Documentation for handoff

ALEX: Fourth. Documentation and implementation guidance.

SAM: One document, three readers. The inheriting engineer, who was not there. The auditor, who wants evidence that a specific control is live. The returning architect, often you, months later with no memory of the sessions. Serve only one and it is incomplete, however detailed.

ALEX: What fields?

SAM: The decision, dated. The rejected alternatives. The tradeoff it resolved. The owner. The evidence artefact. Audit-ready status. Assumptions labelled as assumptions. The completeness test: can a competent architect who was not in the room make a safe change after reading it?

ALEX: Why do rejected alternatives matter so much?

SAM: The course postmortem: a financial-services architect designs a context strategy to keep regulated data in-region, then leaves. The successor inherits a diagram with no rationale, hits a performance issue, switches strategy, and breaks the residency rule. The diagram showed what and lost why.

ALEX: In practice I write the documentation in the last sprint. Earlier drafts go stale as the design moves, and the course itself calls documentation the handoff stage.

SAM: It does, and stale drafts are a real cost. But handoff is when the document is delivered, not when the reasoning gets written. A rejected alternative is clearest the day you reject it. Rebuilt months later from email threads, by a returning architect with no memory of the sessions, the why is the first thing lost.

ALEX: So what is the tell?

SAM: Prefer the option that records the decision and its rejected alternatives when the decision is made. An option that tidies everything up at the end keeps the what and loses the why.

ALEX: So which artefact serves which reader?

SAM: Diagram, decision log and assumption register document intention and mainly serve the successor. A deployment runbook is handoff evidence. The control register with evidence links and the test-result summary are compliance evidence. The trap: a diagram feels authoritative, but a reviewer cannot accept it as proof.

ALEX: And the outcome document?

SAM: Six fields: use case with scope boundary, metric before, metric after on the same definition, the control that makes the comparison auditable, the measurement owner, and reuse potential, which the course marks as partner track. Volume, latency and error rate tell a sponsor the system runs. A before-and-after on the business metric, like claim processing time, tells a C F O what it is worth expanding. Capture the before metric at the start, or there is no story. [sting]

## Supporting the lifecycle

ALEX: Last one. Supporting the lifecycle.

SAM: Discovery, design, handoff, monitoring, iteration. Discovery and tradeoff framing do discovery and design. Documentation is handoff. The feedback loop is monitoring and iteration. The outcome document closes the loop and gates the expansion decision. Naming the phase a decision belongs to is how you judge whether a phase is ready to move on.

ALEX: What does a gate look like in practice?

SAM: An artefact per transition: the translation table to leave discovery, the feasibility verdict with boundary conditions to leave design, the decision log and control register to hand off. And from domain five: in a multi-platform design, set regions explicitly on Bedrock or Vertex, because defaulting to a global endpoint is the common pattern that breaks data residency.

ALEX: And the demo and go-to-market material?

SAM: Marked partner track, not tested by the architect exam. Skip it.

ALEX: One more drill.

SAM: Pause here and answer before we go on. Four weeks after launch, the sponsor of a claims-triage assistant asks for the outcome document today, for a C F O expansion meeting. Baseline processing time was measured before launch. What is the best next action? A: send volume, latency and error-rate figures now. B: extrapolate the after metric from the first week's data. C: name the measurement owner, confirm the reviewer-authorisation log is recording, and schedule completion at a defined post-launch milestone, telling the sponsor what the document will contain. D: tell the sponsor outcome reporting waits for the quarterly review. [pause]

ALEX: C.

SAM: Correct. The gate is not yet satisfied: the after metric needs enough runtime to measure. A answers "does it run", not "what did it change". B asserts a number without enough data behind it. D withholds the expectation-setting the sponsor needs.

ALEX: Back to the cold open. I said C, but let me argue B, since I nearly picked it. A provisional yes, clearly labelled, keeps a delighted sponsor moving, and it is honest. Stalling her is how deals die.

SAM: Momentum is real, and C is not a stall. It ends in a verdict, with its constraints written into the statement of work.

ALEX: Then why not label it and move?

SAM: Because a sponsor hears any verdict as a commitment, whatever the label says, and this one rests on a prototype that saw only expected inputs. C is right. Volume, input size and latency are inputs to the verdict. A commits before the design is possible. D is the bigger-model distractor: you cannot size headroom for a volume nobody has given you.

ALEX: And the tell for B?

SAM: "You do not yet know." When the stem lists missing constraints, any verdict before you gather them, provisional or not, is the trap. [sting]

## Five to remember

ALEX: Five to remember. I'll start: an experience word like seamless or fast is a signal to ask more questions, not a requirement. Translate it into a testable constraint and write it down with any assumption labelled.

SAM: Two: every tradeoff carries gain, give-up and reversal cost, plus compliance posture when regulated. Reversal cost is the one people drop, and dropping it produces false alignment.

ALEX: Three: monitoring is not a feedback loop. The governance table maps each signal to a trigger, an owner and an action, includes slow drift, and wires scheduled regulated checkpoints before launch.

SAM: Four: SLA thresholds trace to something real, user-experience expectation, business criticality or eval acceptance criteria, and cost is the expectation that breaks first, so forecast at production volume before the first invoice.

ALEX: Five: documentation records the decision, the rejected alternatives and the tradeoff, so someone who was not in the room can make a safe change. Reviewers want evidence artefacts, and sponsors want a before-and-after business metric.

## Recap: the exam tells

SAM: Your turn first. Pause and name the five task statements we covered, and the artefact each one leaves behind. [pause]

ALEX: Discovery leaves a translation table. Tradeoffs leave a decision package. Feedback loops and SLAs leave a governance table. Documentation leaves a decision log and a control register. And the lifecycle has an artefact gating each transition.

SAM: Close enough. Now as exam tells. If a question says seamless, fast or intuitive, think signal to ask more questions, not a requirement.

ALEX: If the stem lists what you do not yet know, volume, input size, latency, think gather those before any verdict, provisional or not. A prototype answers only the capability question.

SAM: If it says nobody mentioned something, think label it an assumption, give it an owner, and ask.

ALEX: If an executive approved a direction and the invoice surprised them, think missing reversal cost and a missing monthly figure at forecast volume. That is false alignment.

SAM: If a score drifts for weeks and no alert fires, think missing decision layer: diagnose the cause, then add a quality-drift trigger with an owner to the governance table.

ALEX: If a successor broke a rule the original architect had designed around, think rejected alternatives that were never written down.

SAM: And if a sponsor wants the outcome document before the after metric has had time to run, think name the measurement owner, confirm the log is recording, and set the milestone.

SAM: Next time, domain seven: configuring Claude Code for teams, and keeping AI-assisted developer workflows trustworthy.
