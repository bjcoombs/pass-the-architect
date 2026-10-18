---
episode: 1
slug: solution-design
title: "Solution Design & Architecture"
description: "Domain 1, seventeen percent of the exam: decomposing work across Claude, systems and humans, choosing between an augmented call, a workflow and an agent, designing multi-agent orchestration, and tying it all to business value."
domain: "Solution Design & Architecture"
weight: "17%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect. Episode one: Solution Design and Architecture.

ALEX: What should I be able to do by the end?

SAM: Name Claude's four behaviour properties and the design consequence of each, and split work between Claude, existing systems and humans. Spot a business rule that has drifted into the model. Choose between an augmented call, a workflow and an agent, and know when fine-tuning and Skills earn their place. Design a multi-agent fan-out that can't fail silently, wire an end-to-end architecture onto the right platform layer, and map value to the five pillars.

ALEX: And it's seventeen percent, ten or eleven items, where the trap is reaching for an agent, or a bigger model, before deciding what Claude should own at all.

SAM: Then let's see that trap in an item. [sting]

## Cold open: card disputes

SAM: Let's start with an item. A retail bank wants Claude to handle card dispute emails: read the message, decide whether the dispute qualifies for provisional credit under the bank's published rule on amount and account age, look up the transaction in the core banking system, and draft a reply. The team built an agent with tools for all of it, to keep things flexible. Pilot traces show every email followed one of three paths. Which change best fits the requirements?

SAM: Option A. Keep the agent and add a logging tool that records each eligibility decision for audit. Option B. Replace it with a routing workflow: Claude classifies and extracts, code calls the bank's rules engine for eligibility, a tool fetches the transaction, Claude drafts the reply, and a human approves credits above a value threshold. Option C. Move the agent to Opus with extended thinking so eligibility judgments improve. Option D. Index the transaction history in a vector store so the agent needs fewer tool calls.

ALEX: A is tempting, because audit is clearly the worry and the agent works in the pilot. But I'll commit to B. I want to hear why A is wrong, not just weaker.

SAM: We'll come back to it at the end.

ALEX: So, Domain one, Solution Design and Architecture.

SAM: Seventeen percent, the second-heaviest domain after Integration. That's ten or eleven of the sixty-three items. Six task statements: translate business problems into Claude solutions, design end-to-end architectures from input through processing and output to feedback loops, select a pattern, design multi-agent orchestration, apply decomposition, and align to business value pillars.

ALEX: A lot of ground.

SAM: One habit covers most of it. The course frames design as four decisions in order. What part of the work should Claude own? What shape is the work? Which reference architecture fits? And where does the work meet Claude: entry point, model and context? Many items test whether you made those decisions in that order.

ALEX: Start with how Claude behaves, then.

SAM: Four properties. Next-token prediction: strong on common patterns like summarising, weak on precise names, dates, citations and statistics. Knowledge: reliable on common, stable topics, shaky on rare, private or fast-changing ones, and equally confident on both. Working memory: what's in the context window exists, what's outside doesn't, and the edge is hard. Steerability: good with short, concrete, verifiable instructions, weak with abstract ones and precise numerical logic, and it can follow the letter while drifting from the intent.

ALEX: And they're forces to design around, not bugs.

SAM: Right. The course pairs each with a design consequence, and those pairs are easy marks. Non-determinism is why evaluation frameworks exist. The knowledge boundary is why retrieval and tools exist. Context as a finite resource is why context strategy is a design decision. Confidence is not correctness, which is why human-in-the-loop placement matters.

ALEX: Non-determinism, evals. Knowledge boundary, retrieval and tools. Finite context, context strategy. Confidence, human gates.

SAM: And one cautionary pattern: a demo runs cleanly five times, someone calls it deterministic, ships a reconciliation pipeline with no checks, and the same statement gets a different category in week two. Five clean runs are not evidence of determinism.

ALEX: How do I use that lens to decompose?

SAM: Every solution has three owners. Claude takes language understanding, summarisation, planning, drafting and tool-mediated action. Existing systems keep what the partner already paid to make reliable: the order service, the policy engine, the rules table, the database of record. Humans keep judgment calls, exceptions, approvals, and moments where being right matters more than being fast.

ALEX: And the question isn't "where can Claude help".

SAM: That shift is the core of the module. Ask where the four properties argue for Claude over the system that already does this right. Justify each assignment on reversibility, stakes and accountability. And remember the middle category: collaborative work, where Claude drafts and a person decides.

ALEX: Example?

SAM: A field technician assistant. Summarise case notes, report warehouse stock of a part, check warranty on a serial number, total billable time across three tickets, draft a delay email, decide whether to escalate a safety incident. Sort them.

ALEX: Summary and draft to Claude. Stock and warranty are lookups, so existing systems. Billable time is arithmetic, so code. Safety escalation goes to a human.

SAM: Clean. The misses the exam wants are tasks that read like language but are authoritative data, and consequential calls dressed as drafting. And one step can split: drafting an email is Claude's, sending it belongs to the email system, with human approval above a value threshold.

ALEX: Which brings us to deterministic drift.

SAM: Folding a rule into the model looks cleaner: one component, easier to demo. Picture an insurer whose rule sends claims above a fixed amount to a senior adjuster, enforced today by a database query. Someone has Claude extract the amount and route in one step. Months later an audit finds dozens of misroutes in thousands of claims, all with the amount buried in phrasing like "around five thousand", which the model read as a loose estimate.

ALEX: Letter of the rule, not the intent. Steerability.

SAM: Yes. And two details matter. Nobody had tests for the routing, because it was treated as something the model would handle, not a rule the business depends on. And ordinary logging that would catch a broken query records nothing about a model's choices inside a request, so an audit found it, not monitoring. The distractor is "improve the prompt to handle approximate amounts". The root fix puts the threshold back in deterministic code, with Claude only extracting. [sting]

## Choosing a pattern

ALEX: Once I know what Claude owns, I pick a shape.

SAM: Three patterns on two axes, predictability and model autonomy. The augmented LLM is one bounded call, maybe with tools, retrieval or extended thinking, and control flow never branches on the model's choices. Use it when the task is well defined and verifiable. A workflow is named steps orchestrated in your code: use it when error cost is real, observability matters and steps are knowable. An agent gets a goal and tools and picks its own path: use it only when the path genuinely can't be enumerated and an unexpected output is acceptable and recoverable.

ALEX: And the factors for choosing.

SAM: Five, walked in sequence: predictability, error cost, observability, latency budget, cost. The first one that rules a pattern out decides. Workflows win on error cost because deterministic guards sit between steps. They win on observability because steps log like code, while an agent's trajectory reads like a transcript most tooling can't alert on. Agents need worst-case latency budgets, not median. And a badly bounded agent is often the most expensive pattern.

ALEX: Though cost isn't really about the label.

SAM: Good, that's testable. Cost tracks accumulated context and call count. A poorly designed workflow can cost more than a well-designed agent, so distrust any option claiming agents always cost more.

ALEX: Then the workflow sub-patterns.

SAM: Chaining: each step consumes the last, extract then classify then summarise. Routing: a classifier, often Claude, picks the path, say billing, technical or a human queue. Parallelization: independent sub-tasks run at once and get aggregated. Evaluator-optimizer: one call drafts, another grades against a rubric or schema, looping until it passes or hits a retry limit. They combine. Start with the simplest that meets error tolerance and observability, and escalate only when production data says so.

ALEX: And the agent trap.

SAM: Teams pick agents because a task feels open-ended. Being unsure how to structure work isn't the same as steps that can't be known. The classic retrospective: traces showed four paths, knowable from week one. A router and four chains would have done it. Instead they rebuilt that structure inside the loop, minus the logging, and when compliance asked which step approved a payment, they could only point at a model turn.

ALEX: And the model version had rolled forward unvalidated.

SAM: The subtle bit. That's a model-governance gap under any pattern. Only the missing auditable step is the agent's fault. When an agent is right, bind it: constrained tools, per-turn budgets, explicit permissions, stopping criteria. Its autonomy is your liability surface, so keep the tools as narrow as the task allows.

ALEX: Where does fine-tuning fit? My instinct with flaky prompts is to fine-tune.

SAM: Usually the wrong first move. Optimize the prompt, since most reliability problems are prompt problems. Then add tools or retrieval. Then a stronger pattern like evaluator-optimizer. Only then fine-tuning, and it earns its place in three cases: very high volume where inference cost is the constraint, critical latency where a smaller specialized model wins, or a consistent format prompting hasn't delivered. Otherwise it locks you to a fixed model version. Access is also limited, so confirm with the account team first.

ALEX: And Skills.

SAM: A packaging choice beside the pattern. Prompt-only, direct tool use, or a Skill: a versioned, reusable unit of instructions and optional scripts, governed as one asset. Choose a Skill when a procedure repeats, spreads across teams or products, or needs versioning. A support team running the same reply procedure hundreds of times a day wants a Skill, not templates each agent pastes and lets drift. That's Domain two territory too, beside caching.

SAM: Pause here and answer before we go on. A field-service company extracts part numbers, fault codes and dates from technician notes. Formats vary run to run and downstream parsing breaks. Volume is moderate and latency isn't critical. An engineer proposes fine-tuning, noting that consistent format is an accepted reason. Best next step? Option A. Fine-tune now. Option B. Add an explicit output contract, then structured outputs or an evaluator-optimizer pass against the schema, and revisit fine-tuning only if format still fails. Option C. Convert the extraction into an agent that retries until parsing succeeds. Option D. Move the extraction to Opus. [pause]

ALEX: B. Format is a valid trigger, but only after prompting has failed, and nobody has tried a proper output contract.

SAM: Right. A takes a real trigger and skips the progression. C adds autonomy to fully known steps; retry-until-valid is an evaluator-optimizer, which is a workflow. D is "use a bigger model", which never touches the root cause, an underspecified output contract. [sting]

## Multi-agent systems

ALEX: Multi-agent next.

SAM: Use it when the work exceeds one context, and use the fewest agents that meet the requirement, because each one is another failure boundary to observe and govern. The orchestrator owns the goal, decomposes, delegates and synthesises, and never does sub-task work. Subagents each own a scoped piece in their own context. Design three things explicitly: how work splits, how results are structured to combine, and how conflicts or gaps get resolved.

ALEX: The common shape is fan-out.

SAM: Split a large item into independent units, one subagent each, in parallel where possible, then synthesise. Recovery is asymmetric. A subagent failure is usually recoverable: retry, re-route or flag the gap. An orchestrator failure usually isn't. So make subagent work idempotent and retryable, checkpoint orchestrator state, give it a conflict rule or escalate conflicts to a human, propagate a shared trace ID, scope each subagent's tools, and gate irreversible actions with a human while sampling low-stakes ones.

ALEX: And the silent failure.

SAM: Fifty contract sections fan out, two subagents return nothing, and the summary says "forty-eight reviewed, three flagged". It reads as complete. The fix is a coverage check at synthesis: results returned must equal units dispatched.

SAM: Pause here and answer before we go on. Choose two. A hospital network reviews a patient's records before a procedure, one subagent per document. The report reads "thirty-eight documents reviewed, no contraindications found". The file held forty. Which two changes address the root cause? Option A. A synthesis rule that results returned must equal documents dispatched, flagging any shortfall. Option B. Retry failed or empty subagent results, recording any that still fail as gaps. Option C. Upgrade the orchestrator to the most capable model. Option D. Have the orchestrator re-read every document itself. Option E. A dashboard of average subagent latency. [pause]

ALEX: A and B. A catches the count gap, B recovers at the boundary where recovery is possible.

SAM: Both right. C: a smarter orchestrator still counts only what came back. D breaks the role split and floods the context the fan-out protected. E is a detective control dressed as a fix; it shows signals but ties nothing to an action.

ALEX: That sounds like Domain six.

SAM: It is. Monitoring collects signals; a feedback loop maps each signal to a trigger, an owner and an action: Signals, Triage, Decide, Act, Review. That's the feedback stage of the blueprint's end-to-end architecture.

ALEX: Walk the whole thing end to end, then.

SAM: Input is a context-engineering choice. Stable knowledge like manuals and policy goes through retrieval. Live state like order status and balances goes through a tool call to the system of record. Retrieval doing live state's job is the most common reference-architecture mistake, and the fix isn't better embeddings or faster refresh; it's calling the service. Processing is your pattern plus model and context strategy: Sonnet by default, move only on eval evidence, progressive context for most production work. Output is a structured contract, validation, and a human gate placed by stakes and reversibility. Feedback is evals gating every model change, with the rollback threshold set before the run, plus the governance table.

ALEX: Where do reference architectures fit?

SAM: They're the wiring you shouldn't invent. Five: agent, rag, document processing with evaluator-optimizer, routing for ticket triage, and the coding agent. Adapt them as templates. Combine two only when two parts of the problem fail differently, because composition roughly doubles maintenance and each architecture needs its own eval set, which is Domain four.

ALEX: And the platform map?

SAM: It matters when an option puts a sound design on the wrong layer. Entry points are what people touch: Claude dot ai, Claude Code, a custom app. Build-time interfaces are what engineers code against: the API, SDKs, M C P, the Agent SDK. Delivery routes are where traffic lands: Anthropic, Bedrock, Vertex AI, Foundry. The entry point follows the user, so Claude Code in front of bank branch staff fails immediately. And M C P earns its place when several Claude clients reuse the same tools. [sting]

## Business value

ALEX: Last task statement, business value.

SAM: Translating the problem starts with naming each capability separately, sketching the architecture, setting boundary conditions, then scoping. Then map value to five pillars. Efficiency: the same work faster or cheaper. Transformation: work that wasn't feasible becoming possible. Productivity: more output from the same people. Solution cost: the system's own run cost. Performance SLAs: the service levels it must hold. For ROI, take a baseline from the owner's own data, project the same unit, subtract run cost from the sizing model, and give a payback period with sensitivity. The trap is projecting full automation when humans still review low-confidence cases.

SAM: Pause here and answer before we go on. A government agency gets tens of thousands of consultation responses. Staff read a ten percent sample because reading all of them is impossible with their team. With Claude themeing every response and analysts reviewing the themes, every response is now considered. Which pillar does this primarily advance? Option A. Efficiency. Option B. Productivity. Option C. Transformation. Option D. Solution cost. [pause]

ALEX: Nearly said productivity. But reading everything wasn't possible before, so C, transformation.

SAM: Correct. Efficiency would be the same sample done faster or cheaper. Productivity means more of work the team could already do. Solution cost is a line in the case, not the benefit. And analyst review time stays in the projection. [sting]

## Cold open: the verdict

ALEX: Now the cold open.

SAM: B, and every piece maps to this episode. Three observed paths mean the steps can be enumerated, so predictability, the first factor, rules out the agent. Eligibility is a published deterministic rule, so it stays in the rules engine. The transaction is live state, so a tool call. Claude reads, extracts and drafts, where the properties favour it. A human approves larger credits, where stakes and accountability sit.

ALEX: And A, my temptation?

SAM: A detective control dressed as a fix. Logging records each decision, but a probabilistic system still enforces a rule that must be right every time, and there's still no discrete auditable step. It records the risk instead of removing it. C is the bigger-model family: still right most of the time, with extended thinking adding cost and latency nobody measured a need for. D is retrieval standing in for live state; a transaction index is a snapshot. [sting]

## Five to remember

ALEX: Five to remember. One: decompose before choosing a pattern, Claude, systems or humans, and ask where the four properties argue for Claude over what already works.

SAM: Two: a rule that must be right every time stays in deterministic code. The model extracts, the rules engine decides.

ALEX: Three: walk predictability, error cost, observability, latency, cost in order, and the first to rule out a pattern decides. Agents only when the steps truly can't be enumerated, and always bounded.

SAM: Four: subagent failures are recoverable, orchestrator failures usually aren't. Retry and flag at the boundary, and reconcile coverage at synthesis.

ALEX: Five: prompt, then tools or retrieval, then a stronger pattern, then fine-tuning. Package repeated procedures as Skills, and map every value claim to a pillar.

## Recap: the exam tells

SAM: Before the tease, your turn. Pause and name the main segments of this episode, or the giveaway for each. [pause]

ALEX: The four behaviour properties. Decomposing work across Claude, systems and humans. Deterministic drift. Choosing a pattern. Fine-tuning and Skills. Multi-agent fan-out. The end-to-end architecture and platform map. And business value.

SAM: Now as exam tells. If an option treats five clean demo runs as proof of determinism, think non-determinism, which is why evals exist.

ALEX: If a task reads like language but is really a lookup, arithmetic or a safety call, think existing system, code or human, not Claude.

SAM: If a rule must be right every time and the model is applying it, think deterministic code, with Claude only extracting.

ALEX: If pilot traces show a few known paths, think workflow, and read "agent" as the trap.

SAM: If fine-tuning comes before anyone tried an output contract, think prompt first. If a procedure repeats across teams and needs versioning, think Skill.

ALEX: If a fan-out summary reads complete but fewer results came back than units went out, think coverage check at synthesis.

SAM: If live state is served from an index, think a tool call to the system of record. If Claude Code sits in front of branch staff, think wrong entry point.

ALEX: And if work that wasn't possible before becomes possible, think transformation, not productivity.

SAM: Next time, Domain two: model selection, system prompts, and why a cache that never hits usually comes down to what you put first.
