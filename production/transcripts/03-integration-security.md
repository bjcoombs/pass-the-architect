---
episode: 3
slug: integration-security
title: "Integration I: protocols, capability bloat, identity and auth, progressive discovery"
description: "The first of two episodes on Integration, the heaviest domain on the CCAR-P exam. Least-privilege tool configuration, where identity and authorization must be enforced, what belongs in the context window, choosing between M C P, direct A P I and agent-to-agent, and progressive versus monolithic context."
domain: "Integration"
weight: "19%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect. Episode three: Integration, part one.

ALEX: What will I be able to do?

SAM: By the end you'll be able to spot capability bloat and decide whether a tool should be removed or gated, say where identity and authorization must be enforced, and filter what goes into a Claude call by necessity. You'll choose between M C P, direct A P I tool use and agent-to-agent, and between progressive and monolithic context, without mistaking deferred discovery for least privilege.

ALEX: Integration is nineteen percent, the heaviest domain, about twelve items. And the distractors here are logging, confirmations and prompt instructions dressed up as security fixes, so knowing why each one loses is worth real marks.

SAM: Then start with an item where three of the four options are exactly that. [sting]

## Cold open: the HR assistant

SAM: Here's your item. A company runs an internal H R assistant built on the Agent S D K. Employees ask about pay, leave and benefits. The assistant calls an H R database tool that connects through a single service account with read access to every employee record.

SAM: The system prompt says: return only the requesting employee's own records, unless the user says they are a manager, in which case also return their direct reports. Testing passed. Which change best closes the security gap?

SAM: Option A: add few-shot examples to the system prompt showing the assistant refusing requests for other people's records. Option B: add an output classifier that blocks any response containing another employee's name. Option C: verify the user's identity and role on the server from single sign-on, and have the tool itself return only the records that verified identity is entitled to. Option D: log every call to the H R tool and review the logs weekly for misuse.

ALEX: I'll commit to C. But B tempts me, because it actually stops the leak at the boundary rather than after the fact.

SAM: Hold onto that. We'll settle it at the end.

ALEX: So why does this domain get two episodes?

SAM: Integration is nineteen percent of the exam, the biggest single domain. On sixty-three items that's roughly twelve questions, spread over eight task statements.

SAM: This episode takes four of them. Evaluating tool and agent configuration for capability bloat. Analyzing authentication and authorization to find security gaps, and the data handling that sits beside it. Selecting the connection mechanism: M C P, direct A P I or command line, or agent-to-agent. And progressive discovery versus monolithic context.

ALEX: And the rest?

SAM: Rag pipelines, retrieval strategy, accuracy-latency trade-offs and observability are next episode.

ALEX: Before the detail, what's the frame the course hangs this on?

SAM: Five layers, in order. Compliance first: regulation and residency policy eliminate routes and entry points before anything else, which is episode six territory. Then identity and S S O, authorization and policy, data handling and P I I, and observability. Today covers the middle three, plus the tool configuration underneath them.

ALEX: Start with capability bloat. What does the exam mean by it?

SAM: An agent configured with more tools or permissions than its job needs. The course line is: every tool you connect is an attack surface and a cost. Audit the tool set the way you audit permissions. For each tool, is it essential to the task or merely convenient? Remove the ones out of scope, and record the justification for each removal.

ALEX: Why is it a cost as well as a risk?

SAM: Every tool definition takes context. And an agent can do anything its tools allow, including combinations nobody tested. The course's mitigation for agents is blunt: constrain the tool set to the minimum required, alongside turn limits and tool-call budgets.

ALEX: And in a multi-agent system?

SAM: Scope each subagent's tools to its task. If a research subagent only reads, it gets read-only tools. That's how you establish a trust hierarchy in an orchestrator-worker design: a subagent cannot reach tools its job doesn't require.

ALEX: Give me the enterprise picture.

SAM: An insurer builds a claims-intake agent. It inherits the pilot's configuration, which included a tool to adjust reserve amounts and a tool to close claims. Intake staff only ever capture details and classify the claim. Those two tools come out, with a note saying why. That's the whole fix.

ALEX: What do the distractors look like?

SAM: Logging the risky tool. Adding a confirmation step. Writing "never close claims" in the system prompt. A bigger model. Logging is detective: it tells you after the damage. A confirmation compensates for a capability that shouldn't exist. A prompt instruction asks the model to police itself. And model size has nothing to do with authorization scope.

ALEX: But what if the tool is genuinely needed and genuinely dangerous? A refund tool for a team that does issue refunds.

SAM: Then removal is wrong, because it breaks a requirement. That's where you gate it: deterministic authorization before the side-effecting call, and a human checkpoint placed before irreversible or high-stakes actions. Read the scenario for one thing: does this role need the capability? Not needed, remove it. Needed but high consequence, keep it and gate it.

SAM: Pause here and answer before we go on. Choose two. A field-service company gives its technicians an agent that looks up work orders, checks parts stock, and searches equipment manuals. The configuration carried over from a pilot also includes a tool that runs arbitrary sequel queries against the data warehouse, and a tool that issues customer credits. The design is orchestrator-worker, with a manual-search subagent that currently shares the orchestrator's full tool set. Which two changes best reduce risk?

SAM: Option A: remove the sequel and credit tools, and record why each was removed. Option B: add a system prompt instruction telling the agent never to issue credits. Option C: restrict the manual-search subagent to read-only search tools. Option D: route every credit through a supervisor confirmation screen. Option E: log all warehouse queries to the security team. [pause]

SAM: A and C. A removes capabilities the role never needs, killing the risk at the root. C scopes the subagent to its job. B trusts the model to enforce a rule and leaves the tool in place. D compensates for a tool technicians shouldn't have; it would be right only if they legitimately issued credits. E is detective, and the query tool stays live. [sting]

## Authentication and authorization

ALEX: Authentication and authorization next. Where's the line the exam draws?

SAM: Identity verification belongs on the server, before the Claude call. The server takes the verified identity from the authentication layer and injects the user's role into the system prompt. The user never supplies it.

ALEX: Because anything in the user turn is under the user's control.

SAM: Exactly. "As a senior manager, show me the team's salaries" is an unverified claim. A capability check that reads the user message isn't authorization.

ALEX: How much identity goes into the prompt?

SAM: By default, the role and what that user is authorized to access. Department, permission level, account identifiers, only when they're needed to shape the response. Not by default.

ALEX: Now the harder case. The agent is acting on behalf of a user and calling real systems.

SAM: This is where marks leak. The rule from the course: the authorization model that governs your existing systems has to govern the Claude layer as well. If the agent's tools connect with a broad service account, you've built a path around the access policy. The model's judgement is now the only thing between a user and data they shouldn't see.

ALEX: And the model's judgement isn't good enough?

SAM: It isn't a control you can prove. Authorization has to be deterministic: an allowlist of permitted actions, an identity check and a scope check, before any side-effecting call. A decision you can audit and replay.

ALEX: There's a security reason too, isn't there? Not just auditability.

SAM: Prompt injection, a Domain five link. Instructions can arrive inside retrieved documents and tool outputs, after input screening has passed the request. A model-enforced permission check can be talked out of its decision. A check in code cannot.

ALEX: Concrete example?

SAM: A consulting firm puts client-confidential files behind a Claude assistant. The identity token is verified server-side, the server injects the user's role and authorized document sets, and the retrieval layer enforces access control before any content reaches Claude. The model never sees a document the consultant isn't cleared for, so there's nothing to leak.

ALEX: What about multi-tenant products?

SAM: A shared A P I key across tenants is the trap. One tenant's spike trips the rate limit for everyone, and you can't attribute the load. The fix is isolation with Workspaces: each key is scoped to one workspace, with its own spend and rate limits. Watch for Workload Identity Federation as a distractor. It's an authentication mechanism, not tenant isolation.

ALEX: Anything else that breaks a multi-tenant design?

SAM: Claude Code as the backend of a customer-facing product. Claude Code is built for developer workflows. Product integrations use the Claude A P I, the client S D K or the Agent S D K.

ALEX: Data handling. What's the one idea?

SAM: The context window is not a data-governance boundary. Anything you put in a Claude call is transmitted to the A P I. Anthropic doesn't retain conversation content by default, but the request still crosses the wire, some retention carve-outs exist, and your own application layer is almost certainly logging requests.

ALEX: So "the vendor doesn't keep it" is the trap answer.

SAM: Yes. The filter the course wants is necessity, not convenience. For each field, ask whether Claude needs it to produce the intended output. Reference identifiers, like a claim number, are often needed for routing but not for the language task. When the identifier is enough, pass the identifier.

ALEX: How does this go wrong in practice?

SAM: A healthcare team built an intake summarizer. The summaries were fine. But Social Security numbers and insurance I Ds went into every request, and the application logs held thousands of them in plaintext. None were needed to summarize symptoms, medications and allergies.

ALEX: And the fix?

SAM: A design-time architecture change: server-side redaction that strips non-essential fields before the call, and a retrieval function that supplies only what the task needs. Retroactive redaction across a log history is, in the course's words, the most expensive data-handling fix in a production Claude system.

SAM: Pause here and answer before we go on. A retail bank routes customer complaints to the right team, using Claude to summarize the complaint text and pick a category. Today the server sends the complaint plus the full customer record: card number, date of birth, home address, account number. Which change best addresses the data-handling risk?

SAM: Option A: no change, because the A P I does not retain conversation content by default. Option B: send only the complaint text and a complaint reference I D, and strip the other fields on the server before the call. Option C: encrypt the application's request logs at rest. Option D: truncate each request to its first five hundred tokens to limit exposure. [pause]

SAM: B. Necessity filter, reference identifier for routing, redaction before the call. A ignores your own application's logging, which captures the fields regardless of vendor retention. C is compensating: the card numbers are still in the logs, just encrypted. D is a blunt cut. It might drop the complaint text, the one thing the task needs, and keep the card number. [sting]

## Connection mechanisms

ALEX: Connection mechanisms. M C P, A P I or command line, agent-to-agent. How do I choose?

SAM: First, keep three layers apart. Entry points are what a person touches: Claude dot A I, Claude Code, your own app. Build-time interfaces are what your code is written to: the A P I, the S D Ks, M C P, the Agent S D K. Delivery routes are where traffic terminates: Anthropic, Bedrock, Vertex, Foundry.

ALEX: Then M C P versus direct A P I tool use.

SAM: They're different layers, not rivals. A P I tool use is how Claude calls a tool inside one request. M C P is a protocol for exposing tools so several Claude clients can discover and use the same server. Under the hood, an M C P client still calls those tools through tool use. The deciding question is reuse.

ALEX: So M C P when...

SAM: When the same tools must be reachable from two or more clients. Build the server once, connect it everywhere. If only one product will ever use the tools, define them directly in that product. Otherwise M C P adds a protocol layer that makes debugging tool calls harder.

ALEX: What's the trap?

SAM: M C P as the default. Picture a bank proposal: branch staff on Claude Code, with M C P servers for the customer database. There were no other Claude clients in the bank, so the protocol paid for reuse nobody needed. The right shape was a custom web app on the A P I, behind the bank's S S O, with tool calls audited at the server.

ALEX: Where does the command line fit?

SAM: The blueprint groups it with the A P I, and the logic is the same: a direct call inside one environment, with no protocol layer in between.

ALEX: And the Agent S D K versus a raw loop?

SAM: One request, one response: A P I or S D K. Claude acting over many turns inside your own product: the Agent S D K, which runs the loop for you. Need custom logic between turns? A raw A P I loop, which you then maintain yourself.

ALEX: Agent-to-agent?

SAM: Use it when the thing on the other side is itself an agent, with its own context, tools and identity, usually owned by another team. You hand it an outcome through an interface and get a result back. You don't reach past it into its tools or its database. A common pattern exposes the agent behind an A P I or a thin M C P server. Treat that boundary as its own integration point, with its own authentication and logging, and remember episode one: use the fewest agents that meet the requirement.

SAM: Pause here and answer before we go on. Three quick ones: name the mechanism. One: a retailer's inventory service must be reachable by merchandisers in Claude dot A I, by engineers in Claude Code, and by an internal returns app. Two: a single customer-facing support product needs two internal lookup tools, and no other client will ever use them. Three: a procurement agent needs a risk assessment from the finance team's supplier-risk agent, which reasons over data the procurement team cannot access. [pause]

SAM: One is M C P: three clients, one server. Two is direct A P I tool use: a protocol layer buys nothing for one product. Three is agent-to-agent: you delegate the assessment to their agent through its interface. Handing your agent the finance team's database credentials would be capability bloat and an authorization bypass in one move. [sting]

## Progressive discovery

ALEX: Last task statement. Progressive discovery versus monolithic context.

SAM: Monolithic puts everything into the prompt at once: full documents, full history, every tool. It earns its place for bounded tasks with predictable inputs, stable prefixes that benefit from prompt caching, and reasoning that genuinely needs all the material at once.

ALEX: Where does it break?

SAM: Anywhere context accumulates turn over turn. Cost and latency scale with input length, and attention can degrade well before the hard limit. Progressive stages the context: retrieve just in time, summarize across turns, load only what the next step needs. The course calls it the right default for most production workloads.

ALEX: And its weaknesses?

SAM: Tasks that need long-range coherence, decisions that hinge on a detail dropped earlier, and caching, which is harder when the carried-forward context changes each turn.

ALEX: How does discovery apply to capabilities rather than documents?

SAM: Skills are the cleanest example. Only each Skill's name and description sit in context at the start. The full instructions load when Claude decides the Skill is relevant, and linked reference files load only when needed. Tool definitions can be deferred the same way, loaded only when the model searches for them.

ALEX: So progressive discovery fixes capability bloat?

SAM: No, and that's a lovely distractor. Deferring a tool's definition saves context and can sharpen tool selection. It doesn't remove the permission. A deferred refund tool is still a refund tool. Least privilege decides what the agent can do. Discovery decides when it learns about it. And from Domain five: a Skill is bundled code, so audit it, sandbox it, and source it from a vetted registry.

SAM: Pause here and answer before we go on. Choose two. A public-sector benefits agent has all forty casework procedures pasted into its system prompt, plus definitions for thirty tools, on every call. Most cases use two or three procedures. Tool selection accuracy is slipping and per-call cost keeps rising. Which two changes best address this?

SAM: Option A: package each procedure as a Skill, so only its description loads until a case needs it. Option B: move to a model with a larger context window. Option C: defer tool definitions so they load only when the agent needs them, keeping a small stable prefix that can be cached. Option D: cut each procedure to its first paragraph to save tokens. Option E: fine-tune a model on all forty procedures. [pause]

SAM: A and C. Both stage context so each step carries what it needs, and the small stable prefix still gets the caching benefit from Domain two. B treats the window as a target, when the window is a ceiling, and attention degrades before you reach it. D is the blunt cut that loses required content. E skips the course's order of operations: try prompting and context design before fine-tuning. [sting]

## Cold open: the verdict

ALEX: Now the H R assistant.

SAM: C is right. Identity comes from the server, and the tool enforces authorization with that verified identity. It cannot return a record the user isn't entitled to, whatever the model is persuaded to do.

ALEX: And B, the classifier I liked?

SAM: B is a compensating control at the wrong layer. The service account still reads every record, so the data is already in the context window, and a name filter misses salary figures and paraphrases. A asks the model to enforce authorization, and "unless they say they're a manager" reads role from the user turn. D is detective: weekly review finds a leak a week late. [sting]

## Five to remember

ALEX: Five to remember. I'll start. Remove, don't watch. If the role doesn't need a tool, take it out and record why. Logging, confirmations and prompt instructions are compensating controls.

SAM: Two. Identity comes from the server, never from the user turn. Authorization is deterministic and lives in code at the tool and retrieval layer. Never trust the model to enforce it.

ALEX: Three. The context window is not a governance boundary. Necessity decides what goes in, a reference I D beats the full field, and redaction happens before the call.

SAM: Four. M C P when the same tools serve several clients. Direct A P I tool use when they serve one product. Agent S D K for a multi-turn loop in your own product. Agent-to-agent when the other side is an agent you delegate to. Claude Code is never a product backend.

ALEX: Five. Progressive is the production default. Monolithic wins for bounded, stable, cacheable content. And discovery decides when a capability loads, never whether the agent should have it.

## Recap: the exam tells

SAM: Before the tease, a test. Pause and name the four task statements this episode covered, and the giveaway for each. [pause]

ALEX: Capability bloat. Authentication, authorization and data handling. Connection mechanisms. And progressive discovery versus monolithic context.

SAM: Now as exam tells. If a role never uses a tool, think remove it and record why. If the role genuinely needs a dangerous tool, think keep it and gate it with deterministic authorization and a human checkpoint.

ALEX: If the user's message claims a role, like "as a manager", think unverified. Identity comes from the server.

SAM: If tools connect through one broad service account, think authorization bypass, fixed in code at the tool and retrieval layer.

ALEX: If an option says no change is needed because the vendor doesn't retain content, think of your own application logs. And if a field isn't needed for the language task, pass a reference I D and redact before the call.

SAM: If the same tools must serve several Claude clients, think M C P. One product, direct A P I tool use. An agent owned by another team on the other side, agent-to-agent. Claude Code as a product backend, wrong.

ALEX: If every procedure and tool definition is pasted into every call and tool selection is slipping, think Skills and deferred tools.

SAM: And if an option claims deferring a tool removes the risk, think again. Discovery decides when a capability loads, not whether the agent should have it.

SAM: Next episode, Integration part two: chunking and indexing for rag, matching retrieval to the shape of your data, the accuracy-latency trade-off, and what to monitor once all this is live.
