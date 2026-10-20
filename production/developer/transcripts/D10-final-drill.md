---
episode: "D10"
series: "CCDV-F"
slug: final-drill
title: "Developer final drill"
description: "Thirty-seven quick items across all eight Developer Foundations domains in blueprint proportion, Applications and Integration first and most, then the distractor families this series keeps meeting, exam day in brief, and one last retrieval pass."
domain: "All domains"
weight: "100%"
target_minutes: 18
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode ten, the final drill, for the night before.

ALEX: No new material?

SAM: None. By the end you'll have answered thirty-seven quick items across all eight domains, in exam proportions, and know which episode to replay in the morning. You'll name the distractor families this series keeps meeting and say why each loses. Then exam day in a few lines, and a tell for every domain.

ALEX: Applications and Integration is a third of the paper, so it goes first and gets the most. And tonight is about speed of recognition.

SAM: Then here is how it runs. [sting]

## Drill: applications and integration

SAM: You answer in the pause, then Alex answers. A miss gets one line to fix it. Tally by domain; the one you miss most is your only replay tomorrow.

ALEX: And on the paper they're shuffled, with no labels.

SAM: So answer from the stem, not the heading. Applications and Integration, thirty-three percent, thirteen items.

SAM: An inventory tool times out inside your agent loop. Your code catches the exception and sends nothing back. What should go to Claude? [pause]

ALEX: A tool result with the same tool use I D, first in the next user message, carrying the error text with is error set to true.

SAM: A nightly batch of thirty thousand requests comes back entirely errored, because of one malformed parameter. How do you catch it before the next run? A, split it into smaller batches. B, send one request of that shape through the Messages A P I first. C, move the job to synchronous calls. D, retry every errored result. [pause]

ALEX: B. Batch parameters are validated asynchronously, so the error only shows when the whole batch ends.

SAM: A tax assistant caches a long system prompt. Users reply about every twenty minutes, and almost every reply shows a fresh cache write. Which lifetime? [pause]

ALEX: Stay on five minutes. A one-hour write costs twice base input; five minutes costs one and a quarter.

SAM: Per write, yes. But a five-minute entry expires before each reply, so you pay a write every turn. A gap past five minutes and under an hour is the one-hour tell.

SAM: For each statement, say true or false. A service attaches a two-hundred-page scanned manual as base sixty-four in turn one of every conversation. One: that payload rides along in every later request. Two: uploading it once to the Files A P I and sending its file I D keeps requests under the size limit. Three: a file I D restricts the file to the user who uploaded it. Four: resending history is the application's job, because the Messages A P I keeps no session. [pause]

ALEX: True, true, false, true.

SAM: All four. Uploaded files are visible to the whole workspace, so a file I D is not access control.

SAM: A team wraps every S D K call in its own three-attempt retry loop. One rate-limit failure now becomes up to nine calls. Fix? [pause]

ALEX: Drop the outer loop and configure the S D K's retries. It already retries twice with backoff and honours retry-after.

SAM: A Python web service calls the synchronous client inside an async framework. One long generation, and every other user on that worker waits. [pause]

ALEX: The async client, Async Anthropic, so the worker keeps serving while the call waits on the network.

SAM: A Claude Code session has just written a payment-retry module. Who reviews the diff? [pause]

ALEX: A fresh context: a second session or a subagent, against stated criteria. The writer fixes what comes back, and a human approves the merge.

SAM: A ticket classifier's schema has an enum of eight categories. New kinds of ticket keep landing in whichever category is nearest. [pause]

ALEX: Add an "other" value with a detail field, so what doesn't fit has an honest place to go.

SAM: A support app built on the Messages A P I quotes one customer's order back to a different customer. [pause]

ALEX: Keep each user's history separate. The A P I is stateless, so whatever leaked, the application sent.

SAM: You want a formatting plugin in every project on your machine, and nobody else should get it. Which scope? [pause]

ALEX: User scope, in your home directory's settings. Project reaches the whole repository; local is you in this repository only.

SAM: An auditor asks which prompt and which model produced last month's credit summaries, and nobody can say. What was missing? [pause]

ALEX: The system prompt in version control beside the pinned model I D it was tested on, with an eval run gating each change.

SAM: A requirements list includes a ninety-nine point nine nine percent availability target, and nobody can find the business statement it came from. [pause]

ALEX: Trace it or challenge it. A requirement nobody can trace is an assumption someone liked.

SAM: Three months after launch, a claims summariser's quality is slowly drifting. Which life-cycle activity owns it? [pause]

ALEX: Maintain. Plan a redesign.

SAM: Operate: monitor output quality, cost and errors in production. Maintenance is planned change, such as a model deprecation. Two or more misses in this block, and episodes one to four are your replay. [sting]

## Drill: models, tokens and cost

SAM: Model Selection and Optimization, sixteen point eight percent, six items.

SAM: A team budgets a new model by dividing character counts by three and a half. The bill comes in well over. [pause]

ALEX: A newer tokenizer produces roughly thirty percent more tokens for the same text. Count with the token counting endpoint, for the model you'll actually use.

SAM: Code that sets a manual thinking budget starts failing after a move to a newer model. [pause]

ALEX: On newer models the manual budget is deprecated or rejected. Use adaptive thinking, and steer depth with effort.

SAM: A report generator sets a very large max tokens on a non-streaming call, and the S D K rejects the request. [pause]

ALEX: Stream it. The S D Ks reject a non-streaming request expected to run past ten minutes.

SAM: An Opus orchestrator hands hundreds of simple lookup-and-extract jobs to subagents, and the subagents are most of the bill. Which tier for them? [pause]

ALEX: Haiku, checked against the eval. Fastest and cheapest, and sub-agents are among its documented uses. Opus keeps the orchestration.

SAM: A cost dashboard adds up input tokens and output tokens, and cached requests look almost free. What's missing? [pause]

ALEX: Input tokens is only what follows the last breakpoint. Total input adds cache creation and cache read input tokens.

SAM: A job fires fifty parallel requests that share one long cached prefix, and every one of them writes the cache. [pause]

ALEX: An entry exists only once the first response begins. Send one request first, then the rest. Misses here send you back to episodes one and five. [sting]

## Drill: agents, prompts and context

SAM: Agents and Workflows, fourteen point seven percent, five items.

SAM: A telecom's inbound messages fall cleanly into four kinds: billing, outage, cancellation and sales, each with its own fixed handling. Which architecture? A, an autonomous agent holding every team's tools. B, a routing workflow: classify, then send each message down its fixed path. C, a supervisor with four subagents that agree who owns each message. D, one call with every team's procedures in the prompt. [pause]

ALEX: A. One agent with every tool handles whatever arrives, including the fifth kind next quarter.

SAM: B. Clean categories with fixed handling is the routing tell; the path is known, so it lives in code. A buys variance, C buys three to ten times the tokens, D pastes every procedure into every call. That is the oversized family: more machinery than the stem asks for.

SAM: An Agent S D K agent loops all night on one stubborn ticket and runs up the bill. Which two loop controls? [pause]

ALEX: A maximum number of turns, and a maximum budget that stops the loop at a spend threshold.

SAM: A Pre Tool Use hook must block writes to the infrastructure folder. The developer sets its matcher to that folder's path, and nothing is ever blocked. [pause]

ALEX: Matchers match tool names, not paths. Match the write tools, then check the path inside the hook.

SAM: With the memory tool, who actually reads and writes the memory files? [pause]

ALEX: Your application. It runs client-side: Claude requests the operation, and your code executes it against storage you control.

SAM: A team on an agent framework can't explain a bad answer, because nobody has seen the prompt that reached the model. [pause]

ALEX: Look underneath it at the actual prompts and responses. Anthropic's advice: start with the A P I directly, and know what any framework does underneath.

SAM: Prompt and Context Engineering, eleven percent, four items.

SAM: After compaction, a mortgage agent still has the case, but the applicant's exact loan reference has become "a reference number". [pause]

ALEX: Persist the facts that must survive outside the window, in a notes file or the memory tool, and read them back after the summary.

SAM: A pipeline fishes JSON out of free text with a regular expression for the first brace, and crashes on bad records. [pause]

ALEX: Parse against a schema with a library such as Pydantic or Zod. On failure, retry once or twice with the validation error, then route to a human queue.

SAM: After a model upgrade, an assistant refuses harmless requests. Its prompt carries three defensive lines written for the old model. [pause]

ALEX: Reread the old patches and change one thing at a time against the eval set. A patch for an older model's weakness can make a newer one over-cautious.

SAM: A due-diligence assistant answers fluently from a hundred-page agreement, and some answers cite clauses that don't exist. [pause]

ALEX: Have it extract exact quotes first and answer from them, withdraw any claim it can't support, and let it say it doesn't know.

SAM: Misses here: episode six for agents, seven for prompts. [sting]

## Drill: tools, security, Claude Code and debugging

SAM: Tools and M C P, ten point six percent, four items.

SAM: For each tool, say who executes it: your code, or Anthropic. One, web search. Two, the bash tool. Three, the memory tool. Four, code execution. [pause]

ALEX: Anthropic, your code, your code, Anthropic.

SAM: All four. Bash and memory have schemas Anthropic defines and your code runs; web search and code execution are server tools.

SAM: A Python M C P server's search tool keeps getting called for the wrong jobs. Its docstring says "helper". [pause]

ALEX: The Python S D K builds the tool description from the docstring, so rewrite it: what it does, when to use it and when not, its parameters, and what it returns.

SAM: Choose two. A knowledge-base M C P server must serve forty engineers' Claude Code sessions and a customer-facing A P I application, from one deployment. Which two fit? A, streamable H T T P, with OAuth for authentication. B, stdio, launched on each engineer's machine. C, the A P I application reaches it through the M C P connector, with no M C P client code of its own. D, the server's token written into the project's dot M C P dot json. E, a copy of the server's logic as a custom tool inside the A P I application. [pause]

ALEX: A and D. Remote transport, and the shared project file.

SAM: A and C. D is the right file with the wrong contents: credentials go in as environment-variable placeholders, never the secret. B is local, one client per server. E copies the logic the server exists to share. One wrong clause sinks the option.

SAM: A team plans to write its own web search tool for an A P I agent that needs public web results. [pause]

ALEX: Don't. Web search is a built-in server tool. Build only what built-ins can't reach, such as internal systems.

SAM: Security and Safety, eight point one percent, three items.

SAM: A pricing assistant's system prompt holds the company's proprietary discount formula, and a user has coaxed part of it out. [pause]

ALEX: Add an instruction never to reveal or paraphrase the system prompt.

SAM: That guards a secret with words, and leak-proofing can degrade the main task. Take the formula out of the prompt and compute it on the server. The polite instruction again.

SAM: A reporting agent only ever reads sales data, and it connects with the admin connection string. [pause]

ALEX: Least privilege, decided at design time: a read-only database role.

SAM: Claude Code must never read the project's dot env file. [pause]

ALEX: A Read deny rule for that file in settings. Deny is checked first and holds in every permission mode, bypass included.

SAM: Claude Code, three point one percent, one item. You want to reopen a specific session from last Tuesday, not the most recent one. [pause]

ALEX: Resume, with that session's I D. Continue picks up the most recent.

SAM: Debugging, two point six percent, one item. After a team attaches forty scanned pages inline, calls fail with a four thirteen, and they add retries. [pause]

ALEX: Four thirteen means the request is too large: fix it, don't retry. Fewer pages per request, or upload once and reference the file I D.

SAM: Misses here: eight for tools, nine for security and debugging, four for Claude Code. [sting]

## The distractor families

SAM: Now the families, the wrong answers this series kept meeting. I name it, you give the reason.

SAM: It reaches for a bigger model, a larger context window, fast mode or max effort, with no capability gap in the stem.

ALEX: Faster or bigger. Find the cause first: a missing prompt, stripped thinking blocks, raw tool output, a moving alias.

SAM: It asks nicely: capitals, a CLAUDE dot md line, a system-prompt rule, where the stem says must never.

ALEX: The polite instruction. Must never means a control: a deny rule, a hook, or a check in the tool's own code.

SAM: It pastes data in: the catalogue, yesterday's transcript, every procedure on every call.

ALEX: Pasted data instead of access. Live data needs a tool, a shared capability an M C P server, occasional know-how a Skill.

SAM: It retries what the status code says to fix.

ALEX: Four hundred, four oh one and four thirteen mean fix the request. Back off on four twenty-nine, five hundred and five twenty-nine. And no retry finds a value the source never had.

SAM: It watches the risk: a log, an alert, a page to on-call, fewer people with repository access.

ALEX: Detective or compensating. It reports the damage, or narrows who sees the secret. Prevent at the action, and remove the secret.

SAM: It takes a good rule past its scope: approval on every read, plan mode for a rename, clear after every prompt, a hook for naming style.

ALEX: Each rule has a trigger: irreversible actions, uncertain multi-file changes, unrelated tasks, must-never behaviour. No trigger, no rule.

SAM: It builds more than the cause needs: an agent for fixed steps, an M C P server for one app, a new transport for a print statement.

ALEX: Oversized. Pick the lightest pattern that meets the trigger.

SAM: It trusts what the model says about itself: a confidence field, "I double-checked".

ALEX: Self-report is more generated text. Route on what you can verify in code or against the source.

SAM: It has the right mechanism with one wrong detail: a token in the shared M C P file, the shared settings file for a personal preference, third-party text in the system prompt.

ALEX: Strike any option with one wrong clause, however good its first half.

SAM: And it names a flag, a field or a feature you have never met.

ALEX: Strike it. If neither the guide nor the docs named it, it isn't the answer. [sting]

## Exam day logistics

ALEX: Tomorrow, briefly.

SAM: Photo I D, government-issued, unexpired, the name exactly as registered: by the door tonight. Clear desk; no phone, smart watch or headphones. Online, stay in webcam view. Arrive early; missing the late-arrival window forfeits the fee.

ALEX: On screen?

SAM: Accept the confidentiality agreement. Write the noteboard: count, constraint, mechanism, strike. The clock counts down: item eighteen at one hour twenty-three left, thirty-five at forty-seven, fifty-three at ten. Past two minutes, best answer, flag, move on. Dropdowns, each statement alone. Leave nothing blank.

ALEX: And the morning?

SAM: Episode eleven, and the recap of your weakest domain. Nothing new. [sting]

## Final retrieval

SAM: One last pass. Pause and name the eight domains in weight order, and the domain you missed most tonight. [pause]

ALEX: Applications and Integration, Model Selection and Optimization, Agents and Workflows, Prompt and Context Engineering, Tools and M C Ps, Security and Safety, Claude Code, then Eval, Testing and Debugging. My misses were spread, and two were the oversized family.

SAM: Now one tell per domain. Applications and Integration: if every turn writes the cache, look for changing content before the breakpoint, or a gap past five minutes.

ALEX: Models: a quality bar, a latency and a volume mean the smallest tier that clears the bar. Old requests failing on a new model mean a breaking change.

SAM: Agents: same steps every time, a workflow; steps nobody can predict, an agent with a turn limit and a budget. Must never, a Pre Tool Use hook that checks the path inside.

ALEX: Prompts and context: if quality falls as the session grows, prune and compact, and persist what must survive. If it parses but the values are wrong, validate in code.

SAM: Tools: a wrong tool picked means descriptions. Several apps, one M C P server; one app, a custom tool; occasional know-how, a Skill.

ALEX: Security: injected text near a real action means a check at the action. A secret in a prompt comes out of the prompt.

SAM: Claude Code: who it reaches and when it loads; unattended means dash p. Debugging: fix four hundreds, back off on four twenty-nines, and check what reached the model before blaming it.

ALEX: And the pace: one twenty-three, forty-seven, ten.

SAM: You've worked every domain on the paper. Sleep now; it will do more for your score than another hour.

ALEX: Good luck to everyone sitting it.

SAM: Read the question on the page, and pick the purpose-built mechanism for the constraint it states.
