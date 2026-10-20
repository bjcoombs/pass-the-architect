---
episode: "D06"
series: "CCDV-F"
slug: agents
title: "Agents and workflows"
description: "When a fixed workflow beats an agent, when supervisors and subagents earn their token cost, choosing between your own loop, the Claude Agent S D K and Managed Agents, hooks that make an action certain, and keeping a long-running agent's context under control."
domain: "Agents and Workflows"
weight: "14.7%"
target_minutes: 20
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode six: agents and workflows.

ALEX: What will I be able to do by the end?

SAM: Tell from the stem whether a job needs a workflow or an agent. Say when a supervisor with subagents pays for itself. Choose between your own agent loop, the Claude Agent S D K, and Anthropic-hosted Managed Agents. Use a hook when an action must happen, or must never happen. And keep a long-running agent's context clean.

ALEX: Domain one is nearly fifteen percent, about eight items. And it is where a builder's instinct for the most autonomous design costs marks.

SAM: So we start with that instinct. [sting]

## Cold open: the claims pipeline

SAM: Here is your opening item. An insurer's claims intake runs the same three steps for every claim: extract the fields, check them against the policy record, and route the claim to an adjuster queue. The team built an autonomous agent with all three tools. Auditors find that in a small share of claims it routed before checking the policy, and cost and latency are over budget. What is the best change? Option A, rebuild it as a workflow: three model calls in a fixed sequence in code, with a programmatic check between steps. Option B, add a line in capitals to the system prompt saying the policy check must always come before routing. Option C, move to a larger model that follows instructions more reliably. Option D, split it into a supervisor agent with three subagents, one per step.

ALEX: D. Each subagent owns a step, the supervisor enforces the order, and it scales when they add steps.

SAM: Hold that. We come back to it at the end.

ALEX: So what does domain one cover?

SAM: Three skills of similar weight. Agent architecture: workflow versus agent, supervisors and subagents. Agent construction: the Agent S D K, custom loops, self-hosted versus Anthropic-hosted, and hooks. Agent patterns and frameworks: tool-use loops, memory, context management, and frameworks such as Strands, Lang Graph and Pydantic A I.

SAM: As ever, the answer is the purpose-built mechanism for the stated constraint, not bigger, faster, or a polite instruction. [sting]

## Segment one: workflow or agent

SAM: Segment one. Anthropic's guidance draws one line. A workflow runs the model and tools through predefined code paths. An agent lets the model direct its own process and tool use. The difference is who picks the next step: your code, or the model.

ALEX: And which comes first?

SAM: The simplest thing that works: often a single call with good retrieval. Then a workflow, for well-defined tasks that need predictability. Then an agent, when the steps cannot be predicted. Agents cost more, and their errors compound.

ALEX: Name the workflow shapes.

SAM: Prompt chaining, routing, parallel sections or votes, orchestrator-workers, and evaluator-optimizer.

ALEX: Let me argue for agents anyway. Requirements change. A rigid chain gets rebuilt next quarter; an agent adapts.

SAM: Flexibility has real value, and for open-ended work it is the point.

SAM: But the exam reads the stem, not next quarter. When every case runs the same steps, the path is known, and handing it to the model buys variance you did not need: more tokens, more latency, the occasional skipped step.

ALEX: The tell?

SAM: "The same steps every time", "predictable", "must always happen in this order": workflow. "Cannot know in advance how many files or sources", "depends on what it finds": agent. And a link back to episode zero: ten thousand documents overnight, cost first, may need neither. That is the batch A P I.

SAM: Pause here and answer before we go on. A bank's research team wants an assistant for analysts' questions about companies. Some questions need one filing; others need a dozen filings, news searches and a pricing lookup, and nobody can say in advance which sources a question will need. What is the best architecture? A, a fixed three-step chain: search, summarise, answer. B, an agent with search and lookup tools in a loop, with stopping conditions such as a turn limit. C, a routing workflow that sends each question to one of four fixed pipelines. D, a single call with every recent filing pasted into the context. [pause]

ALEX: B.

SAM: B. "Nobody can say in advance" is the agent tell, and stopping conditions bound the loop. A forces every question down one path. C suits clean categories, but here steps vary within a question. D pastes data instead of giving access, and still misses news and pricing. [sting]

## Segment two: supervisors and subagents

SAM: Segment two, hierarchies. A supervisor, also called an orchestrator or manager, breaks the task into bounded pieces, sends each to a subagent with a scoped prompt and only the tools it needs, then checks and combines the results.

ALEX: Why bother? One capable agent can do all of it.

SAM: Often it can, and Anthropic's stated prior is to start with one. Multi-agent systems typically use three to ten times more tokens than a single agent on the same task. A subagent has to earn that.

ALEX: How?

SAM: Three cases. Context protection: a subtask produces a lot the main task does not need, like pages of logs to find one cause; the subagent works in its own context window and returns a short summary. Parallelisation: independent lines of inquiry at once, mostly for thoroughness. Specialisation: too many tools, or conflicting modes, for one prompt.

ALEX: Then I would build it like a team. Planner agent, coder agent, tester agent. That is how my last company's engineers worked.

SAM: It mirrors a real team, and role clarity helps people.

SAM: For agents, split by context, not by role. The agent that wrote the feature already holds what it needs to write the tests. Hand off to a tester and you play telephone: each handoff loses detail. Good boundaries are independent research paths, components with clean contracts, and blackbox verification, where a checker needs only the criteria.

ALEX: Tell?

SAM: Planner, implementer, tester on one tightly coupled piece of work is the trap. "Independent", "verbose output the main agent does not need", or "too many tools" justify a subagent.

SAM: Pause here and answer before we go on. Choose two. A support platform team is deciding where subagents are justified. Which two situations justify one? A, a diagnosis step reads thousands of lines of service logs, but the main agent needs only the probable cause. B, three independent questions about a customer's account history that can be investigated at the same time. C, writing a code fix and its unit tests, split into a coder agent and a tester agent. D, a simple F A Q assistant with four tools and short answers. E, outlining, drafting and polishing one reply, each by its own agent. [pause]

ALEX: A and C. The tester comes in fresh, without the coder's blind spots.

SAM: A is right. C is the role split we just named: the fix and its tests share one context, and the handoff throws it away. Fresh eyes is the case for a blackbox verifier with stated criteria, and C states none. The second answer is B, independent paths in parallel. D has no problem to solve. E is sequential phases of one job, telephone again. So, A and B.

SAM: Now the opposite mistake. A coding agent's session fills with file dumps from a search, and its answers drift. Subagent or not?

ALEX: Single agent. You just told me that is the prior.

SAM: That rule just outran its scope. "The search output floods the session" is context protection by name. A subagent returns only its final response, so the main context grows by a summary, not the whole search.

ALEX: So the prior is a default, not a verdict.

SAM: Right. The tell for overriding it is a named cost: flooding, bloat, a crowded context. [sting]

## Segment three: building the agent

SAM: Segment three, construction. Three ways to build, and the difference is who owns what. First, your own loop on the Messages A P I. When Claude calls a tool, the response holds a tool-use block; your code runs the tool, sends back a tool-result block, and calls again, until a response arrives with no tool call. You own the loop, tool execution, retries, context and infrastructure.

ALEX: Then the Agent S D K.

SAM: Claude Code's harness as a Python or TypeScript library, in a process you operate. The same agent loop, built-in tools for files, shell commands and web search, automatic compaction, subagents, permissions, resumable sessions, M C P and hooks. You still own hosting, scaling and credentials.

ALEX: And Managed Agents.

SAM: The Anthropic-hosted option. You define the agent, tools and guardrails through the Claude A P I; Anthropic runs the harness, with sessions in an Anthropic-managed sandbox. If generated code must stay on your infrastructure, a self-hosted sandbox keeps tool execution on your side while Anthropic runs the loop.

ALEX: So self-hosted versus Anthropic-hosted is about who runs the loop and where tools execute.

SAM: That is the axis. Your own loop when you need full control of the loop itself. The Agent S D K for the tuned harness on your infrastructure. Managed Agents when hosting, sessions and sandboxes are overhead that does not set your product apart.

ALEX: Here is my push. A tool loop is twenty lines. Why take a dependency at all?

SAM: The basic loop really is short, and the guidance says many patterns take a few lines against the A P I.

SAM: But read the stem. File editing, shell access, compaction, subagents and resumable sessions turn twenty lines into rebuilding a harness. Custom dispatch and control over every step: that is when your own loop wins.

ALEX: Tell?

SAM: "Full control of the loop": your own loop. "Claude Code's capabilities, in our application, on our servers": the Agent S D K. "Without running infrastructure", "small team", "long-running hosted sessions": Managed Agents.

SAM: Two loop controls by name: a maximum number of turns, and a maximum budget that stops the loop at a spend threshold.

SAM: Pause here and answer before we go on. For each statement, say custom loop, Agent S D K, or Managed Agents. One: a team needs its own tool dispatch, its own retry policy and control over every step. Two: a team wants Claude Code's built-in file and shell tools, compaction and subagents, inside its own service on its own Kubernetes cluster. Three: a three-person team wants long-running agent sessions without operating hosting, session storage or sandboxes. Four: a team wants Anthropic to run the agent loop, but generated code must execute inside its own cloud account. [pause]

ALEX: One, custom loop. Two, Agent S D K. Three, Managed Agents. Four, Agent S D K, because the code stays on their side.

SAM: Three out of four. Four is Managed Agents with a self-hosted sandbox. Anthropic runs the loop; only tool execution stays home. The Agent S D K would put the whole loop on their servers. Read who runs the loop, then where the tools run. [sting]

## Segment four: hooks for deterministic actions

SAM: Segment four, hooks. A hook is your code, called at a fixed point in the loop: before a tool runs, after it returns, before compaction, when the agent finishes. Hooks run in your application's process, not in the context window, so they cost no context.

ALEX: Which matter most?

SAM: Pre Tool Use runs before a tool call and can allow it, deny it, ask for approval, or rewrite its input. A denied call never executes; Claude gets the reason and tries another approach. Post Tool Use runs after a tool returns: audit logging, extra context, side effects. A matcher filters by tool name.

ALEX: One catch I have hit. The matcher matches the tool name, not the file path.

SAM: Right. Match the write tools, then check the path inside the hook. And that hook never sees a shell command writing the same file.

ALEX: My push. I would put "never modify production configuration" in the system prompt and add an eval for it. That has worked for me.

SAM: It works most of the time, and evals are worth having.

SAM: But a prompt is guidance. A long session, an ambiguous request or an injected instruction in a file can defeat it. When something must never happen, a Pre Tool Use hook blocks it every time. The eval measures how often the prompt held; the hook removes the question.

ALEX: Tell?

SAM: "Must never", "every time", "guarantee", "deterministic", "regardless of what the model decides". Those point to a hook or a permission rule, not better wording.

SAM: Pause here and answer before we go on. A field-service company's operations agent, built on the Agent S D K, must never run a destructive command against the production database, whatever a ticket says. What should the developer implement? A, a Pre Tool Use hook matching the shell tool that inspects each command and denies destructive ones against production. B, a system prompt section, in capitals, listing forbidden commands. C, a Post Tool Use hook that pages the on-call engineer whenever a destructive command has run. D, a larger model that is less likely to follow malicious ticket text. [pause]

ALEX: A.

SAM: A. It stops the call before it executes, deterministically. B is guidance, and injected ticket text is exactly where guidance fails. C is a detective control dressed as a fix: it tells you after the damage, though it can sit alongside A for audit. D is the bigger model, and no model size turns a likelihood into a guarantee. [sting]

## Segment five: loops, memory, context and frameworks

SAM: Segment five, patterns. The context window does not reset between turns: every tool call and output accumulates. And as context grows, recall of any one detail gets worse. Anthropic calls it context rot.

ALEX: Then I would take the biggest context window and stop worrying.

SAM: A larger window does postpone the limit, and for some single-pass jobs that is enough.

SAM: But it does not stop the rot: stale tool results dilute the details that matter. The exam's answer is to manage what is in the window.

ALEX: So the tell is "drifts" or "forgets" in a long session.

SAM: Yes, and the remedy is one of four. Subagents, for isolation. Clearing old tool results: a file read fifty turns ago rarely needs its raw text kept, and the A P I's context editing does this. Compaction: near the limit, older history is summarised and the conversation continues from the summary. The Agent S D K does it automatically.

ALEX: And the catch with compaction?

SAM: Specifics from early on may not survive the summary. So persistent rules do not belong in the first prompt. In the Agent S D K, put them in the project CLAUDE dot md the S D K loads, which is re-injected on every request.

ALEX: And the fourth?

SAM: Memory, for what must outlive the session. The memory tool lets Claude keep files in a memories directory that persists between sessions. It runs client-side: Claude requests the operation, and your application executes it against storage you control. The pattern is a progress log, read at the start of a session and updated before the end.

ALEX: And frameworks? The guide names Strands, Lang Graph and Pydantic A I.

SAM: As examples of agentic abstraction frameworks, which wrap the loop, tools and state. Anthropic's guidance on any framework: start with the A P I directly, since many patterns take a few lines. If you use one, understand what it does underneath, because the layer can hide the actual prompts and responses and make debugging harder.

SAM: Pause here and answer before we go on. Choose two. A healthcare provider's documentation agent runs for hours on the Agent S D K. After a few hours it stops following a formatting rule given in the first prompt. And each morning's session spends its first hour re-reading records to work out what yesterday's session finished. Which two changes address the causes? A, move the formatting rule into the project CLAUDE dot md the S D K loads, so it is re-injected on every request. B, give the agent the memory tool and have it keep a progress log it reads at the start of each session and updates before the end. C, turn compaction off so nothing is summarised. D, raise the maximum number of turns. E, switch to the largest context window and paste the previous day's full transcript in each morning. [pause]

ALEX: A and B.

SAM: Both. A answers the rule lost in compaction; B answers the morning re-exploration. C removes what keeps a long session alive. D fixes a cap neither symptom touches. E pastes a transcript instead of keeping state: context rot on purpose. [sting]

## Cold open: the verdict

SAM: Back to the claims pipeline. Alex, you picked D, a supervisor with three subagents.

ALEX: And after segment two I can see it. Three to ten times the tokens on a budget already over. And the supervisor is still a model deciding the order.

SAM: That is the core of it. The answer is A, a workflow. "The same three steps for every claim" means the path is known, so the order goes in code, where it cannot be skipped. With no open-ended loop, cost and latency fall too. B is a polite instruction aimed at an ordering guarantee. C makes the skip rarer, not impossible. D adds coordination cost and leaves the order in model hands.

ALEX: And the words that should have stopped me?

SAM: "Every claim" and "the same three steps". A known, fixed path is a workflow. [sting]

## Five to remember

SAM: Five to remember. One: a workflow runs on predefined code paths; an agent directs its own steps. Same steps every time, workflow. Steps you cannot predict, an agent with stopping conditions.

ALEX: Two: start with one agent. A subagent earns its three to ten times token cost through context protection, parallel independent work, or specialisation. Split by context, not by role.

SAM: Three: your own loop on the Messages A P I for full control; the Agent S D K for Claude Code's harness on your infrastructure; Managed Agents when Anthropic should run the harness, with a self-hosted sandbox when tools must run on your side.

ALEX: Four: must always or must never means a hook. Pre Tool Use denies or rewrites before the call runs; Post Tool Use audits after. Matchers match tool names, so check paths inside the hook.

SAM: Five: manage context, do not enlarge it. Subagents isolate, context editing clears old tool results, compaction summarises, persistent rules live in CLAUDE dot md, and the memory tool carries state between sessions.

## Recap: the exam tells

SAM: Recall first. Pause and name the five segments, and the giveaway that points to each. [pause]

ALEX: Workflow or agent; subagents; building the agent; hooks; memory and context. Giveaways: same or unpredictable steps; verbose or independent work; who runs the loop; must never; forgets or drifts.

SAM: Now as exam tells. If every case runs the same steps, think workflow. If nobody knows the sources in advance, think agent, with a turn limit or budget.

ALEX: If a subtask floods the session or paths are independent, think subagent. If it is planner, coder, tester on one piece of work, think telephone game, and keep one agent.

SAM: Full control of the loop, your own loop. Claude Code's tools on your servers, the Agent S D K. No infrastructure to run, Managed Agents, with a self-hosted sandbox if tools must run in your cloud.

ALEX: If it says must never, or every time, think Pre Tool Use hook. An alert after the fact is detective, not preventive.

SAM: If a long session forgets an early rule, think CLAUDE dot md. If each new session starts from scratch, think memory tool and a progress log. And if a framework hides the prompts, look underneath it.

ALEX: Next, episode seven: prompts, context and output handling.
