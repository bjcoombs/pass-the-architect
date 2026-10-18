---
episode: "F08"
series: "CCAR-F retake"
slug: context-reliability
title: "Context, review and provenance"
description: "Keeping exact facts alive through long sessions, exploring large codebases without context degradation, routing extractions to human review by calibrated confidence and stratified sampling, and carrying sources and conflicts intact through multi-agent synthesis."
domain: "Context Management & Reliability"
weight: "15%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode nine, context, review and provenance.

ALEX: And by the end?

SAM: You'll be able to keep exact amounts, dates and order numbers alive through a long conversation, and trim tool output before it floods the context. You'll spot context degradation in a long codebase exploration and choose between a scratchpad file, subagents and slash compact.

SAM: You'll decide when confident extractions can skip human review and how to keep checking them. And you'll carry sources and conflicting figures intact through a multi-agent report.

ALEX: Fifteen percent, the smallest domain, but primary for four of the six scenarios. And human review scored thirty-three percent last time.

SAM: Then start with a statistic that lost its source. [sting]

## Cold open: the uncited statistic

SAM: Multi-agent research scenario. The system writes a report on electric bus adoption in European cities. The final report says adoption reached thirty-one percent, with no citation. The logs show one subagent found thirty-one percent in a ministry dataset published this year, and another found twenty-two percent in an industry survey from two years earlier. Each subagent handed the synthesis agent a prose summary. What is the best fix? Option A, instruct the synthesis agent to always prefer the most recent source and cite it. Option B, require subagents to return structured claim-source mappings, with excerpts and publication dates, which the synthesis agent must preserve, so the report shows both figures with their sources and dates. Option C, add a fact-checking subagent after synthesis that re-searches every statistic in the final report. Option D, pass the full raw documents to the synthesis agent instead of summaries.

ALEX: C. A verification pass catches this and every other uncited number. That is what I would build.

SAM: Hold that. We come back to it at the end.

ALEX: What are we covering?

SAM: Context Management and Reliability, fifteen percent of the exam. It is the smallest domain, but it is a primary domain for four of the six scenarios: support, code generation, multi-agent research and structured extraction. Today is four task statements. Five point one, keeping critical information alive across long interactions. Five point four, context in large codebase exploration. Five point five, human review and confidence calibration, which scored thirty-three percent last time. Five point six, provenance and uncertainty in synthesis. Escalation and error propagation were covered in earlier episodes.

SAM: Segment one, five point one. Symptom: a support conversation runs forty turns across two issues. The system summarises older turns to save space. Near the end the agent offers a refund "for the recent order", and the customer replies that it was two hundred and forty-seven dollars eighty-three, order ending four four one, and they were promised it by Friday. The agent has none of that.

ALEX: Progressive summarisation ate the details.

SAM: Exactly the guide's phrase. Each round of summarising condenses numbers, percentages, dates and what the customer said they expect into something vague. "Customer wants a refund" survives. The amount, the date and the promise do not.

ALEX: Then stop summarising. Windows are huge now. Keep the whole transcript and the problem disappears.

SAM: There is something right in that. The API is stateless, so you do resend the full history on each request, and dropping it breaks coherence. That is a knowledge bullet in this task statement. But the guide's answer to lost figures is not "never summarise". It is a persistent case facts block: amounts, dates, order numbers and statuses extracted into a structured block that goes into every prompt, outside the summarised history.

ALEX: So summarisation can be as lossy as it likes, because the facts never pass through it.

SAM: Right. And for a session with several issues, the guide adds a separate context layer of structured issue data, keyed by order ID with amount and status, so issue one's refund never blurs into issue two's replacement. The tell in a stem is "exact", "specific amount", or "the customer later disputes". Precise values that must survive point to a facts block, not a better summary prompt.

SAM: Second symptom. The agent calls lookup order, and each result carries more than forty fields: warehouse codes, carrier events, marketing flags. The return decision needs five. After a dozen lookups, the context is mostly order noise.

ALEX: I would add a line to the system prompt: ignore fields not relevant to returns.

SAM: That helps the model's focus a little, and it costs nothing. But the forty fields are still in the context, still consuming tokens on every turn. Tool results consume tokens far out of proportion to their relevance. The guide's skill is trimming verbose tool outputs to the relevant fields before they accumulate, in code, between the tool and the conversation.

ALEX: So "tell the model to ignore it" is the probabilistic fix, and trimming is the structural one.

SAM: Yes. The tell is "accumulates" or "consumes context". The fix happens before the result lands.

SAM: Third mechanism, position. Models reliably process the start and end of a long input but may miss findings in the middle. The guide calls it the "lost in the middle" effect. When a coordinator aggregates many subagent reports, put a key findings summary at the beginning and organise the detail under explicit section headers.

ALEX: And when the downstream agent's budget is tight?

SAM: Change the upstream agent. Have it return structured data, key facts, citations and relevance scores, instead of verbose content and reasoning chains. And require subagents to include metadata: dates, source locations, methodological context. That metadata is what lets synthesis be accurate later.

SAM: Pause here and answer before we go on. Choose two. Multi-agent research scenario. The coordinator passes twelve document analysis reports to the synthesis agent. Each report is a long narrative including the subagent's reasoning. The synthesis agent's context is nearly full, and its reports regularly omit findings from reports in the middle of the batch. Which two changes best address this? A, have the document analysis subagents return structured key facts with citations and relevance scores instead of narrative reasoning. B, place a key findings summary at the start of the aggregated input and give each subagent's detail its own section header. C, increase max tokens on the synthesis call so it has room for all twelve. D, add an instruction telling the synthesis agent to read every section with equal care, especially the middle ones. E, truncate each report to its first five hundred words so the batch fits. [pause]

ALEX: B and D. D names the exact problem, and in my experience telling the model where to pay attention works.

SAM: B is right. D is the miss. Instinct says a direct instruction fixes attention, and it may help slightly, but it is a request, not a structural change to the input. That is miss pattern one, real-world instinct over the guide's answer. The guide's mitigations for position effects are a summary first and explicit headers. The second answer is A: smaller, structured upstream output for a limited downstream budget. C misreads a real parameter: max tokens caps output length; it does not enlarge the input. E is the blunt cut: it keeps the size down by throwing away whatever findings sit past word five hundred.

ALEX: The tell?

SAM: "Middle" plus "context nearly full". One points to position, the other to upstream structure. [sting]

## Segment two: context degradation

SAM: Segment two, five point four. Code generation scenario. A developer spends three hours with Claude Code exploring a legacy payments monorepo. Early on it found a class called refund ledger service and traced how it posts reversals. Now, asked about reversals again, it says the code "typically uses a repository pattern" and contradicts what it said earlier.

ALEX: Context degradation.

SAM: And the guide gives you the two symptoms by name: inconsistent answers, and references to "typical patterns" instead of the specific classes discovered earlier. When you see those words in a stem, this task statement is being tested.

ALEX: What fixes it?

SAM: Four tools. First, a scratchpad file. The agent writes key findings to a file as it goes: class names, the call chain, decisions. For later questions it reads the file back, so findings survive across context boundaries. Second, subagents for specific questions, "find all test files" or "trace refund flow dependencies". Each one does verbose exploration in its own context and returns a condensed summary, while the main agent keeps the high-level picture.

ALEX: The subagents already know what the main agent found, though. They inherit the conversation.

SAM: No, and that is the trap. A subagent starts with its own context and gets what you put in its prompt. So the third tool is to summarise the findings of one exploration phase before spawning subagents for the next, and inject that summary into their initial context. Fourth, slash compact. When the context fills with verbose discovery output, compaction summarises the history and replaces it, freeing space.

ALEX: Compaction is lossy, though. We just said summarisation loses exact detail. So I would never compact during exploration.

SAM: That is the earlier rule running past its scope. The guide names slash compact explicitly for extended exploration when the context fills with verbose discovery output. Raw grep results and file listings are exactly what you can afford to lose. What you protect are the findings, and those live in the scratchpad file, which compaction does not touch. Compact the noise; keep the facts on disk.

ALEX: Miss pattern four.

SAM: Yes. The tell is "verbose discovery output" or "context filling up". That is slash compact's job.

ALEX: And if the whole thing crashes halfway?

SAM: Structured state persistence. Each agent exports its state to a known location. On resume, the coordinator loads a manifest of that state and injects it into the agents' prompts. Rerunning everything from scratch throws away completed work, and hoping the session history survived is not a design.

SAM: Pause here and answer before we go on. Code generation scenario. After three hours exploring an unfamiliar insurance platform, Claude Code is giving answers that contradict its earlier ones and describing "common approaches" rather than the modules it found. The next phase is a migration plan touching four services. What is the most effective approach? A, run slash clear and re-explore from the beginning with a tighter prompt. B, record the key findings so far in a scratchpad file, then spawn a subagent per service with a summary of those findings in its prompt, and refer back to the scratchpad for later questions. C, switch to a model with a larger context window and continue in the same session. D, add a line to CLAUDE dot md telling Claude to always name specific classes rather than common approaches. [pause]

ALEX: B.

SAM: B. It persists findings, isolates the per-service exploration and injects the phase summary. A discards three hours of valid findings. C is scale instead of structure; degradation is about what the context holds, not only its size. D treats the symptom as a style problem. The wording drifts because the specific findings are no longer reliably in view, and an instruction cannot bring them back. [sting]

## Segment three: aggregate accuracy

SAM: Segment three, five point five, where you scored a third. Structured extraction scenario. An insurer extracts fields from claim documents. Overall accuracy on the validation set is ninety-seven percent. Leadership wants to stop human review of anything the model is confident about.

ALEX: Ninety-seven percent is better than most human teams. I would agree, with a threshold.

SAM: The number is real, and it is a good result. The guide's point is what an aggregate hides. Ninety-seven percent overall can sit on top of seventy-eight percent for handwritten repair estimates, or for the date-of-loss field on one form type. Typed claim forms are most of the volume, so they carry the average.

ALEX: So before cutting review, break it down.

SAM: By document type and by field. Verify consistent performance across every segment before you automate high-confidence extractions. The guide lists that as a skill in its own right. Then the routing itself. Have the model output field-level confidence scores, and calibrate the review threshold against a labelled validation set. Route fields with low confidence, and documents that are ambiguous or contradict themselves, to people, so limited reviewer time lands where errors are likely.

ALEX: Wait. Escalation in five point two says self-reported confidence is an unreliable proxy. Now five point five says have the model output confidence. Which is it?

SAM: Good catch, and both are in the guide. The difference is calibration. A raw self-reported score used as an escalation trigger is the distractor. A field-level score, checked against labelled data to set where the threshold actually sits, is the answer. The tell is "calibrated" or "labelled validation set". An option using the model's stated confidence with a fixed cut-off and no calibration loses.

ALEX: Then once it is running, I would put every reviewer on the low-confidence queue. Why spend anyone on extractions the model was sure about?

SAM: Because capacity is limited, that instinct is half right; most attention should go to low confidence. But if no one looks at the high-confidence stream, you cannot measure its error rate, and you will not see new error patterns. A new repair-shop template arrives, the model extracts the wrong total with high confidence, and nothing routes it anywhere. So the guide prescribes stratified random sampling of high-confidence extractions, for ongoing error rate measurement and novel pattern detection.

ALEX: Why stratified? A plain random sample is simpler.

SAM: A plain random sample is mostly typed claim forms, because that is most of the volume. Rare document types barely appear. Stratifying by document type guarantees each segment is sampled. The tell is "novel", "ongoing", or "measure the error rate" alongside "high confidence".

SAM: Pause here and answer before we go on. Choose two. Structured extraction scenario. A customs broker extracts shipment declarations. Validation accuracy is ninety-seven percent overall, and the team plans to auto-approve every extraction with field confidence above zero point nine. Which two steps should come with that change? A, measure accuracy by document type and by field on labelled data, and confirm every segment performs before auto-approving. B, after launch, review a stratified random sample of auto-approved extractions to track error rates and catch new error patterns. C, auto-approve now, because ninety-seven percent beats the human team's measured accuracy. D, ask the model to re-check any extraction it rated above zero point nine before approval. E, review only the lowest-confidence ten percent of extractions from now on. [pause]

ALEX: A and B.

SAM: Both. A checks the segments the average hides, before automation. B keeps measuring after it. C trusts the aggregate the guide warns about. D is a second probabilistic pass with no labelled check behind it. E is a fixed slice, not a calibrated threshold, and it never looks at the confident stream at all. [sting]

## Segment four: provenance

SAM: Segment four, five point six, provenance. Back to research. A web search subagent finds a claim, a document analysis subagent summarises it, the synthesis agent summarises the summaries. By the report, the claim has no source. Attribution is lost when findings are compressed without keeping the link between claim and source.

ALEX: So the claim-source link has to be data, not prose.

SAM: Yes. Require subagents to output structured claim-source mappings: the claim, the source URL or document name, and the relevant excerpt, plus the publication or collection date. The synthesis agent must preserve and merge those mappings, not rewrite them away.

ALEX: Now two credible sources disagree on a statistic. An analyst would pick the more authoritative one and move on. Readers want an answer.

SAM: A good analyst does make that call, and readers do want clarity. The guide's answer is different: annotate the conflict, both values with their attribution, rather than selecting one arbitrarily. The document analysis subagent completes its work with the conflicting values included and marked, and the coordinator decides how to reconcile them before anything goes to synthesis.

ALEX: Why not let the subagent decide? It read the documents.

SAM: It sees only its slice. The coordinator sees the whole task. The tell is "two credible sources" or "conflicting figures". Any option that picks one, averages them or drops the metric loses.

ALEX: So every difference between sources gets flagged as contested.

SAM: Careful, that over-reaches. Check the dates first. Twenty-two percent from two years ago and thirty-one percent today may both be right; that is growth, not contradiction. That is why the guide requires publication or collection dates in structured outputs: so temporal differences are not misread as conflicts.

ALEX: And the report itself?

SAM: Explicit sections separating well-established findings from contested ones, keeping each source's original characterisation and methodological context. If a source says "preliminary" or "sample of two hundred", that survives. And render content by type: financial data as tables, news as prose, technical findings as structured lists, not one uniform format. It links back to error propagation too: where a source was unavailable, coverage annotations say which areas have gaps.

SAM: Pause here and answer before we go on. Multi-agent research scenario. A document analysis subagent finds that two credible industry reports give different figures for the same market's size in the same year. What should it do? A, report the figure from the more recently published report. B, return both figures with their sources, excerpts and dates, marked as conflicting, and let the coordinator decide how to reconcile before synthesis. C, leave the market size out of its output, since the value is uncertain. D, report the average of the two figures with both sources cited. [pause]

ALEX: A. Newer data supersedes older. That is basic.

SAM: That is miss pattern five, importing a constraint the stem never stated. Nothing says the newer report corrects the older one; they may use different methods or definitions, and the stem says same year, so this is not a temporal difference. The answer is B: conflict included, annotated, coordinator decides. C is silent suppression, which the guide treats as an anti-pattern. D invents a number that neither source reported, though it cites both.

ALEX: D sounded balanced.

SAM: It has one right clause, citing both, and one wrong one, the average. That is miss pattern two. Every clause must hold. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you picked C, a fact-checking subagent.

ALEX: And I still like it. It catches uncited numbers wherever they come from, and it ships without touching the subagents.

SAM: Verification passes are useful, and it would catch some of these. But it is detective, added after the damage. It re-searches a number whose source was already lost, and it may find either figure and still not know the two disagree. The answer is B. Structured claim-source mappings with dates, preserved through synthesis, so the report shows both figures, each with its source and year. That fixes the root: the prose summaries dropped attribution and dates. A imports a rule, newest wins, and still hides the other figure. D pushes the problem into a larger, noisier input, and gives the synthesis agent more middle to lose things in.

ALEX: The tell?

SAM: "No citation" plus "prose summary". Attribution lost in a hand-off is fixed in the hand-off's structure. [sting]

## Five to remember

SAM: Five to remember. One: exact figures, dates and IDs go in a persistent case facts block outside the summarised history, and tool results get trimmed to relevant fields before they pile up.

ALEX: Two: lost in the middle is fixed by a key findings summary first and explicit section headers, and a tight downstream budget is fixed by structured upstream output.

SAM: Three: "typical patterns" and contradictions mean context degradation. Scratchpad files for findings, subagents with phase summaries in their prompts, slash compact for verbose discovery output, manifests for crash recovery.

ALEX: Four: an aggregate accuracy hides weak segments. Check by document type and field, calibrate field-level confidence on labelled data, and keep a stratified random sample of the confident stream under review.

SAM: Five: claim-source mappings with dates survive synthesis. Conflicts are annotated, never picked, and the coordinator reconciles them.

## Recap: the exam tells

SAM: Before we finish, your turn. Pause and name the four task statements we covered, with the giveaway word for each. [pause]

ALEX: Long interactions, giveaway "exact" or "the customer later disputes". Codebase exploration, giveaway "typical patterns". Human review, giveaway "ninety-seven percent overall". Provenance, giveaway "two credible sources".

SAM: Good. Now as exam tells.

SAM: If a figure, date or order number disappears after summarisation, think a persistent case facts block outside the summarised history. If tool results pile up with fields nobody uses, think trimming them in code before they land.

ALEX: If findings from the middle of a big input go missing, think a key findings summary first and section headers. If the downstream context is nearly full, think structured output from the upstream agent, not a bigger max tokens.

SAM: If Claude Code starts describing typical patterns and contradicting itself, think a scratchpad file, subagents with a phase summary in their prompt, and slash compact for verbose discovery output.

ALEX: If high overall accuracy tempts the team to drop review, think accuracy by document type and field first, confidence calibrated on a labelled set, then a stratified random sample of the confident stream.

SAM: If an option uses the model's raw self-rated confidence with a fixed cut-off, it loses. "Calibrated" is the word that makes confidence the answer.

ALEX: And if a report has an uncited number or two sources disagree, think claim-source mappings with dates, the conflict annotated, and the coordinator deciding. Check the dates before calling it a conflict.

ALEX: Next time, all six scenarios, one at a time, and what each one tends to test.
