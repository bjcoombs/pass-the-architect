---
episode: "D08"
series: "CCDV-F"
slug: tools-mcp
title: "Tools, MCP servers and choosing a customization"
description: "How the tool-use loop works and who runs each tool, descriptions and errors that keep an agent on track, approval gates, building and deploying M C P servers with tools, resources and prompts over stdio or H T T P, and choosing between a built-in tool, a custom tool, a skill and M C P."
domain: "Tools and MCPs"
weight: "10.6%"
target_minutes: 18
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode eight: tools, M C P servers, and choosing a customization.

ALEX: What will I be able to do by the end?

SAM: Trace the tool-use loop and say who executes each kind of tool. Write descriptions and error results that keep an agent on the right tool. Put an approval gate where it belongs. Build an M C P server, choose its transport, and sort its capabilities into tools, resources and prompts. And pick between a built-in tool, a custom tool, a skill and M C P for a given need.

ALEX: Ten point six percent, so five or six items, and most of them are design choices where every option works a little.

SAM: So we start with one. [sting]

## Cold open: the wrong lookup

SAM: A retailer's support agent has thirty-one tools, contributed by five teams. Three of them overlap: search orders, find order, and lookup customer orders. Each has a one-line description. The agent often calls the wrong one and returns another customer's order history. What is the best fix? Option A, consolidate the overlapping tools into one, with a service prefix in its name and a detailed description of what it does, when to use it and what it returns. Option B, add a section to the system prompt listing which tool to use for which kind of question. Option C, move the agent to the largest model. Option D, force the agent to call the same order tool on every turn.

ALEX: B. One table in the system prompt, done in ten minutes, and no team has to change its tool.

SAM: Hold that. We come back to it at the end. [sting]

## Tool implementation

SAM: Domain eight has three skills: tool implementation, four point four percent of the exam; M C P server development, two point one; agentic customization, four point one. Tools first, starting with the loop.

ALEX: I define a tool with a name, a description and an input schema. Claude decides to call it.

SAM: The response comes back with a stop reason of tool use and tool use blocks, each with an I D, the tool name and its input. Your harness dispatches: it finds the handler by name, runs it, and sends back a tool result carrying the same I D. The loop runs until Claude gives a normal answer. Or the S D K's tool runner runs that loop for you.

ALEX: And server tools skip all that.

SAM: That is the client-side versus server-side distinction. Client tools run in your application: your own functions, and Anthropic-defined ones like bash, the text editor and the memory tool, where Anthropic supplies the schema but your code executes. Server tools run on Anthropic's infrastructure, such as web search, web fetch and code execution. You declare them, and the results arrive in the response with no handler code.

SAM: Descriptions. Anthropic's documentation calls detailed descriptions by far the most important factor in tool performance. Say what the tool does, when to use it and when not to, what each parameter means, and what it does not return. Aim for at least three or four sentences. For complex inputs, the tool definition can also carry input examples.

ALEX: Every word of a description is billed on every call, though. With thirty tools I keep them to one line.

SAM: Tool definitions do cost tokens, and episode one showed how caching softens that.

SAM: But a one-line description is how an agent calls the wrong tool, and a wrong call costs far more than a few sentences. The documentation's answer is longer descriptions and fewer tools, not shorter descriptions. The tell: "picks the wrong tool" or "similar tools" points to the description and the tool set, not to the model.

SAM: Which is tool set construction. Keep the set small. Consolidate related operations into one tool with an action parameter. Prefix names with the service, so a GitHub tool and a Slack tool never look alike. Return only high-signal fields, with stable identifiers, which is episode seven's pruning applied at the source. And for a very large library, a tool search tool lets Claude find and load tools on demand.

SAM: Error handling. Symptom: an order-status tool's backend times out, the harness catches the exception, and the agent tells the customer their order shipped.

ALEX: Because the harness returned nothing useful, and the model filled the gap. But I would rather handle failures in code. Retry in the harness and keep the model out of it.

SAM: A quick retry in code for a momentary blip is reasonable.

SAM: But when the failure persists, the model has to know, or it guesses. Return a tool result with is error set to true and an instructive message: what failed, and what to try next, such as "rate limit exceeded, retry after sixty seconds". Anthropic's guidance is exactly that: say what went wrong and what to do, not just "failed". And strict tool use, which constrains tool inputs to your schema, removes the invalid-argument failures before they happen. The tell: "the agent made up an answer when the tool failed" points to an instructive error result.

SAM: Last, approval patterns. The model proposes a call; your harness decides whether it runs. For a consequential action, the harness pauses for a person or a policy check before executing. In Claude Code, permission rules allow, ask or deny a tool, and episode nine adds hooks that can block a call in code.

ALEX: Then put approval on everything. Safest.

SAM: That rule just outran its scope. Approve every read and people click yes without looking, which is no control at all, and the stem usually says reads must not interrupt the user. Gate the irreversible ones. The tell: "payment", "delete", "send" or "irreversible" means gate that tool in the harness, and leave the reads alone.

SAM: Pause here and answer before we go on. Choose two. A finance operations agent can read invoices and can issue payments through the company's internal payments A P I. Policy says no payment goes out without a human sign-off, and invoice lookups must not interrupt the user. Which two design choices meet the policy? A, implement payment as a client tool that the harness executes only after a human approves the specific call. B, let the invoice-reading tools run without an approval step. C, add a line to the system prompt telling Claude to ask before paying. D, implement payment as a server tool so Anthropic executes it securely. E, require human approval for every tool call, reads included. [pause]

ALEX: A and B.

SAM: Both. A puts the gate in code, on the one action that needs it; B honours "must not interrupt". C is a polite instruction where the policy needs a control. D is not available: server tools are Anthropic's own, and they cannot reach your internal payments service. E breaks the second requirement and trains people to approve blind. [sting]

## MCP server development

SAM: M C P server development. Start with client versus server. The host is the application, such as Claude Code or Claude Desktop. For each M C P server it connects to, the host creates one M C P client, which holds that connection. The server is the program that exposes capabilities. Messages are JSON R P C.

ALEX: And the server exposes tools.

SAM: Tools, resources and prompts, and the exam wants you to tell them apart by who controls each. Tools are model-controlled: Claude decides when to call them, and they can act, such as creating a ticket. Resources are application-controlled: read-only data, each with a U R I, that the application attaches as context, such as a database schema or a document. Prompts are user-controlled: templates with arguments that a person invokes, typically surfaced as slash commands.

ALEX: Why not make everything a tool? Claude can call a get-schema tool just fine.

SAM: It can, and for a small server it works.

SAM: But read-only context the application should simply attach is what resources are for, and it saves the agent exploratory calls before every query. A workflow template a person picks is a prompt. The tell: "read-only", "catalogue" or "context the app provides" points to a resource. "The user picks from a menu" points to a prompt. "Takes an action" points to a tool.

SAM: Pause here and answer before we go on. For each item, say tool, resource or prompt. One: the warehouse database schema, which the application attaches as read-only context. Two: a create-incident action that Claude decides to call. Three: a "triage this incident" template a user picks from the slash menu. Four: a run-query operation that takes a S Q L string and returns rows. [pause]

ALEX: Resource, tool, prompt, tool.

SAM: All four. Four is a tool because Claude invokes it with arguments and it executes, even though it only reads.

SAM: Transports, the guide's communication patterns. Stdio is for a local server: the client launches it as a process on the same machine and talks over standard input and output, usually one client per server. Streamable H T T P is for a remote server: it runs as a network service, serves many clients, and uses standard H T T P authentication, with OAuth recommended.

SAM: Authoring. The official S D Ks do the protocol work; the Python S D K builds each tool's definition from the function's type hints and docstring, so the docstring is your tool description, and the same description rules apply.

SAM: Deployment and integration. In Claude Code, a shared server goes in the project's dot M C P dot json, committed, with credentials as environment-variable placeholders, never the secret itself; a personal server goes in user scope. Claude Desktop runs local servers. And from the Messages A P I, the M C P connector lets a request use a remote M C P server directly, without you writing an M C P client.

SAM: Pause here and answer before we go on. A developer's local stdio M C P server worked in testing. After they added print statements to debug a tool, Claude Code reports that it cannot talk to the server. What is the most likely cause? A, the print statements write to standard output, which corrupts the JSON R P C messages; log to standard error instead. B, stdio is unreliable, so the server must move to streamable H T T P. C, the tool descriptions became too long for the client. D, the model in use does not support M C P. [pause]

ALEX: Let me argue B. Stdio means a child process and pipes. Remote H T T P is what you would run in production anyway, so move now and stop fighting it.

SAM: Remote has real advantages for a shared server. But look at the trigger: it worked, then print statements went in, then it broke. That distractor is a rebuild sized far beyond the cause. The M C P documentation is plain: a stdio server must never write to standard output, because that channel carries the protocol.

ALEX: So A.

SAM: A. Send logs to standard error and the server works again. B rebuilds the deployment around a one-line bug. C and D have nothing to do with print statements. The tell: "worked until" names the cause. [sting]

## Agentic customization

SAM: Agentic customization: built-in tools, custom tools, Skills or M C P. Four questions, in order.

SAM: One: does a built-in tool already do it? Web search, web fetch and code execution on the A P I; Read, Grep and Bash in Claude Code. If yes, use it. Do not build your own web search. But built-ins do not reach your internal systems.

SAM: Two: is it an action for one application? A custom tool, defined in that application's code, next to the logic it calls. Simplest thing that works.

SAM: Three: will several applications or clients need the same access, maintained by one team, independently of any one app? That is an M C P server. One server, many hosts: Claude Code, Desktop, and an A P I application through the connector.

ALEX: M C P is the standard now. I would build an M C P server even for one app, so it is ready when the second one arrives.

SAM: Reuse is the whole point of M C P, and if the stem says a second consumer is coming, that counts.

SAM: But for one application calling one internal function, M C P adds a process, a transport, deployment and auth for no gain. The tell: "several applications", "Claude Code and our app" or "maintained independently" points to M C P. "Only this service" points to a custom tool.

SAM: Four: is it know-how rather than access? A procedure, a policy, a template, a script for how to do a task. That is a Skill. Only its name and description load up front; the full instructions load when a task matches, and its bundled files only when the instructions call for them.

ALEX: Or I put the procedure in the system prompt. Then it is always there and never fails to trigger.

SAM: Always there is real, and for a rule every request needs, that is the right place.

SAM: But a twelve-step procedure that most requests never use is paid for on every call and can conflict with other instructions. A Skill loads it when it is relevant. The tell: "only when", "procedure", or "with a script and template" points to a Skill. And they combine: M C P gives access, a Skill says how to use it.

SAM: Pause here and answer before we go on. An insurer's claims assistant should follow a ten-step fraud-referral procedure, with a scoring table and a small calculation script, but only on claims that hit a red flag. Nothing external needs connecting. Which approach fits best? A, package the procedure, table and script as a Skill, so it loads when a claim matches. B, build an M C P server that exposes the procedure as a tool. C, paste the procedure and table into the system prompt. D, write one custom tool for each of the ten steps. [pause]

ALEX: A.

SAM: A. Know-how, needed only sometimes, with a script bundled: a Skill. B builds connectivity nobody needs. C pays for the procedure on every claim. D crowds the tool set with ten tools. [sting]

## Cold open: the verdict

SAM: Back to the support agent. Alex, you picked B, a routing table in the system prompt.

ALEX: Which works around three thin descriptions and still leaves three near-identical tools.

SAM: So the answer is A. One consolidated tool, a service prefix, and a description that says what it does, when to use it and what it returns. That is the documentation's top factor in tool performance, plus the tool set rule: fewer, clearer tools. C is scale instead of a fix. D forces one tool even on turns that need none of them.

ALEX: The words that should have caught me?

SAM: "Three of them overlap" and "a one-line description". Overlap means consolidate; thin descriptions mean rewrite them. [sting]

## Five to remember

SAM: One: the loop. Stop reason tool use, your harness dispatches by name, a tool result returns with the same I D. Client tools run in your code; server tools such as web search and code execution run on Anthropic's side.

ALEX: Two: descriptions are the top factor. What, when, when not, parameters, limits, at least three or four sentences. Fewer tools, service prefixes, high-signal returns.

SAM: Three: errors go back as a tool result with is error true and an instructive message. Approval gates live in the harness, on the irreversible actions only.

ALEX: Four: M C P. One client per server inside the host. Tools are model-controlled, resources application-controlled, prompts user-controlled. Stdio for local, streamable H T T P for remote, and never print to standard output in a stdio server.

SAM: Five: built-in if it exists, a custom tool for one app, M C P for access shared across apps, a Skill for know-how loaded on demand.

## Recap: the exam tells

SAM: Recall first. Pause and name the three skills from today, and the question that sorts each one. [pause]

ALEX: Tool implementation: who runs the call, and what does it say when it fails? M C P development: tool, resource or prompt, local or remote? Customization: does it already exist, who needs it, and is it access or know-how?

SAM: Now as exam tells. If the agent picks the wrong one of several similar tools, think consolidate and rewrite the descriptions, not a routing table or a bigger model.

ALEX: If the agent invents an answer when a tool fails, think an error result with is error set and a message that says what to do next.

SAM: If the action is a payment, a delete or a send, think an approval gate in the harness on that tool. If reads must not interrupt, do not gate them.

ALEX: If the item is read-only context the app attaches, think resource. If a user picks it from a menu, prompt. If Claude calls it with arguments, tool.

SAM: If a stdio server broke after print statements went in, think standard output, and log to standard error. If many clients need a server over a network, streamable H T T P.

ALEX: If several applications need the same access, think M C P. One app, a custom tool. A procedure needed only sometimes, a Skill. And if a built-in already does it, use the built-in.

SAM: Next, episode nine: security, hooks, secrets and debugging.
