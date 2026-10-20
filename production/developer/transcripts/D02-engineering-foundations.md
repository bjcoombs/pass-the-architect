---
episode: "D02"
series: "CCDV-F"
slug: engineering-foundations
title: "Software engineering for Claude applications"
description: "REST, JSON and status codes under every Claude call, what the official S D K does for you, async concurrency inside rate limits, server-sent events versus websockets, and version control, C I, code review and refactoring with Claude Code."
domain: "Applications and Integration; Model Selection and Optimization"
weight: "7.4% and 6.1%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode two: software engineering for Claude applications.

ALEX: What do I walk away able to do?

SAM: Read a Claude A P I call as plain REST and JSON, and tell an error you retry from an error you fix. Say what the official S D K does for you, so you stop rebuilding it. Run many calls at once with async code without tripping rate limits, and put server-sent events and websockets in the right place in a streaming app. And use version control, C I, code review and refactoring with Claude Code the way the exam expects.

ALEX: Two skills, seven point four and six point one percent. Together that is about seven items, more than the whole Claude Code domain.

SAM: And each one looks like ordinary engineering, which is the trap. We start with an item. [sting]

## Cold open: the catalogue import

SAM: A retail team's service writes product descriptions with Claude. When a catalogue import lands, the code uses the async client to fire five thousand requests at once. The products go live within the hour, so the descriptions must be ready by then. About half the calls fail with a four twenty-nine rate limit error. What is the best fix? Option A, cap how many requests are in flight at once, sized to the organisation's rate limits, and let the S D K's built-in retries honour the retry-after header. Option B, wrap every call in a loop that retries immediately until it succeeds. Option C, move the job to the Message Batches A P I. Option D, switch to the largest model so each request does more.

ALEX: C. Five thousand requests in one job, and episode one said volume goes to batch.

SAM: Hold that. We come back to it at the end.

SAM: Here is what the guide names. Software engineering foundations: REST A P Is, JSON, asynchronous programming, version control, S D L C integration, code review, and small and large refactoring. Technical fundamentals: integrating with S D Ks that wrap REST A P Is, and websockets.

ALEX: So no questions on how git works in general.

SAM: Assume not. Expect a Claude application with an ordinary engineering fault, and four fixes that differ in whether they use the mechanism built for it.

SAM: Segment one, REST and JSON. Under every S D K call sits one H T T P request: a POST to slash v one slash messages on api dot anthropic dot com. Three headers matter: your A P I key, an anthropic-version header, and content-type application JSON. The body is JSON too: the model, max tokens, and a list of messages.

ALEX: And the response comes back as JSON.

SAM: With a shape you must respect. Content is a list of blocks, each with a type: text, tool use, thinking. A stop reason says why generation ended: end turn, max tokens, tool use, and a few others. A tool use block carries its input as a JSON object, already shaped by the schema you gave.

ALEX: I read content zero dot text and move on. Every response in my chat app has had one text block.

SAM: For plain chat with no tools and no thinking, that usually holds.

SAM: But add tools or thinking and the first block may not be text. And when the stop reason is max tokens, the output was cut off, so the JSON you asked for may be missing its closing brace. Defensive parsing means checking the block type and the stop reason before you parse.

ALEX: What should catch my eye?

SAM: "Fails to parse now and then", or "broke when we added a tool". Pick the option that checks block types and the stop reason, not the one that adds "always return valid JSON" to the prompt.

SAM: Errors are JSON as well: a type, a message, and a request I D. The status code tells you what to do. Four hundred, invalid request: the request is wrong, so fix it. Four oh one, authentication, and four oh three, permission: fix the key or its access. Four twenty-nine, rate limit, and five hundred, an internal error: retry with exponential backoff. Five twenty-nine means the A P I is overloaded: retry with backoff as well.

ALEX: Why not retry everything? One wrapper, no branching, and a retry that fails again costs nothing.

SAM: For transient errors that wrapper is exactly right, and it is less code.

SAM: But a four hundred fails the same way every time. Retrying it spends requests against your rate limit, delays the real error and hides a bug in your request. The status code has already told you which kind you hold.

ALEX: The tell?

SAM: "Invalid request", "authentication" or "permission": fix, don't retry. Rate limit, overloaded or server error: back off and retry.

SAM: Pause here and answer before we go on. For each statement, say true or false. A Claude application logs four failures. Statement one: a four hundred invalid request error should be retried with exponential backoff. Statement two: a four twenty-nine that carries a retry-after header should be retried after waiting that many seconds. Statement three: a five twenty-nine overloaded error should be retried with backoff. Statement four: a four oh one authentication error usually clears if the application retries a few times. [pause]

ALEX: False, true, true, false.

SAM: All four. One: an invalid request fails the same way on every attempt, so fix the request. Two: retry-after tells you exactly how long to wait. Three: overloaded is transient, so back off. Four: a bad or revoked key stays bad; fix the credential, and in production, alert someone. [sting]

## Segment two: SDKs that wrap REST

SAM: Segment two, the technical fundamentals skill: integrating with S D Ks that wrap REST A P Is. Anthropic ships official client S D Ks, Python and TypeScript among them. Know what the wrapper does, because exam options often offer to rebuild it. It sets the key, version and content-type headers for you, and types requests and responses. It retries connection errors, rate limits and server errors automatically, twice by default, with exponential backoff, honouring retry-after. In Python a request times out after ten minutes by default; both settings are configurable. It raises typed exceptions, such as a rate limit error or an authentication error, rather than handing you raw JSON. It exposes the request I D on its responses. And its streaming helpers assemble the final message for you.

ALEX: Let me argue for raw H T T P. One less dependency, I see every byte, and I know exactly which retries happen because I wrote them.

SAM: Seeing the wire is useful. Curl is a good way to debug a header or a body.

SAM: But in an application you would rebuild the retries, backoff, timeouts and types the S D K already provides, and get some of it wrong. And teams that keep the S D K often add their own retry loop on top, so each failure is retried several times over.

ALEX: So my three attempts wrap its three attempts. Nine calls for one failure.

SAM: Nine. The tell: "hand-written H T T P client", "custom retry loop", or "parses the error message text". The answer uses the official S D K, configures its retries, and catches typed exceptions, most specific first, instead of matching message strings.

SAM: One more habit. Log the request I D from every failure. Support needs it to trace a specific request, and it ties your own logs to the failing call.

SAM: Pause here and answer before we go on. Choose two. A field service company's dispatch assistant calls the Claude A P I through a hand-written H T T P client. Two problems: its rate-limit handling broke when the wording of an error message changed, and Anthropic support asked for the identifier of a failing request that the team never stored. Which two changes fix these at the root? A, move to the official S D K and catch its typed rate limit exception instead of matching message text. B, record the request I D from each failed response in the application logs. C, add more phrases to the message-matching code so it catches new wordings. D, set the S D K's retries to zero and retry forever in application code. E, switch to a larger model so fewer requests fail. [pause]

ALEX: A and B.

SAM: Both. A removes the dependency on wording, because typed exceptions follow the status, not the prose. B stores the I D support asked for. C patches the symptom and breaks on the next wording change. D throws away backoff and retry-after for an endless loop. E is "bigger" applied to a plumbing fault. [sting]

## Segment three: async, streaming and websockets

SAM: Segment three, asynchronous programming. A call to Claude spends most of its time waiting on the network, and synchronous code blocks while it waits. Async code, with async and await, lets one process keep many calls in flight, or keep a web server answering other users while one generation runs.

ALEX: And the S D K has an async client.

SAM: In Python it is Async Anthropic, with the same interface as the sync client; in TypeScript, calls already return promises. The textbook fault is a sync client inside an async web framework: one slow generation stalls every other request on that worker.

ALEX: So async everything, gather it all, let it fly. Fastest wall-clock time there is.

SAM: Concurrency is the right tool for latency-bound, interactive work.

SAM: But rate limits are measured in requests per minute, input tokens per minute and output tokens per minute, and the A P I enforces them with a token bucket that refills continuously. A short burst can exceed the limit even when your per-minute average would not. Unbounded fan-out turns a fast job into a wall of four twenty-nines.

ALEX: Tell?

SAM: "Fires all the requests at once", "bursts", "half of them fail with four twenty-nine". The fix is concurrency you control, not more of it. And recall episode one: when the stem says cost first and results tomorrow, async gives way to the Batch A P I.

SAM: Now streaming, which is where websockets come in. With stream set to true, the Messages A P I answers with server-sent events: one long H T T P response that the server writes to, event by event. Message start, then each content block's start, deltas and stop, then message delta and message stop. Ping events can arrive in between.

ALEX: One way, then. Server to client.

SAM: Yes. A websocket is different: a persistent, two-way connection where either side can send at any time. The Messages A P I streams over server-sent events, not websockets. Websockets belong in your own architecture, typically between a browser and your backend, when the user must send something mid-stream, such as a stop button.

ALEX: Anything else in the stream that bites?

SAM: Two things. An error can arrive as an event after the response has already returned two hundred, an overloaded error for example, so the status code alone is not enough. And a tool call's input streams as fragments of a JSON string: accumulate them and parse when that block's stop event arrives, or let the S D K's helpers do it. Parsing each fragment as it lands fails.

ALEX: The guide mentions sockets under M C P too.

SAM: Episode eight goes deeper. M C P's standard transports are stdio and streamable H T T P, which can use server-sent events. A websocket would be a custom transport.

SAM: Pause here and answer before we go on. A healthcare provider's patient-portal assistant must show Claude's reply as it is written, and let the patient press stop mid-answer. The front end is a single-page web app. What is the best design? A, the browser holds a websocket to the provider's backend; the backend keeps the A P I key, calls the Messages A P I with streaming, relays the events, and closes the stream when stop arrives. B, ship the A P I key in the front-end code so the browser calls the Messages A P I directly. C, make a non-streaming call and have the browser poll every second until the reply is ready. D, open a websocket from the browser straight to the Messages A P I to remove the backend hop. [pause]

ALEX: D. Shortest path. Every hop you remove is latency you never pay, and stop just closes the socket.

SAM: That is the "faster" distractor wearing a protocol name. The Messages A P I streams over server-sent events; the websocket D relies on is not what it offers. And going direct from the browser puts the key on every patient's device.

ALEX: Which is B's problem too.

SAM: B leaks the key outright; episode nine covers why secrets stay server side. C gives up streaming, so the patient sees nothing until the end and has nothing to stop. A is right: two-way where you need it, browser to backend; server-sent events where the A P I provides them; and the key never leaves the server.

ALEX: Tell?

SAM: "Browser", "front end" or "mobile app" anywhere near the A P I key. The answer puts a backend between the client and Claude. [sting]

## Segment four: version control, CI, review and refactoring

SAM: Segment four, starting with version control. In a Claude application, the files that shape behaviour are code: prompt files, the project CLAUDE dot md, the project settings dot json in the dot claude folder, and the dot M C P dot json that lists shared servers. Commit them and review them in pull requests. Episode four covers prompt versioning and model pinning.

ALEX: And the key stays out.

SAM: Always. The S D K reads the A P I key from an environment variable. Locally it can sit in a dot env file that git ignores; in C I it is a repository secret the workflow references by name.

ALEX: Our repo is private. Is a key in the workflow file really a problem?

SAM: Private narrows who can see it today, and plenty of teams have got away with it.

SAM: But the key now lives in every clone and in history, and deleting the line later does not revoke it. The exam treats any committed secret as a leak. The tell is "committed", "hard-coded" or "in the workflow file": the answer moves it to a secret store and rotates the key.

SAM: Two points from Claude Code. Checkpoints rewind its file edits, but only edits made through its editing tools, not shell commands, so they do not replace git. And git worktrees let parallel Claude Code sessions work on separate branches without their edits colliding.

SAM: S D L C integration. Claude Code runs non-interactively with claude dash p, for C I jobs, pre-commit hooks and scripts, with a JSON output format a pipeline can parse. On GitHub, the Claude Code GitHub Action answers an at-claude mention on an issue or pull request, or runs a fixed prompt on a repository event. Give the workflow only the permissions it needs, cap its turns, and review its changes before merging.

ALEX: Code review, then. Claude just wrote the change in my session. It knows the code best, so I ask that session to review it.

SAM: It holds the context, and for a quick sanity check that is fine.

SAM: But Claude Code's own guidance is that a fresh context reviews better, because it is not biased toward code it just wrote. The pattern is writer and reviewer: one session writes, a second session or a subagent reviews the diff against stated criteria, and the writer fixes what comes back. A human still approves the merge.

ALEX: Tell?

SAM: "Independent review", "fresh context", or "reviewing its own work". Pick the separate reviewer.

SAM: Refactoring last, small and large. Small: if you could describe the diff in one sentence, a rename or a log line, ask Claude to make it directly, keep behaviour the same, and run the tests.

ALEX: I'd still use plan mode every time. Read first, then edit. Safer is safer.

SAM: That rule has outrun its scope. Plan mode adds overhead, and Claude Code's guidance says skip it when the scope is clear and the change is small. It earns its place when the approach is uncertain, the change touches many files, or the code is unfamiliar.

SAM: Which describes large refactoring. Plan mode first: Claude reads and proposes, and edits nothing until you approve. Make sure tests exist, because a check Claude can run is how it knows it has finished. Then work in small, testable increments. For a change across hundreds of files, fan out: generate the file list, loop over it calling claude dash p with the needed tools pre-approved, try two or three files first, refine the prompt, then run the rest.

SAM: Pause here and answer before we go on. A bank must move four hundred services from a deprecated internal logging client to its replacement. Behaviour must not change, and the team wants every change reviewable. What is the best approach? A, one interactive session with the prompt "migrate every service", relying on Claude Code's checkpoints to undo anything that goes wrong. B, plan the migration in plan mode, confirm tests cover the logging paths, then run a scripted claude dash p loop with only the needed tools pre-approved, on two or three services first, refine, and run the rest as reviewable changes. C, switch to the model with the largest context window so all four hundred services fit in one session. D, ask each service owner to paste their code into a chat and apply the suggested changes by hand. [pause]

ALEX: B.

SAM: B. It plans before editing, makes behaviour checkable with tests, pilots before scaling, and keeps each change small enough to review. A trusts checkpoints that never see shell commands and are no substitute for git, and one giant session fills its context. C is "bigger" again; a larger context window does not make four hundred edits reviewable. D throws away the repository and the tests. [sting]

## Cold open: the verdict

SAM: Back to the catalogue import. Alex, you picked C, the Batch A P I.

ALEX: And the stem said the products go live within the hour.

SAM: That is the constraint that rules batch out. Batch is cheaper, but its results can take up to twenty-four hours, and nothing in the stem said cost first. The answer is A: cap the requests in flight, sized to the rate limits, so bursts stop draining the token bucket, and let the S D K's retries wait out retry-after on the few that still hit a limit. B hammers the limit harder and ignores retry-after. D changes nothing about how fast requests arrive.

ALEX: So the words that should have stopped me?

SAM: "Within the hour". Batch answers "overnight" and "cost first". A deadline in minutes, with four twenty-nines from a burst, points to controlled concurrency. [sting]

## Five to remember

SAM: Five to remember. One: a Claude call is REST and JSON. Content is a list of typed blocks; check the block type and the stop reason before you parse.

ALEX: Two: the status code decides. Invalid request, authentication or permission: fix it. Rate limit, overloaded or server error: back off and retry, honouring retry-after.

SAM: Three: use the official S D K. It retries twice by default with backoff, sets timeouts, raises typed exceptions and exposes the request I D. Don't rebuild it, and don't stack your own retries on top.

ALEX: Four: async for concurrency, capped to fit the rate limits. The Messages A P I streams over server-sent events, one way; websockets belong between your client and your backend, which keeps the key.

SAM: Five: commit prompts and Claude configuration, never keys. Run Claude in C I with claude dash p or the GitHub Action, review with a fresh context, skip plan mode for a one-sentence diff, and plan, test and pilot a large refactor before you fan out.

## Recap: the exam tells

SAM: Recall first. Pause and name the four segments, and the giveaway for each. [pause]

ALEX: REST and JSON, where the giveaway is the status code. S D Ks, where it's a hand-written client. Async and streaming, where it's a burst of four twenty-nines or a key in the browser. And version control through refactoring, where it's a committed secret or a one-shot migration.

SAM: Now as exam tells. If a response fails to parse only sometimes, think a max tokens stop or a first block that is not text.

ALEX: If the error says invalid request or authentication, think fix the request or the key. Retrying will not help.

SAM: If the code matches error message text or wraps its own retry loop, think the official S D K and typed exceptions. If support wants to trace a call, think the request I D.

ALEX: If every request goes at once and half return four twenty-nine, think capped concurrency. If the stem says overnight and cost first, think batch instead.

SAM: If an option opens a websocket to the Messages A P I, remember it streams over server-sent events. If the key appears in a browser or a workflow file, move it server side or into a secret store.

ALEX: If a session reviews its own code, think a fresh reviewer. A one-line rename, skip plan mode. Four hundred services, plan, test, pilot on a few, then fan out.

SAM: Next, episode three: designing Claude applications, from requirements through the system life cycle.
