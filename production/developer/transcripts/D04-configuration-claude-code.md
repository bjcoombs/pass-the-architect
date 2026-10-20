---
episode: "D04"
series: "CCDV-F"
slug: configuration-claude-code
title: "Configuration and Claude Code"
description: "Where Claude Code configuration lives and who it reaches: the CLAUDE dot md hierarchy, rules, settings precedence, model pinning, prompt versioning, plugins, skills, subagents and their memory, sessions, headless runs and auto mode."
domain: "Applications and Integration; Claude Code"
weight: "4.1% and 3.1%"
target_minutes: 16
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode four: configuration and Claude Code.

ALEX: What do I leave able to do?

SAM: Place an instruction at the right level of the CLAUDE dot md hierarchy, and know when it loads. Read the settings precedence and pin a model so upgrades happen when you choose. Pick between a skill, a command and a subagent, and give a subagent memory that lasts. And run Claude Code unattended: headless, streaming, and in the right permission mode.

ALEX: Seven percent of the paper between the two skills, so about four items. Small, and every one is a lookup.

SAM: Then let's start with one. [sting]

## Cold open: the overnight change

SAM: Here is your opening item. A platform team runs Claude Code in a nightly job. The project settings set the model to the sonnet alias. One morning the job's summaries arrive in a different structure, although nobody changed code, prompts or settings. The team wants model upgrades to happen only when they choose. What should they do? Option A: add a line to CLAUDE dot md telling Claude to keep the old structure. Option B: set the model to a full model name in the project settings, and move to a newer model only after their evals pass on it. Option C: switch the alias to opus so the job always runs the most capable model. Option D: run each night's job with continue, so the session sees the previous night's output.

ALEX: A. One line, no config change, and the alias keeps giving us free upgrades.

SAM: Hold that. We come back to it at the end.

ALEX: Two skills today, then.

SAM: Configuration management: CLAUDE dot md, settings, model pinning, prompt versioning and plugin dependencies. And Claude Code operation: rules, skills, commands, agents and their memory, sessions, headless and streaming modes, and auto mode. Under all of it sit two questions. Who does this reach, and when does it load? [sting]

## The CLAUDE.md hierarchy and rules

SAM: Four levels of CLAUDE dot md. Managed policy, which I T deploys and reaches everyone in the organisation. User, in the dot claude folder in your home directory, which is you in every project. Project, at the repository root or inside its dot claude folder, committed and shared. And local: CLAUDE dot local dot md at the project root, gitignored, for you in this project only.

ALEX: And they override each other?

SAM: No. They are concatenated. Files from where you launched and the directories above load at start-up; a subdirectory's CLAUDE dot md loads when Claude first works on a file there. If two instructions contradict, Claude may pick either, so remove the conflict.

ALEX: Imports?

SAM: An at sign and a path pulls another file in, up to four hops deep. But imported files load at launch with the file that imports them. Imports organise; they do not save context. What saves context is a rules file in dot claude slash rules with a paths field in its frontmatter: a glob such as star star slash star dot T F, and the rule loads only when Claude works with matching files.

ALEX: And repository initialisation is slash init.

SAM: Slash init reads the codebase and writes a starting CLAUDE dot md with the build commands, test commands and conventions it finds; if one exists, it suggests improvements instead. Slash memory lists your memory files and opens them for editing.

ALEX: Here's my habit, though. Anything I care about goes in CLAUDE dot md. Never run migrations without asking. One file, everyone reads it, and it works.

SAM: It mostly works, and for conventions it is the right home.

SAM: But the documentation is plain: CLAUDE dot md is context, not enforced configuration. Claude reads it and usually follows it. When an action must be blocked every time, that belongs in a deny rule in settings or a pre-tool-use hook, which the security episode covers.

ALEX: The tell?

SAM: "Must never", "every time", "guarantee". Those words want a control in settings or a hook. "Prefer", "convention", "style" want CLAUDE dot md.

SAM: Pause here and answer before we go on. A developer wants Claude to use their own sandbox U R L and test account when working in one repository. Teammates must not get these instructions, and the developer does not want them in other projects. Where should they go? A, the project's CLAUDE dot md. B, the CLAUDE dot md in the dot claude folder of their home directory. C, a CLAUDE dot local dot md at the project root, kept out of git. D, a rules file in dot claude slash rules with a paths field. [pause]

ALEX: C. A reaches every teammate. B reaches every project of mine. D is still committed, and it scopes by file, not by person.

SAM: C. Personal, one project, never committed. [sting]

## Settings, pinning and plugins

SAM: Settings dot json has the same shape of question with a strict order. Highest first: managed settings from your organisation, then command-line flags for this session, then dot claude slash settings dot local dot json, which is you in this project, then dot claude slash settings dot json, shared and committed, then your user settings in your home directory. A key set higher wins.

SAM: Permission rules come in three kinds, allow, ask and deny, and the lists merge across scopes. Deny rules block in every permission mode, including bypass permissions.

SAM: Now pinning. In Claude Code the short aliases, opus, sonnet and haiku, resolve to the recommended version and change over time. To pin, use a full model name, or set an environment variable such as ANTHROPIC underscore DEFAULT underscore OPUS underscore MODEL so the alias resolves where you say. An organisation can also restrict which models people may pick. On the A P I, the model I D you send is itself a pinned snapshot.

ALEX: Pinning sounds like a way to rot on an old model while everyone else gets the improvements.

SAM: Unpinned, you do get every improvement the day it ships, and for a developer's own terminal that is often fine.

SAM: But a production job needs to know which model produced which output, and a release can change behaviour. Pinning does not mean never upgrading. It means upgrading on purpose: point a branch at the new model, run the evals, then move the pin.

ALEX: Tell?

SAM: "Only when we choose", "reproducible", "audit which model produced this". Pin, then upgrade behind an eval.

ALEX: And prompt versioning?

SAM: Treat the system prompt as code. Keep it in version control beside the model I D it was tested on, and let an eval run gate each change. Then you can say which prompt and which model produced an output, and roll both back.

ALEX: Plugins?

SAM: A plugin bundles skills, agents, hooks and M C P servers under one namespaced name. Its manifest can set a version, which keeps users on it until you change it, and a dependencies list naming the plugins that must be enabled for this one to work.

SAM: Pause here and answer before we go on. For each statement, say true or false. One: an at-sign import in CLAUDE dot md lowers context cost, because the imported file loads only when needed. Two: a rules file with a paths field loads only when Claude works with a matching file. Three: a deny rule in settings still blocks the action in bypass permissions mode. Four: settings in your home directory override the project's committed settings dot json. [pause]

ALEX: False, true, true, false. Imports load at launch, and user settings sit below the project file.

SAM: All four. [sting]

## Skills, commands and agents

SAM: Custom slash commands have been merged into skills. A file in dot claude slash commands and a skill in dot claude slash skills, in its own folder with a SKILL dot md, both create the same slash command, and old command files keep working. Skills add a folder for supporting files and frontmatter that controls invocation.

ALEX: Which matters how?

SAM: A skill's description sits in context so Claude can load it when relevant. Set disable model invocation to true and only a person can start it, with slash and its name: the documented choice for side-effect workflows such as deploy or commit.

ALEX: I like Claude spotting when to deploy, though. It saves me typing the command.

SAM: For a read-only lookup, automatic loading is exactly what you want.

SAM: But a deploy changes the world. If the stem says the workflow must run only when a developer asks, the answer is the frontmatter that removes Claude's ability to start it, not a sentence in the body saying "only when asked".

ALEX: Tell?

SAM: "Side effect", "only when the developer runs it", "must not trigger on its own". Disable model invocation.

SAM: Subagents live in dot claude slash agents, in the project or your home directory. Each starts with a fresh context window, its own system prompt and tool list, and only its final result comes back, so forty files of search output stay out of your session.

ALEX: Agent memory?

SAM: Two kinds. Auto memory is the main session's notes, kept per repository in your home directory, machine-local, with the first two hundred lines of its MEMORY dot md index loaded each session. A subagent can have its own through the memory field: user scope in your home directory, project scope in the repo's dot claude folder, which can be version-controlled, or local scope, kept out of git. Project is the recommended default.

SAM: Pause here and answer before we go on. A team's review subagent should build up knowledge of this repository's recurring defects across sessions, and teammates should benefit through version control. What should they configure? A, the subagent's memory field set to project. B, the memory field set to user. C, a CLAUDE dot md line telling the subagent to remember what it finds. D, rely on the main session's auto memory. [pause]

ALEX: A. B is mine alone, D is machine-local, C is a request with nowhere to write.

SAM: A. [sting]

## Sessions, headless and auto mode

SAM: Sessions. Slash clear starts an empty conversation. Slash compact summarises the current one to free space. Resume with a session I D reopens a specific session; continue picks up the most recent. Slash rewind returns the conversation or the code to an earlier point.

SAM: Headless mode is the dash p flag: Claude Code runs non-interactively and exits with a status your script can branch on. Output format text is the default. Output format json returns the result with the session I D and metadata. Output format stream-json emits newline-delimited events as they happen, and with the verbose and include partial messages flags you get tokens as they are generated.

ALEX: For C I I'd just start an interactive session in a terminal multiplexer and read the screen.

SAM: For a demo, fine. But nobody answers the prompts at three in the morning, and nothing parses a screen reliably. The exam's answer to "unattended", "pipeline" or "script" is dash p, with an output format the script can read.

SAM: Pause here and answer before we go on. Choose two. A nightly pipeline must run Claude Code with no one watching, and a script must read the final result and the session I D so a later step can resume it. Which two? A, run with the dash p flag. B, set output format to json. C, start an interactive session and copy the result into a file. D, add a CLAUDE dot md line asking Claude to print its answer as json. E, run slash compact before the job exits. [pause]

ALEX: A and B. D is a polite request for a format the flag already gives you.

SAM: A and B. C needs a person, E frees context but returns nothing to the script.

SAM: Last, permission modes. Default asks before most actions. Accept edits writes files and common filesystem commands without asking. Plan researches and proposes without changing anything. Don't ask denies anything that would prompt, for locked-down C I. Bypass permissions skips prompts and safety checks, and belongs only in isolated containers or virtual machines. And auto mode: a separate classifier model reviews actions before they run and blocks what escalates beyond your request, such as a force push or a production deploy.

SAM: Pause here and answer before we go on. A developer on their own laptop is running a long refactor and is tired of approving every shell command. They want Claude to keep working while something still blocks risky actions like force pushes and production deploys. Which permission mode fits? A, bypass permissions. B, accept edits. C, auto mode. D, don't ask. [pause]

ALEX: Bypass. I trust the direction, and I'll review the diff at the end anyway.

SAM: That is a classic distractor: the most permissive option dressed as productivity. Bypass removes the safety checks, and the documentation keeps it for isolated containers. B still prompts for most shell commands. D denies them. C keeps Claude moving and puts a classifier in front of the risky actions. It does not guarantee safety, so review still matters.

ALEX: Tell?

SAM: "Fewer prompts" plus "still block risky actions" is auto mode. "Isolated container" is bypass. "Locked-down C I" is don't ask. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you chose A, the CLAUDE dot md line.

ALEX: Guidance aimed at a version problem.

SAM: The answer is B. The alias moved to a newer model, as aliases do. A full model name in project settings stops the drift, and the evals decide when to move. A is a request that may hold for a while and gives no control over the next release. C keeps the job on a moving alias and adds cost. D carries old output forward and fixes nothing.

ALEX: The words?

SAM: "Only when they choose" and "nobody changed anything". Behaviour changed with no change of yours: look for a moving alias, and pin. [sting]

## Five to remember

SAM: Five to remember. One: CLAUDE dot md levels are managed, user, project and local, concatenated, not overriding. Local is CLAUDE dot local dot md: you, this project, never committed.

ALEX: Two: imports organise but load at launch. A rules file with a paths glob loads only for matching files. Slash init writes the starter file, slash memory opens the files.

SAM: Three: settings order is managed, command line, local, project, user. Deny blocks in every mode. CLAUDE dot md is context; "must never" belongs in settings or a hook.

ALEX: Four: aliases move. Pin a full model name, version prompts beside the model they were tested on, gate both with evals. Plugins carry a version and a dependencies list.

SAM: Five: side-effect skills get disable model invocation. Subagents isolate context; the memory field set to project shares learning through git. Unattended means dash p with json or stream-json, and fewer prompts with safety checks means auto mode.

## Recap: the exam tells

SAM: Recall first. Pause and name the four segments, and the two questions under all of them. [pause]

ALEX: The CLAUDE dot md hierarchy and rules, settings and pinning, skills and agents, sessions and modes. Who does it reach, and when does it load.

SAM: As exam tells. If the stem says "must never" or "every time", think a deny rule or a hook, not CLAUDE dot md.

ALEX: If it is personal and for one project, think CLAUDE dot local dot md. If it is one file type spread across the tree, a rules file with a paths glob.

SAM: If behaviour changed and nobody changed anything, think a moving alias, and pin a full model name. If two settings disagree, the higher level wins and deny always holds.

ALEX: If a skill has side effects, disable model invocation. If an agent should learn across sessions and share it, the memory field set to project.

SAM: If the job is unattended, dash p with json for a result or stream-json for live events. If the developer wants fewer prompts but risky actions blocked, auto mode; bypass only in an isolated container.

ALEX: Next, episode five: L L M fundamentals and choosing a model.
