---
episode: "F02"
series: "CCAR-F retake"
slug: coordinators
title: "Coordinators, subagents and decomposition"
description: "How a coordinator runs a team of subagents: hub-and-spoke routing, isolated subagent context and explicit context passing, the Task tool and parallel spawning, scoped subagent tools, coverage loops, and when to pick a fixed pipeline over dynamic decomposition."
domain: "Agentic Architecture & Orchestration"
weight: "27%"
target_minutes: 24
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode six: coordinators, subagents and decomposition.

ALEX: So by the end?

SAM: You'll be able to say why every message between subagents goes through the coordinator. You'll know what a subagent can see, and what to put in its prompt so the citations survive. You'll configure spawning with the Task tool, run independent work in parallel, and scope each subagent's tools. You'll spot duplication and gaps in a coordinator's plan and close them with a loop. And you'll choose between a fixed pipeline and a plan that adapts.

ALEX: Which matters because Agentic Architecture is twenty-seven percent of the exam, and subagent context is the most tested idea in it.

SAM: Then let's open with an item. [sting]

## Cold open: the over-routed query

SAM: Multi-agent research system. A user asks, "What year did the E U A I Act enter into force?" The coordinator sends the question to all four subagents: web search, document analysis, synthesis and report. Three minutes later the user gets a twelve-page cited report. It does the same for every question, simple or broad. Which change fixes this best? Option A, have the coordinator analyse what each query needs and invoke only the subagents that query calls for. Option B, add a rule that sends any query under fifteen words down a short path. Option C, cap every subagent at a small number of turns so the full run finishes faster. Option D, tell the report subagent to keep reports short when the question is simple.

ALEX: B. A length rule is cheap, it's deterministic, and you all keep telling me deterministic beats prompts.

SAM: Hold that. We come back to it at the end.

ALEX: Domain one, Agentic Architecture and Orchestration. Twenty-seven percent, the biggest domain.

SAM: And this episode takes three of its task statements. One point two, orchestrating a coordinator with subagents. One point three, how subagents are invoked, what context they get, and how they are spawned. One point six, decomposition: a fixed pipeline or a plan that adapts. Your score report said seventy-five percent on dynamic decomposition, so that part gets its own segment.

ALEX: Which scenarios?

SAM: Mostly the multi-agent research system, where a coordinator runs four subagents, and developer productivity, where an Agent S D K agent explores codebases with Read, Write, Bash, Grep and Glob.

SAM: Segment one, the shape. The guide calls it hub-and-spoke. The coordinator is the hub. It manages all communication between subagents, all error handling and all routing of information. Subagents never talk to each other directly. Everything goes up to the coordinator and back down.

ALEX: What does the coordinator actually do, beyond pass messages?

SAM: Four jobs in the guide. It decomposes the task, delegates the pieces, aggregates the results, and decides which subagents to invoke based on how complex the query is. That last one is the cold open.

ALEX: I'll push on the routing rule. Document analysis finishes, and synthesis needs its output. Sending it up to the coordinator and back down is an extra hop. A direct pipe from analysis to synthesis is faster and simpler. I'd build that.

SAM: The hop is real. But the guide gives three reasons to route everything through the coordinator: observability, consistent error handling, and control over what each subagent receives. Wire analysis straight into synthesis and the coordinator can no longer see what passed between them, catch a failure in one place, or decide that synthesis should get only part of the analysis.

ALEX: And if synthesis keeps needing quick fact checks mid-run?

SAM: A narrow, scoped tool for that one common need can be right; that is least privilege, not a side channel. A direct agent-to-agent link is still wrong.

SAM: The tell: if an option says "directly" between two subagents, or an item asks why to keep the coordinator in the middle, look for observability, consistent error handling and controlled information flow. [sting]

## Segment two: isolated context

SAM: Segment two, context. This is the most tested idea in the domain. A subagent runs in its own isolated context. It does not inherit the coordinator's conversation history. It does not share memory with earlier runs of itself. It knows what is in its prompt, and nothing else.

ALEX: So the symptom of forgetting that?

SAM: A synthesis subagent that writes a fluent report with no citations, or fills gaps with general knowledge. The coordinator assumed synthesis could see what search found. It could not.

ALEX: And the fix is put it in the prompt.

SAM: Two parts. First, include the complete findings from the earlier agents directly in the synthesis subagent's prompt: the web search results and the document analysis output. Second, pass them in a structured format that keeps content apart from metadata. Each finding carries the claim, an evidence excerpt, and the source URL or document name, with page number and date where they apply. Structure is what lets attribution survive the hand-off.

ALEX: Here I'd go the other way. Context is expensive and long prompts dilute attention. I'd have the coordinator write a tight paragraph summarising what search and analysis found, and pass that.

SAM: The instinct is right in one place. Dumping raw search pages and every subagent's reasoning into the prompt is bad; key facts get lost in the middle, the same effect you meet in Domain five.

SAM: But you've stretched "keep it lean" past where it holds. A prose paragraph throws away exactly what synthesis needs: which source said what. Once the URLs and page numbers are gone, no instruction can bring the citations back. Lean means the findings without the raw material and reasoning, not a summary in place of the findings.

SAM: The tell: when the symptom is lost attribution or missing citations, pick complete findings in a structured form with source metadata. An option that says "summary" or "relies on the subagent having access" is the trap.

SAM: Pause here and answer before we go on. Multi-agent research system. Reports on contested topics come back with citations missing, and twice the report gave one market-size figure where the two sources disagreed. Logs show the coordinator spawns synthesis with a one-paragraph prose summary of what search and analysis found. Choose two. Option A, include the complete search and analysis findings directly in the synthesis subagent's prompt. Option B, pass each finding as a structured record with the claim, an evidence excerpt, the source URL or document name, and page number. Option C, spawn synthesis inside the coordinator's session so it inherits the earlier findings automatically. Option D, add "always cite your sources" to the synthesis subagent's system prompt. Option E, pass the full raw text of every page the search subagent retrieved. [pause]

ALEX: A and B.

SAM: A and B. A gives synthesis the material; B keeps each claim tied to its source, which is also what lets synthesis report both figures with their sources instead of quietly picking one. C rests on a mechanism the guide says does not exist: subagents do not inherit parent context. D asks for citations the subagent was never given. E is the over-correction: complete, but raw, long, and no better at tying claims to sources. [sting]

## Segment three: spawning subagents

SAM: Segment three, spawning. In the Agent S D K, the coordinator spawns a subagent by calling the Task tool. That brings a configuration rule the exam likes: the coordinator's allowed tools list must include Task. Leave it out and the coordinator cannot delegate at all.

ALEX: So the symptom is a coordinator that does everything itself.

SAM: Or one that never calls a subagent however you word the prompt. That is configuration, and rewording will not fix it.

ALEX: And each subagent is defined where?

SAM: An agent definition for each subagent type, which the guide names AgentDefinition. Three things matter: a description, a system prompt, and tool restrictions. The description works like a tool description from Domain two: it is what the coordinator reads when deciding which subagent fits. Vague descriptions mean wrong picks.

ALEX: And tool restrictions is least privilege.

SAM: Each subagent gets the tools its job needs and no more. A synthesis subagent has no reason to hold web search. An explore subagent has no reason to hold Write.

SAM: Pause here and answer before we go on. Developer productivity. Your agent uses an explore subagent to map an unfamiliar legacy service before engineers start changing it. Twice this week the explore subagent edited files while "tidying" as it read, and one edit broke a build. The system prompt already says to read only. What is the best change? Option A, restrict the explore subagent's definition to the Read, Grep and Glob tools. Option B, rewrite the system prompt in capitals and add an example of a read-only run. Option C, log every file write so engineers can review and revert changes. Option D, remove Task from the coordinator's allowed tools so no subagent can run unsupervised. [pause]

ALEX: A. Take the tool away and it cannot write.

SAM: A. It removes the capability at the root, the same way the guide prefers hooks and gates over prompts when an outcome must hold. B is a probabilistic fix for a deterministic need; the prompt already said read-only and it failed. C is a detective control: it tells you after the build broke. D stops the coordinator spawning anything, which throws away the whole design to fix one subagent.

SAM: Now speed. When subtasks are independent, the coordinator spawns them in parallel by emitting several Task tool calls in a single response. Not one call per turn, waiting for each to finish.

ALEX: Let me argue for sequential. One subagent at a time is easier to debug, logs read in order, and if the first search fails I haven't spent tokens on the other two. My team ran sequential for months.

SAM: Part of that is right, and it is the part people forget. When one step needs another's output, sequential is the correct design. Synthesis cannot start before search and analysis return. Spawning it in parallel with them would be wrong.

SAM: But for independent work, three subtopics or three source types, sequential adds the full latency of each run for no gain in quality.

SAM: The tell is the word "independent" or a set of searches that do not depend on each other. Then the answer is several Task calls in one coordinator response. If an option says "across separate turns", that is the slow version.

SAM: Last piece of one point three: how the coordinator writes the subagent's prompt. The guide wants research goals and quality criteria, not step-by-step procedure.

ALEX: Here I'd disagree hardest. When I've given agents vague goals they wander. When I've given exact steps, exact queries, exact sources, exact filters, I get predictable output. Predictable is what production needs.

SAM: For a fixed, predictable workflow, that's true, and segment five agrees with you. Step-by-step is the right call when the steps really are known.

SAM: Research is not that. If the coordinator dictates exact queries and the first returns little, a subagent following orders reports "insufficient results" and stops. Goals plus criteria, such as "find peer-reviewed or government sources on X from the last three years, at least two per claim", let it adapt when the planned route fails.

SAM: The tell: a subagent that gives up when the planned route fails, or ignores a better source it found along the way, points to a coordinator prompt that is too procedural. The fix is goals and quality criteria.

ALEX: The guide also lists fork-based sessions under one point three.

SAM: One line here, the detail is next episode. Forking creates independent branches from a shared analysis baseline, so you can try two different approaches without redoing the shared groundwork. [sting]

## Segment four: duplication and gaps

SAM: Segment four, coverage. Two failure modes, and they are opposites. Duplication is subagents covering the same ground. Gaps are ground nobody covers. Both start in the coordinator's decomposition.

ALEX: Duplication first.

SAM: Fix it by partitioning the research scope before delegating. Give each subagent distinct subtopics, or distinct source types: one takes academic papers, one takes regulator publications, one takes industry reports.

ALEX: Let me defend some overlap. Two agents finding the same fact from different angles is corroboration. In a cited report I'd want that. Isn't a bit of redundancy a feature?

SAM: Corroboration has value, and the synthesis stage should note where sources agree or conflict.

SAM: But the exam frames overlap as cost without design. If the item says two subagents investigated the same subtopics and token use nearly doubled, the root cause is unclear task boundaries, and the fix happens before any work starts: the coordinator partitions the space.

SAM: The tell: "same subtopics", "overlap", or "tokens doubled" means partition the scope in the coordinator, by subtopic or by source type.

ALEX: And gaps?

SAM: The guide names a specific risk: overly narrow decomposition by the coordinator gives incomplete coverage of a broad topic. Every subagent can succeed at its assignment and the report is still lopsided, because the assignments were too narrow. When the logs show the coordinator's subtasks, read them. If they cover a slice of the topic, that is your root cause, not the search queries downstream.

ALEX: And the cure is the refinement loop.

SAM: The coordinator evaluates the synthesis output for gaps, re-delegates targeted queries to search and analysis for exactly those gaps, then re-invokes synthesis. It repeats until coverage is sufficient. The stopping condition is coverage, not a count.

SAM: Pause here and answer before we go on. Multi-agent research system. A user asks how European hospitals are adopting A I. The synthesis output covers diagnostic imaging and scheduling well, but has almost nothing on nursing workflows or procurement, both of which the request named. Which design closes gaps like this best? Option A, the coordinator checks the synthesis output against the request, sends targeted queries for the missing areas to search and analysis, and re-runs synthesis, repeating until coverage is sufficient. Option B, run the whole pipeline three times on every request and merge the three reports. Option C, instruct synthesis to fill thin areas from its own knowledge so the report is complete. Option D, let synthesis call the web search subagent directly whenever it spots a gap. [pause]

ALEX: D. Synthesis is the one that knows what's missing, so let it ask. Fewest hops, and the gap closes at the source. That's what I'd build.

SAM: That's miss pattern one, real-world instinct overriding the guide, and it lands on a hub-and-spoke violation. D wires one subagent straight to another, so the coordinator loses sight of what was asked, why, and what came back. The answer is A, the loop in the guide's own words: evaluate for gaps, re-delegate with targeted queries, re-invoke synthesis, stop when coverage is sufficient.

SAM: B is a fixed iteration count, which the guide treats as an anti-pattern when it is the main stopping rule. Three blind runs can miss the same gap three times. C swaps research for invention: uncited claims in a report whose whole point is citations.

ALEX: What should have stopped me?

SAM: The phrase "closes gaps" in a coordinator scenario. Gap closing is the coordinator's job, through the coordinator. [sting]

## Segment five: decomposition strategy

SAM: Segment five, decomposition strategy, your seventy-five percent. Two patterns. A fixed sequential pipeline, which the guide also calls prompt chaining, runs the same steps in the same order every time. Dynamic adaptive decomposition creates the next subtasks from what the last step found.

ALEX: When does each win?

SAM: The guide's rule: prompt chaining for predictable, multi-aspect reviews. Dynamic decomposition for open-ended investigation. If you can write the steps down before you see the input, chain them. If the first finding could change the plan, go dynamic.

ALEX: Then I'd go dynamic everywhere. The model is good at planning. Why hard-code anything when it can work out the steps for each input?

SAM: That's the over-application. On a predictable review, dynamic planning adds cost and variation for nothing; the plan comes out the same each time, except when it quietly skips a step. Applying a dynamic, orchestrator-style design to a predictable workflow is a named pitfall in the study material.

SAM: The tell: "every", "always", "the same checks" or a known list of aspects means prompt chaining. "Unfamiliar", "legacy", "investigate", "open-ended" or "we don't know yet" means dynamic.

ALEX: Give me the chaining example from the guide.

SAM: Large code reviews. Splitting the review into a local analysis pass on each file, then a separate cross-file integration pass. One pass over twenty files spreads attention thin, and problems that live between files get missed.

SAM: Pause here and answer before we go on. Developer productivity. An engineer asks your agent to review a twenty-two-file branch before it goes to pull request. The review is thorough on the first few files, shallow on the rest, and missed that a renamed field in one module broke two callers elsewhere. What is the best change? Option A, run a local analysis pass on each file, then a separate cross-file integration pass. Option B, move to a model with a larger context window so all twenty-two files fit comfortably. Option C, add "review every file with equal care and check cross-file effects" to the prompt. Option D, spawn one subagent per file and merge their findings as the final review. [pause]

ALEX: A.

SAM: A. Per-file passes fix the uneven depth; the integration pass catches the broken callers. B is scale instead of structure: the files already fit, and attention still spreads. C asks for the outcome without changing the mechanism. D is the half-right trap: per-file passes, but no integration pass, so the renamed field still slips through. One correct clause is not enough.

SAM: Now the dynamic side. The guide's example is "add comprehensive tests to a legacy codebase". You cannot list the steps up front, because you do not know the code yet. So: first map the structure, then identify the high-impact areas, then build a prioritised plan that adapts as dependencies are discovered.

ALEX: I'll argue for a full map first. Before writing one test, I'd have the agent read the whole codebase, list every module and dependency, and fix the complete plan. No surprises halfway.

SAM: Mapping first is right; the guide puts it first. Where it goes wrong is "complete plan, fixed". In a legacy system the first dependency you find can reorder everything, and an exhaustive survey burns context on areas that turn out not to matter.

SAM: The tell is the phrase "adapts as dependencies are discovered". A plan that cannot change after step one is a fixed pipeline wearing an investigation's clothes.

SAM: Pause here and answer before we go on. Developer productivity. An engineer asks the agent to find out why a legacy billing export sometimes drops records overnight. Nobody on the team knows the code. Which decomposition fits? Option A, a fixed five-step pipeline: read the export script, read the scheduler config, read the database schema, read the logs, write a report. Option B, map the export's structure with Grep and Glob, form hypotheses from what turns up, and create the next subtasks from each finding, reprioritising as dependencies appear. Option C, spawn one subagent per file in the repository in parallel and merge what they report. Option D, ask the agent to read every file first and only then decide what to investigate. [pause]

ALEX: B.

SAM: B. Intermittent, unknown code, root cause not yet known: open-ended investigation, so dynamic decomposition. A fixes the steps before anything is learned; if the cause is a retry job that is not on its list, it never looks. C is parallelism without a plan: most subagents read irrelevant files and nobody connects the findings. D is the exhaustive-survey trap from a moment ago. [sting]

## Cold open: the verdict

SAM: Back to the cold open. The research system sends a one-line factual question through all four subagents. Option A, the coordinator analyses what the query needs and invokes only those subagents.

ALEX: I said B. The length rule.

SAM: A. That is the guide's skill bullet almost word for word: coordinators that analyse query requirements and dynamically select which subagents to invoke, rather than always routing through the full pipeline.

SAM: B looks deterministic, and that's what makes it tempting. But determinism matters when a rule must hold, like identity checks before a refund. Here the need is judgement about complexity, and word count is a poor proxy. "Compare E U and U S A I regulation" is short and broad; a long, chatty question can need one search. You imported "deterministic is always better" into a stem that never asked for a guarantee.

ALEX: Miss pattern four. Over-applying the rule.

SAM: C is an arbitrary cap: it makes broad questions worse without making simple ones smarter. D trims the last step, but the coordinator still runs the whole pipeline; it treats the symptom at the wrong layer.

SAM: The tell: "every query goes through every subagent" means dynamic subagent selection in the coordinator. [sting]

## Five to remember

SAM: Five to remember. One: hub-and-spoke. The coordinator decomposes, delegates, aggregates and picks which subagents a query needs. All subagent traffic goes through it, for observability, consistent error handling and controlled information flow.

ALEX: Two: subagents inherit nothing. Put the complete prior findings in the prompt, structured so claim and source metadata travel together.

SAM: Three: the coordinator spawns with the Task tool, so Task must be in its allowed tools. Independent work goes out as several Task calls in one response. Each agent definition carries a description, a system prompt and only the tools that job needs.

ALEX: Four: partition scope by subtopic or source type to stop duplication. Narrow decomposition causes gaps, so read the coordinator's subtasks first. Close gaps with a loop that stops on coverage, not a count.

SAM: Five: chain the predictable, decompose the open-ended. Per-file passes plus a cross-file integration pass for big reviews. Map, prioritise, and adapt as you go for legacy investigation.

## Recap: the exam tells

SAM: Before the next episode, recall. Pause and name the five segments, and the giveaway for each. [pause]

ALEX: Hub-and-spoke. Isolated context. Spawning with Task. Coverage, meaning duplication and gaps. And a fixed pipeline against dynamic decomposition.

SAM: As exam tells, then. If an option wires two subagents together directly, think observability, consistent error handling and controlled information flow, and keep the coordinator in the middle.

ALEX: If a report loses its citations, think complete findings in the prompt, structured so each claim keeps its source.

SAM: If a coordinator never delegates, check that Task is in its allowed tools. If the searches are independent, think several Task calls in one response, not one per turn.

ALEX: If a subagent edits files it should only read, take the tool out of its definition rather than rewording the prompt.

SAM: If two subagents covered the same subtopics, partition the scope in the coordinator. If the report is lopsided, read the coordinator's subtasks before the search queries, and close the gap with a loop that stops on coverage.

ALEX: If the stem says every, always or the same checks, chain it, like per-file passes plus a cross-file pass on a big review. If it says unfamiliar, legacy or investigate, decompose as you go.

ALEX: Next, episode seven: hooks, sessions and escalation, including the fork we skipped today.
