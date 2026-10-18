---
episode: "F06"
series: "CCAR-F retake"
slug: structured-output
title: "Prompts and structured output"
description: "Explicit review criteria, few-shot examples, tool use with JSON schemas and tool choice, validation and retry loops, the Message Batches API, and independent review passes, drilled inside the extraction and continuous integration scenarios."
domain: "Prompt Engineering & Structured Output"
weight: "20%"
target_minutes: 26
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode four, prompts and structured output.

ALEX: What will I be able to do by the end?

SAM: Fix a noisy review bot with explicit criteria instead of "be conservative", and know when two to four few-shot examples beat another paragraph of instructions. Choose between tool choice auto, any and a named tool, and design a schema with nullable fields, "unclear" and "other".

SAM: Then tell a failure a retry can fix from one it never will, plan a batch run and its resubmission, and know why a generator should not review its own work.

ALEX: This domain is twenty percent of the exam, and my score report put schema design at thirty-three percent and feedback loops at zero. That is where some of my missing answers are.

SAM: Then start with an invoice field that will not extract. [sting]

## Cold open: invoice payment terms

SAM: Structured data extraction scenario. A logistics company extracts supplier invoices with a tool-use schema and a validation-retry loop. One field, payment terms, fails validation on about one invoice in eight. Those invoices say "terms as per master agreement", and the master agreement is not part of the input. The loop retries three times with the validation error appended, and the field still fails. What should the architect change? Option A, raise the retry limit to five and make the appended error message more specific. Option B, recognise that the value is absent from the source, stop retrying that failure, return null with a reason, and route it for review or supply the referenced agreement. Option C, add few-shot examples of correctly extracted payment terms. Option D, move the pipeline to a larger model.

ALEX: A. Retry with error feedback is the guide's own technique. Sharpen the feedback and give it room.

SAM: Hold that. We come back to it at the end.

ALEX: Where does this episode sit?

SAM: Prompt Engineering and Structured Output is twenty percent of Foundations and the primary domain of two scenarios, structured data extraction and continuous integration. Six task statements: explicit criteria, few-shot examples, structured output, validation and retry, batch processing, and multi-pass review. Your score report put schema design at thirty-three percent and feedback loops at zero, so those get the most time.

SAM: Segment one, explicit criteria. Continuous integration scenario. A review bot flags comments as "possibly inaccurate", suggests renames, and questions patterns the team uses everywhere. The prompt says "check that comments are accurate and flag anything suspicious". What do you change?

ALEX: Tell it to be conservative. "Only report findings you are highly confident in." That cuts the noise.

SAM: It sounds like precision, and the guide says it fails. "Be conservative" and "only report high-confidence findings" are general instructions with no shared definition behind them, so precision barely moves.

ALEX: Then what does?

SAM: Categorical criteria. Say which issues to report, bugs and security, and which to skip, minor style and local patterns the team has chosen. Replace "check that comments are accurate" with "flag a comment only when the behaviour it claims contradicts what the code actually does". That is a test the model can apply to each case.

ALEX: The tell?

SAM: Any option built on "conservative", "confident" or "be careful". Those are confidence-based filtering. The answer names categories.

ALEX: And severity?

SAM: Same mechanism. If severity comes back inconsistent, define each level with explicit criteria and a concrete code example for each. Consistent classification comes from shared definitions, not adjectives.

ALEX: One part of this I would argue with. The guide says temporarily disable high false-positive categories. If the comment checker sometimes finds a real bug, turning it off hides real problems. That feels like lowering the bar.

SAM: You do lose those true positives for a while. The guide's reason is trust. When one category is mostly noise, developers stop reading every finding, including the accurate security ones. Switch the noisy one off, fix its prompt, turn it back on.

ALEX: So the tell is "developers ignoring" or "dismissing".

SAM: Yes. And "temporarily" is doing work in that option. A permanent deletion is the blunt cut.

SAM: Pause here and answer before we go on. Choose two. Continuous integration scenario. A payments company's review bot has a sixty percent dismissal rate. Most dismissed findings are style nits and "this comment may be outdated" warnings. Security findings are rarely dismissed. Which two changes best restore precision? A, rewrite the criteria to report bugs and security issues and to skip minor style and established local patterns. B, add "be conservative and only report high-confidence findings" to the prompt. C, temporarily disable the comment-accuracy category while rewriting it to flag only comments whose claimed behaviour contradicts the code. D, have three reviewer instances vote and post only findings two of them agree on. E, post only findings the model rates as high severity. [pause]

ALEX: A and C.

SAM: Both. A defines what to report and what to skip. C protects trust in the accurate categories while the noisy one is fixed. B is the vague instruction the guide names as failing. D adds cost and still has no definition of what counts as a finding. E is confidence filtering by another name, and severity without defined criteria is inconsistent anyway. [sting]

## Segment two: few-shot examples

SAM: Segment two, few-shot. Symptom: the review prompt has a full paragraph describing the format, location, issue, severity, suggested fix. The output still varies. Sometimes the fix is missing, sometimes the location is a vague "near the top".

ALEX: More detailed instructions. Spell out each field.

SAM: The guide's answer is that when detailed instructions alone give inconsistent results, few-shot examples are the most effective technique. Two to four targeted examples showing the exact output shape do what another paragraph cannot.

ALEX: Why two to four? If examples work, give it twenty.

SAM: Careful, that is a good rule outrunning its scope. The skill is targeted examples aimed at the ambiguous cases, each showing why one action was chosen over a plausible alternative. Twenty easy examples teach nothing about the hard ones.

ALEX: What else do the examples teach?

SAM: Three things. Judgment on ambiguous cases: which tool fits an ambiguous request, whether a missing branch is a real coverage gap. Acceptable code versus genuine issues: one pattern that looks risky but is fine, one that really is a bug, which cuts false positives. And generalisation: examples let the model carry judgment to novel patterns. They are not a lookup table.

ALEX: And in extraction?

SAM: Few-shot examples reduce hallucination and missing values. Documents arrive in varied shapes: citations inline or in a bibliography, the method in its own section or buried in the narrative, measurements written informally. Examples of correct extraction from each shape fix it.

ALEX: Episode ten made few-shot the wrong answer, though. The refund ordering.

SAM: Different job. Few-shot is still probabilistic. An order that must hold every time belongs in code. Consistent format and better judgment on ambiguous cases belong to few-shot.

SAM: Pause here and answer before we go on. Structured data extraction scenario. A pharmaceutical company extracts sample size and primary endpoint from published studies. On studies with a dedicated methods section, extraction is accurate. On studies where those details appear in the narrative of the results, the sample size field comes back null, even though a reviewer can find the number in the text. What is the best fix? A, add few-shot examples showing correct extraction from studies where the details are embedded in the narrative. B, make the sample size field nullable so the null is legal. C, add a retry loop that re-asks when the field is null. D, add a sentence to the prompt saying sample size may appear anywhere. [pause]

ALEX: B. Episode ten taught me: missing data needs a legal value.

SAM: Is the data missing?

ALEX: [sighs] No. "A reviewer can find the number in the text." It is there.

SAM: That is miss pattern four, a rule learned last week applied beyond its scope. Nullable fields are for information the source does not contain. Here the source contains it in a shape the model was not shown. The answer is A: examples of extraction from varied document structures, which is exactly the guide's fix for empty or null extraction of required fields. B makes the wrong answer legal. C re-asks with no new information about where to look. D is a vague instruction where an example would show the way.

ALEX: The tell?

SAM: "Varied structures", "different formats", "some layouts work, others don't". That points to few-shot. "Not present in the document" points to nullable. [sting]

## Segment three: structured output

SAM: Segment three, structured output. Symptom: a team asks for JSON in the prompt and parses the reply. A few percent of replies fail to parse: a trailing comma, a stray sentence before the opening brace.

ALEX: Tighten the prompt and add a parser that strips everything outside the braces. Cheap and it works.

SAM: It does work most of the time. The guide's answer is tool use with a JSON schema. Define an extraction tool whose input schema is the shape you want, and read the data from the tool use block in the response. The guide calls it the most reliable approach for schema-compliant output; it eliminates JSON syntax errors.

ALEX: So the tell for a parse failure is tool use.

SAM: Yes. Now the parameter that decides whether the tool gets called at all: tool choice. Auto is the default; the model may call a tool or may answer in text. Any means it must call a tool, but it chooses which. And forced selection, type tool with a name, means it must call that one named tool.

ALEX: When does each one win?

SAM: Any, when you have several extraction schemas and do not know the document type in advance. The model must produce structured output, and it picks the right schema. Forced, when one particular extraction has to run first. The guide's example is forcing a tool called extract metadata so it always runs before enrichment steps.

ALEX: Then why not force everything? Forcing is the strongest guarantee.

SAM: For a single known document type, forcing is right. With three schemas and an unknown type, forcing the invoice tool squeezes a contract into an invoice shape: valid, and wrong. The tell: "document type is unknown" means any; "must run before" means the named tool.

ALEX: Valid and wrong?

SAM: Strict schemas eliminate syntax errors. They do not prevent semantic errors: line items that do not sum to the total, a value in the wrong field. Shape is guaranteed; meaning is not.

SAM: Pause here and answer before we go on. Structured data extraction scenario. A bank's operations team receives a mixed inbox of invoices, receipts and contracts, with no reliable way to tell which is which beforehand. Each type has its own extraction tool. With tool choice on auto, about five percent of responses come back as a prose summary with no tool call. What should change? A, keep auto and add a firm instruction to always call a tool. B, set tool choice to any. C, force the invoice extraction tool, since invoices are the most common type. D, remove the tools and ask for JSON in the prompt. [pause]

ALEX: B.

SAM: B. Any guarantees a tool call and lets the model pick the schema that fits. A leaves the decision with the model, so prose can still come back. C forces the wrong schema onto receipts and contracts. D removes the mechanism that eliminates syntax errors.

SAM: Now schema design, your thirty-three percent. Episode ten covered nullable fields and an "other" value for currencies, so here is the rest of the bullet. Required versus optional: a field is required only when every source document will contain it. An enum gets an "unclear" value for genuinely ambiguous cases, and an "other" value paired with a detail string for categories you cannot list in full. And format normalisation rules go in the prompt alongside the strict schema.

ALEX: Why the prompt? The schema says the field is a date string.

SAM: The schema guarantees a string. It cannot tell the model that "third of March" and "three slash four" should become one format, or which way round an ambiguous date reads. Rules handle inconsistent source formatting; the schema handles shape.

SAM: Pause here and answer before we go on. Choose two. Structured data extraction scenario. A utility company extracts fault reports from engineers' free-text visit notes into a schema with a fault category enum of six values. Two problems: vague notes such as "unit tripped, reset, seems fine" are being labelled "electrical" with no basis, and new equipment faults that fit none of the six are being forced into the nearest category. Which two schema changes address these? A, add an "unclear" value for notes that do not support a confident category. B, add an "other" value with a free-text fault detail field. C, replace the enum with a free-text category field. D, keep the field required and instruct the model to pick the closest category. E, expand the enum to forty values covering every fault the team can imagine. [pause]

ALEX: A and B.

SAM: Both. A gives ambiguity an honest answer; B gives unlisted faults somewhere to go with the detail preserved. C throws away the consistency downstream systems need. D is the instruction that causes the problem. E is scale instead of structure, and the forty-first fault still has nowhere to go. [sting]

## Segment four: validation and retry

SAM: Segment four, validation, retry and feedback loops. You scored zero here, so slowly. Start with retry with error feedback. When validation fails, the follow-up request carries three things: the original document, the failed extraction, and the specific validation errors. "Field invoice date: expected a date in year-month-day format, received 'Q3'." The model corrects against named errors.

ALEX: Not just "try again".

SAM: Never. The specific error is what makes the retry work. When does a retry succeed? Format mismatches and structural output errors: wrong date format, a value in the wrong field, a list where one item was expected. When does it fail? When the information is simply absent from the source, for example when it lives only in an external document that was not provided. No amount of feedback makes the model see a page it was never given.

ALEX: Then retries are mostly a waste. I would drop them and route every validation failure to a person. Simpler, and a human gets it right.

SAM: You have just over-applied the limit. Retries are cheap and fix a large class of errors. Routing format mismatches to a person floods the queue with work a retry fixes. The skill is telling the classes apart: retry format and structure, route absence.

ALEX: Miss pattern four again.

SAM: The tell is the word "always" or "every" in front of a retry decision. "Always retry" and "never retry" both lose. The right option distinguishes by failure type.

ALEX: What about semantic errors? Tool use does not catch those.

SAM: Self-correcting validation flows. Extract a calculated total, the sum of the line items, alongside the stated total printed on the invoice. If they differ, flag it. Add a conflict detected boolean for source data that is internally inconsistent, say a delivery date before the order date. The schema now carries the evidence your validator needs.

ALEX: Why not just have the model fix the total so it matches?

SAM: If the supplier's invoice is wrong, a silently corrected total hides a real discrepancy from accounts payable. Capture both, flag the conflict, let a rule or a reviewer decide.

ALEX: And the feedback loop part?

SAM: This is the structured error metadata your score report flagged. In the continuous integration scenario, add a detected pattern field to every finding: the code construct that triggered it, such as "unchecked return value" or "string concatenation in a query". When developers dismiss findings, you can group dismissals by pattern and see which ones are false positives. That tells you which criteria to rewrite, which category to disable, which acceptable-pattern example to add.

ALEX: And in extraction?

SAM: The same idea: each failure recorded by field and category becomes a targeted change to a prompt, a schema or an example.

SAM: Pause here and answer before we go on. Continuous integration scenario. A retailer's review bot posts about forty findings a day. Developers dismiss about a third. The team wants to cut false positives but cannot tell which kinds of finding are being dismissed, because findings are free-form comments. What should the architect add first? A, a detected pattern field on each structured finding, recording the code construct that triggered it, so dismissals can be analysed by pattern. B, a prompt instruction to report only findings the model is confident developers will accept. C, a rule that hides any finding not acted on within a week. D, a larger model for the review step. [pause]

ALEX: A.

SAM: A. It turns dismissals into data you can group. B is confidence filtering again, and it still tells you nothing about which patterns fail. C hides symptoms and destroys the signal. D is scale instead of structure; a bigger model with the same criteria makes the same calls. [sting]

## Segment five: batch processing

SAM: Segment five, batch. You scored well on synchronous versus batch, so the mechanics only. The Message Batches API: fifty percent cost saving, a processing window of up to twenty-four hours, and no guaranteed latency. Fit for non-blocking work such as overnight reports, weekly audits, nightly test generation. Wrong for anything blocking, such as a pre-merge check.

ALEX: And the limit people forget?

SAM: A batch request cannot do multi-turn tool calling. It cannot call a tool mid-request, get your result, and carry on. If your extraction needs a lookup halfway through, it is not batchable as written. The agentic loop needs your code in the middle, and a batch has nobody there.

ALEX: Correlating results?

SAM: Each request carries a custom ID that you set, a document identifier, and each result comes back with the same custom ID. Do not rely on the order of results.

ALEX: The SLA calculation.

SAM: Say the promise is results within thirty hours of arrival, and processing can take twenty-four. A document arriving just after a submission waits for the next. Submit every four hours: worst case four plus twenty-four, twenty-eight, inside thirty. Submit daily and the worst case is forty-eight.

ALEX: When a batch has failures, I would resubmit the whole thing. One code path, and the prompt may have changed anyway.

SAM: One code path is attractive. The guide's answer is to resubmit only the failed documents, identified by custom ID, with the change that addresses why they failed: an oversized document gets chunked, because unchanged it fails again. And before a large run, refine the prompt on a sample set so the first pass succeeds. Resubmission is the expensive path.

SAM: Pause here and answer before we go on. Choose two. Structured data extraction scenario. A law firm batches twelve thousand contracts overnight. In the morning, a hundred and sixty requests have failed, most because the contract exceeded the context limit. Which two steps are correct? A, resubmit only the failed requests, identified by their custom IDs. B, split the oversized contracts into chunks before resubmitting them. C, resubmit the full batch so every result comes from the same run. D, send the failed requests unchanged through the synchronous API. E, raise the maximum output tokens and resubmit. [pause]

ALEX: A and D. Sync gets them done before the lawyers arrive.

SAM: Half right. A is correct. Now, why did they fail?

ALEX: Context limit. [sighs] And D sends them unchanged. They fail again, just faster.

SAM: Miss pattern two: one good clause, the speed, attached to a fatal one, "unchanged". The answer is A and B. C pays to redo eleven thousand eight hundred and forty successes. E changes output length, but the problem is input size. [sting]

## Segment six: multi-pass review

SAM: Segment six, multi-instance and multi-pass review. Continuous integration scenario. Claude Code writes a change, then the same session is asked to review it. It approves its own work, and the bug ships.

ALEX: Turn on extended thinking for the review step, or add "critically examine your own code". Make it think harder.

SAM: Here the obstacle is context, not effort. The session still holds the reasoning that produced the code, so it is less likely to question its own decisions. The guide says an independent instance without that context catches subtle issues better than self-review instructions or extended thinking.

ALEX: So the tell is "same session".

SAM: "Same session" or "asks it to double-check". The answer is a second instance that sees the code, not the reasoning.

ALEX: And large reviews?

SAM: Split them. Focused per-file passes for local issues, then a separate integration pass for cross-file data flow. One pass over many files dilutes attention and produces contradictory findings. A bigger context window does not fix attention.

ALEX: Where does confidence come in?

SAM: A verification pass where the model reports confidence alongside each finding, so low-confidence findings route to a human. That is routing on a per-finding signal, not the vague "only report confident findings" filter from segment one.

SAM: Pause here and answer before we go on. Continuous integration scenario. A health-tech team's pipeline has Claude Code generate unit tests for each pull request and then, in the same session, review the tests for gaps. The review almost never finds anything, but engineers keep finding untested branches. What is the best change? A, run the review in a separate, independent Claude instance that receives the code and tests but not the generation session's reasoning. B, add an instruction to the generation session to review its tests critically before finishing. C, enable extended thinking for the generation session. D, run the same-session review three times and merge the results. [pause]

ALEX: A.

SAM: A. Fresh context removes the bias. B and C are the self-review instructions and extended thinking that the guide says lose to an independent instance. D repeats the same bias three times.

SAM: Back to the cold open. Alex, you said A, raise the retry limit and sharpen the feedback.

ALEX: I will defend it a little. Retry with error feedback is in the guide by name, and I have seen a retry find a value on page six that the first pass missed.

SAM: When the value is in the document, that is exactly right. Read the stem: "the master agreement is not part of the input". So, B. Classify the failure as absent from source, stop retrying, return null with a reason, and route it or supply the agreement. A spends more calls per invoice, and its best case is a fabricated term. C teaches format with nothing to format. D is scale instead of structure: no model reads a document it was not given.

ALEX: What should have stopped me?

SAM: "Not part of the input", or "refers to an external document". That phrase marks the limit of retry. [sting]

## Five to remember

SAM: Five to remember. One: explicit categories beat "be conservative". Say what to report and what to skip, define each severity with a code example, and temporarily disable a noisy category to protect trust in the rest.

ALEX: Two: when instructions give inconsistent output, add two to four targeted few-shot examples covering the ambiguous cases and the varied document shapes. If the value is in the document but comes back null, that is an example problem, not a schema problem.

SAM: Three: tool use with a schema eliminates syntax errors, not semantic ones. Tool choice auto may return text, any forces a call from several schemas, a named tool forces one extraction first. Required only when always present; "unclear" and "other" plus detail in enums; normalisation rules in the prompt.

ALEX: Four: retry with the document, the failed extraction and the specific errors. Retries fix format and structure, never absence. Calculated total beside stated total, a conflict flag, and a detected pattern field so dismissals become data.

SAM: Five: batch is half price, up to twenty-four hours, no tool round trips, results matched by custom ID; resubmit only the failures, changed. And a generator should not review itself: use an independent instance, then per-file passes plus an integration pass.

## Recap: the exam tells

SAM: Before we finish, your turn. Pause and name the six things this episode covered, with the giveaway for each. [pause]

ALEX: Explicit criteria, giveaway "be conservative". Few-shot, giveaway varied document shapes. Tool use and tool choice, giveaway a parse failure or an unknown document type. Retry, giveaway "not part of the input". Batch, the custom ID. Review, "same session".

SAM: Good. Now as exam tells.

SAM: If a question shows developers dismissing a review bot's findings and an option says "only report high-confidence findings", skip it and look for named categories to report and to skip.

ALEX: If detailed instructions still give inconsistent output, or some layouts extract and others come back null although the value is in the text, think few-shot examples.

SAM: If JSON fails to parse, think tool use with a schema. If the document type is unknown and prose comes back, think tool choice any. If one extraction must run first, force that named tool.

ALEX: If a retry keeps failing and the stem says the value lives in a document nobody provided, think stop retrying, return null with a reason, and route it. If it is a wrong date format or a value in the wrong field, retry with the specific error.

SAM: If line items do not add up to the total, think calculated total beside stated total and a conflict flag. If nobody can tell which findings get dismissed, think a detected pattern field.

ALEX: If the work is overnight and non-blocking, think batch at half price. If it needs a tool call mid-request or blocks a merge, it is not batchable. Failures go back alone, by custom ID, and changed.

SAM: And if the session that wrote the code is asked to review it, think an independent instance that sees the code but not the reasoning.

ALEX: Next, episode five: the agentic loop, stop reasons and enforced workflows.
