---
episode: "F07"
series: "CCAR-F retake"
slug: tools-mcp
title: "Tool design and built-in tools"
description: "How Claude picks a tool, how a tool should fail, how many tools each agent should hold, and which built-in tool fits which job: task statements 2.1, 2.2, 2.3 and 2.5, drilled in the customer support and developer productivity scenarios."
domain: "Tool Design & MCP Integration"
weight: "18%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode eight, tool design and built-in tools.

ALEX: What do I walk away with?

SAM: By the end you'll be able to write a tool description that wins the model's choice, and know when to split one tool or rename two that overlap. You'll shape the error a tool returns so the agent knows whether to retry, fix its input or explain.

SAM: You'll decide how many tools each agent holds and choose between tool choice auto, any and a named tool. And you'll pick the right built-in tool for the job: Grep, Glob, Read, Write or Edit.

ALEX: Tool Design is eighteen percent of the exam, and tool choice with sequencing scored zero last time. So this one closes a real gap.

SAM: Then start with an agent that never calls its best tool. [sting]

## Cold open: the unused index tool

SAM: Developer productivity scenario. An Agent SDK agent helps engineers explore a large monorepo. It has the built-in Grep tool and an M C P tool from the team's code-index server, which searches every repository, including ones not checked out locally. The system prompt says, "Whenever the user asks you to search, use grep for speed." Engineers ask cross-repository questions and the agent never calls the code-index tool, so the answers miss most of the code. What is the best fix? Option A, remove Grep from the agent's tool set. Option B, take the keyword instruction out of the system prompt and expand the code-index tool's description: what it searches, its input format, what it returns, and when to use it rather than Grep. Option C, put a routing classifier in front of the agent that sends cross-repository questions to the code-index tool. Option D, set tool choice to force the code-index tool on every turn.

ALEX: A. If Grep keeps winning, remove it.

SAM: Hold that. It comes back at the end.

ALEX: What is this episode for?

SAM: Domain two, Tool Design and M C P Integration, eighteen percent of the exam. Four of its five task statements: two point one, designing tool interfaces; two point two, structured error responses; two point three, spreading tools across agents and setting tool choice; and two point five, the built-in tools. Two point four, M C P server scope, was in the Claude Code configuration episode.

ALEX: And my numbers here?

SAM: Tool descriptions, fifty percent. M C P error handling, seventy-five. Tool choice with sequencing, zero. Customer support and developer productivity both list this domain as primary.

SAM: Segment one, how a tool gets chosen. Symptom: a customer support agent has the refund tool and a new tool that issues account credit. Both descriptions say "handles customer compensation". Customers who ask for their money back get credit, and some who ask for credit get refunds. Why?

ALEX: The model guesses between two tools that sound the same.

SAM: Right. The guide's first knowledge bullet: the tool description is the main thing the model uses to pick a tool. A short, vague description leads to unreliable choices among similar tools.

ALEX: So what goes in a good one?

SAM: The guide lists it. What the tool does. Its expected inputs and input format, for example "an order ID such as O R D dash one two three four five, never an email address". What it returns. Example queries it is meant for. Edge cases. And the boundary: when to use it rather than a similar tool. For the refund tool: "returns money to the original payment method for a specific order; use only when the customer asks for their money back; for goodwill gestures, use the credit tool instead."

ALEX: I would fix this differently. One line in the system prompt: "refunds go to the refund tool, credit goes to the credit tool". Faster than rewriting two descriptions, and I control it in one place.

SAM: It would help. But the overlap lives in the descriptions, so the guide fixes the descriptions. A prompt line patches a cause that is still there.

ALEX: The tell?

SAM: "Near-identical descriptions" or "similar tools", plus misrouting. The answer rewrites or renames the tools. The guide's own example renames a generic analyze content tool to extract web results, with a description that says it handles web results only.

ALEX: And the system prompt has nothing to do with tool choice?

SAM: Plenty, which is the fourth bullet. "When the user mentions an order, check the order" pulls the model to the order tool for a refund question that mentions an order. The skill is reviewing the system prompt for keyword-sensitive instructions that override good descriptions. Remember that for the cold open.

ALEX: Then the other direction. When do I split a tool, and when do I merge?

SAM: Split a generic tool that does several jobs. The guide's example: one analyze document tool becomes extract data points, summarize content, and verify claim against source, each with defined inputs and outputs. Merge, or rename, when two tools do the same job. Either way, each tool ends up with one purpose.

ALEX: Splitting means more tools, though. And you are about to tell me more tools is bad.

SAM: [laughs] Both are true. Three sharp tools beat one vague one. Eighteen tools on one agent is a different problem, and that is segment three.

SAM: Pause here and answer before we go on. Choose two. Developer productivity scenario. An internal agent has one tool called code helper, with a mode parameter for explain, find usages and generate tests. Its description is "Helps with code." Engineers report it picks the wrong mode about a third of the time, and the output shape varies from call to call. Which two changes best address this? A, split code helper into three purpose-specific tools, each with a defined input and output contract. B, write each tool's description with its input format, example queries, edge cases, and when to use it rather than the others. C, add an instruction to the system prompt telling the agent to think carefully about which mode to choose. D, move to a larger model that infers intent better. E, add a validation layer that rejects outputs with the wrong shape and asks the model to try again. [pause]

ALEX: A and B.

SAM: A and B. A removes the generic tool doing three jobs; B gives each new tool what the model needs to choose it. C is a prompt nudge about a problem the interface causes. D is scale instead of structure. E catches the bad output after the fact and leaves the cause alone: the contract was never defined. [sting]

## Segment two: tool error design

SAM: Segment two, how a tool should fail. Symptom, customer support scenario. A customer asks for a refund on an order delivered ninety days ago; the policy window is thirty. The refund tool returns the text "Operation failed". The agent retries three times, then tells the customer the system is down. What went wrong?

ALEX: The agent could not tell a policy refusal from an outage.

SAM: Exactly. "Operation failed" gives the agent nothing to choose a recovery from. The fix starts with the M C P is error flag: the tool returns its failure as a result with that flag set to true, so the agent knows the call failed rather than reading the text as data.

ALEX: Then the categories.

SAM: Four in the knowledge bullets. Transient: timeouts, service unavailable; a retry may work. Validation: the input was invalid; fix the input, don't resend it. Business: a policy says no, like the refund window; a retry will never work. Permission: the caller is not allowed; retrying won't help, it needs a different route.

ALEX: And the structure?

SAM: The guide's skills bullet names it: an error category, a boolean saying whether a retry makes sense, which the guide spells "is retryable", and a description a human can read. For business rule violations, add a retriable false flag and an explanation the agent can pass to the customer, so it can say "this order is outside our thirty-day refund window" instead of "something went wrong".

ALEX: I would throw an exception in the M C P server and let the agent framework deal with it. That is what exceptions are for.

SAM: In ordinary code, yes. But here the reader of the error is the model, and a raw exception or a generic string tells it nothing about whether to retry, fix its input, or explain. The guide's answer is structured metadata in the tool result. The tell is any option where the agent "cannot distinguish" errors, or keeps retrying something that will never succeed.

ALEX: So retrying is the anti-pattern. Never retry.

SAM: No. That's the over-application trap. Retrying a timeout is right. Retrying a policy refusal is waste. The point of the is retryable flag is that the agent retries exactly the failures worth retrying. An option that bans all retries throws away the cheap fix for transient errors.

ALEX: Where do subagents fit?

SAM: Two more skills bullets. First, recovery happens close to the failure. A subagent that hits a timeout retries locally. It passes up to the coordinator only errors it cannot resolve, and when it does, it sends the partial results and what it already tried, so the coordinator doesn't start over blind.

SAM: Second, and this is the one people miss: an access failure is not an empty result. "I searched and found no matching orders" is a successful query. "I could not reach the order system" is a failure that needs a retry decision. If the tool returns an empty list in both cases, the agent will tell a customer they have no orders when the database was simply down.

ALEX: Pause and drill it.

SAM: Pause here and answer before we go on. Customer support scenario. A customer whose loyalty plan excludes refunds on sale items asks for one on a sale purchase. The refund tool returns "Operation failed". The agent retries twice, then gives up and apologizes vaguely. First-contact resolution on these cases is falling. What is the best fix? A, have the refund tool return an error flagged as an error, with a business category, retriable set to false, and a customer-friendly explanation of the policy. B, add exponential backoff to the agent's retries. C, route every failed refund to the escalate to human tool. D, add a system-prompt instruction to apologize clearly when a refund fails. [pause]

ALEX: C. When money and policy collide, a human should look. That is what I would want as the customer.

SAM: That is miss pattern one: the real-world instinct beating the guide's answer. And the stem never said the customer asked for a human, or that the case was unclear. You imported that. The policy is clear; the agent just could not see it. The answer is A. With a business category and retriable false, the agent stops retrying and explains the rule, and the case is resolved on first contact. B makes the pointless retry slower. C sends resolvable cases to humans and works against the eighty percent target. D improves the tone of a message that still has nothing in it.

SAM: Pause here and answer before we go on. Choose two. Developer productivity scenario. A coordinator delegates to a subagent that searches the incident-tracking M C P server for past incidents touching a service. The subagent's credentials lack access to one team's project, and the tool returns zero results for it. Separately, the server times out now and then, and the subagent sends every timeout straight up to the coordinator, which restarts the whole search. Which two changes are best? A, return the access failure as an error flagged as an error, with a permission category and is retryable set to false, instead of an empty result. B, have the subagent retry transient timeouts locally and pass only unresolved errors to the coordinator, with partial results and what it tried. C, return an empty list for every failure so the coordinator's logic stays simple. D, have the coordinator re-run any search that comes back empty three times, in case it was a failure. E, give the subagent admin credentials for every project. [pause]

ALEX: A and B.

SAM: A and B. A separates "no access" from "no incidents". B keeps recovery local and gives the coordinator what it needs when recovery fails. C is the empty-result bug on purpose. D retries valid empty results, which wastes calls and still never fixes a permission error. E fixes one symptom by widening access well beyond the role, which least privilege rules out. [sting]

## Segment three: tool count and scope

SAM: Segment three, how many tools, and which agent holds them. The guide's numbers: an agent with eighteen tools picks less reliably than one with four or five. Each extra tool is one more option to weigh on every turn.

ALEX: But the coordinator might need any of them. Give every agent the full set and let it choose. Flexibility costs nothing.

SAM: It costs selection accuracy, and it invites misuse. The guide's example is a synthesis agent with web search: it should be combining findings it was given, and instead it goes off searching. Agents with tools outside their role tend to use them. The guide's answer is scoped access: each subagent gets only the tools its role needs.

ALEX: Only? Then the synthesis agent comes back to the coordinator for every little fact check. That's slow.

SAM: Which is why the guide allows a narrow exception: a limited cross-role tool for a frequent need. Give the synthesis agent a verify fact tool for quick checks, and route complex cases through the coordinator. The tell in the stem is "frequently" or "high-frequency". Then a narrow tool is right; full search access is not.

ALEX: And replacing tools?

SAM: Replace a generic tool with a constrained one. The guide swaps a fetch URL tool, which can reach anything, for a load document tool that validates document URLs. In support: not a general database query tool, but lookup order, which takes an order ID.

ALEX: Now tool choice, my zero.

SAM: Three settings in the guide. Auto: the model decides whether to call a tool, and which. Any: the model must call a tool, but picks which one. And forced selection: you name one tool, as an object with type set to tool and the tool's name, and the model must call that tool. The A P I also has none, which stops tool calls entirely.

ALEX: So when do I use which?

SAM: Use any when you need a tool call rather than conversational text, and more than one tool could be right. Force a named tool when one specific tool must run first. The guide's example: force an extract metadata tool on the first turn, then handle the enrichment tools in follow-up turns. Forcing applies to that one request. It is not a standing order for the whole conversation.

ALEX: Then force the right tool on every turn and the model can never stray.

SAM: That's over-applying it. Force a tool on every turn and the model can never pick a different tool, never answer, never finish. Force the first step that must happen, then return to auto. And if an order must hold across the whole conversation, such as verifying a customer before any refund, that belongs in code, a hook or a check in the tool handler, as in the hooks episode.

SAM: Pause here and answer before we go on. Customer support scenario. A triage step has three tools: route to billing, route to returns, and route to account security. Downstream code expects exactly one tool call per message. About one message in twenty, the model replies with friendly text instead of calling any tool, and the message sits unrouted. What should tool choice be? A, auto, with a stronger system-prompt instruction to always route. B, any. C, forced selection of route to billing, since billing is the most common case. D, none, with routing done by parsing the model's text reply. [pause]

ALEX: B.

SAM: B. Any guarantees a tool call and still lets the model pick which of the three. A leaves the one-in-twenty gap open; it is a probabilistic fix for a requirement that has to hold every time. C guarantees a call but sends every security case to billing. D parses the model's prose to drive control flow, the same fragile move the guide names as an anti-pattern for loop termination. [sting]

## Segment four: built-in tools

SAM: Segment four, the built-in tools. Developer productivity scenario. Six names: Read, Write, Edit, Bash, Grep, Glob. Grep searches file contents: a function name, an error message, an import statement. Glob matches file paths: names and extensions, like star star slash star dot test dot T S X for every test file.

ALEX: The mnemonic I use: Glob finds files, Grep finds text inside them.

SAM: That's the one. Read loads a whole file. Write writes a whole file. Edit makes a targeted change by matching a unique piece of existing text and replacing it.

ALEX: Unique is doing the work there.

SAM: It is. If the anchor text appears four times in the file, Edit fails. The guide's fallback: Read the full file, then Write the whole corrected file back.

ALEX: In practice I would just widen the anchor. Take three more lines of context until the match is unique, and Edit again. Cheaper than rewriting the file.

SAM: That works in real life, and the guide doesn't forbid it. But the one fallback the guide names for a non-unique match is Read plus Write. If both appear as options, pick Read plus Write. The tell is "non-unique", "multiple matches", or "cannot find unique anchor text".

ALEX: And Bash? It can grep and find and sed all of it.

SAM: It can, and engineers use it that way. But the guide tests choosing the built-in tool made for the job: Grep for content, Glob for paths. Bash for a plain search loses when the dedicated tool is listed.

ALEX: What about understanding a legacy codebase? I would load as much as fits in the context window. Models have big windows now.

SAM: The guide's skill is building understanding step by step. Grep for the entry points, then Read to follow the imports and trace the flow. Reading everything up front fills the context with noise, which the Context domain warns about.

ALEX: And wrapper modules?

SAM: The trap is a function re-exported under another name. Grep for the original name and you miss every caller that uses the wrapper's name. The guide's skill: first list every name the wrapper module exports, then search for each one across the codebase.

SAM: Pause here and answer before we go on. Developer productivity scenario. An engineer asks the agent to find every test file that calls a deprecated helper named format currency. The project has thousands of files. Which approach fits best? A, Read every file in the repository, then filter for test files that mention the helper. B, Glob for files matching the test-file pattern, then Grep those files for format currency. C, Grep the whole repository for the word "test". D, use Bash to list every directory, then Read each test file one by one. [pause]

ALEX: B.

SAM: B. Glob narrows by path, Grep by content, and nothing is read in full until it matters. A reads everything up front. C searches content for a word that belongs in a path. D does Glob's job by hand. [sting]

## Cold open: the verdict

SAM: Now the cold open. The code-index tool never gets called; the system prompt says "whenever the user asks you to search, use grep". You said A, remove Grep.

ALEX: I'm moving to B. The prompt line is a keyword trigger: the word "search" pulls the model to Grep every time, and the code-index description never says what it does better.

SAM: B. It fixes both causes: the keyword instruction overriding the descriptions, and a description too thin to win. A throws away a tool that is right for local searches and leaves the thin description in place. C is over-engineering: a classifier to do the job the descriptions should do. D forces one tool on every turn, so the agent can no longer use Grep, Read, or anything else.

ALEX: And the miss on A?

SAM: A blunt cut that loses something you need. Remove a tool when it is unneeded or outside the role. Grep is neither. [sting]

## Five to remember

SAM: Five to remember. One: the description is how the model chooses. Input format, examples, edge cases, and when to use this tool rather than its neighbor.

ALEX: Two: split a tool that does several jobs, rename tools that overlap, and check the system prompt for keywords that override good descriptions.

SAM: Three: errors come back flagged as errors, with a category, an is retryable boolean, and a readable message. Business violations get retriable false and an explanation the customer can hear.

ALEX: Four: an empty result is a success, and an access failure is not. Subagents retry transient errors locally and pass up only what they can't fix, with partial results and what they tried.

SAM: Five: four or five tools per agent, scoped to its role. Tool choice any when a tool call must happen, forced when one named tool must go first, auto after that. Glob finds files, Grep finds text, and when Edit can't find a unique match, Read then Write.

## Recap: the exam tells

SAM: Before we finish, your turn. Pause and name the four things this episode covered, with the giveaway for each. [pause]

ALEX: Tool descriptions, giveaway "similar tools" plus misrouting. Error responses, giveaway an agent that cannot tell a refusal from an outage. Tools per agent and tool choice, giveaway "frequently", or text where a tool call was needed. Built-in tools, giveaway "non-unique".

SAM: Good. Now as exam tells.

SAM: If two tools have near-identical descriptions and the agent misroutes, think rewrite or rename the tools. If the system prompt says "whenever the user asks you to search, use grep", think a keyword-sensitive instruction overriding a good description.

ALEX: If a tool returns "operation failed" and the agent keeps retrying a policy refusal, think the is error flag, a business category and retriable false, with an explanation the customer can hear. If an access failure comes back as an empty list, think error, not success.

SAM: If a subagent sends every timeout up and the coordinator restarts the search, think local retry, passing up only what it cannot fix, with partial results and what it tried.

ALEX: If one agent holds eighteen tools, or a synthesis agent goes searching, think four or five tools scoped to the role. If the stem says "frequently", think one narrow cross-role tool.

SAM: If downstream code needs exactly one tool call and the model sometimes answers in text, think tool choice any. If one tool must run first, force it on that request, then go back to auto.

ALEX: And if the stem says "every test file", think Glob. "Every caller", think Grep. And if Edit cannot find a unique match, think Read then Write.

ALEX: Next time: context, review and provenance, and keeping facts intact over a long session.
