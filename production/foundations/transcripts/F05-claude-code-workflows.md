---
episode: "F05"
series: "CCAR-F retake"
slug: claude-code-workflows
title: "Plan mode, refinement and CI"
description: "When to plan and when to just make the change, how to steer Claude Code with examples, tests and targeted feedback, and how to run it in a CI pipeline that posts clean, non-duplicated, low-noise review comments."
domain: "Claude Code Configuration & Workflows"
weight: "20%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode three: plan mode, refinement and CI.

ALEX: Meaning that by the end I can do what?

SAM: Choose between plan mode and direct execution from the wording of a stem, and know when to hand discovery to the Explore subagent. Pick the refinement technique that fits the symptom: examples, tests first, an interview, a named edge case, or batching. And set up Claude Code in a pipeline that doesn't hang, posts structured comments, reviews with a fresh instance, and keeps false positives down.

ALEX: For the exam that's the workflow half of a twenty percent domain, and refinement was my twenty-five percent.

SAM: First, an item from the CI scenario, about review comments that keep coming back. [sting]

## Cold open: repeating review comments

SAM: Scenario five, Claude Code for Continuous Integration. A payments team runs an automated review on every push to a pull request. Developers complain that after each new commit the same eleven comments reappear, and two of them flag problems the author already fixed. What should the team change? Option A, give the review the previous run's findings and instruct it to report only issues that are new or still unaddressed. Option B, have the posting script hash each comment's text and skip any comment it has posted before. Option C, run the review only once, when the pull request is opened. Option D, add "do not repeat earlier feedback" to the review prompt.

ALEX: B. It is deterministic, it is ten lines of script, and it never depends on the model behaving.

SAM: Hold that. We come back to it at the end.

ALEX: Where are we in the blueprint?

SAM: Domain three, Claude Code Configuration and Workflows, twenty percent of the exam. Last episode was the configuration half. Today is the workflow half: task statement three point four, plan mode versus direct execution; three point five, iterative refinement; and three point six, Claude Code in CI. Two scenarios carry most of these items: Code Generation with Claude Code, and Claude Code for Continuous Integration.

ALEX: And three point five is the one I scored twenty-five percent on.

SAM: Which is why it gets the longest segment. One habit for today: these items describe a symptom, and the answer is the technique whose trigger matches the symptom's words.

SAM: Segment one, plan mode. Plan mode is for complex work: large-scale changes, several valid approaches, architectural decisions, edits across many files. Claude explores the codebase and designs an approach before anything changes, which prevents costly rework. Direct execution is for simple, well-scoped changes: a single-file bug fix with a clear stack trace, or adding one date validation check to one function.

ALEX: So the test is size?

SAM: Size, and uncertainty. A library migration touching forty-five files, restructuring a service into microservices, choosing between two integration approaches with different infrastructure needs: plan mode. And the guide's favourite combination is both in sequence. Plan the migration, then execute the planned approach directly.

ALEX: Let me argue the other side. I know this codebase. For a big refactor I would write a detailed brief up front, exactly how each module should change, and run it directly. Planning mode feels like ceremony when the engineer already has the design in their head.

SAM: Sometimes the engineer does have it, and a precise brief is a good brief.

SAM: But the exam's wording for plan mode is "multiple valid approaches" and "architectural decisions". If the stem says the team must decide service boundaries or choose between approaches, the design is not yet known, and a detailed brief assumes an answer nobody has explored. That option is over-confidence dressed as thoroughness.

ALEX: So the tell?

SAM: "Decide", "choose between", "dependencies not yet understood", or a file count in the dozens. Those point to plan mode. "Clear stack trace", "one function", "single file" point to direct execution.

ALEX: Then here is my rule: anything in the payments service goes through plan mode. That code is critical.

SAM: That is the rule stretched past its scope. Risk to the business is not the same as complexity of the change. A one-line null check in a payments file, with a stack trace pointing at the line, is a well-scoped change. Direct execution. Protecting critical code is a job for review, tests and permissions, not for a planning phase.

ALEX: Miss pattern four. Over-applying a new rule.

SAM: And five, importing a constraint the stem did not give. If the item does not say the change is uncertain, do not make it uncertain.

SAM: Now the Explore subagent. Discovery is verbose. Reading thirty files to map how authentication works pours output into the main conversation, and on a multi-phase task that output crowds out the context you need for the later phases. The Explore subagent does that reading in its own context window and hands back a summary. It reads and searches; it does not write.

ALEX: Why not just compact when the window fills up?

SAM: Compaction is real and Claude Code does it. But it acts after the window has filled, and it summarises everything, including the decisions you wanted kept word for word. The Explore subagent keeps the noise out in the first place. Both are in the guide: plan a multi-phase task with the Explore subagent so discovery never floods the session, and use slash compact once a long exploration has already filled it with verbose output. Episode nine comes back to that.

ALEX: Tell?

SAM: "Verbose discovery", "multi-phase", "context window running out during exploration". Isolate the discovery, keep the summary. Same idea as subagents in Domain one: the coordinator gets the result, not the working.

SAM: Pause here and answer before we go on. Code Generation scenario. A logistics team will replace its logging library across about sixty files. Some modules wrap the old logger in helper functions, and nobody is sure how many. What is the best approach? A, use direct execution file by file, fixing each module as it comes up. B, use plan mode to map how the old logger is used and design the migration, then carry out the planned approach with direct execution. C, write a detailed prompt describing the new logging calls and run it once in direct execution across the repository. D, start with direct execution and switch to plan mode if the wrappers cause trouble. [pause]

ALEX: B.

SAM: B. Sixty files and unknown wrappers are the plan-mode triggers, and the guide names this exact pairing: plan the migration, then execute it. A discovers the wrappers one surprise at a time, which is the rework plan mode prevents. C assumes a design before anyone has looked at the wrappers. D waits for complexity the stem has already told you about. The tell was "nobody is sure how many". [sting]

## Segment two: iterative refinement

SAM: Segment two, iterative refinement. Five techniques, each with its own trigger. First: when prose descriptions are interpreted inconsistently, give two or three concrete input-output examples. Examples are the most effective way to show a transformation.

ALEX: Example?

SAM: A retail team asks Claude Code to "normalise product codes". One run uppercases them, the next strips the hyphens, the next pads the numbers. Three examples settle it: this raw code in, this exact code out.

ALEX: I would push on that. Write the spec properly. Uppercase, strip hyphens, pad to eight digits. Precise prose is more maintainable than examples, and examples can be over-fitted.

SAM: Precise prose helps, and when you can write the rule cleanly you should.

SAM: But the guide's trigger is "interpreted inconsistently". Once the prose has already been read three ways, more prose is the thing that failed. Examples remove the ambiguity the words left. And this connects to Domain four: few-shot examples are the guide's answer for consistent format there too.

ALEX: Tell?

SAM: "Inconsistent results" or "interpreted differently" from a natural-language description. Reach for two or three examples.

SAM: Second technique: test-driven iteration. Write the test suite first, covering expected behaviour, edge cases and performance requirements. Then iterate by sharing the failing tests. A failing test tells Claude exactly what is wrong, in a form it can check after every change.

SAM: Third: the interview pattern. Before implementing in an unfamiliar domain, have Claude ask you questions. A developer adding a caching layer may never have considered cache invalidation or what happens when the backing store is down. The questions surface those before the code exists.

ALEX: In practice I would rather Claude just start. Ten questions up front feels slow.

SAM: For familiar work it is slow, and the guide would not ask for it. The trigger is "unfamiliar domain" and "considerations the developer may not have anticipated". Then a few questions are cheaper than rebuilding the cache.

SAM: Fourth: specific test cases for edge cases. When a migration script mishandles null values, the fix is not "handle nulls better". It is this input row, with this null, and this expected output.

SAM: Fifth, and the one the score report flagged: batching. If problems interact, so that fixing one changes the other, put them all in one detailed message. If they are independent, fix them one at a time.

ALEX: Why not always batch? One message, fewer round trips.

SAM: Because independent fixes are easier to check separately, and a long list of unrelated items invites partial fixes. Batching is the answer to interaction, not to cost.

ALEX: And why not always go one at a time, then?

SAM: Because with interacting problems, fixing one alone can break the other, and you go round in circles. The tell is in the stem: "depends on", "affects", "fixing one broke the other". Interacting: one message. Independent: sequential.

SAM: Pause here and answer before we go on. Choose two. Code Generation scenario. Claude Code has written a script that moves loyalty-programme accounts into a new schema. Three problems: accounts with no loyalty tier come out with the text "None" instead of an empty value; points are rounded before the currency conversion, so balances drift, and the conversion and rounding steps are written so that changing one changes the other; and a log message has a typo. Which two approaches will fix this most effectively? A, describe the rounding and conversion problem in one detailed message, because the two fixes interact. B, give a specific test case: an account with no tier as input, and an empty tier value as the expected output. C, send all three problems in one message ending with "please be more careful with edge cases". D, ask for the rounding fix now, then the conversion fix in a later message once rounding is correct. E, ask Claude to rewrite the script from scratch from a longer description. [pause]

ALEX: B and D. One change at a time is how I debug. Fix rounding, check it, then conversion.

SAM: B is right. D is the miss. The stem told you the conversion and rounding steps interact, so a rounding fix on its own will be checked against a conversion that is still wrong, and you chase your tail. That is miss pattern four: "one at a time" is a good rule for independent problems, and you applied it past that scope. The answer is A and B.

ALEX: And the others?

SAM: C batches independent problems with interacting ones and adds vague feedback, "be more careful", which names no case. E throws away working code and swaps a specific problem for a longer prose description, which is how you got here. The typo is independent; fix it on its own. [sting]

## Segment three: Claude Code in CI

SAM: Segment three, Claude Code in CI. Start with the hang. Interactive Claude Code waits for a person. In a pipeline there is no person, so the job sits there. The dash p flag, long form dash dash print, runs it non-interactively: it takes the prompt, prints the result and exits.

ALEX: And the distractors are invented flags.

SAM: Invented environment variables, invented batch flags, shell tricks that feed it empty input. If an option names a mechanism you have never seen in the docs, treat it as invented. The guide's answer is the print flag.

SAM: Next, structured output. A pipeline that posts inline pull request comments needs findings it can parse: file, line, severity, issue, suggested fix. The guide pairs the output format flag set to JSON with a second flag that supplies a JSON schema, so the findings come back as machine-parseable data that matches the schema.

ALEX: Then context. A CI run starts cold. Where do the testing standards come from?

SAM: CLAUDE dot md. It is how CI-invoked Claude Code gets project context: testing standards, fixture conventions, review criteria. For test generation, the guide adds two more moves. Document what makes a test valuable, and which fixtures exist, in CLAUDE dot md, so you get fewer low-value tests. And put the existing test files in context, so it does not propose scenarios the suite already covers.

ALEX: I would put the standards straight into the pipeline's prompt. It is one job, and the prompt is right there in the workflow file.

SAM: That works for one job. But the guide names CLAUDE dot md as the mechanism, and for good reason: every CI job and every developer's session reads the same standards from one place, version-controlled with the code. A prompt buried in one workflow file drifts from the others.

ALEX: Tell?

SAM: "Testing standards", "fixture conventions", "review criteria" for CI-invoked Claude Code. That points to CLAUDE dot md.

SAM: Now session isolation. The session that wrote the code is a poor reviewer of it. It still holds its own reasoning from generation, so it is less likely to question its own decisions. An independent instance, without that reasoning context, catches more.

ALEX: Let me defend self-review. Same session, extended thinking on, an instruction to be ruthlessly critical. It knows why every line is there. That is an advantage.

SAM: It sounds like one, and thinking does help on hard problems.

SAM: But knowing why every line is there is the problem. The reviewer shares the author's assumptions, so it misses the same things. The guide says it outright in Domain four: independent review instances catch subtle issues better than self-review instructions or extended thinking. The tell is "the same session that generated", or any option that adds effort to the author instead of adding a second reader.

SAM: Then false positives, which tie straight into task statement four point one. Developers stop reading a noisy reviewer, and one high false-positive category drags down trust in the accurate ones.

ALEX: So you tell it to only report high-confidence findings.

SAM: That is the guide's named failure. "Be conservative" and "only high-confidence" do not raise precision. Explicit categorical criteria do: report bugs and security issues, skip minor style and local patterns. Define each severity level with a concrete code example. And while you fix the prompt for a noisy category, switch that category off for now to win trust back.

SAM: Pause here and answer before we go on. CI scenario. A review job runs Claude Code in print mode and a script turns its output into inline comments. About one run in ten, the script fails because the output is a paragraph of prose followed by a findings list. What should change? A, add a regular expression to the script that extracts the list from the prose. B, add "respond with JSON only" to the prompt. C, use the JSON output format with a schema for the findings, so the script receives structured data that matches it. D, retry the job when parsing fails. [pause]

ALEX: C.

SAM: C. The script needs machine-parseable findings, and the guide's answer is structured output enforced through the CLI, with a schema. B is a probabilistic fix for a deterministic need: the prompt already implies the format and it fails one run in ten. A works around the symptom and breaks the next time the prose changes. D repeats the same unreliable call and hopes.

SAM: Pause here and answer before we go on. Choose two. CI scenario. A hospital software team's automated reviewer posts about forty comments per pull request: naming preferences, possible null warnings on values already checked upstream, and occasional real security issues. Developers now dismiss every comment, including the security ones. Which two changes best restore trust? A, add "only report findings you are highly confident in" to the review prompt. B, define explicit criteria: report bugs and security issues, skip naming and local style patterns, with a concrete code example for each severity level. C, temporarily switch off the possible-null category while its prompt is improved. D, run the review three times and post only findings that appear in at least two runs. E, switch to a larger model. [pause]

ALEX: B and C.

SAM: B and C. B is categorical criteria with examples, the guide's mechanism for precision. C restores trust now, while the noisy category is fixed. A is the confidence-word distractor the guide names. D is a voting scheme that suppresses real findings that only show up some of the time. E is scale instead of structure: a larger model applying vague criteria is still applying vague criteria. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you picked B, hash the comment text.

ALEX: I will defend it. It is deterministic, it is cheap, and I have shipped exactly that in a pipeline.

SAM: The instinct is sound, and deterministic deduplication beats asking nicely. But two facts in the stem break it. The model will word the same finding differently on the next run, so the hash changes and the duplicate gets through. And two comments flagged problems the author already fixed. A text hash cannot know a problem was fixed. Only a review that sees its previous findings next to the new code can say "this one is resolved, this one is still open".

ALEX: So A.

SAM: A. Include the prior findings and instruct the review to report only new or still-unaddressed issues. That is the guide's exact skill. C stops reviewing the commits that most need it. D is a bare instruction with nothing to compare against: the review cannot avoid repeating findings it cannot see.

ALEX: What should have stopped me?

SAM: "Already fixed". Deduplication is a text problem; "already fixed" is a judgement about the code, and judgement needs the prior findings in context. Your real-world instinct was good engineering for the wrong problem. Miss pattern one. [sting]

## Five to remember

SAM: Five to remember. One: plan mode for many files, several valid approaches or architectural decisions; direct execution for a clear, single-file change. Plan the migration, then execute it. Risky code is not the same as a complex change.

ALEX: Two: the Explore subagent does verbose discovery in its own context and returns a summary, so a multi-phase task does not run out of room.

SAM: Three: prose read inconsistently, give two or three input-output examples. Tests first, then share the failures. Interview Claude before building in an unfamiliar domain. Name the failing case, not "still wrong".

ALEX: Four: problems that interact go in one detailed message; independent problems go one at a time.

SAM: Five: in CI, print mode so it never waits for input; JSON output with a schema so findings post as inline comments; CLAUDE dot md for standards and fixtures; a separate instance to review; prior findings in context to stop duplicates; explicit categories, not confidence words, to cut false positives.

## Recap: the exam tells

SAM: Retrieval before the tease. Pause and name the three segments, and one technique from each. [pause]

ALEX: Plan mode against direct execution, with the Explore subagent. Iterative refinement, five techniques. And Claude Code in CI.

SAM: Now as exam tells. If a stem says choose between approaches, dozens of files, or nobody is sure how many, think plan mode, then execute the plan. If it says one function and a clear stack trace, direct execution, even in payments code.

ALEX: If discovery is verbose and the task has several phases, think the Explore subagent, which reads in its own context and hands back a summary.

SAM: If a prose description is read three different ways, think two or three input-output examples. If the domain is unfamiliar, let Claude interview you first.

ALEX: If fixing one problem changes another, send them in one detailed message. If they are independent, one at a time, so each fix can be checked.

SAM: If the CI job hangs, think the print flag. If the parser chokes on prose, JSON output with a schema. If the same session reviews its own code, add an independent instance.

ALEX: And if comments repeat or developers dismiss everything, think prior findings in context, and explicit categories instead of confidence words.

ALEX: Next, episode four: prompts and structured output, where those explicit criteria and examples get the full treatment.
