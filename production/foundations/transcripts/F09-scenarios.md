---
episode: "F09"
series: "CCAR-F retake"
slug: scenarios
title: "The six scenarios"
description: "All six Foundations scenarios in the exam guide's order: the system, its primary domains, the three decisions the exam keeps probing, the classic trap, an argued distractor and a drill for each, then the patterns that run through all six."
domain: "All five domains, per scenario"
weight: "All domains"
target_minutes: 24
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode eleven, the six scenarios.

ALEX: All six in one go?

SAM: All six. By the end you'll be able to read a scenario frame and know what it rules out before you reach the options. For customer support, code generation, multi-agent research, developer productivity, continuous integration and structured extraction, you'll know the three decisions each one keeps probing and the trap it sets.

SAM: Then you'll see the six patterns that run through all of them.

ALEX: Four of the six turn up at random, and each frames a set of items. A weak scenario costs a run of answers, not one. Where do we start?

SAM: With the left column of the exam screen. [sting]

## The frame and customer support

SAM: Before any scenario, one habit. On the exam screen the scenario frame sits in the left column and hardly changes. Last time you stopped reading it, and that probably cost you more marks than any single fact.

ALEX: It's the same paragraph for a whole run of questions. I read it once.

SAM: Glance at it on every item, and reread it whenever it changes. The frame carries constraints the stem leaves out. Customer support says the target is eighty percent first-contact resolution while knowing when to escalate. That one sentence rules out answers in both directions: escalate everything and you miss the target, never escalate and you fail the second half.

ALEX: So an option that sends every frustrated customer to a human...

SAM: Loses to the frame before you reach the stem. The C I frame says minimise false positives, so answers that flag more lose. The extraction frame says integrate with downstream systems, so an answer that leaves prose where a parser expects JSON loses. The frame also names the product: the Agent SDK in scenarios one, three and four, Claude Code in two and five.

ALEX: And four of the six turn up at random, so none is optional.

SAM: Right. All six, in the guide's order. For each: the system in one breath, its primary domains, three decisions the exam keeps probing, the classic trap, one argument and one drill. Then the patterns that cross all six.

SAM: Scenario one, Customer Support Resolution Agent. An Agent SDK agent handles returns, billing disputes and account issues through four custom M C P tools: get customer, lookup order, process refund and escalate to human. The target is eighty percent first-contact resolution while knowing when to escalate. Primary domains: Agentic Architecture, Tool Design and M C P, and Context Management.

ALEX: Three decisions.

SAM: First, guidance or enforcement. When an order must hold, such as a verified customer ID from get customer before process refund, or no refund above five hundred dollars, it lives in code: a programmatic prerequisite that blocks the call, or a hook that intercepts the outgoing tool call and redirects it to escalate to human. Prompt instructions have a non-zero failure rate, and money is moving.

SAM: Second, escalation calibration. The guide names three triggers: the customer asks for a human, policy is silent or needs an exception, or the agent cannot make progress. Honour an explicit request at once, without investigating first. If get customer returns several matches, ask for another identifier instead of picking one. When calibration is off, the fix is explicit criteria with few-shot examples in the system prompt.

SAM: Third, context over a long conversation. Amounts, dates and order numbers go into a case facts block outside the summarised history. Lookup order results get trimmed to the relevant fields before they pile up. And an escalation carries a structured summary: customer ID, root cause, refund amount, recommended action, because the human cannot see the transcript.

ALEX: The trap?

SAM: Sentiment and self-reported confidence. Both look like escalation signals, and the guide calls both unreliable proxies for case complexity. An angry customer with a simple return still has a simple return.

SAM: Pause here and answer before we go on. Choose two. Which two situations should go to escalate to human? A, on a routine return, the customer writes "I want a person, not a bot." B, the customer wants the refund paid to a different card from the one they used, and the refund policy says nothing about changing payment methods. C, the customer is writing in capitals and swearing about a late parcel that qualifies for a standard refund. D, the agent rates its own confidence at four out of ten. E, get customer returns three accounts matching the customer's name. [pause]

ALEX: A and C. I've run support teams. An angry customer stuck with a bot gets angrier, and that's where churn comes from.

SAM: The churn risk is real, and the anger needs acknowledging. But the answer is A and B. A is an explicit request: honour it straight away. B is policy silence, which is a policy gap. C is within the agent's capability: acknowledge the frustration, offer the refund, and escalate only if the customer repeats that they want a person. D is self-reported confidence, which the guide rules out. E needs another identifier, not a human.

ALEX: Miss pattern one, then.

SAM: Real-world instinct over the guide. The tell is "asks for a person" against "sounds upset". And the frame backs it: send every angry customer to a human and eighty percent slips away. [sting]

## Scenario two: code generation

SAM: Scenario two, Code Generation with Claude Code. The team uses Claude Code for generation, refactoring, debugging and documentation, wired in through custom slash commands and CLAUDE dot md configuration, and must know when to use plan mode and when direct execution. Primary domains: Claude Code Configuration, and Context Management.

SAM: Decision one, where configuration lives. Team-wide means project scope in version control: the project CLAUDE dot md, commands in the dot claude commands folder, skills in dot claude skills. Personal means your home folder, which teammates never see. Conventions for files scattered across the tree, like every test file, go in a rules file under dot claude rules with a paths glob, so it loads only when Claude works on matching files. A bloated CLAUDE dot md splits into topic files in that rules folder, or pulls standards in with an at-sign import.

SAM: Decision two, skill or CLAUDE dot md. CLAUDE dot md is always loaded, so it holds universal standards. A skill loads on demand for one task. Three frontmatter settings get tested: context fork runs the skill in an isolated sub-agent so its verbose output stays out of the main session, allowed tools restricts what it can touch, and argument hint prompts for a missing parameter.

SAM: Decision three, plan mode or direct execution. Plan mode for architectural decisions, several valid approaches, many files. Direct execution for a well-scoped change. Verbose discovery goes to the Explore subagent, which hands back a summary.

ALEX: Then I'd default to plan mode. It costs a minute and never hurts.

SAM: That's a rule outrunning its scope. Planning before anything uncertain is good engineering, granted. But the guide names direct execution as right for a single-file bug fix with a clear stack trace, or one added validation check. Planning there is ceremony.

ALEX: The tell?

SAM: "Single file", "clear stack trace", "one function" mean direct. "Dozens of files", "service boundaries", "two integration approaches" mean plan.

SAM: The classic trap in this scenario is scope. An instruction that works for three developers and not for the new hire lives in someone's user-level file, not the project's.

SAM: Pause here and answer before we go on. A retail team's project CLAUDE dot md requires a shared error-handling helper. In one package Claude keeps ignoring it, and developers say the behaviour differs between sessions. What should they do first? A, run the slash memory command there to see which memory files are actually loaded. B, restate the rule in capitals at the top of the project CLAUDE dot md. C, copy the rule into each developer's user-level CLAUDE dot md. D, add a hook that rejects any edit that skips the helper. [pause]

ALEX: D. If it keeps being ignored, enforce it.

SAM: D might be where you end up. Read the stem again.

ALEX: [sighs] "First." And "differs between sessions".

SAM: Miss pattern three. A is the first step: slash memory shows whether the file you think is loading is loading at all, which is the guide's tool for inconsistent behaviour across sessions. B is louder guidance before you know the cause. C moves a team rule into personal scope, the mismatch we just named. D enforces before anyone has diagnosed. [sting]

## Scenario three: multi-agent research

SAM: Scenario three, Multi-Agent Research System. An Agent SDK coordinator delegates to four subagents: web search, document analysis, synthesis and report generation. The output is comprehensive, cited reports. Primary domains: Agentic Architecture, Tool Design and M C P, and Context Management.

SAM: Decision one, the coordinator. It decomposes the topic, partitions scope so subagents don't duplicate each other, picks the subagents a query needs instead of running the full pipeline every time, and loops: check synthesis for gaps, re-delegate targeted searches, synthesise again. Mechanically, its allowed tools must include Task, the tool that spawns subagents. Parallel subagents come from several Task calls in one response. And each subagent gets its context written into its prompt, because it inherits nothing.

SAM: Decision two, tools per role. Four or five each, not eighteen. A synthesis agent given web search starts searching. Where it needs something often, give it a scoped cross-role tool, such as a fact verification tool, and send complex cases back through the coordinator. Tool names and descriptions must not overlap.

SAM: Decision three, provenance and errors. Findings travel as structured claim-source mappings: the claim, an excerpt, the source URL or document name, the publication date. Failures come back as structured context: failure type, the query attempted, partial results, alternatives. A timeout is not a search that found nothing.

SAM: The classic trap is blaming the wrong agent. When every subagent did its job and the report is still narrow, the coordinator's decomposition is the cause.

ALEX: Let me argue a conflict case. Two sources disagree on a growth figure, one a national statistics office, one a trade body. I'd take the government number. It's more credible, and readers want one number.

SAM: Judging source quality is fair, and readers do like one number. But the guide wants both values kept with attribution, the conflict annotated, and the coordinator deciding how to reconcile before synthesis. The report then separates well-established findings from contested ones. And dates matter: two figures from different years may not conflict at all.

ALEX: The tell?

SAM: "Both credible" and "conflicting". An option that quietly picks one value loses.

SAM: Pause here and answer before we go on. Choose two. A public health research run produces reports whose claims carry no citations, although the web search subagent's results included URLs and dates. Which two changes fix the root cause? A, require the search and analysis subagents to return structured claim-source mappings that synthesis must preserve and merge. B, pass prior findings to the synthesis subagent as structured data that keeps content separate from metadata such as URLs, document names and page numbers, instead of a prose summary. C, add "always cite your sources" to the report subagent's system prompt. D, give the synthesis subagent web search so it can find the sources again. E, move synthesis to a model with a larger context window. [pause]

ALEX: A and B.

SAM: Both. Attribution was lost in the hand-off, so the hand-off has to carry it. C asks for citations the report agent no longer has. D is a tool outside the agent's role, and it repeats work already done. E is scale instead of structure: a bigger window cannot restore mappings nobody passed. [sting]

## Scenario four: developer productivity

SAM: Scenario four, Developer Productivity with Claude. Agent SDK tools help engineers explore unfamiliar codebases, understand legacy systems, generate boilerplate and automate repetitive tasks, using the built-in tools Read, Write, Bash, Grep and Glob, plus M C P servers. Primary domains: Tool Design and M C P, Claude Code Configuration, and Agentic Architecture.

SAM: Decision one, which built-in tool. Grep searches file contents: every caller of a function, an error message. Glob matches file paths: every file ending in dot test dot T S X. Edit changes a spot found by unique text; when the anchor isn't unique, Read the whole file and Write it back. And build understanding step by step: Grep for entry points, then Read and follow the imports, instead of reading everything up front.

SAM: Decision two, M C P. Shared servers go in the project's dot M C P dot json, with tokens referenced through environment variable placeholders. Personal or experimental servers go in the user-level dot claude dot json in your home folder. Tools from every configured server are discovered at connection and available together. If the agent keeps choosing Grep over a more capable M C P search tool, improve that tool's description. Catalogs, such as database schemas or documentation trees, go out as M C P resources, so the agent doesn't spend calls exploring.

SAM: Decision three, long explorations. Hand verbose investigations to subagents, and use slash compact when discovery output fills the window. Resuming tomorrow after edits: resume the named session and tell it which files changed. Comparing two approaches from the same analysis: fork the session.

SAM: The classic trap is reading every file to understand the system. It floods the context, and the guide prescribes the incremental path instead.

ALEX: My argument. We need Jira. I'd write our own M C P server: we control the code, the authentication and the fields that come back.

SAM: Control is a real benefit. But the guide draws the line plainly: existing community servers for standard integrations like Jira, custom servers for team-specific workflows. Building your own for a standard integration is effort the item counts against you.

ALEX: The tell?

SAM: A well-known product in the stem points to the community server. Custom wins when the stem describes something only your team does.

SAM: Pause here and answer before we go on. Three hours into mapping a legacy insurance claims system, the agent stops naming the classes it found earlier and starts saying things like "services like this usually follow a repository pattern". What is the best change? A, have the agent keep a scratchpad file of key findings and consult it for later questions. B, raise the maximum output tokens. C, start a new session and have it read every file again. D, add "be specific" to the system prompt. [pause]

ALEX: A.

SAM: A. Talk of typical patterns instead of named classes is how the guide describes context degradation, and a scratchpad file keeps findings across that boundary. B changes output length, not what the model holds. C repeats the read-everything mistake and will degrade the same way. D asks for detail the model has already lost. [sting]

## Scenario five: continuous integration

SAM: Scenario five, Claude Code for Continuous Integration. Claude Code runs in the C I C D pipeline: automated code reviews, generated test cases, feedback on pull requests. The prompts must give actionable feedback and minimise false positives. Primary domains: Claude Code Configuration, and Prompt Engineering and Structured Output.

SAM: Decision one, running unattended. The dash p flag, long form dash dash print, runs Claude Code non-interactively so the job doesn't hang waiting for input. JSON output checked against a schema gives machine-parseable findings to post as inline comments. Project context, meaning testing standards, fixtures and review criteria, comes from CLAUDE dot md.

SAM: Decision two, precision. Explicit categorical criteria: report bugs and security issues, skip minor style and local patterns. Few-shot examples fix the output format: location, issue, severity, suggested fix. If one category's false positives are wrecking trust, switch that category off while you improve its prompt.

SAM: Decision three, review architecture. A large pull request gets per-file passes plus a cross-file integration pass. Re-runs carry the prior findings and report only new or unresolved issues. Test generation sees the existing tests so it doesn't duplicate them. Blocking pre-merge checks stay synchronous; overnight and weekly analysis can go to the Message Batches API at half the cost.

SAM: The classic trap: "be conservative" or "only report high-confidence findings". The guide says general instructions like these don't improve precision. Specific criteria do.

ALEX: My argument. The session that generated the change knows why every line is there. Have it review its own work. Nobody has more context.

SAM: It has the context, true, and that is the problem. The guide says a model keeps its reasoning from generation and is less likely to question its own decisions. An independent instance without that reasoning catches subtler issues than self-review instructions or extended thinking do.

ALEX: The tell?

SAM: "Same session" next to "review". Fresh eyes win.

SAM: Pause here and answer before we go on. A bank's review bot posts findings, and developers dismiss about a third of them. The team wants to know which code constructs produce the dismissed findings, so they can fix the prompt for those. What should they add? A, a detected pattern field on each structured finding, so dismissals can be grouped by the construct that triggered them. B, an instruction to report only findings the model is confident about. C, a move from synchronous calls to the Message Batches API. D, a free-text box where developers explain each dismissal. [pause]

ALEX: A.

SAM: A. It turns dismissals into data you can count, which is the guide's feedback-loop design. B is the confidence-filtering trap. C changes cost and latency, not precision. D produces comments nobody aggregates. [sting]

## Scenario six: structured extraction

SAM: Scenario six, Structured Data Extraction. The system pulls information out of unstructured documents, validates it against JSON schemas, keeps accuracy high, handles edge cases gracefully and feeds downstream systems. Primary domains: Prompt Engineering and Structured Output, and Context Management.

SAM: Decision one, enforcing structure. Define an extraction tool whose input schema is the shape you want, and read the data from the tool use response. That removes JSON syntax errors. Then tool choice: auto lets the model answer in text, any forces it to call some tool, and naming a tool forces that one, for example forcing the metadata extraction first and running enrichment in follow-up turns. Fields the source may lack are nullable, and enums get "unclear", plus "other" with a detail field.

SAM: Decision two, validation. A schema catches syntax, not meaning. Line items that don't add up need a semantic check: extract a calculated total beside the stated total and flag the difference. When validation fails, retry with the original document, the failed extraction and the specific error.

SAM: Decision three, scale and review. The Message Batches API gives fifty percent savings, up to twenty-four hours of processing and no latency guarantee. Resubmit only the failures, found by their custom ID, chunking any that were too long, and refine the prompt on a sample before the big run. And a high overall accuracy figure can hide one weak document type, so check accuracy by type and field, sample the high-confidence output, and calibrate field-level confidence against labelled data.

SAM: The classic trap is a required field for information that may be absent. The model fills it with a plausible invention.

ALEX: My argument. Retry with error feedback is cheap and it works. I'd wrap every failure in three retries and move on.

SAM: For format and structure errors it works well. But the guide sets a limit: when the information isn't in the document, say it lives in a separate contract nobody provided, no retry can find it. You spend calls and invite an invention on the third attempt.

ALEX: The tell?

SAM: "Not in the source" or "in another document". That calls for null or human review, not a retry.

SAM: Pause here and answer before we go on. A logistics firm has three extraction tools: one for bills of lading, one for customs declarations, one for delivery receipts. The document type isn't known in advance, and sometimes the model replies with a prose summary instead of calling any tool, which breaks the downstream loader. What fixes this? A, set tool choice to any. B, force the bill of lading tool on every request. C, keep tool choice on auto and tell the model to always use a tool. D, merge the three into one schema with every field optional. [pause]

ALEX: A.

SAM: A. Any guarantees a tool call and still lets the model choose the right schema, which is the guide's answer when several schemas exist and the type is unknown. B guarantees the wrong tool for two document types in three. C is still probabilistic, the same gap with more words. D throws away the per-type contracts downstream systems rely on. [sting]

## Patterns across scenarios

SAM: Six scenarios. Now the patterns that run through them.

ALEX: One: what must happen every time lives in code. Prerequisites and hooks in support, allowed tools on a skill, tool choice and schemas in extraction.

SAM: Two: specific beats general. Explicit escalation criteria, distinct tool descriptions, categorical review criteria, concrete examples. "Be careful", "be conservative" and a raw self-rated confidence score lose in support, in C I and in extraction alike. Confidence only earns a place once it is calibrated against labelled data and used to route review.

ALEX: Three: context is passed, never assumed. Subagents get findings in their prompt, re-reviews get prior findings, test generation gets the existing tests, a resumed session is told what changed, and the human gets a structured handoff.

SAM: Four: absence and failure get honest values. Null for a missing field, "unclear" for an ambiguous one, a structured error for a timeout, an empty result for a search that found nothing, an annotation for a conflict, a coverage note for a gap.

ALEX: Five: fresh eyes and focused passes. An independent reviewer, per-file passes plus an integration pass, context fork, the Explore subagent, a scratchpad file.

SAM: Six: scope follows audience. Team-wide goes in the project and version control, personal goes in your home folder. That decides items in scenarios two and four.

## Recap: the exam tells

SAM: Before the last word, your turn. Pause and name the six scenarios, and the classic trap in each. [pause]

ALEX: Customer support, escalating on sentiment or self-rated confidence. Code generation, scope: a rule sitting in someone's user-level file. Research, blaming the wrong agent when the coordinator's decomposition is the cause. Developer productivity, reading every file. Continuous integration, "be conservative". Extraction, a required field for information that may be absent.

SAM: Good. Now one exam tell per scenario.

ALEX: Support: if the customer asks for a person, escalate at once. If they are only angry about something the agent can fix, acknowledge it and resolve it. If a refund rule must always hold, think hook or prerequisite.

SAM: Code generation: if behaviour differs between sessions, think slash memory first. "Single file" and "clear stack trace" mean direct execution; "dozens of files" means plan mode.

ALEX: Research: if the report is narrow and every subagent did its job, think the coordinator's decomposition. If citations vanish, think structured claim-source mappings in the hand-off.

SAM: Developer productivity: if the agent talks about typical patterns instead of named classes, think scratchpad file. If the stem names a well-known product like Jira, think community M C P server.

ALEX: Continuous integration: if the same session reviews its own change, think independent instance. If nobody can tell which findings get dismissed, think a detected pattern field.

SAM: Extraction: if the document type is unknown and prose comes back, think tool choice any. If the value lives in another document, think null or human review, not a retry.

ALEX: And over all of it, the left column.

SAM: Glance at it on every item. Eighty percent while knowing when to escalate. Minimise false positives. Comprehensive and cited. Downstream systems. The frame often settles the item before the options do.

ALEX: Next, the final drill: everything mixed, for the night before.
