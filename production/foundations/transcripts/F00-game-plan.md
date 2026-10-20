---
episode: "F00"
series: "CCAR-F retake"
slug: game-plan
title: "Foundations game plan"
description: "How the Foundations exam is built: sixty items across four of six scenarios, the domain weights, a pacing plan for the Pearson VUE screen, and a four-step method worked through three official sample questions."
domain: "All domains"
weight: "100%"
target_minutes: 14
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode zero, the Foundations game plan.

ALEX: What will I walk away with?

SAM: By the end you'll be able to describe the paper you are walking into: sixty items, four scenarios drawn from six, and how the five domains are weighted. You'll be able to pace it with three checkpoints and the Review button. You'll have a four-step method for reading any item, and you'll recognise the five families of wrong answers on sight. Then you'll put the method to work on three official sample questions.

ALEX: And that matters because last time I was four or five answers short. Not a domain I didn't know, but items where the method slipped.

SAM: Then let's start with one of those samples, before any of the theory. [sting]

## Cold open: misrouted tool calls

SAM: An item before anything else. Customer support scenario. Production logs show the agent often calls get customer when people ask about an order, "check my order one two three four five", instead of calling lookup order. Both tools have one-line descriptions, "Retrieves customer information" and "Retrieves order details", and accept similar identifiers. What is the most effective first step to improve tool selection?

SAM: Option A, add five to eight few-shot examples to the system prompt showing order questions routed to lookup order. Option B, expand each tool's description with the input formats it handles, example queries, edge cases, and when to use it rather than the similar tool. Option C, add a routing layer that parses each message before the turn and pre-selects a tool by keyword. Option D, merge both into one lookup entity tool that works out which backend to query.

ALEX: A. Few-shot examples are the strongest lever on behaviour I know. Show it the pattern and it follows.

SAM: Hold that. It is an official sample question, and by the end of this episode you should be able to say why it loses.

ALEX: Then the shape of the thing first. What am I walking back into?

SAM: Sixty items in a hundred and twenty minutes. Multiple-choice and multiple-response, and every item states how many to select. The pass mark is a scaled seven hundred and twenty on a range of one hundred to one thousand. It is criterion-referenced: you are measured against a fixed standard, not against the other candidates.

ALEX: Last time I scored six hundred and sixty-one.

SAM: About four or five answers short. Not a domain you do not know: four or five items where the method slipped. The score report shows percent correct per domain, but the pass decision uses only the total, so a strong domain can carry a weak one.

ALEX: Multiple-response items. How do I handle them?

SAM: Read the number first, before the scenario. Then judge every option on its own: true here, or not. A choose-two item is five small true-or-false questions. The guide does not say whether partial credit exists, so act as if one wrong pick costs the whole item.

ALEX: Now the scenarios.

SAM: Six in the bank, four drawn at random for your sitting, each framing a run of items. One, a customer support resolution agent on the Agent S D K, with M C P tools get customer, lookup order, process refund and escalate to human, aiming for eighty percent first-contact resolution while knowing when to escalate. Two, code generation with Claude Code: slash commands, CLAUDE dot md, plan mode against direct execution. Three, a multi-agent research system: a coordinator with search, document analysis, synthesis and report subagents, producing cited reports. Four, developer productivity: an Agent S D K tool for exploring codebases with the built-in tools Read, Write, Bash, Grep and Glob, plus M C P servers. Five, Claude Code in continuous integration: automated review, test generation and pull request feedback that is actionable with few false positives. Six, structured data extraction: JSON schemas, validation, edge cases and downstream systems.

ALEX: And on screen the scenario sits on the left.

SAM: Left column, with the question and options on the right. It rarely changes, and last time you stopped reading it. That likely cost marks, because the frame carries constraints the item never repeats: "eighty percent first-contact resolution", "minimize false positives", "integrate with downstream systems". When the left panel changes, stop and read it in full before the next item. It takes twenty seconds. [sting]

## Domain weights and pacing

ALEX: Weights.

SAM: Agentic Architecture and Orchestration, twenty-seven percent, about sixteen items. Claude Code Configuration and Workflows, twenty percent, about twelve. Prompt Engineering and Structured Output, twenty percent, about twelve. Tool Design and M C P Integration, eighteen percent, about eleven. Context Management and Reliability, fifteen percent, about nine. The guide calls the weights approximate, so treat the counts as a guide.

ALEX: Agentic is over a quarter of the paper.

SAM: And it overlaps your gaps: stop reason, tool choice with prerequisite calls, hooks against prompts. Two of your zero-percent objectives, settings and hooks versus CLAUDE dot md, and PostToolUse hooks after every edit, sit in Claude Code configuration. The third, project versus user scope, runs through Claude Code and M C P integration alike. All three are mechanics, not judgment, which makes them the cheapest marks to win back.

ALEX: Pacing. I felt short of time and used every minute.

SAM: About one minute fifty an item. Three checkpoints, read off a clock that counts down in hours and minutes. Item twenty with one hour twenty-three left, item forty with forty-seven minutes left, item sixty with ten minutes left. Those ten minutes are for flagged items. If an item runs past two minutes, pick your best answer, flag it, and move on. The Review button, bottom left, lists every item and jumps to flagged or unanswered ones. The clock, top right, can be hidden; look at it only at the checkpoints.

ALEX: And concentration dipped late.

SAM: Eat beforehand and drink water before you go in. The last twenty items count the same as the first twenty. [sting]

## The four-step method

ALEX: The method.

SAM: Four steps. One, constraint words. Read the last line of the stem and name what it asks: most effective, first step, NOT, most likely root cause. Then the words that set the bar: "every", "always", "guaranteed", anything involving money. Two, which component the trigger touches. A symptom points at one part of the system: the decomposition, a tool description, the schema, the config scope. The right answer acts on that part. Three, the smallest mechanism that guarantees the outcome. Not the biggest or the cleverest; the smallest one that makes the failure impossible rather than less likely. Four, strike out half-right options. Right-click strikes an option on screen. Any option with one wrong clause goes, however good its first half sounds.

ALEX: And the distractors come in families.

SAM: Five. A probabilistic fix for a deterministic need: a prompt instruction where a hook or gate is required. Over-engineering: a classifier or routing layer before the simple fix has been tried. Blaming the wrong layer: a downstream agent when the coordinator's logs show the problem. Invented features: flags and config files that do not exist. And scale instead of structure: a bigger model or a bigger context window for a design problem.

SAM: Pause here and answer before we go on. Second sample, same scenario. In twelve percent of cases the agent skips get customer and calls lookup order using only the name the customer gave, which occasionally leads to the wrong account and an incorrect refund. What change most effectively addresses this? A, a programmatic prerequisite that blocks lookup order and process refund until get customer has returned a verified customer I D. B, a system prompt stating that verification through get customer is mandatory before any order operation. C, few-shot examples showing the agent always calling get customer first. D, a routing classifier that enables only the tools appropriate to each request type. [pause]

ALEX: Constraint words: "most effectively", "incorrect refunds". The component is tool ordering. A.

SAM: Right, and orchestration safeguards were a strength last time. So argue the other side.

ALEX: Fine. B and C ship today. Twelve percent down to one percent is a huge win, and a prerequisite gate is engineering work with its own bugs.

SAM: The prompt fix would help, and on a low-stakes task that trade can be right. But the guide says it plainly: when compliance must be deterministic, as with identity before financial operations, prompt instructions alone have a non-zero failure rate. One percent of refunds to the wrong account is still refunds to the wrong account. D changes which tools are available, not their order, so it acts on the wrong component.

ALEX: The tell?

SAM: Money moving after a step that must come first. Order that must hold lives in code, not in the prompt.

SAM: Pause here and answer before we go on. Third sample, Claude Code scenario. You want a slash command called review that runs the team's checklist, available to every developer when they clone or pull the repository. Where does the file go? A, the dot claude commands folder in the project repository. B, the commands folder under dot claude in each developer's home directory. C, the CLAUDE dot md file at the project root. D, a dot claude config dot json file with a commands array. [pause]

ALEX: A. "Every developer, clone or pull" means version control, which means project scope.

SAM: Yes. B is personal scope, never shared. C holds instructions and context, not command definitions. D is an invented feature: there is no such file. This is the shape that scored zero last time. The test is who needs it. Everyone on this repository: project, committed. Only you: your home directory. It holds for commands, skills, CLAUDE dot md and M C P servers alike.

ALEX: So M C P servers follow the same split.

SAM: Project scope is a dot M C P dot json file in the repository, with tokens referenced through environment-variable placeholders rather than committed. User scope is the dot claude dot json file in your home directory. Episode two goes deeper. [sting]

## Cold open: the verdict

ALEX: Back to the cold open. I said A, few-shot.

SAM: And there is a real rule behind it: the guide rates few-shot examples as the most effective technique for consistent output when instructions alone are not working.

ALEX: But?

SAM: But the stem says the descriptions are minimal. Tool descriptions are the primary mechanism the model uses to choose a tool, so the root cause sits there, and few-shot examples add tokens to work around it. That is a rule carried past its scope, miss pattern four. The answer is B.

ALEX: And D? Merging tools is a real design choice.

SAM: The guide calls it a valid architectural choice, and it loses here on two words: "first step". Merging takes more effort than a first step warrants. C is over-engineering that bypasses the model's own language understanding.

ALEX: So the tell was "minimal descriptions", plus "first step".

SAM: "Minimal" names the component. "First step" rules out anything heavier than the cheapest fix that reaches it. Read the last line before the options and both words are waiting for you. [sting]

## Using the series

ALEX: How do I use this series alongside episodes one and ten?

SAM: Those two were made for the Professional exam, but they are built on your Foundations score report. Episode one drills your five miss patterns: real-world instinct over the guide's answer, accepting an option with one wrong clause, misreading NOT or first step, over-applying a new rule, and importing a constraint the stem never stated. Episode ten re-teaches the mechanics you scored zero to fifty percent on. Ignore their item counts and Professional domain names; the habits and the mechanics transfer unchanged.

ALEX: Order?

SAM: This episode, then one. Then two and three on Claude Code, four on prompts and structured output, five to seven on agents, hooks and escalation, eight on tools, nine on context. Then ten, which by then lands as revision, eleven on the six scenarios, and twelve the night before and the morning of.

ALEX: And when you say pause?

SAM: Pause, and say your answer out loud before you hear ours. In choose-two drills, say true or false for every option. Recalling an answer does more than hearing it twice.

ALEX: The method once more, short enough to hold on the day.

SAM: Read how many to choose. Reread the scenario when it changes. Name what the last line asks. Find the component the trigger touched. Pick the smallest mechanism that guarantees the outcome. Strike out anything half right. [sting]

## Recap: the exam tells

SAM: One more pass before we go. Pause and name the five parts of the game plan: the format, the scenarios, the weights, the pacing, and the method. [pause]

ALEX: Sixty items in a hundred and twenty minutes, with the number to select on every item. Four scenarios of six. Agentic biggest at twenty-seven percent. Checkpoints at items twenty, forty and sixty. Four steps, five distractor families.

SAM: Now the same ground as exam tells. If an item says choose two, judge each option alone, as if it were five true-or-false questions.

ALEX: If the left panel changes, stop and read the whole scenario, because its constraints never get repeated in the item.

SAM: If you reach item twenty after thirty-seven minutes, or an item runs past two minutes, pick your best answer, flag it, and move on.

ALEX: If the last line says first step, rule out anything heavier than the cheapest fix that reaches the cause.

SAM: If an option is a prompt instruction where money or identity must be protected, it is the probabilistic fix for a deterministic need.

ALEX: If an option names a file or flag you have never seen, like a config dot json with a commands array, treat it as invented.

SAM: And if the stem says the tool descriptions are minimal, the fix lives in the descriptions.

ALEX: Next?

SAM: Episode one, your five miss patterns, each with a trap built to catch you.
