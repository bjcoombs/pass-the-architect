---
episode: "F03"
series: "CCAR-F retake"
slug: hooks-sessions
title: "Hooks, sessions and escalation"
description: "Agent SDK hooks that block, redirect and normalise; when to resume, fork or start fresh with a summary; and the escalation triggers the exam trusts versus the ones it calls unreliable."
domain: "Agentic Architecture & Orchestration; Context Management & Reliability"
weight: "27% and 15%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode seven: hooks, sessions and escalation.

ALEX: What will I be able to do by the end?

SAM: Pick where a hook belongs: before the tool call to block it, or after to clean up the result. Make a block send the agent somewhere useful. Tell a rule a hook can check from a judgement that belongs in the prompt. Choose between resuming a session, forking it, or starting fresh with a summary. And name the three escalation triggers the exam trusts, the two it calls unreliable, and what to do when a lookup returns three matching customers.

ALEX: For the exam that spans two domains, twenty-seven and fifteen percent, and resuming with targeted re-analysis is one I scored only sixty-seven percent on.

SAM: First, an item. [sting]

## Cold open: the refund limit

SAM: Customer support scenario. Policy says refunds above five hundred dollars need a human. The team added a PostToolUse hook on process refund: whenever a refund over five hundred goes through, it posts an alert to the finance channel. Over-limit refunds are still reaching customers. What should change? Option A, keep the hook and add an automatic reversal when the alert fires. Option B, replace it with a hook that intercepts the process refund call before it runs, blocks any amount over five hundred, and tells the agent to hand the case to escalate to human. Option C, add the limit to the system prompt in capitals with two few-shot examples. Option D, intercept the call before it runs and block over-limit amounts with a generic "operation not permitted" error.

ALEX: A. The alert already exists, reversal closes the loop, and finance keeps visibility. Minimum change.

SAM: Noted. It comes back at the end.

ALEX: What are we covering?

SAM: Three task statements. One point five, Agent SDK hooks: intercepting tool calls and tool results. One point seven, session state: resuming, forking, and starting fresh. Five point two, escalation and ambiguity. The first two sit in Agentic Architecture, twenty-seven percent of the exam. Five point two sits in Context Management and Reliability, fifteen percent. All three show up most in the customer support and code generation scenarios.

ALEX: You said I scored full marks on hooks for business rules.

SAM: You did, so we skip "hooks are deterministic, prompts are probabilistic". Today is the edges: where in the call the hook sits, what it does after it blocks, what it does to results, and when a hook is the wrong tool.

SAM: Segment one. There are two places to intercept. Before the call goes out, a hook sees the tool name and the arguments, and can stop the call. After the call returns, a PostToolUse hook sees the result and can transform it before the model reads it. The guide gives one job to each. Blocking a policy-violating action, such as a refund over five hundred dollars, is outgoing-call interception. Normalising data formats is PostToolUse.

ALEX: So the hook in the cold open was in the wrong place.

SAM: The tell is in the timing. A PostToolUse hook fires after the tool ran. The money has moved. An alert after the fact is a detective control: it tells you a breach happened. The guide's bullet says intercept outgoing tool calls to enforce compliance.

ALEX: Second edge?

SAM: What happens after the block. The guide's skill bullet has two verbs: block the policy-violating action and redirect to an alternative workflow, such as human escalation. A bare block leaves the agent with a refusal and no path. It may retry, rephrase the amount, or tell the customer it cannot help. The block should return a reason the agent can act on: this exceeds the refund limit, escalate to a human with a summary. The rule holds in code, and the customer still reaches someone who can approve it.

ALEX: Let me argue for the prompt anyway. In my experience a well-written instruction with examples holds ninety-nine times in a hundred. A hook is another moving part.

SAM: Ninety-nine in a hundred is real, and for most behaviour it is enough. The guide's line is "when business rules require guaranteed compliance". Money, identity, legal exposure: one in a hundred is a breach, not a rounding error. A prompt also does nothing against text inside a ticket that tries to talk the agent past the limit. The tell is any word like "must", "never", "guaranteed", or a dollar threshold tied to a policy.

SAM: Third edge, results. Your agent reads customer records from get customer with Unix timestamps, orders from lookup order with ISO eight six oh one dates, and shipment status from a carrier's M C P server as numeric codes: one, two, three. The agent tells a customer their order is "status two" and misreads a delivery date.

ALEX: I'd fix it at the source. Change our own tools to return readable dates and labels. For the carrier, wrap it.

SAM: For tools you own, fixing the source is sound engineering, and I'd do it on a real team. But read the stem. When it says some tools are third-party M C P servers you cannot modify, or stresses many tools with different formats, the guide's answer is one PostToolUse hook that converts every result into one format before the model processes it. One place, deterministic, covers servers you do not control. Wrappers per tool spread the same logic across many places.

ALEX: What about a normalise tool the agent calls after each lookup?

SAM: Then normalisation depends on the agent remembering to call it, which is the probabilistic failure you were trying to remove. Same for documenting every format in the system prompt: the model still interprets raw values, and that is what is failing. The tell for PostToolUse is "before the agent processes them" or "heterogeneous formats from different tools".

ALEX: So the rule is: business logic goes in hooks.

SAM: Careful. That's the over-reach. Tone, empathy, how to phrase a refusal, when a case feels like a policy gap: those are judgement, and they belong in the prompt with examples. A hook needs a condition code can check: an amount, a tool name, a missing verified ID, a field format. If you cannot write the check as an if statement, it is not a hook.

SAM: Pause here and answer before we go on. Customer support scenario. Choose two. Which two requirements should be enforced with Agent SDK hooks rather than system prompt instructions? A, refunds above five hundred dollars must never be issued without human approval. B, the agent should acknowledge frustration before proposing a fix. C, order dates from a third-party M C P server, which arrive as Unix timestamps, must reach the agent in the same format as dates from your own tools. D, the agent should escalate when policy does not cover the customer's request. E, replies should stay under a hundred and fifty words. [pause]

SAM: A and C. A is outgoing-call interception with a checkable threshold and a financial consequence. C is the PostToolUse normalisation case, and "third-party" means you cannot fix it at the source. B is tone: prompt guidance. D is a judgement about policy coverage, which code cannot check; it belongs in escalation criteria with few-shot examples, which is segment three. E is style, and a length limit is not a guarantee the business needs.

ALEX: I'd have been tempted by D. Escalation sounds like a business rule.

SAM: It is, but the trigger is a judgement. The hook can enforce the dollar limit and route to escalation. Deciding that policy is silent is the agent's job, guided by criteria. [sting]

## Segment two: sessions

SAM: Segment two, sessions. Three moves. Resume: continue a prior conversation with its context. In Claude Code, dash dash resume with a session name picks up a named investigation across work sessions. Fork: the guide calls it fork underscore session. It creates an independent branch from a shared analysis baseline, so two approaches can be explored from the same starting point without disturbing each other. Fresh with a summary: a new session seeded with a structured summary of what is still true.

ALEX: You've flagged this one. I scored sixty-seven percent on resuming with targeted re-analysis.

SAM: Then let's get the decision rule exact. The guide's skill bullet: resume when prior context is mostly valid; start fresh with an injected summary when prior tool results are stale. And when you resume after code changes, tell the agent which files changed so it re-analyses those, rather than re-exploring everything.

ALEX: Why tell it at all? It can read the files.

SAM: Because its earlier tool results are still in the conversation, and it has no reason to doubt them. It will reason from yesterday's file contents as if they were current. Naming the changed files turns stale results into a short, targeted job.

ALEX: Then I'll argue the other side. Stale context is dangerous, so always start fresh. Clean slate, no risk.

SAM: That over-applies a good instinct. A fresh session throws away analysis that is still valid and pays to rebuild it. The guide rewards the cheapest move that keeps the agent correct. If three of twelve files changed, resume and name the three. If the ground has moved under most of the findings, a branch rebased onto a rewrite, a dependency upgrade that changed most call sites, then the old tool results are mostly wrong, and a summary of the conclusions that still hold is more reliable than a transcript full of outdated reads.

ALEX: And in customer support?

SAM: Same logic. A customer returns the next day. Yesterday's order status and refund state may have changed. Start a new session with a structured summary of the case, customer ID, order, what was promised, and make fresh tool calls, rather than resuming a transcript whose lookups are a day old.

SAM: Pause here and answer before we go on. Code generation scenario. A developer spent an hour in Claude Code mapping a payments module: dependencies, test gaps, risky functions. Now the team wants to compare two testing strategies, contract tests at the service boundary versus property-based tests on the core calculations, and pick one. What should the developer do? A, start two new sessions, one per strategy, and have each map the module again so neither is biased by the other. B, use fork underscore session to create two branches from the existing analysis and explore one strategy in each. C, try the first strategy in the current session, revert the files, then try the second in the same session. D, ask the current session to describe both strategies and recommend one without writing any tests. [pause]

SAM: B. "Compare two approaches" plus "from the existing analysis" is the guide's own fork case: independent branches from a shared baseline. A repeats an hour of work, and two separate mappings may not even agree, so the comparison is not like for like. C runs both in one context, so the second attempt carries the first one's reasoning and failures. D compares descriptions, not results.

ALEX: I'd have argued for A. Independence matters when you compare.

SAM: Forks are independent once they branch. That is the point of them. Independence of the baseline is a constraint the stem never asked for: miss pattern five. It asked for two strategies from one analysis.

SAM: Pause here and answer before we go on. Code generation scenario. Two weeks ago a developer ran a named Claude Code session that analysed an authentication service and recorded findings about session handling and token refresh. Since then another team replaced the token library and rewrote most of the service's files. The developer wants to continue the investigation. What is the most reliable approach? A, resume the named session with dash dash resume and list the files that changed so it re-analyses them. B, resume the named session and ask it to carry on. C, start a new session seeded with a structured summary of the earlier findings that still apply, and have it read the current code. D, fork the old session so the original stays intact while the fork re-analyses. [pause]

ALEX: A. That's the rule we just learned: resume, name the changed files, targeted re-analysis.

SAM: That's the miss I wanted to hear. Miss pattern four: a rule applied past its scope. Targeted re-analysis is right when the prior context is mostly valid. Here "most of the files" changed and the library underneath was replaced. Nearly every earlier tool result is stale, so the answer is C: fresh session, structured summary, current reads. B is worse than A: it does not even flag the change. D keeps every stale result in the fork, so it does not fix the problem.

ALEX: So the tell is the proportion.

SAM: "A few files changed" points to resume and name them. "Most files rewritten", "weeks later", "underlying library replaced" points to fresh with a summary. Read the size of the change before you pick the move. [sting]

## Segment three: escalation

SAM: Segment three, escalation. The guide names three triggers. One, the customer explicitly asks for a human. Two, a policy exception or a policy gap: the guide says "not just complex cases". Three, the agent cannot make meaningful progress.

ALEX: Take the first. The scenario target is eighty percent first-contact resolution. If a customer says "get me a person" over a simple address change, I'd offer to fix it first. It takes thirty seconds and protects the metric.

SAM: Some study material even says "offer a choice". The guide is plainer: honour explicit requests for a human immediately, without first attempting investigation. The metric is first-contact resolution while knowing when to escalate, and an explicit request is the clearest signal there is.

ALEX: Then where does "offer to resolve" come from?

SAM: A different case. The customer is frustrated but has not asked for a human, and the issue is within the agent's capability. Then acknowledge the frustration, offer the resolution, and escalate only if the customer reiterates that they want a person. The tell is the verb. "I want to speak to someone" is a request. "This is the third time I've written about this" is frustration.

ALEX: Sentiment, then. My last contact centre auto-routed angry customers to senior staff, and complaints dropped.

SAM: As a service policy, that may well work, and sentiment is useful for quality review. But the guide calls sentiment-based escalation an unreliable proxy for case complexity. An angry customer with a damaged item and photo evidence is a simple case. A calm customer asking for something policy never anticipated is a hard one. Self-reported confidence fails the same way: the model is often confident on exactly the cases it gets wrong, which is why it handles them alone. The tell: any option that escalates on a score the model or a classifier produces about feelings or certainty.

ALEX: Policy gaps. Give me one that isn't the price-match example.

SAM: Delivery policy refunds the shipping fee when an order arrives late. A customer says the late parcel made them miss an event and asks for compensation for the tickets. Policy says nothing about losses beyond the order. The agent should not refuse as if policy forbade it, and should not invent a payout by stretching the shipping rule. Policy is silent, so escalate with a structured summary: customer ID, order, what was asked, which policy applies and where it stops. That handoff format is from task statement one point four, because the human may not see the transcript.

ALEX: And "cannot make progress"?

SAM: The agent has tried the tools and the case is no closer to resolution: a lookup keeps failing, or the information needed is not in any system it can reach. Judge progress, not a count of turns.

SAM: How do you get the agent to apply this? The guide's skill bullet: explicit escalation criteria in the system prompt, with few-shot examples showing when to escalate and when to resolve autonomously. That's the proportionate first move before classifiers or extra infrastructure.

SAM: Last piece, ambiguity. get customer searches by name and returns three matches. The guide's answer: ask the customer for an additional identifier. Do not pick by heuristic.

SAM: Pause here and answer before we go on. Customer support scenario. A customer gives the name Jordan Lee and asks to cancel an order. get customer returns three Jordan Lee accounts. The agent picks the one with an open order, and audits show it sometimes cancels the wrong customer's order. What is the best fix? A, instruct the agent to ask for another identifier, such as the email or order number, whenever get customer returns more than one match, before taking any account action. B, change get customer to return only the highest-ranked match. C, proceed with the most likely account and state the account's email in the reply so the customer can correct it. D, have the agent rate its confidence in the match and ask only when confidence falls below seven. [pause]

SAM: A. The customer knows who they are; one extra turn removes the guess. B hides the ambiguity inside the tool, so the wrong account arrives looking certain. D is self-reported confidence again. C is the one to watch.

ALEX: C was mine. It confirms with the customer.

SAM: Half of it. Showing the email is a sensible confirmation step. But it acts first: the cancellation may already be done when the customer reads the reply. One right clause and one wrong clause: miss pattern two. Every clause in the option has to be true.

SAM: Pause here and answer before we go on. Customer support scenario. Choose two. Which two situations should trigger escalation to a human? A, a customer writes "I want to talk to a real person" about a duplicate charge the agent could refund in one step. B, sentiment analysis scores the customer's last three messages as strongly negative. C, a customer asks to transfer a loyalty balance to a family member's account, and the loyalty policy covers earning and redeeming points but says nothing about transfers. D, the agent rates its own confidence in a refund decision as five out of ten. E, a customer is annoyed that a replacement is late but has not asked for a person, and the replacement policy covers the case. [pause]

SAM: A and C. A is an explicit request: honour it now, even though the agent could resolve it. C is a policy gap: the policy exists but is silent on the request. B is sentiment, an unreliable proxy. D is self-reported confidence, same problem. E is frustration on a case within capability: acknowledge, resolve, and escalate only if the customer then asks for a person.

ALEX: E is where I'd have slipped. It sounds like the frustrated customer.

SAM: The tell is "has not asked" and "policy covers the case". Both point to resolve. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Refund limit of five hundred, a PostToolUse alert, over-limit refunds still going out. You picked A.

ALEX: Keep the alert, add a reversal. Having heard the episode, A is a compensating control. The money moves, then you try to claw it back.

SAM: Right. A loses because PostToolUse fires after execution; reversal repairs a breach the guide wants prevented. C is prompt guidance for a rule that must hold. D is the closest distractor: it intercepts in the right place and blocks, but a generic error gives the agent nothing to do next, so it retries or strands the customer. B intercepts before execution, blocks the over-limit amount, and redirects to escalate to human. That's both verbs in the guide's bullet. [sting]

## Five to remember

SAM: Five to remember. One: block before the call, transform after it. Policy limits are outgoing-call interception; PostToolUse normalises results before the model reads them, including from servers you cannot modify.

ALEX: Two: a block needs a next step. Return a reason that sends the agent to escalation, or it will retry or stall.

SAM: Three: hooks need a condition code can check. Thresholds, formats, missing IDs go in hooks. Tone and judgement go in the prompt with examples.

ALEX: Four: resume and name the changed files when most context is still valid. Fresh session with a structured summary when most tool results are stale. Fork when you want two approaches from one baseline.

SAM: Five: escalate on an explicit request, a policy gap, or no progress. Never on sentiment or self-rated confidence. Several matches means ask for another identifier.

## Recap: the exam tells

SAM: A recall check before the tease. Pause and name the three topics, and the word in a stem that gives each one away. [pause]

ALEX: Hooks, where the giveaway is timing. Sessions, where it's how much changed. Escalation, where it's whether the customer actually asked for a person.

SAM: Now as exam tells. If a hook raises an alert after the refund went through, think detective control, and move the check before the call.

ALEX: If a block returns a generic error, look for the option that also redirects to escalate to human.

SAM: If results arrive in mixed formats, some from servers you cannot modify, think one PostToolUse hook that normalises them before the model reads them.

ALEX: If you cannot write the requirement as an if statement, like tone or a policy gap, it goes in the prompt with examples.

SAM: If a few files changed, resume and name them. If most were rewritten weeks later, start fresh with a structured summary. If the stem says compare two approaches from the existing analysis, fork.

ALEX: If the customer says they want a person, escalate now. If they are frustrated but have not asked, acknowledge, resolve, and escalate only if they ask again.

SAM: And if an option escalates on sentiment or on the model's own confidence, strike it.

ALEX: Next time?

SAM: Tool design and built-in tools: descriptions that stop misrouting, structured errors, and when Grep beats Glob.
