---
episode: "F04"
series: "CCAR-F retake"
slug: claude-code-config
title: "Claude Code configuration"
description: "Where each instruction lives in Claude Code and who receives it: the CLAUDE dot md hierarchy, imports and rules files, project and personal commands and skills, path-scoped rules, and M C P servers at project and user scope."
domain: "Claude Code Configuration & Workflows; Tool Design & MCP Integration"
weight: "20% and 18%"
target_minutes: 24
---

## In this episode

SAM: Welcome to Pass the Architect, Foundations retake. This is episode two: Claude Code configuration.

ALEX: And by the end?

SAM: You'll be able to find where an instruction lives when one teammate doesn't get it. You'll split a bloated CLAUDE dot md into imports and rules files. You'll choose between a project and a personal command or skill, and pick the frontmatter that isolates, restricts or prompts. You'll scope a rule to one file type with a paths glob. And you'll fix an M C P setup where the agent ignores a better tool or wastes calls exploring.

ALEX: This is where my score report hurt most: three zeros, across domains worth twenty and eighteen percent.

SAM: So we start with an item. [sting]

## Cold open: test conventions

SAM: Code Generation with Claude Code scenario. A team's monorepo has test files in every package, next to the code they test. The testing conventions sit in the root CLAUDE dot md, so they load in every session, including the ones that never touch a test. The team wants them to load only when Claude works on a test file. What should they do? Option A, add a CLAUDE dot md with the testing conventions to every directory that contains tests. Option B, move the conventions into a file in the dot claude slash rules folder, with a paths field in its frontmatter set to star star slash star dot test dot T S X. Option C, ask each developer to move the conventions into their own user-level CLAUDE dot md. Option D, turn the conventions into a skill that developers invoke before writing tests.

ALEX: A. Conventions next to the code they govern, owned by the people who work there. That is how I would set up a monorepo.

SAM: Hold that. We come back to it at the end.

ALEX: Why does this episode go first after the miss patterns?

SAM: Because this is where your score report hurt most. Settings and hooks versus CLAUDE dot md, zero. Post-edit hooks, zero. Project versus user scope, zero. M C P integration, fifty percent. Claude Code Configuration and Workflows is twenty percent of the exam, and Tool Design and M C P Integration another eighteen. Today covers task statements three point one, the CLAUDE dot md hierarchy and how to split it up; three point two, slash commands and skills; three point three, path-specific rules; and two point four, M C P servers in Claude Code.

ALEX: And episode ten already did the formatter hook and the token in the shared config.

SAM: So we will not redo those. Underneath every item today sit two questions: who receives this instruction, and when does it load?

SAM: Segment one. Symptom: a new developer joins a payments team, clones the repo, and Claude ignores the team's rule about naming API handlers. Everyone else gets it. Where is the rule?

ALEX: In someone's personal CLAUDE dot md. The one in the dot claude folder in their home directory.

SAM: Right. Three levels. User level is the CLAUDE dot md in the dot claude folder in your home directory. It applies to you, in every project, and it never travels through version control. Project level is a CLAUDE dot md at the repository root, or inside the repo's own dot claude folder; either one is committed and shared. Directory level is a CLAUDE dot md in a subdirectory, which carries that area's conventions and loads when Claude works on files there.

ALEX: My fix would be quicker. Send the new hire my file, or put a line in the onboarding doc telling them what to add. Done in five minutes.

SAM: It is quicker, and onboarding docs are useful. For one person on one day, it works.

SAM: But it fixes the person, not the configuration. The next hire hits the same gap, and copies drift apart the moment anyone edits theirs. The guide's skill here is diagnosing exactly this: instructions that sit at user level when they belong at project level. The fix is moving the rule into the project CLAUDE dot md, where version control delivers it to everyone.

ALEX: So what should catch my eye?

SAM: "New team member", "teammate", or "everyone else gets it". When the stem says one person is missing what the rest have, look for an instruction stored at user level, and pick the option that moves it to project level.

ALEX: Then I would move everything to project level. No more surprises.

SAM: That rule just outran its scope. Your preference for terse answers, or for explanations in British spelling, is yours. Commit it and every teammate inherits it. The test is who the instruction is for. The whole team on this repo: project. Only you, everywhere: user.

ALEX: How do I confirm which files actually loaded?

SAM: The slash memory command. It shows which memory files are loaded in the current session. When behaviour differs between two developers, or between Monday's session and Tuesday's, that is the first look.

SAM: Now modular organisation. Symptom: the root CLAUDE dot md has grown to six hundred lines. API conventions, testing, deployment, a database section nobody owns. People stop reading it and edits collide. Two tools. First, the at-sign import: a CLAUDE dot md can reference another file with an at sign followed by its path, and that file is pulled in. The guide's example is each package's CLAUDE dot md importing only the standards files that package needs, chosen by the people who maintain it.

ALEX: And the second?

SAM: The dot claude slash rules folder. Instead of one monolith, topic files: testing dot md, api conventions dot md, deployment dot md. Each one small, each with an obvious owner.

ALEX: Do imports save context, though?

SAM: Not by themselves. An imported file is expanded into context when the file importing it loads, so imports organise rather than economise. The saving comes from where the import sits, in a package file instead of the root, and from path scoping, which is segment three.

SAM: Pause here and answer before we go on. Code Generation with Claude Code scenario. Two developers on the same repository report that Claude follows the team's error-handling convention in one developer's sessions and not the other's. What should the architect do first? A, run the slash memory command in both developers' sessions and compare which memory files are loaded. B, rewrite the convention in capitals with an example. C, add a PreToolUse hook that blocks edits which break the convention. D, move both developers to a larger model. [pause]

ALEX: C. If the convention has to hold, enforce it. Episode ten taught me guidance is probabilistic.

SAM: That is a real principle, applied to the wrong question. Read the stem again.

ALEX: "First." [sighs] And the same repo behaves differently for two people.

SAM: Miss pattern three: "first step" read as "most effective". Same repo, different behaviour, points to configuration that differs between the two machines, probably a user-level file. So, A. You diagnose before you build. C may come later if the convention genuinely needs enforcing, but it skips the diagnosis and would hide a scoping fault. B is louder guidance aimed at a loading problem. D is scale instead of structure.

SAM: One link to your zero on settings versus CLAUDE dot md. Everything in this episode so far is guidance. When something must happen every time, it goes in settings: a permission rule or a hook. And those have the same scope question. A hook in the project's settings file, settings dot json inside the repo's dot claude folder, is committed and reaches every developer. The same hook in your personal settings reaches only you.

ALEX: So if the formatter hook works for me and not for the new hire...

SAM: Same diagnosis as the naming rule. It lives at user scope. Move it to project settings. [sting]

## Segment two: commands and skills

SAM: Segment two, commands and skills. Symptom: every developer on a team pastes the same ten-line review prompt from a wiki page, slightly edited, and reviews come back inconsistent.

ALEX: Make it a slash command.

SAM: In the right place. Project-scoped commands live in the repo's dot claude slash commands folder. They are committed, so the whole team gets the same slash review on clone. User-scoped commands live in the dot claude slash commands folder in your home directory, and they are personal.

ALEX: And skills?

SAM: Skills live in dot claude slash skills, each in its own folder with a SKILL dot md file. That file starts with frontmatter, and the guide names three options. Context colon fork runs the skill in an isolated sub-agent context, so its output does not pollute the main conversation. Allowed-tools restricts which tools the skill may use while it runs. Argument-hint prompts the developer for a required parameter when they invoke the skill without one.

ALEX: When would I fork?

SAM: The guide names two cases. Verbose output, such as a codebase analysis that reads forty files. And exploratory context, such as brainstorming three alternative designs you will mostly throw away. In both, you want the conclusion back in your session, not the working.

ALEX: Let me argue for no fork. When the analysis runs inline I can see every file it read. If it forks I get a summary and have to trust it.

SAM: Visibility is worth something, and a summary can drop a detail you wanted.

SAM: But the stem will tell you the cost: the session fills with file dumps, later answers lose the thread, the developer's actual task gets crowded out. That is pollution of the main conversation, which is exactly what context fork exists to stop. The guide picks isolation for verbose and exploratory work.

ALEX: The tell?

SAM: "Verbose", "floods the session", "brainstorming", or "keep the main conversation clean". Those point to context fork. And do not fork everything: a short skill whose output you work with directly gains nothing from isolation.

SAM: Now allowed-tools. Symptom: a skill that generates test scaffolding once ran a shell command that deleted a directory. The team's first draft fix is a line in the skill saying "never delete files".

ALEX: Which is guidance again.

SAM: Which is guidance again. Allowed-tools in the frontmatter restricts tool access while the skill runs, for example to file-writing tools only, so the destructive action is not available. The tell is "restrict" or "prevent destructive actions" attached to one skill.

SAM: Last piece, personal variants. Symptom: one developer prefers the team's review skill to also check spelling in comments. They edit the shared SKILL dot md.

ALEX: I have done that. It is a one-line change and it makes the skill better.

SAM: For you it does. And the instinct to improve shared tooling is a good one when it goes through review.

SAM: But a quiet edit to a committed skill changes behaviour for every teammate. The guide's answer is a personal variant in the dot claude slash skills folder in your home directory, under a different name, so the team's skill is untouched. The tell is "personal preference" next to "shared" or "team".

ALEX: And how do I choose between a skill and CLAUDE dot md?

SAM: Load timing. CLAUDE dot md is always loaded, so it holds universal standards: true for every task in this repo. A skill is invoked on demand for a task-specific workflow, so a thirty-line release checklist belongs in a skill. Putting it in CLAUDE dot md charges every session for a procedure most sessions never run.

SAM: Pause here and answer before we go on. Choose two. Code Generation with Claude Code scenario. A team's codebase-impact skill needs the name of the module being changed. Developers often invoke it with no arguments and get a vague result. When it does run, it reads dozens of files and the analysis buries the developer's session. Which two frontmatter changes address these problems? A, add context colon fork so the analysis runs in an isolated sub-agent context. B, add an argument-hint so developers are prompted for the module name. C, add allowed-tools listing the shell tool so the skill can search faster. D, move the skill's instructions into the root CLAUDE dot md so they are always available. E, add a line to the skill body asking Claude to keep its output short. [pause]

ALEX: A and B.

SAM: Both. A answers "buries the session" and B answers "invoked with no arguments". C widens tool access, which is the opposite of what allowed-tools is usually for, and it fixes neither symptom. D loads a task-specific workflow into every session. E is a request: it trims some output but the files still pass through the main conversation. [sting]

## Segment three: path-specific rules

SAM: Segment three, path-specific rules. Symptom: the team split its monolith into rules files, and context use did not drop. Terraform conventions load while someone edits a React component.

ALEX: Because a rules file with no scoping loads every session.

SAM: Exactly. A rules file in dot claude slash rules can start with YAML frontmatter containing a paths field: a list of glob patterns. The rule loads only when Claude is working with a file that matches. Terraform slash star star slash star loads the Terraform rule for anything under the Terraform folder. Star star slash star dot test dot T S X loads the test rule for test files anywhere in the codebase. Without a paths field, the rule behaves like CLAUDE dot md: loaded every time, costing tokens every time.

ALEX: Now the hard one. Why a glob rule rather than a CLAUDE dot md in each directory? Directory files give each team ownership and the conventions sit next to the code.

SAM: That is a strong case, and for one package owned by one team, a directory CLAUDE dot md is a fine answer.

SAM: It breaks when the files are spread out. Test files live in forty directories. Forty copies of the same conventions drift apart, and a new package arrives with no copy at all. One rule with star star slash star dot test dot T S X covers every test file, including ones that do not exist yet. The guide is explicit: choose path-specific rules over subdirectory CLAUDE dot md files when conventions must apply to files spread across the codebase.

ALEX: So the tell?

SAM: "Spread throughout", "regardless of directory", "all test files" or "every Terraform file". A file type scattered across the tree points to a glob in a rule. A convention that belongs to one folder points to that folder's CLAUDE dot md.

SAM: Pause here and answer before we go on. Code Generation with Claude Code scenario. A platform team writes Terraform in an infra folder, and several services also keep their own Terraform files in a deploy subfolder of each service. The team wants its Terraform conventions applied whenever Claude edits any Terraform file, and loaded at no other time. What is the best approach? A, a rules file in dot claude slash rules with a paths field matching star star slash star dot T F. B, a CLAUDE dot md in the infra folder containing the conventions. C, a section in the root CLAUDE dot md headed "when editing Terraform". D, a skill that developers run before editing Terraform. [pause]

ALEX: A.

SAM: A. One glob catches every Terraform file wherever it lives, and the rule loads only then. B misses every service's deploy folder. C loads in every session, which breaks "at no other time". D depends on a developer remembering, and conventions that must apply on every edit should not rely on someone invoking them. [sting]

## Segment four: MCP in Claude Code

SAM: Segment four, M C P in Claude Code. Developer Productivity with Claude scenario: an internal agent built on the Agent SDK with the built-in tools and several M C P servers. Quick recap of what episode ten covered. A shared server goes in the project's dot M C P dot json, committed. Credentials go in as environment-variable placeholders, dollar sign, brace, GITHUB underscore TOKEN, close brace, so each developer's own token is expanded at runtime and no secret is committed. A personal or experimental server goes in your user-level configuration, which the guide names as the dot claude dot json file in your home directory.

ALEX: So what is new today?

SAM: Discovery, descriptions, community servers and resources. Discovery first. Tools from every configured M C P server are discovered when the agent connects, and all of them are available at the same time, alongside the built-in tools. You do not point the agent at one server. It picks from everything it can see.

ALEX: Which is why descriptions matter.

SAM: Symptom: the team connected a code-search M C P server that understands symbols and call graphs. The agent still runs Grep for everything. Why?

ALEX: The M C P tool's description is too thin. "Searches code." Grep's is clearer, so it wins.

SAM: Right. The fix is to expand the M C P tool's description: what it can do that a text search cannot, such as finding every caller across wrapper modules, what it returns, and when to use it instead of Grep.

ALEX: Or one line in CLAUDE dot md: "prefer the code-search tool over Grep." That is faster than rewriting descriptions.

SAM: It would help, and it is cheap. Guidance has its place.

SAM: But the model chooses tools from their descriptions at the moment of choosing. A thin description is the root cause, and a CLAUDE dot md line is a patch over it that every other client of that server misses. The guide's skill is enhancing the description so the agent stops preferring the built-in tool.

ALEX: Tell?

SAM: "Prefers Grep", "ignores the more capable tool", or "keeps using the built-in tool". The fix lives in the description of the tool being ignored.

SAM: Next, build or reuse. Symptom: a team plans six weeks to write its own Jira M C P server.

ALEX: I would build it. Our own code, our own fields, no dependency on someone else's release schedule.

SAM: Control is a real benefit, and some teams do need custom behaviour.

SAM: But Jira is a standard integration, and a maintained community server already covers it. The guide reserves custom servers for team-specific workflows, such as your internal deployment approvals. Six weeks rebuilding a commodity is over-engineering.

ALEX: Tell?

SAM: A well-known product name, Jira, GitHub, a database. "Standard integration" points to an existing community server. "Our internal process" points to a custom one.

SAM: Last, resources. Symptom: before answering any question about the data warehouse, the agent spends a dozen calls listing tables and describing columns. The guide's answer is M C P resources: the server exposes a content catalogue, such as database schemas, issue summaries or a documentation hierarchy, so the agent can see what exists without exploratory tool calls.

SAM: Pause here and answer before we go on. Choose two. Developer Productivity with Claude scenario. A team's agent has a code-search M C P server and a database M C P server. Two complaints: it uses Grep instead of the code-search tool for tracing function callers, and it makes fifteen exploratory calls to discover table structures before every query. Which two changes address the root causes? A, expose the database schemas as an M C P resource so the agent can see available data without exploratory calls. B, expand the code-search tool's description to explain its capabilities and outputs and when to use it instead of Grep. C, remove Grep from the agent's tools. D, raise the agent's maximum number of turns so the exploration finishes. E, replace both servers with a single custom server that combines them. [pause]

ALEX: A and B.

SAM: Both. B fixes the description that loses to Grep; A removes the need to explore. C is the blunt cut: Grep is still the right tool for finding error messages and plain text. D pays for the symptom instead of removing it. E is over-engineering that fixes neither cause. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you picked A, a CLAUDE dot md in every directory with tests.

ALEX: And after segment three I can see the problem. Forty copies.

SAM: Forty copies that drift, and every new package starts with none. The answer is B: one rules file with a paths field matching every test file, loaded only when Claude works on one. A is the right tool for a single folder's conventions, applied to files spread across the tree. C puts team conventions at user level, where the next new hire never gets them. D makes always-needed conventions depend on someone remembering to invoke a skill.

ALEX: And the word that should have stopped me?

SAM: "Every package" and "only when". Files of one type scattered across the tree, loading only on contact: that is a glob in a rule. [sting]

## Five to remember

SAM: Five to remember. One: user-level files reach only you. When a new teammate is missing something everyone else has, it lives at user level; move it to project level, and check with slash memory first.

ALEX: Two: at-sign imports and topic files in dot claude slash rules keep CLAUDE dot md modular. Imports organise; a paths field is what stops loading.

SAM: Three: a rules file with a paths glob loads only for matching files. Spread across the codebase, use a glob; owned by one folder, a directory CLAUDE dot md.

ALEX: Four: project commands and skills live in the repo's dot claude folder and are shared; personal ones live in your home directory, with a different name. Context fork isolates verbose or exploratory work, allowed-tools restricts, argument-hint prompts for the parameter.

SAM: Five: project dot M C P dot json for shared servers with environment-variable placeholders, user config for experiments. All servers' tools are discovered at connection; a tool that loses to Grep needs a better description, a standard integration needs a community server, and a catalogue belongs in a resource.

## Recap: the exam tells

SAM: Recall first. Pause and name the four segments, and the question that runs under all of them. [pause]

ALEX: The CLAUDE dot md hierarchy, commands and skills, path-specific rules, and M C P in Claude Code. The question is who receives the instruction, and when it loads.

SAM: Now as exam tells. If one new teammate is missing what everyone else gets, think user level, check with slash memory, and move it to project level.

ALEX: If the root file has grown to hundreds of lines, think at-sign imports and topic files in dot claude slash rules. But imports organise; they do not save context.

SAM: If a skill floods the session, think context colon fork. If it must not run something destructive, allowed-tools. If it gets invoked without its parameter, argument-hint. If one person wants a change to a shared skill, a personal variant under a different name.

ALEX: If the conventions are for one file type spread across the tree, think a rules file with a paths glob. One folder's conventions, that folder's CLAUDE dot md.

SAM: If the agent keeps using Grep over a more capable M C P tool, fix that tool's description. If it explores tables before every query, expose a resource. And if the plan is to build a Jira server, use the community one.

ALEX: Next, episode three: plan mode, iterative refinement, and Claude Code in continuous integration.
