---
episode: "D03"
series: "CCDV-F"
slug: application-design
title: "Designing Claude applications"
description: "How Claude reads the same instruction in the A P I, the Agent S D K, Claude Code, claude.ai and Desktop; keeping instructions apart from data; schemas that always parse and never force invented values; clean sessions and plugin scopes; and turning business requirements into functional and infrastructure requirements across the systems life cycle."
domain: "Applications and Integration"
weight: "14.8%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode three: designing Claude applications.

ALEX: What will I be able to do by the end?

SAM: Predict how Claude reads the same instruction across the A P I, the Agent S D K, Claude Code, claude dot ai and Desktop. Keep instructions and data apart, and design a schema that always parses and never forces an invented value. Keep a session clean and put a plugin at the right scope. And turn a business requirement into functional and infrastructure requirements, then place a problem in the life cycle.

ALEX: Application design is eight point six percent, the biggest single skill on the paper. With requirements and the life cycle, about eight items.

SAM: So we open with one. [sting]

## Cold open: it worked in the chat

SAM: A developer prototypes a support-reply assistant inside a claude dot ai project, with project instructions on tone and format and the team's style guide uploaded as knowledge. The replies are excellent. The production version is built on the Messages A P I, sending each customer's ticket as the user message. Replies are now generic, wrong on format and off on tone. What is the most likely cause, and the best fix? Option A, the A P I runs with a lower temperature, so raise it until the replies sound less mechanical. Option B, the A P I call carries none of the project's instructions or knowledge, so move them into the system prompt and test through the A P I. Option C, claude dot ai runs a stronger model than the A P I, so switch production to the largest model tier. Option D, add the line "use our house style" to the start of every user message.

ALEX: C. Same prompt, worse output. Something different is answering.

SAM: Hold that. We come back to it at the end.

ALEX: What does the guide list for today?

SAM: Three skills. Application design: how Claude interprets instructions on each surface, content boundaries, schema design, session hygiene and plugin management. Understanding requirements, functional and infrastructure. And the systems life cycle.

SAM: Segment one: one model, five surfaces. The question under it: what else is in the context besides the words you wrote? Start with the bare A P I. When you call the Messages A P I, Claude sees your system prompt, the messages you send and your tool definitions. Nothing else. Anthropic adds no system prompt of its own, and the A P I keeps no memory between calls, so your application sends the history every time.

ALEX: And claude dot ai is different.

SAM: Claude dot ai and the mobile apps start every conversation with a system prompt Anthropic maintains, carrying the current date and formatting habits. Anthropic's release notes say it does not apply to the A P I. On top sit your account-wide instructions, and project instructions that apply only inside that project. Desktop adds local M C P servers on your machine.

SAM: Claude Code has its own system prompt, with tool guidance and safety instructions. Your CLAUDE dot md files are then injected into the conversation as project context. The documentation is explicit: Claude treats them as context, not enforced configuration.

ALEX: Let me push on that. CLAUDE dot md loads every session and Claude follows it. If I write "never edit the migrations folder" there, that is my rule. Why would I need more?

SAM: Most of the time it will be followed, and a short, specific CLAUDE dot md is the right home for conventions.

SAM: But "most of the time" is the problem. Context shapes behaviour; it blocks nothing. To block an action regardless of what Claude decides, the docs point to a PreToolUse hook, or a deny rule in permissions. A polite instruction is not a control.

ALEX: And the tell?

SAM: "Must never", "every time", "regardless". Those words move the answer out of CLAUDE dot md and into a hook or a permission rule.

SAM: Last, the Agent S D K. Leave its system prompt option unset and you get a minimal default that covers tool calling and leaves out the rest of Claude Code's prompt, including its security and safety instructions. Set the claude code preset and you get the prompt the Claude Code C L I uses. Or pass your own string, and the S D K sends only what you wrote.

ALEX: And the preset takes extra instructions?

SAM: Through append. Your rules go on the end and nothing is removed; the docs call that the lowest-risk customisation. One contrast worth a mark: claude dash p, the non-interactive C L I, uses the Claude Code system prompt by default. The S D K's default does not.

ALEX: I would still write my own prompt. Full control, no surprises from someone else's text.

SAM: For a support bot or a research agent, that is the docs' own advice: a different surface, identity or permission model wants its own prompt.

SAM: But with a custom string you must replace the tool guidance and safety instructions yourself. For a coding agent that should behave like Claude Code, preset with append keeps all of it. The tell: "behave like the C L I" or "keep the built-in behaviour" means preset plus append. "Its own persona" or "not a coding task" means your own prompt.

SAM: One habit holds on every surface. Current Claude models follow instructions precisely. If you want more than the literal ask, say so, and say why: the reason helps Claude aim.

SAM: Pause here and answer before we go on. A platform team ran its issue-triage job in continuous integration with claude dash p, and it behaved well. They rewrote it on the Agent S D K with no system prompt option set, and now it ignores tool guidance it used to follow and is looser with risky commands. What is the best fix? A, set the claude code preset and append the team's triage rules. B, copy the triage rules into the repository's CLAUDE dot md. C, move the job to the largest model tier. D, pass a custom system prompt string containing only the triage rules. [pause]

ALEX: A.

SAM: A. The rewrite fell from the Claude Code prompt to the minimal default, which drops the preset's tool and safety guidance. The preset restores it; append adds the team's rules. B adds project context but none of the missing guidance. C is a bigger model for a missing prompt. D is a custom string that still lacks everything the preset carried. [sting]

## Content boundaries and schemas

SAM: Segment two: content boundaries and schemas. A prompt usually mixes instructions, context, examples and the input being worked on. Anthropic's guidance is to wrap each kind in its own X M L tag so Claude does not confuse them. Several documents go inside a documents tag, each with its source and content.

ALEX: Any order?

SAM: Long documents near the top, above the question and instructions; the docs say that improves performance across all models.

SAM: The second boundary is trust. Anything your application did not write, a customer email, a retrieved web page, a tool result, is data. It goes in the user turn or the tool result, labelled as material to work on, never into the system prompt as if you had written it.

ALEX: So I tag every untrusted email and I am protected against injection.

SAM: That rule just went past its scope. Tags make the structure clear, and that helps. They do not stop a page that says "ignore your instructions" from being read. The defence is making sure injected text cannot reach sensitive tools: least privilege and hooks, episode nine. Tags organise; controls enforce.

SAM: Now schemas. Structured outputs covers two features. JSON outputs, set through the output format option, control the shape of Claude's answer. Strict tool use, strict set to true on a tool, guarantees the tool's name and inputs match its schema. Both use constrained decoding, so the response parses and the required fields arrive with the right types.

ALEX: Here is my pushback. I ask for JSON in the prompt, parse it, and retry on failure. It works ninety-nine times in a hundred and needs no extra feature.

SAM: Ninety-nine is real, and prompt-requested JSON is fine for a prototype.

SAM: But at thousands of records a day, one in a hundred is dozens of failures, and every retry pays twice. The guarantee removes the failure instead of catching it. Tell: "parse failures", "malformed", "must always be valid". Pick structured outputs over a stricter instruction or a retry loop.

ALEX: Guaranteed valid means guaranteed right?

SAM: No. The schema guarantees structure, not truth. And two stop reasons can still break the shape: a refusal, which takes precedence over the schema, and hitting max tokens, which can cut the output short. Check the stop reason before you parse.

ALEX: What makes a good schema, then?

SAM: Closed categories as enums, with an "other" value and a detail field for what does not fit. A description on every field. And the one that matters most: if the source might not contain a value, do not make the field required with no way out. Allow null. A required policy number on a note that has none is a request to invent one.

SAM: Know the limits too. Structured outputs reject some JSON Schema features, among them numeric minimum and maximum, string lengths and recursive schemas. Range checks belong in your code after parsing.

SAM: Pause here and answer before we go on. Choose two. An insurer's claims app extracts fields from adjusters' notes into JSON for its claims system. About one response in two hundred fails to parse, and some records carry a policy number when the note contains none. Which two changes fix the causes? A, use structured outputs with a JSON schema for the response. B, let the policy number field be null when the note does not state one. C, add "return only valid JSON" to the system prompt in capitals. D, retry every failed parse up to five times. E, add a minimum and maximum to the policy number field so invented values are rejected. [pause]

ALEX: A and B.

SAM: Both. A removes parse failures by construction. B gives absent information an honest place to go. C is a louder instruction for a problem the decoder can solve. D pays to catch the failure instead of removing it. E is a constraint structured outputs does not support, and a range would not catch a plausible invented number anyway.

SAM: Pause here and answer before we go on. For each statement, say true or false. One: wrapping a retrieved web page in X M L tags makes it safe to follow any instructions inside it. Two: long documents belong near the top of the prompt, above the question. Three: structured outputs guarantee that every extracted value is factually correct. Four: when the stop reason is a refusal or max tokens, the output may not match the schema. [pause]

ALEX: False, true, false, true.

SAM: All four. Tags clarify structure; they are not a trust boundary. Documents go up top. The schema guarantees shape, not truth. And you check the stop reason before you parse. [sting]

## Sessions and plugins

SAM: Segment three: session hygiene and plugins. Claude Code's documentation builds most of its advice on one constraint: the context window fills fast, and performance degrades as it fills.

ALEX: So the habits are?

SAM: Slash clear between unrelated tasks; the docs call the failure the kitchen sink session. Slash compact, with instructions on what to keep, when one long task needs room. Subagents for investigation, so a sweep through fifty files happens in its own context and only the summary comes back. Slash rewind to return to a checkpoint. And the continue or resume flags to pick up tomorrow without re-explaining.

ALEX: Checkpoints replace commits, then.

SAM: No. Checkpoints track only changes made through Claude's file editing tools. Anything a shell command changed is not captured. They are an undo, not version control.

ALEX: Then I will clear after every prompt. Clean context, always.

SAM: That over-applies it. The docs say sometimes you should let context build, because you are deep in one hard problem and the history is valuable. The trigger is unrelated work, or a context full of failed attempts. The tell: "unrelated", "switched tasks", "keeps reintroducing".

SAM: In your own A P I application, the same hygiene is your code's job, because the A P I is stateless. Keep each user's history separate, trim or summarise old turns, and never let one customer's history ride along in another's request.

SAM: Now plugins. A plugin bundles skills, agents, hooks and M C P servers into one installable unit, from a marketplace: a catalogue you add once, then install from.

ALEX: And scope?

SAM: Three. User scope: you, in every project on your machine, recorded in your home directory's settings. Project scope: everyone in this repository, recorded in the repository's dot claude slash settings dot json, which you commit. Local scope: you, in this repository only, recorded in settings dot local dot json. Local beats project, and project beats user. Plugins your organisation installs through managed settings you cannot switch off.

ALEX: Say the repo enables a review plugin at project scope and I find it noisy. I would delete the entry from the shared settings file. It is my repo too.

SAM: On a solo repo, that is fine.

SAM: On a team, it removes the plugin for everyone, through a commit nobody asked for. You want it off for you, in this repository: local scope, set to false in your settings dot local dot json, which overrides the project setting. The tell: "only for me, in this repo" is local; "everyone on this repository" is project; "me, everywhere" is user.

SAM: Before installing from a marketplace you do not know, read what the plugin adds: it can run hooks and M C P servers on your machine. And disable plugins you no longer use, which still cost context.

SAM: Pause here and answer before we go on. A developer has spent an afternoon in one Claude Code session: a database migration, then a question about a C S S bug, then back to the migration. Claude has been corrected three times on the same migration error and keeps bringing it back. What is the best next step? A, run slash clear and start again with a more specific prompt that includes what the corrections taught. B, add the correction to CLAUDE dot md in capitals. C, run slash compact so the session has room to keep going. D, switch the session to a larger model. [pause]

ALEX: C. Compaction keeps the lessons and frees space. Clearing throws away an afternoon.

SAM: That is the compensating fix that keeps the cause. Compaction summarises what is there, and what is there is three failed approaches and an unrelated C S S thread. The docs say that after two failed corrections, you clear and write a better prompt with what you learned. So, A. B is louder guidance for a context problem. D is scale for clutter.

ALEX: So the afternoon goes into the new prompt.

SAM: Exactly. [sting]

## Requirements and the life cycle

SAM: Segment four: requirements and the life cycle. Business requirements say why: cut reply time, meet a regulation. The solution architecture says where: the platforms, clouds and data stores the system must fit. From those two you derive requirements a developer can build and test.

ALEX: Functional and infrastructure.

SAM: Functional requirements say what the system does: inputs, outputs, behaviour, workflow. Classify each ticket into one of six queues. Infrastructure requirements say what it runs on and within: latency, throughput, availability, where data may live, security and access, cost ceilings, the platform. If the architecture says everything runs inside the company's A W S accounts, that is an infrastructure requirement, and it can decide how you reach Claude: through Amazon Bedrock rather than the direct A P I.

ALEX: That is the third-party vendor point from the A P I skill.

SAM: Reached from the requirements side. And each requirement should trace to the statement that produced it. One nobody can trace is an assumption someone liked.

SAM: Pause here and answer before we go on. Choose two. A hospital group's business requirement: discharge summaries drafted within two minutes of a clinician signing the final note. Its solution architecture: all patient data stays inside the group's A W S environment. Which two of these are infrastructure requirements? A, each summary lists medications, follow-up appointments and pending results. B, Claude is reached through Amazon Bedrock in the group's A W S environment. C, a clinician approves every summary before it reaches the record. D, the draft is ready within two minutes of signing, at peak volume. E, summaries are written in plain language for the patient. [pause]

ALEX: B and D.

SAM: Both. B comes from the architecture: where the data lives and how the model is reached. D is a latency target at a stated load. A and E describe content, so they are functional. C is a workflow rule, also functional, even though it sounds like a control.

SAM: Now the life cycle. The guide's words are develop, implement, operate and maintain. Most frameworks name the stages plan, design, build, test, deploy, operate, maintain, and in the end retire.

ALEX: Pushback. We are agile. Phases are waterfall vocabulary, and nobody on my team says "maintenance phase".

SAM: Fair. Waterfall runs the stages once, in order; agile and DevOps loop through them in short cycles.

SAM: But every framework still does the same activities; agile repeats them. The exam asks which activity a problem belongs to. Two Claude examples. Operate: monitoring output quality, cost and errors in production. Maintain: models are deprecated and later retired, so a model change is planned work. You rerun your evals against the successor before you switch, rather than changing the model I D and shipping.

ALEX: Tell?

SAM: "Deprecation notice", "successor model", "upgrade". That is maintenance, and the answer is an eval regression run before the swap. "Quality drifting in production" is operate: monitoring, not a redesign. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you picked C: claude dot ai must run a stronger model.

ALEX: And now I can see what the chat had that my A P I call did not. Anthropic's system prompt, the project instructions, the style guide.

SAM: Which makes the answer B. The tone rules and the style guide lived in the project, so the production call never saw them. Put them in the system prompt, and test through the A P I with the prompt you will ship. A changes randomness, not missing instructions. C blames the model for missing context. D is one line standing in for a whole style guide.

ALEX: And the words that should have stopped me?

SAM: "Inside a claude dot ai project", next to "built on the A P I". Two surfaces in one stem: ask what the first one added that the second one lacks. [sting]

## Five to remember

SAM: Five to remember. One: the A P I sees only your system prompt, messages and tools. Claude dot ai adds Anthropic's system prompt, account instructions and project instructions, and none of it reaches the A P I.

ALEX: Two: CLAUDE dot md is context, not enforcement; "must never" means a hook or a permission rule. In the Agent S D K the default prompt is minimal; the claude code preset with append keeps Claude Code's behaviour and adds yours.

SAM: Three: tag instructions and input apart, documents at the top, and anything you did not write is data. Structured outputs guarantee shape, not truth; allow null where the source may be silent.

ALEX: Four: slash clear between unrelated tasks and after two failed corrections; subagents for investigation. Plugins: user is me everywhere, project is the whole repo, local is me in this repo, and local wins.

SAM: Five: functional requirements say what the system does; infrastructure requirements say what it runs on and within. A model deprecation is maintenance: rerun the evals before you switch.

## Recap: the exam tells

SAM: Recall first. Pause and name the four segments, and the question that ran under the first half. [pause]

ALEX: One model across five surfaces, content boundaries and schemas, sessions and plugins, requirements and the life cycle. The question: what else is in the context besides what I wrote.

SAM: Now as exam tells. If a prompt worked in claude dot ai and fails through the A P I, look for what the chat added.

ALEX: If a stem says "must never" about Claude Code, think hook or permission rule, not CLAUDE dot md. If an S D K rewrite lost the C L I's behaviour, think claude code preset with append.

SAM: If responses fail to parse, think structured outputs. If values appear that the source never contained, look for a required field with no way to say null. Tags organise; controls stop injection.

ALEX: If a session mixes unrelated tasks or keeps repeating a corrected mistake, think slash clear and a better prompt. If one person wants a team plugin off, think local scope.

SAM: If an option names a platform, a latency target, a data location or a cost limit, it is an infrastructure requirement. If a stem mentions a deprecation notice, think maintenance, and an eval run before the swap.

ALEX: Next, episode four: configuration and Claude Code, from settings dot json to model version pinning.
