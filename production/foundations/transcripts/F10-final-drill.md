---
episode: "F10"
series: "CCAR-F retake"
slug: final-drill
title: "Foundations final drill"
description: "About forty rapid-fire items across the five Foundations domains, weighted by the blueprint and by the last attempt's gaps, each set in one of the six scenarios, then the guide's named anti-patterns and a calm walk through exam day."
domain: "All domains"
weight: "100%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode twelve, the Foundations final drill.

ALEX: The one for the night before, and the morning of.

SAM: By the end you'll be able to answer about forty quick items across all five domains, in blueprint order: the agentic loop and coordinators, Claude Code configuration, prompts and structured output, tool design, and context and reliability.

SAM: Then you'll spot the guide's own anti-patterns on sight, and walk into exam day knowing what happens at the desk and on the screen.

ALEX: Every item sits in one of the six scenarios, because that is how the paper asks. I was four or five answers short; this is where I find out which domain still leaks.

SAM: Then here is how tonight works. [sting]

## Drill: agentic architecture

SAM: No new material tonight. About forty quick items, weighted like the paper and leaning on last time's gaps, each in a named scenario. You answer in the pause, then Alex answers.

ALEX: And when I get one wrong?

SAM: One line to fix it, and the miss pattern it fits. Tally misses by domain; the worst one is your only replay tomorrow morning: agents, episodes five to seven; Claude Code, two and three; prompts, four; tools, eight; context, nine.

ALEX: Choose-two rules?

SAM: Read how many first, then call every option true or false on its own. Agentic Architecture, twenty-seven percent, ten items.

SAM: Developer tools. The loop exits whenever a response contains text, so the agent stops after "let me check the imports" with a tool call pending. What should drive the loop? [pause]

ALEX: The stop reason. Continue while it is tool use, append the tool results to the history, and call again. Stop on end turn.

SAM: Support agent. Choose two. Which are anti-patterns for ending the loop? A, stopping when the stop reason is end turn. B, stopping when the reply contains "your issue is resolved". C, a cap of ten iterations as the main stopping rule. D, appending tool results before the next request. E, continuing while the stop reason is tool use. [pause]

ALEX: B and C: parsing natural language, and an arbitrary cap as the primary stop. The other three are the correct loop.

SAM: Research system. Every attempt by the coordinator to spawn a subagent is rejected. What is missing? [pause]

ALEX: "Task" in the coordinator's allowed tools. That is the spawning mechanism.

SAM: Research system. The synthesis subagent writes a report that ignores the search results. The coordinator assumed it could see them. Fix? [pause]

ALEX: Put the complete findings in its prompt, as structured data keeping source U R L, document name and page number beside each claim. Subagents inherit nothing.

SAM: Research system. The coordinator launches four search subagents, one per turn, and latency is poor. [pause]

ALEX: Emit all four Task calls in a single coordinator response, so they run in parallel.

SAM: Support agent. Policy sends refunds above five hundred dollars to a human. The prompt says so, and a six-hundred-dollar refund went through last week. [pause]

ALEX: A hook that intercepts the process refund call, blocks anything above the threshold and redirects to escalate to human. Guaranteed rule, so a hook, not a prompt.

SAM: Support agent. One M C P tool returns Unix timestamps, another I S O eight six oh one dates, and the agent compares them wrongly. [pause]

ALEX: A PostToolUse hook that normalizes the formats before the model sees the results.

SAM: Developer tools. "Add comprehensive tests to this legacy billing module." Fixed prompt chain, or dynamic decomposition? [pause]

ALEX: Prompt chain. Predictable and testable; that is what I would ship.

SAM: Dynamic: map the structure, find high-impact areas, then a prioritized plan that adapts as dependencies appear; chaining is for predictable reviews. Pattern one, instinct over the guide.

SAM: Developer tools. You resume yesterday's named investigation with dash dash resume, and two files changed overnight. What do you tell it? [pause]

ALEX: Name the two files for targeted re-analysis. If most of yesterday's results are stale, start fresh with an injected structured summary instead.

SAM: And to compare two refactoring approaches from that same analysis? [pause]

ALEX: Fork session: two independent branches from a shared baseline. [sting]

## Drill: Claude Code configuration

SAM: Claude Code Configuration, twenty percent, nine items.

SAM: Claude Code team. A new hire's sessions ignore the team's testing conventions, which live in a senior engineer's CLAUDE dot md in her home directory. [pause]

ALEX: User level, never shared. Move them to the project CLAUDE dot md, commit, and check with slash memory which files load.

SAM: Claude Code team. Choose two. Tests must run after every file edit, and the CLAUDE dot md line asking for it is followed most of the time. A, a PostToolUse hook on the file-edit tools that runs the affected tests. B, that hook in project settings, committed. C, the CLAUDE dot md line rewritten in capitals. D, a skill developers run after editing. E, the hook in your user settings. [pause]

ALEX: A and B. C is louder guidance, D needs someone to remember, E reaches only you.

SAM: Claude Code team. Nobody may edit the generated client folder. Simplest enforcement? [pause]

ALEX: A permission deny rule in settings. A PreToolUse hook only if the rule needs more precision than a pattern can give.

SAM: Claude Code team. Terraform conventions should load only when someone edits Terraform files. [pause]

ALEX: A file in dot claude slash rules whose YAML frontmatter paths field globs everything under the terraform folder.

SAM: Claude Code team. Which of these is NOT a reason to put a convention in a path-scoped rule in dot claude slash rules? A, it covers test files scattered across directories. B, it loads only when matching files are edited. C, the convention applies to every file, all the time. D, one glob matches files by type wherever they sit. [pause]

ALEX: B. Saving context is the whole point.

SAM: B is a reason. The answer is C: always-on universal standards belong in the root CLAUDE dot md. Pattern three, the true option picked on a NOT question.

SAM: Claude Code team. Choose two. A scaffolding skill must never run destructive commands, and developers keep invoking it without the component name. Which two frontmatter fields? A, allowed-tools. B, argument-hint. C, context fork. D, paths. E, a longer description. [pause]

ALEX: A and B. Context fork isolates verbose output, which is not the problem here.

SAM: Claude Code team. A single-file bug with a clear stack trace, and then a library migration touching about fifty files. Plan mode or direct for each? [pause]

ALEX: Direct for the bug. For the migration, plan mode to investigate and design, the Explore subagent for the verbose discovery, then direct execution of the plan.

SAM: Claude Code team. Two rounds of prose have not fixed a migration script's null handling, which turns out to interact with its default-value logic. A log wording issue is separate. [pause]

ALEX: Specific test cases: input with nulls, exact expected output. The interacting pair in one detailed message; the log wording separately.

SAM: C I pipeline. Review findings must be posted as inline pull request comments by a script. [pause]

ALEX: Dash p for non-interactive mode, with dash dash output format json and dash dash json schema, so the findings are machine-parseable. [sting]

## Drill: prompts and structured output

SAM: Prompt Engineering and Structured Output, twenty percent, seven items.

SAM: C I pipeline. The review prompt says "only report high-confidence findings", and false positives have not moved. [pause]

ALEX: Replace it with explicit categories: report bugs and security issues, skip minor style and local patterns.

SAM: C I pipeline. Choose two. Developers dismiss most naming suggestions and now ignore every finding. A, temporarily disable the naming category while improving its prompt. B, add a detected pattern field so dismissals can be analyzed. C, tell the model to be more conservative. D, post only findings seen in two of three runs. E, raise the severity threshold everywhere. [pause]

ALEX: A and C. Conservative is what I would write first.

SAM: A and B. "Be conservative" is the guide's own example of an instruction that fails to improve precision; pattern one. D suppresses real bugs that surface intermittently, and E punishes the categories that work.

SAM: C I pipeline. Detailed instructions are in place, and the comment format still drifts. [pause]

ALEX: Two to four few-shot examples showing the exact format: location, issue, severity, suggested fix.

SAM: Extraction. Choose two. Contracts lacking a governing-law clause get an invented one, and unlisted contract types land on the nearest listed type. A, make governing law nullable, absent means null. B, add "other" plus a detail string to the type enum, and "unclear" for ambiguous cases. C, make every field required. D, retry until the field has a value. E, a larger model. [pause]

ALEX: A and B. C causes the invention, D retries for information that is not there, and E is scale instead of structure.

SAM: Extraction. Strict schema through tool use, and invoice line items still do not add up to the total. [pause]

ALEX: The schema removes syntax errors, not semantic ones. Extract a calculated total beside the stated total and flag any gap, with a conflict-detected boolean.

SAM: Extraction. Choose two. Which failures will a retry carrying the specific validation error likely fix? A, a date in the wrong format. B, a value that exists only in an appendix nobody provided. C, values placed in the wrong fields. D, a field the source does not contain. E, a page missing from the scan. [pause]

ALEX: A and C. The rest is absent information. The retry carries the document, the failed extraction and the specific errors.

SAM: Extraction. An overnight Message Batches run loses forty documents to the context limit. And with a thirty-hour deadline and up to twenty-four hours of processing, how often do you submit? [pause]

ALEX: Resubmit only the forty, by custom I D, chunked. Submit every four hours: four of waiting plus twenty-four of processing fits inside thirty. [sting]

## Drill: tool design and MCP

SAM: Tool Design and M C P, eighteen percent, seven items.

SAM: Extraction. Three extraction tools, the document type is unknown, and sometimes the model answers in prose. Tool choice? [pause]

ALEX: Any. It must call a tool, and it can pick which.

SAM: Extraction. Choose two. Extract metadata must run before the enrichment tools. Which two? A, force extract metadata by name with tool choice on the first request. B, handle enrichment in follow-up turns once the metadata is back. C, tool choice any on the first request. D, a system prompt line saying always call extract metadata first. E, force extract metadata on every request. [pause]

ALEX: A and E. Forcing is the guarantee, so force it every time.

SAM: A and B. Forcing it on every request means enrichment never runs; pattern two, the right mechanism welded to the wrong scope. C lets it pick any tool, and D is guidance.

SAM: Developer tools. Two M C P tools, search docs and find docs, have near-identical descriptions, and the agent misroutes between them. [pause]

ALEX: Rename and rewrite so each says what it does, its input format, an example query, and when to use it instead of the other. Split or merge only if they truly overlap.

SAM: Developer tools. Choose two. The agent prefers Grep over a more capable M C P code-index tool, and the system prompt says "always search the files first". A, expand the M C P tool's description of capabilities and outputs. B, revise that keyword-sensitive instruction. C, remove Grep. D, a routing classifier. E, a larger model. [pause]

ALEX: A and B. C throws away the right tool for plain content search, D is over-engineering, and E is scale.

SAM: Research system. The search subagent hits a timeout. What happens first? [pause]

ALEX: It returns structured error context to the coordinator straight away.

SAM: First it retries locally, because a timeout is transient; only what it cannot resolve goes up, with what was attempted and partial results. Pattern four, a good rule applied one step too early.

SAM: Support agent. Process refund rejects a request outside the return window. What should the response carry? [pause]

ALEX: The is-error flag, a business category, retryable false, and a customer-friendly explanation the agent can pass on. And a valid empty result, like no orders found, is a success, not an error.

SAM: Developer tools. Choose two. A shared schema M C P server for the team, and one engineer's experimental server. A, the shared one in the project's dot M C P dot json, token as an environment-variable placeholder. B, the experimental one in the dot claude dot json in that engineer's home directory. C, the experimental one in the project file. D, the shared one in each user's config. E, the literal token in the project file, since the repository is private. [pause]

ALEX: A and B. Tools from both servers are discovered at connection time and available together. [sting]

## Drill: context and reliability

SAM: Context Management and Reliability, fifteen percent, six items.

SAM: Support agent. After summarization, "a two hundred and forty-seven dollar refund on order eight eight one two, promised by Friday" has become "customer wants a refund". [pause]

ALEX: A persistent case facts block of amounts, dates, order numbers and statuses, in every prompt, outside the summarized history. And trim lookups to the relevant fields.

SAM: Support agent. Choose two. Which call for escalating now? A, the customer asks for a human. B, a competitor price match, when policy covers only your own site's prices. C, anger over a late delivery the agent can fix. D, get customer returns two accounts. E, self-rated confidence of four out of ten. [pause]

ALEX: A and D. Two possible accounts is an identity risk, so hand it to a person.

SAM: A and B. The stem never raised identity risk: two matches means asking for another identifier; pattern five, an imported constraint. C is sentiment, not complexity, so acknowledge it and offer the fix. E is uncalibrated self-report.

SAM: Support agent. When it does escalate, the human cannot see the transcript. [pause]

ALEX: A structured handoff: customer I D, root cause, refund amount, recommended action.

SAM: Research system. Two credible sources give different market sizes. [pause]

ALEX: Keep both, each annotated with its source, with publication dates so a difference in time is not read as a contradiction. The coordinator decides how to reconcile.

SAM: Developer tools. Hours into exploring, the agent talks about "typical patterns" instead of the classes it found earlier. [pause]

ALEX: A scratchpad file of key findings it refers back to, subagents for the verbose exploration, and slash compact when discovery output fills the context.

SAM: Extraction. Choose two. Accuracy is ninety-seven percent overall, and the team wants to drop human review. What comes first? A, accuracy by document type and field. B, ongoing stratified random sampling of high-confidence extractions. C, drop review now. D, route on raw model confidence with a fixed threshold. E, review everything forever. [pause]

ALEX: A and B. The aggregate can hide a document type that fails badly, and field-level confidence only routes well once it is calibrated on a labelled set. [sting]

## The anti-patterns

SAM: Now the guide's own anti-patterns. If the option does one of these, it is the trap. I name it, you give the reason.

SAM: It ends the loop by reading the model's words, checking for text, or treating an iteration cap as the main stopping rule.

ALEX: The stop reason decides. Tool use continues, end turn stops.

SAM: It enforces a business rule or a required order with a prompt instruction.

ALEX: Prompts have a non-zero failure rate. Hooks and prerequisite gates guarantee.

SAM: It returns "operation failed", or an empty result marked as success.

ALEX: The agent cannot choose a recovery. Category, retryable flag, explanation; empty only when the query truly found nothing.

SAM: It ends the whole workflow over one subagent failure.

ALEX: Recover locally, propagate what is left with partial results, and annotate the coverage gaps.

SAM: It escalates on sentiment or self-reported confidence, or picks the likeliest of several customer matches.

ALEX: Neither tracks complexity. Escalate on request, on policy gaps and on lack of progress. Ask for another identifier.

SAM: It asks the generating session to review its own work.

ALEX: An independent instance, without the generator's reasoning.

SAM: It fixes an uneven big review with a bigger model or a larger context window.

ALEX: Attention dilution. Per-file passes, then a cross-file integration pass.

SAM: It sends a blocking pre-merge check to the Batches A P I.

ALEX: Up to twenty-four hours with no latency guarantee, and no tool calls mid-request. Batch is for overnight and weekly work.

SAM: It retries for information the document lacks, or makes required a field the source may not have.

ALEX: Retry fixes format and structure. Absence needs a null.

SAM: It gives one agent eighteen tools, or the synthesis agent the full search kit.

ALEX: Four or five per role, plus a scoped cross-role tool for a frequent need.

SAM: It puts team configuration in someone's home directory, or a secret in the shared file.

ALEX: Team configuration in the project, committed. Personal in user scope. Secrets as environment-variable placeholders.

SAM: It picks one of two conflicting figures, or drops sources while summarizing.

ALEX: Annotate the conflict with attribution, and keep claim-source mappings through synthesis.

SAM: And it names a flag or file you have never met.

ALEX: Invented features. If neither the guide nor the docs ever named it, strike it.

SAM: Before the day itself, one more pass. Pause and name the five domains with their weights, and the miss pattern you hit most tonight. [pause]

ALEX: Agentic Architecture twenty-seven, Claude Code Configuration twenty, Prompt Engineering twenty, Tool Design eighteen, Context fifteen. My misses spread across all five patterns, and pattern one, instinct over the guide, came up twice.

SAM: Now one exam tell per domain.

SAM: Agentic: if an option ends the loop on text, a phrase or an iteration cap, it loses to the stop reason. If a rule must hold every time, like a refund threshold, think hook, not prompt.

ALEX: Claude Code: if one person's sessions behave differently from everyone else's, think scope, and check with slash memory. If a convention applies to some files only, think a path-scoped rule. If something must happen after every edit, think a committed PostToolUse hook in project settings.

SAM: Prompts and structured output: if the stem says "only report high-confidence findings", think explicit categories. If the format drifts, think few-shot. If the value is absent from the document, think nullable, not retry.

ALEX: Tools: if the document type is unknown, think tool choice any. If one tool must go first, force it on the first request only. If the agent misroutes between similar tools, think descriptions, and check the system prompt for keyword triggers.

SAM: Context: if exact amounts vanish after summarization, think case facts block. If the agent talks about typical patterns, think scratchpad file and subagents. If ninety-seven percent overall tempts the team to drop review, think accuracy by type and field, then stratified sampling.

ALEX: And if an option names a flag or file I have never met, strike it. [sting]

## Exam day logistics

ALEX: Now the day itself.

SAM: A valid, unexpired, government-issued photo I D, with the name matching your registration exactly. Check it tonight, not at the desk.

ALEX: The room?

SAM: Clear desk. Phones, smart watches, headphones, notes and recording devices are prohibited; scratch paper only if Pearson VUE provides it. Online, stay in webcam view throughout. Arrive on time: miss the late-arrival window and the fee is forfeit.

ALEX: Before the first item?

SAM: You accept a confidentiality agreement. Decline and the session ends with no refund. Afterwards, the questions, options and scenarios stay with you.

ALEX: On the screen?

SAM: Read how many to choose. Reread the left panel whenever the scenario changes. Right-click to strike out half-right options. Past two minutes, flag it and move on. The clock counts down: item twenty at one twenty-three left, forty at forty-seven minutes left, sixty at ten minutes left, then flags. The Review button finds anything flagged or unanswered. Leave nothing blank.

ALEX: And the last half hour?

SAM: Eat beforehand and drink water before you go in. The last twenty items count the same as the first twenty.

ALEX: The morning?

SAM: Replay the anti-patterns and your weakest domain, nothing else. I D by the door. Then stop studying. You were four or five answers short, and since then you have worked on exactly the mechanics that cost them.

ALEX: And tonight?

SAM: Sleep. On the day, read the question on the page, and pick the smallest mechanism that guarantees the outcome.
