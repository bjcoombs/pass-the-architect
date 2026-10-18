---
episode: "F01"
series: "CCAR-F retake"
slug: agentic-loop
title: "The agentic loop and enforced workflows"
description: "Stop reasons, appending tool results to a stateless API, forced tool choice for first calls, programmatic prerequisites, structured handoffs, and how errors should travel between agents. Drilled in the customer support and multi-agent research scenarios."
domain: "Agentic Architecture & Orchestration; Context Management & Reliability"
weight: "27% and 15%"
target_minutes: 24
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode five, the agentic loop and enforced workflows.

ALEX: Which means that by the end I can do what, exactly?

SAM: Tell a finished response from one that wants a tool, using the stop reason and nothing else. Spot why an agent repeats a call it already made. Choose between forced tool choice and a check in code when one step has to come first. Write an escalation a human can act on without asking the customer to start again. And decide what a failing subagent should send back to its coordinator.

ALEX: And for the exam, this sits in the biggest domain, twenty-seven percent, with tool choice and sequencing where I scored zero last time.

SAM: Then we start where the exam does, with an item. [sting]

## Cold open: the narrating agent

SAM: Customer support scenario. Your agent runs on the Agent SDK with the four M C P tools: get customer, lookup order, process refund and escalate to human. Customers report that the agent says "Let me pull up that order for you" and then nothing happens. Your loop code shows the reply to the customer and stops whenever the response contains any text. Which change fixes it? Option A, instruct the model never to write text in the same response as a tool call. Option B, keep looping until the reply contains a closing phrase such as "anything else I can help with". Option C, continue while the stop reason is tool use and stop when the stop reason is end turn. Option D, run every conversation for six iterations, then show the latest text.

ALEX: A. The model is narrating when it should be acting. Stop the narration and the text check works.

SAM: Hold that. We come back to it at the end.

ALEX: What does this episode cover?

SAM: Three task statements. One point one, the agentic loop. One point four, multi-step workflows with enforcement and handoffs. Both sit in Domain one, Agentic Architecture and Orchestration, twenty-seven percent of the exam, the biggest domain. And five point three, error propagation across multi-agent systems, from Domain five at fifteen percent.

ALEX: And my score report says I left marks here.

SAM: Stop reason handling at fifty percent, the stateless API at fifty, and tool choice with sequencing at zero. So every segment starts with a symptom, the way the exam asks it.

SAM: Segment one. Before I explain anything: walk me through one turn of the loop.

ALEX: Send the messages and the tool definitions. Claude answers. If it wants a tool, I run it and send the result back. Repeat until it is done.

SAM: Good. Now make "wants a tool" and "done" precise.

ALEX: The stop reason field. Tool use means it wants a tool. End turn means it has finished.

SAM: That is the whole control flow. When the stop reason is tool use, append Claude's response to the conversation exactly as it came back. Run each tool it asked for. Then add a user message carrying a tool result for every one of those calls, each result pointing back at the call it answers by its ID. Send the whole conversation again. When the stop reason is end turn, stop and present the answer.

ALEX: And a truncated response?

SAM: Hitting max tokens means the response was cut off. It is neither finished nor a tool request, so it needs its own handling. The exam's core pair is tool use and end turn.

ALEX: So the cold open bug is that Claude writes a sentence and asks for a tool in the same response.

SAM: Yes, and that is normal behaviour. A response can hold text and a tool call together. The guide names three anti-patterns for deciding when the loop is finished: parsing natural language signals, setting an arbitrary iteration cap as the primary stopping mechanism, and checking for assistant text as a completion indicator. Every one of them turns up as a distractor.

ALEX: I'll argue for the cap. Every agent I have shipped has a maximum number of turns. A runaway loop burns money, and I would fail a code review that did not have one.

SAM: Keep it. A cap as a safety backstop is sound engineering, and nothing in the guide forbids one.

SAM: Read the anti-pattern again, though: "as the primary stopping mechanism". A cap does not know whether the work is done. Set it at six and a refund that needs seven steps stops halfway. Set it at fifty and it does nothing on a simple question. The stop reason is the completion signal. The cap is what catches a bug.

ALEX: So the tell?

SAM: Whether the option says the cap decides when the task is finished, or catches a loop that never ends. "Primary", "determines completion", "regardless of whether Claude needs more work": strike it. [sting]

## Segment two: returning tool results

SAM: Segment two, how results get back in. Pause here and answer before we go on. Multi-agent research scenario. The coordinator asks the web search subagent to research battery recycling regulation. Logs show the subagent running the same search three times, then giving up with no findings. Each request it sends to the model contains the system prompt and the original task, nothing else. The search tool returned good results every time. What is the root cause and fix? A, the loop has no limit; cap the subagent at three search calls so it stops repeating and returns what it has. B, the loop never appends the model's tool call and the tool result to the conversation; append both and send the full history on every request. C, the model is choosing tools badly; replace its choices with a fixed sequence of one search followed by a summary. D, add each search result to the next request as a new user message, leaving out the model's own tool call to save tokens. [pause]

ALEX: A. It is looping and burning calls. A cap stops the burn, and every subagent should have one anyway.

SAM: That is miss pattern one, real-world instinct, and segment one already gave the cap its job: a backstop. Reread the stem: the search worked every time. The problem is not the number of repeats. The model never saw the result, so from its point of view it has not searched yet. A cap of three still buys three blind searches and no findings.

ALEX: Treating the symptom.

SAM: And blaming the wrong layer. The answer is B. The Messages API is stateless: each request stands alone, and the model knows only what is in that request. Your code holds the history and resends all of it, including every tool call and every result. A makes a cap the stopping mechanism, and the subagent still returns nothing. C throws away model-driven decisions to dodge a bug in the plumbing; fix the history and the model stops repeating on its own. D sends half the exchange: each tool result has to point back at the call it answers, so Claude's response goes into the history too.

ALEX: Let me push on statelessness. Resending everything on every call feels wasteful. Forty turns in, I am paying for the same tokens forty times. Why not send a summary?

SAM: The cost concern is real. The guide itself says tool results pile up and use tokens out of proportion to their value, like an order lookup returning forty fields when five matter.

SAM: So trim the tool output to the fields the model reasons with, and use prompt caching for the repeated prefix. What you do not do is drop the history the model needs. The guide's wording is that complete conversation history goes in subsequent requests to keep the conversation coherent.

ALEX: And the tell?

SAM: "Forgets", "asks again", "repeats the same call". The first question is always what was in the request, not how big the model is. [sting]

## Segment three: who decides next

SAM: Segment three. Who decides what happens next? The guide contrasts model-driven decision-making, where Claude reasons about which tool to call next from what it has learned so far, with pre-configured decision trees or fixed tool sequences.

ALEX: Here I am on the other side. A fixed sequence is predictable. I can test it, I can audit it, and a regulator can read it. Why hand the routing to the model?

SAM: For steps that never vary, you are right, and a later episode covers fixed pipelines. Predictability is worth a lot.

SAM: But a support conversation branches on what the tools return. A missing order, two accounts with the same name, a refund already issued: a decision tree has to anticipate every branch in advance, and it breaks on the first one nobody drew. The loop exists so the model can choose the next step from the last result.

ALEX: Then where does control come back in?

SAM: At the specific steps whose order must hold. Model-driven by default, enforced at the points that matter. The tell is "depends on what it finds" in the stem: that points to model-driven. "Must always happen before" points to enforcement.

ALEX: Which brings us to tool choice. My zero.

SAM: Tool choice has three settings the guide names. Auto: the model may call a tool or answer in text. Any: the model must call a tool but chooses which. And forced: you name one tool, and the model must call that one. The guide's skill is using forced selection to make sure a specific tool is called first, then handling the later steps in follow-up turns, with tool choice set back to auto.

ALEX: Wait. Episode ten said order that must hold lives in code. So I would put every sequencing problem behind a prerequisite check.

SAM: That is miss pattern four, a rule outrunning its scope. Episode ten was money moving: a refund that must never run before identity is verified, at any point in the conversation. Forced tool choice works on one request. It makes this call happen now. That is exactly right when the need is "this has to run first so the next tools have its output".

ALEX: And it cannot protect a refund on turn five.

SAM: No. So the split is this. One request, "call this first", the output feeds the next step: forced tool choice. A business rule that must hold across the whole conversation, especially with money or identity at stake: a programmatic prerequisite. The tell is "first" plus "before the enrichment steps" for tool choice, and "never" plus a financial operation for code.

SAM: Pause here and answer before we go on. Multi-agent research scenario. The document analysis subagent has three tools: one extracts a paper's identifier, title and publication date, and two others look up citation counts and retraction notices, both of which need that identifier. When asked to analyse a paper and report its standing, the subagent often calls the lookup tools first, and they fail. What is the most effective fix? A, force the extraction tool on the first request with tool choice naming it, then set tool choice to auto for the follow-up turns. B, set tool choice to any on every request. C, add a system prompt line saying always extract first. D, merge all three tools into one. [pause]

ALEX: A.

SAM: A. Forced selection guarantees the extraction call happens first, and auto afterwards lets the model use the lookups with the identifier in hand. B guarantees a tool call but not which tool, so the lookups can still go first. C is prompt guidance with a non-zero failure rate, which is what is failing now. D trades a sequencing fix for a bloated tool that does three jobs. [sting]

## Segment four: enforced prerequisites

SAM: Segment four, task statement one point four. Prompt instructions alone have a non-zero failure rate. When compliance must be deterministic, the guide's example being identity verification before financial operations, you enforce in code: a prerequisite that blocks the downstream tool until the earlier step has returned what it needs.

ALEX: Give me a support case that is not refund before lookup.

SAM: A customer verifies as themselves, then reads out an order number from a family member's account and asks for a refund. The prompt says refunds only on the customer's own orders. Now and then the agent processes it. The fix is a check in the process refund path that the order's customer ID matches the verified customer ID from get customer. If not, the call is blocked and the tool returns an error saying why, so the model can tell the customer.

ALEX: Multi-concern requests are in this task statement too.

SAM: "I was charged twice for one order, a second order arrived damaged, and I want to change my email." The guide's skill: decompose that into distinct items, investigate each in parallel using shared context, then give one unified resolution. Shared context means the customer is verified once and every item uses that ID. Parallel means the agent can request several tool calls in one response. And one reply that answers all three, not three replies.

ALEX: And when it has to escalate?

SAM: The guide says it plainly: the human agents lack access to the conversation transcript. So the escalation carries a structured handoff summary: customer ID, root cause, refund amount, recommended action.

SAM: Pause here and answer before we go on. Customer support scenario. A refund request goes over the limit the agent may approve, and the agent calls escalate to human. Human agents report that they spend the first five minutes of every escalation asking the customer to repeat everything, and some reverse checks the agent already did. What should the escalation contain? A, a structured summary with the customer ID, the order, the root cause found, the refund amount, what has been verified, and a recommended action. B, the full conversation transcript, so nothing is lost. C, a one-line note: customer requests refund above limit. D, nothing extra; have the human ask the customer to explain the issue again. [pause]

ALEX: I'll argue B. A summary is the agent's interpretation. The transcript is the evidence. If the agent got the root cause wrong, the human only finds out from the transcript.

SAM: Fidelity matters, and a transcript loses nothing.

SAM: But the stem is about a human who needs to act fast, and the guide answers it directly: compile a structured summary for humans who lack the transcript. A long transcript buries the refund amount in the middle, and the human still has to work out the root cause. So, A. B hands over the work instead of its result. C drops the fields the human needs. D is the current failure.

ALEX: Tell?

SAM: "Human agents", "repeat", "lack access to the conversation". The answer names fields: customer ID, root cause, amount, recommended action. [sting]

## Segment five: multi-agent errors

SAM: Segment five, task statement five point three: errors in multi-agent systems. Research scenario. When a subagent fails, what should reach the coordinator?

ALEX: The fact that it failed, and why.

SAM: More than that. The guide lists structured error context: the failure type, what was attempted, any partial results, and alternative approaches. With those, the coordinator can decide: retry with a changed query, try a different source, or carry on with what it has.

ALEX: And the distinction the guide makes?

SAM: Access failures versus valid empty results. A timeout is an access failure: we do not know what is there, so somebody must decide whether to retry. A query that ran and matched nothing is a valid result. It tells you something real, that the source has nothing on this.

ALEX: Here is my pushback. The guide itself says subagents should handle transient failures locally. So retry with backoff in the subagent, and if it still fails, return "search unavailable". That is local recovery.

SAM: The first half is straight from the guide. Subagents should recover locally from transient failures and only pass up what they cannot resolve.

SAM: The second half is where it breaks. When the error does go up, it must say what was attempted and carry the partial results. "Search unavailable" is the guide's own example of a generic status that hides context from the coordinator. Retrying locally is right. A bare status after the retries is wrong.

ALEX: So the tell is the word generic.

SAM: "Generic", "unavailable", "a single status". Local retry is fine; check what the option sends up afterwards.

ALEX: Then the opposite. When a source times out, return an empty result and let the pipeline finish. The report still ships, and the user gets something.

SAM: Keeping the pipeline going is the right instinct. One failed source should not sink a research run.

SAM: But an empty result marked as success is silent suppression, one of the two anti-patterns the guide names. The coordinator now believes the source had nothing, so it cannot retry, cannot try an alternative, and the report claims coverage it does not have. The other anti-pattern is yours from a minute ago turned around: terminating the whole workflow on a single failure.

ALEX: So between swallowing it and stopping everything.

SAM: Report it with structure, and let the coordinator decide. Then the synthesis output carries coverage annotations: which findings are well supported, and which topic areas have gaps because a source was unavailable. The tell for suppression is "marked as successful" or "returns empty on failure".

SAM: This links to Domain two, by the way. The same idea at the tool level is the M C P is error flag: a failure comes back to the agent marked as an error, not dressed as data.

SAM: Pause here and answer before we go on. Choose two. Multi-agent research scenario. Researching a drug's safety record, the web search subagent queries three sources. A journal database returns eleven relevant papers. A court filings database returns zero matches. A regulator's archive times out on all three local retries, after returning two documents. Which two belong in what the subagent reports to the coordinator? A, the regulator archive as an access failure, with the query attempted, the two partial documents, and an alternative such as a mirror of the archive. B, the court filings search as a successful query that found no matches. C, one combined figure, sixty-seven percent source coverage, with details in the logs. D, the regulator archive as zero results, so the run completes cleanly. E, a terminal error that stops the research run, because one of three sources failed. [pause]

ALEX: A and B.

SAM: Both. A gives the coordinator the failure type, the attempt, the partial results and an alternative. B keeps a real finding real: no court filings is information. C erases the difference between the timeout and the empty result. D is silent suppression. E terminates the workflow on one failure. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you said A: stop the model narrating.

ALEX: And I will defend it. Ask Claude not to mix text with tool calls, and the text check works again. It is one line of prompt.

SAM: It is one line, and it would cut the failure rate.

SAM: But it is a probabilistic fix for a deterministic need, and it still uses text as the completion signal, which is the anti-pattern itself. Text alongside a tool call is legitimate. So, C: loop while the stop reason is tool use, stop at end turn. B parses natural language for a closing phrase. D makes an arbitrary cap the primary stopping mechanism, and six iterations will cut off longer cases.

ALEX: What should have stopped me?

SAM: The stem told you the loop decides "whenever the response contains any text". When the option keeps deciding by text, it keeps the bug. The structured field that exists for this is the stop reason. [sting]

## Five to remember

SAM: Five to remember. One: loop while the stop reason is tool use, stop at end turn. Text, closing phrases and iteration counts are not completion signals; a cap is a backstop only.

ALEX: Two: the API is stateless. Append Claude's response and a tool result for every call, then resend the full history. "It forgot" or "it repeated the call" means look at what was sent.

SAM: Three: forced tool choice makes one named tool run first on a request, then switch to auto. Any guarantees a tool call, not which one. A rule that must hold across the conversation, like money or identity, is a programmatic prerequisite.

ALEX: Four: split multi-concern requests, investigate in parallel with shared context, answer once. Escalations carry a structured summary: customer ID, root cause, amount, recommended action.

SAM: Five: errors travel with their type, the attempt, partial results and alternatives. A timeout is not an empty result. Do not swallow failures and do not stop the whole run over one.

## Recap: the exam tells

SAM: Before the tease, a recall check. Pause and name the five topics we covered, with the giveaway for each. [pause]

ALEX: Stop reason and the loop. The stateless API. Forced tool choice against a prerequisite in code. Multi-concern requests and handoffs. And errors between agents.

SAM: Now the same ground as exam tells. If the loop decides by text, a closing phrase or a turn count, think stop reason: tool use continues, end turn stops.

ALEX: If an agent repeats a call or asks again for something it was already told, think about what was in the request, and append the call and its result.

SAM: If the stem says one tool must run first so the next tools have its output, think forced tool choice, then auto. If it says never, with money or identity at stake, think a prerequisite in code.

ALEX: If a human has to ask the customer to repeat everything, think structured handoff summary: customer ID, root cause, amount, recommended action. And a customer with three problems gets one reply that answers all three.

SAM: If a subagent sends up "search unavailable", or an empty result after a timeout, think structured error context, and let the coordinator decide.

ALEX: And if one failed source ends the whole run, that is the other anti-pattern.

ALEX: Next episode: coordinators, subagents and how to split the work between them.
