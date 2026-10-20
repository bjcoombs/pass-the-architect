---
episode: "A01"
series: "CCAO-F"
slug: prompting
title: "Prompting and task execution"
description: "How to write a prompt a capable newcomer could act on, break a big request into stages, iterate by changing one thing at a time, and adapt the approach for analysis, research, drafting and brainstorming."
domain: "Prompting and Task Execution"
weight: "14%"
target_minutes: 18
---

## In this episode

SAM: Welcome to Pass the Architect, Associate Foundations. This is episode one: prompting and task execution.

ALEX: What will I be able to do by the end?

SAM: Write a prompt that gives Claude the audience, the purpose and the shape of the answer. Decide when a big request should become a chain of smaller ones. Improve a prompt by changing one thing at a time instead of hitting regenerate. And switch your approach for analysis, research, drafting and brainstorming, because each wants something different.

ALEX: Fourteen percent of the paper, about eight items. And the trap is the one I fall into at work: adding adjectives or pasting in everything instead of saying what I need.

SAM: Then we start with a project update that went wrong. [sting]

## Cold open: the steering committee update

SAM: Here is your opening item. A consultant asks Claude to "write a project update" for a client's steering committee. The draft is long, generic and leads with activity rather than decisions. What is the most effective next prompt? Option A: repeat the request and add "make it excellent, concise and professional". Option B: state that the readers are the steering committee with ten minutes on the agenda, that the purpose is a decision on the phase two budget, that it must cover status against milestones, the top two risks and the decision needed, on one page, and attach this month's status notes. Option C: switch to the most capable model and repeat the request. Option D: attach every project document from the last six months so Claude has the full picture.

ALEX: D. The draft was generic because Claude didn't know enough. Give it everything and it can't miss.

SAM: Hold that. We come back to it at the end.

ALEX: So what does this domain actually test?

SAM: Four objectives. Create effective prompts for business and technical tasks. Apply task decomposition to structure complex requests. Iterate prompts to improve output quality. And adapt your strategy to the task type: analysis, research, drafting, brainstorming.

ALEX: Start with the first. What makes a prompt effective?

SAM: Anthropic's own guidance says to treat Claude as a brilliant but new employee who lacks context on your norms and workflows. Their golden rule: show the prompt to a colleague with minimal context. If they would be confused, Claude will be too.

ALEX: So what would that colleague need?

SAM: The task, led by a clear verb. Who it is for and how it will be used. Why any constraint exists, because Claude generalises from the reason. The shape of the answer: length, format, sections. And the material to work from, kept apart from the instructions in clearly labelled sections.

ALEX: Why does the reason matter?

SAM: Compare "never use ellipses" with "this will be read aloud by a text-to-speech engine, so never use ellipses, it cannot pronounce them". The second lets Claude make sensible choices about things you didn't list. Two more habits: say what to do rather than what not to do, so "write in flowing paragraphs" beats "no bullet points". And give it permission to say the data is insufficient, which cuts guessing.

ALEX: And examples?

SAM: Examples are one of the most reliable ways to steer format and tone. Start with one. If the output still drifts, add a few varied ones, and make sure they show only what you want, because Claude copies them closely.

ALEX: And technical tasks? I'm not a developer.

SAM: Same rules, more precision. Asking for a spreadsheet formula, give the column layout, a sample row and the result you expect. Asking about an error from the finance system, paste the exact message and what you were doing.

ALEX: Here is my honest workflow, though. I type one line, see what comes back, and fix it in the follow-ups. Writing a full brief up front takes longer than two quick corrections.

SAM: For a quick one-off, that's fine, and Anthropic's own advice is that longer prompts are not always better. Use the minimum structure that works.

ALEX: So why would the exam disagree?

SAM: Because the item will tell you the first attempt already failed, and how. Generic, wrong level for the reader, missed the point. Each of those is a missing piece of context, and adjectives like "better" or "more professional" add none of it. The tell: when the stem describes output that is generic or pitched at the wrong reader, pick the option that adds audience, purpose and format.

SAM: Pause here and answer before we go on. Choose two. A finance analyst asks Claude to explain this quarter's cost variance for regional managers. The draft is three pages, full of accounting terms, and the managers don't read past page one. Which two changes to the prompt most directly fix it? A: state that the readers are regional managers without finance training, and that they will use it to decide where to cut spend. B: ask for one page, the three biggest drivers first, each with a plain-language line on what the manager can do. C: add "be very careful and accurate". D: ask Claude to rate its confidence at the end. E: switch on research mode. [pause]

ALEX: A and B.

SAM: Both. A fixes the level, B fixes the length and shape. C is a polite instruction that names no gap. D trusts self-reported confidence, which is not an accuracy signal. E answers a question nobody asked: the data is in the file, not on the web. [sting]

## Breaking a task into stages

ALEX: Second objective. Task decomposition.

SAM: When one prompt asks for too much, parts get dropped or done thinly. The fix is a chain: each prompt does one stage well, and its output feeds the next. You trade a little speed for accuracy, and you get to check each stage before building on it.

ALEX: Give me a workplace version.

SAM: A consultant turning thirty interview notes into a client deck. Stage one, extract the facts and quotes. Stage two, group them into themes. Stage three, draft the storyline. Stage four, write the slides. If the themes are wrong, she fixes stage two, and nothing downstream inherits the mistake.

ALEX: And a lighter version inside a single prompt?

SAM: Numbered steps, when order or completeness matters. And a common chain is self-correction: draft, then have Claude review the draft against your criteria, then revise.

ALEX: I'd push back here. The newer models plan multistep work on their own. Splitting it up feels like overhead from a couple of years ago.

SAM: Partly true. Anthropic's guidance says Claude now handles most multistep reasoning internally.

ALEX: Then where does chaining still win?

SAM: Where you need to inspect the intermediate output, or the task has genuinely separate stages. That same guidance keeps chaining for exactly those cases. The tell: "parts were missed", "must check before", or a request with distinct stages. Then break it up. A short, single-purpose request stays one prompt.

SAM: Pause here and answer before we go on. For each request, choose one prompt or a chain of stages. One: rewrite a two-paragraph email to a supplier in a warmer tone. Two: turn forty customer interview transcripts into themes and then a prioritised recommendations memo, where the product director wants to approve the themes first. Three: translate a short internal notice into Spanish. Four: build a tender response that needs the requirements extracted, matched against your capabilities, gaps flagged, and the answer drafted. [pause]

ALEX: One prompt, chain, one prompt, chain.

SAM: All four. The tells for a chain are the approval in the middle of two, and the four distinct stages in four. And if that tender process had to run automatically every week, pulling from internal systems, that is the point to bring in a Developer or Architect. The exam expects you to recognise that boundary. [sting]

## Iterating a prompt

ALEX: Third objective. Iterating.

SAM: The first prompt rarely works perfectly. So the loop is: decide what good looks like before you start, compare the output against it, name the specific gap, change one thing, and run it again.

ALEX: Why only one thing?

SAM: Because if you change five things and it improves, you don't know which one did it, and when it breaks next month you can't tell which to undo. Anthropic's advice is to test each addition and keep it only if it helps.

ALEX: And feedback inside the chat?

SAM: Specific beats general. "Make it better" gives Claude nothing. "Section two is too technical for a board; explain the risk in terms of cost and timing" gives it a target. And if you want a change made, ask for the change. Ask "how could this be improved" and you get suggestions instead of a revised draft.

ALEX: Honestly, when it's wrong, I just hit regenerate until a good one comes up. It usually does in two or three goes.

SAM: Regenerating is useful. Comparing a few runs can even expose inconsistencies worth checking.

ALEX: But?

SAM: It doesn't change the instruction. If the gap is in the prompt, the next run, next week, has the same gap, and you've spent the time again. The fix belongs in the prompt, and if you reuse that prompt in a Project, in its instructions, which is domain five. The tell: "every week", "keeps leaving out", "each time". A repeating gap needs a changed prompt, not another roll.

SAM: Pause here and answer before we go on. A sales lead uses the same prompt every Monday to draft account summaries from her pipeline notes. The summaries keep leaving out contract renewal dates. Last week she added "please be thorough", with no change. What is the best next step? A: regenerate each summary until one includes the renewal date. B: add renewal date as a required field in the output format, include one finished example summary, and test the revised prompt on last week's accounts. C: move to the most capable model, since a stronger model will be more thorough. D: stop using Claude for summaries and write them by hand. [pause]

ALEX: I'll argue C. "Thorough" is a capability. A stronger model reads more carefully and catches the dates.

SAM: That's the bigger-model distractor. Nothing in the stem says the task is hard. It says the instruction never asked for the field. Anthropic's own guidance notes that not every failure is a prompting problem, and model choice does fix things like cost and speed. A missing field is not one of them.

ALEX: Then it's B.

SAM: B. It names the gap as a required field, shows one finished summary, and tests the change on real cases before trusting it. A repeats the gamble every week. "Please be thorough" already proved that polite adjectives don't work. D abandons a task that a small change fixes. [sting]

## Matching the approach to the task

ALEX: Last objective. Adapting to the task type.

SAM: Four types, four different prompts. Analysis first. Give Claude the data, the question and the decision it supports. Put long material first and your question after it, which Anthropic says improves results with long, complex inputs. For long documents, ask it to quote the relevant passages before it analyses, so the answer stays tied to the text.

ALEX: Research?

SAM: Say what a successful answer looks like, and ask it to check claims across several sources. Then pick the right feature. The help centre describes web search for straightforward factual questions that take one or two lookups, and research mode for comprehensive information gathering, five or more lookups over one to three minutes, ending in a cited report. Extended thinking is for complex reasoning that doesn't need recent information from the web.

ALEX: I'd use research mode for everything. More sources, more thorough. Why would I ever choose less?

SAM: For a big comparison, you should. Research mode earns its minutes when you're comparing competitors across many sources.

ALEX: And when doesn't it?

SAM: When the answer is one current fact. It isn't a quality ladder. The heavier mode only adds wait. The tell: "a single figure", "quickly confirm" points to web search; "compare", "across sources", "a report with citations" points to research. And either way, you check the citations before they leave your desk, which is domain two.

ALEX: Drafting.

SAM: The full brief: audience, purpose, tone, length, an example in house style, and the facts it must use. For anything factual, tell it to use only the material you supplied.

ALEX: So every prompt gets the full template. Audience, format, length, examples, constraints. I'll just use it everywhere.

SAM: Not for brainstorming. That rule just outran its task. Brainstorming wants range. Heavy constraints up front narrow the ideas before you've seen them. Ask for many distinct options across different angles, then narrow them in a second step against your criteria.

ALEX: So constraints come later.

SAM: Yes. The tell: "ideas", "options", "early stage". Go wide first, narrow second. And treat ideas as ideas, not as facts someone checked.

SAM: Pause here and answer before we go on. A communications lead wants ideas for an internal campaign to raise uptake of a new expenses tool. Which approach fits the task best? A: ask for the single best campaign with a full rollout plan. B: ask for twenty distinct ideas across different channels and tones, then in a second prompt shortlist three against the budget and the audience. C: run research mode on other companies' campaigns and adopt the top result. D: write a detailed template covering tone, length and channel, and ask for one idea that fits it. [pause]

ALEX: B.

SAM: B. Go wide, then converge against criteria. A and D collapse to one idea before any range exists. C copies someone else's answer instead of generating options for this audience. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you chose D: attach six months of documents.

ALEX: And now I'd argue it differently. Context was the problem, so more context has to help. Is the exam just penalising thoroughness?

SAM: Context was the problem. Volume is not the cure. Six months of documents buries this month's status notes in old decisions, and some of it may be material that policy says shouldn't be shared at all, which is domain six. And Claude still doesn't know who is reading or what they must decide.

ALEX: So B.

SAM: B. It names the reader, the time they have, the decision, the three things to cover, the length, and the right source material. A adds adjectives, not information. C pays for a bigger model to guess at the same missing facts.

ALEX: And the tell?

SAM: "Generic" and "leads with activity rather than decisions". That is missing audience and purpose. When an option says "every document" or "everything", it is offering volume in place of specificity. [sting]

## Five to remember

SAM: Five to remember. One: write for a brilliant newcomer. Task, audience, purpose, the reason behind each constraint, the shape of the answer, and the material in labelled sections.

ALEX: Two: say what to do rather than what not to do, start with one example and add more only if it drifts, and give permission to say the data is insufficient.

SAM: Three: chain a task when it has distinct stages or you must check an intermediate result. One prompt for a short, single-purpose request. Automation across systems goes to a Developer or Architect.

ALEX: Four: iterate by naming the gap and changing one thing, then testing on real cases. Regenerating and polite adjectives don't change the instruction.

SAM: Five: match the approach to the task. Analysis, long material first and quotes before conclusions. Research, the lightest feature that fits, citations checked. Drafting, the full brief. Brainstorming, wide first, narrow second.

## Recap: the exam tells

SAM: Your turn. Pause and name the four objectives we covered, and the habit that goes with each. [pause]

ALEX: Effective prompts, with audience, purpose and format. Decomposition, a chain when there are stages to check. Iteration, one change at a time. And task type, a different approach for analysis, research, drafting and brainstorming.

SAM: Now as exam tells. If the output is generic or pitched at the wrong reader, think missing audience, purpose and format, not adjectives.

ALEX: If an option offers every document or all the history, think volume dressed up as context.

SAM: If parts were dropped, or someone must approve a stage, think chain. If the work must run automatically across systems, think escalate.

ALEX: If the same gap comes back every week, think change the prompt and test it, not regenerate and not a bigger model.

SAM: If it's one current fact, think web search. If it's a comparison across sources with citations, think research mode.

ALEX: And if the stem says ideas or options, think wide first, narrow second.

SAM: Next, episode two: checking what Claude gives you, the biggest domain on the paper.
