---
episode: "A05"
series: "CCAO-F"
slug: projects-knowledge
title: "Projects, knowledge and connectors"
description: "Setting up a Project with instructions and knowledge, choosing between uploaded files and connectors such as Google Drive and Gmail, writing project instructions that work, and keeping a shared configuration current."
domain: "Configuration and Knowledge Management"
weight: "12%"
target_minutes: 16
---

## In this episode

SAM: Welcome to Pass the Architect, Associate Foundations. This is episode five: Projects, knowledge and connectors.

ALEX: What will I be able to do by the end?

SAM: Decide what goes in a Project's instructions and what goes in its knowledge. Choose between uploading a file and connecting a source such as Google Drive or Gmail. Rewrite weak project instructions into ones that hold up. And keep a shared Project current when the documents behind it change.

ALEX: Twelve percent, about seven items. And my weak spot is the workaround: when something is not set up, I find a way round it instead of getting it set up.

SAM: Then the opening item is for you. [sting]

## Cold open: the missing connector

SAM: A marketing coordinator at a company on a Team plan wants her campaign Project to use the brand guidelines and campaign briefs kept in the company's Google Drive. When she looks for the Google Drive connector, it is not available to her. What is the most appropriate action? Option A: download the files each week and upload them to the Project by hand. Option B: ask the organisation's Owner or Primary Owner to enable the Google Workspace connectors at the organisation level. Option C: connect her Drive through a personal Claude account instead. Option D: paste the Drive folder's link into the chat and ask Claude to open it.

ALEX: A. It works today, and the campaign launches Friday.

SAM: Hold that. We come back to it at the end.

ALEX: Seven items. What do they cover?

SAM: Four objectives. Configure Projects with instructions and knowledge sources. Manage uploaded knowledge and connectors, with Google Drive and Gmail as the guide's examples. Create effective system-level instructions, which in claude.ai means project instructions. And inform, maintain and update the configuration as things change. Under all of them: where does each piece belong, and who keeps it current? [sting]

## Segment one: instructions and knowledge

SAM: A Project has two parts you configure. Instructions tell Claude how to behave: the help centre says Claude uses them for all the chats within the Project. Knowledge tells Claude what to know: documents, text and code you upload, used across every chat in the Project.

ALEX: And my settings?

SAM: Different scope. The instructions in your profile settings apply to all of your conversations, everywhere. Project instructions apply only to chats in that Project. So your preference for short answers goes in your profile. The team's proposal structure goes in the Project.

ALEX: How much can a Project hold?

SAM: More than you might think. On paid plans, the help centre says that when project knowledge approaches the context limit, Claude switches to retrieval automatically: it searches the Project and pulls in only what is relevant to your question, expanding capacity by up to ten times. You see an indicator when it is on.

ALEX: Then I'll put everything in. Every version of every policy, every old proposal. More context, better answers.

SAM: Capacity is real, and a well-stocked Project does beat pasting files in by hand.

SAM: But retrieval pulls whatever matches the question. If last year's rate card and this year's both sit in the knowledge, either can come back, and Claude has no way to know which one you meant. Curate: one current version of each document, nothing superseded. The help centre's tips point the same way: keep project instructions concise, and limit active tools and connectors, because they use context.

ALEX: The tell?

SAM: "Old and new versions", "contradicts", "sometimes quotes last year's". The fix is curating the knowledge, not adding more to it.

SAM: Pause here and answer before we go on. A sales lead sets up a shared Project for her team's proposals. Every proposal must follow the company's five-section structure and use British spelling. Where should that requirement go? A, in her own profile settings, so Claude always writes that way for her. B, in the Project's instructions, so it applies to every chat in the Project. C, in a note at the top of each proposal chat. D, in an uploaded document called "style notes", with no instructions pointing to it. [pause]

ALEX: B.

SAM: B. It is a rule for how Claude behaves in every chat in this Project, for everyone using it. A only reaches her, in every conversation, including ones that have nothing to do with proposals. C depends on everyone remembering. D puts a behaviour rule where Claude treats it as reference material, with nothing saying it must be followed. [sting]

## Segment two: uploads and connectors

SAM: Two ways to give a Project knowledge. Upload a file, and the Project holds the version you uploaded. Or connect a source. For Google Drive, the help centre says you can add Drive files to a Project's knowledge, and a linked Google Doc keeps syncing with the latest version in Drive.

ALEX: So a document that changes every week should be connected, not uploaded.

SAM: Exactly. A signed contract that never changes can be uploaded. A pricing sheet the finance team updates every Monday should be linked from Drive. Two more details from the help centre: Claude can read Sheets, Slides, PDFs and Office files through Drive, but images embedded in documents are not processed. And Claude can only open files your own Google account can access. Your Drive permissions still apply.

ALEX: And Gmail?

SAM: The Gmail connector lets Claude search and read your emails and draft replies. It sees attachment details, not attachment content. So "summarise this week's client emails" is a Gmail connector job. "Analyse the spreadsheet attached to that email" needs the file itself, uploaded or in Drive.

ALEX: If I'm connecting Drive anyway, why not connect all of it? Then Claude can find anything.

SAM: It is convenient, and search over a whole drive can surface things you forgot you had.

SAM: But the guidance runs the other way: active connectors use context, and a Project works best scoped to its job. There is also governance, which is episode six: the more Claude can reach, the more care each request needs. Give the Project the folders its work needs. The tell is "only the files for this engagement" or "keep the Project focused": scope it.

ALEX: And on a Team or Enterprise plan?

SAM: An Owner or Primary Owner must enable the Google Workspace connectors at the organisation level before members can connect their accounts. Hold that thought for the cold open.

SAM: Pause here and answer before we go on. Choose two. An HR partner's policy Project keeps quoting the old parental leave terms. The policy handbook was updated in Google Drive two weeks ago. The Project's knowledge holds a P D F of the handbook exported last spring. Which two actions fix this? A, add the handbook to the Project's knowledge from Google Drive, so the linked Google Doc keeps syncing. B, remove the old P D F from the Project's knowledge. C, switch the Project to Opus. D, add an instruction saying "always use the latest policy". E, turn on research for policy questions. [pause]

ALEX: A and D. Link the live doc, and tell Claude to prefer the latest.

SAM: Half right. A is in. D is the polite-instruction distractor: Claude cannot tell which copy is newer just because you asked, and the old P D F is still there to be retrieved. The second answer is B, removing the superseded file. A and B together: one current, syncing source and nothing stale beside it. C is the bigger-model reflex. E searches the web for an internal handbook. [sting]

## Segment three: instructions that work

SAM: Now the instructions themselves. Weak project instructions sound like this: "You are a helpful assistant. Be accurate."

ALEX: Which says nothing.

SAM: Nothing Claude can act on. Strong instructions cover five things. The role and audience: "you support the client delivery team, writing for finance directors". The task and output format. Which knowledge files are authoritative, and for what: "pricing comes only from the current rate card". What to do when the knowledge does not answer the question: "say so and ask; do not estimate". And any limits, such as never naming other clients.

ALEX: Why the fallback line? It feels obvious.

SAM: Because without it, the gap gets filled with something plausible. Telling Claude to say when the knowledge does not cover a question turns a quiet guess into a visible question. That is still not a guarantee: anything bound for a client still gets checked, as in episode two.

ALEX: Let me push back. Why not paste the whole delivery manual into the instructions? Then every rule is right there.

SAM: You would never lose a rule, I grant you that.

SAM: But instructions are for how to behave, and the help centre's tip is to keep them concise. A thirty-page manual belongs in knowledge, where retrieval can find the relevant part. The instructions then point to it. The tell: if it is a rule for behaviour, instructions; if it is reference material, knowledge.

SAM: Pause here and answer before we go on. A consultant's Project instructions read: "You are helpful. Be accurate." Outputs come back in different formats each time, and sometimes cite terms from an old engagement letter that is still in the knowledge. What is the best fix? A, rewrite "be accurate" in capitals and add "never make mistakes". B, rewrite the instructions to state the role, audience and required format, name which documents are authoritative, and tell Claude to say when the knowledge does not cover a question; and remove the old engagement letter. C, paste the text of every knowledge file into the instructions. D, start each chat in research mode. [pause]

ALEX: B, though it's the long one, and I'm always suspicious of the long one.

SAM: Good instinct to check, but here the length is doing work. B fixes both symptoms: the format drift with a stated format, and the stale citation by naming the authority and removing the old letter. A is louder guidance with nothing new in it. C bloats the instructions and keeps the stale letter. D searches the web for something that lives in the Project. [sting]

## Segment four: keeping it current

SAM: Last objective: inform, maintain and update. A Project is a configuration, and configurations go stale. Three habits. Name an owner. Tie updates to triggers: when a policy, price list or template changes, the knowledge and any instruction that mentions it change the same day. And after a change, rerun a handful of standard questions and compare the answers to before.

ALEX: On a shared Project, can everyone edit?

SAM: On Team and Enterprise, the help centre gives two levels: "can view", to see and chat, and "can edit", to change instructions and knowledge and manage members. So the people who maintain it get edit; the people who use it get view.

ALEX: That feels restrictive. If anyone spots an error, they should be able to fix it.

SAM: It's quicker, and in a small team of three it may be fine.

SAM: But in a Project a whole department relies on, untracked edits are how a stale file or a contradictory rule creeps back in. The exam wants a named owner and a controlled change. Users report; the owner updates. The tell: "shared across the team", "who maintains", "someone changed the instructions": controlled edit access and an owner.

SAM: One more, in the dropdown style. Pause here and answer before we go on. For each source, choose upload to the Project, connect it, or hold and check policy first. One: a signed master services agreement that will not change, needed in every chat. Two: a weekly pricing sheet maintained in Google Drive. Three: this week's client emails, to summarise open actions. Four: an HR export with employee home addresses and salaries, where policy restricts personal data. [pause]

ALEX: One, upload. Two, connect through Drive. Three, connect Gmail. Four, hold and check policy.

SAM: All four. One never changes, so an upload is fine. Two changes weekly, so link it and let it sync. Three lives in the inbox, which is what the Gmail connector reads. Four is a data-sensitivity question, which episode six covers in full: check what policy allows, and remove or anonymise the personal details before anything goes in. [sting]

## Cold open: the verdict

SAM: Back to the marketing coordinator. Alex, you picked A: download and upload by hand every week.

ALEX: And after segment two I see the cost. Every upload is a snapshot, so the Project is out of date the day after, and it depends on me remembering every week.

SAM: Right. The answer is B. On a Team plan, an Owner or Primary Owner enables the Google Workspace connectors at the organisation level, and then she can connect her account. A is the workaround that turns a one-time setup into a weekly chore and stale knowledge. C moves company documents into a personal account, outside the organisation's controls. D asks Claude to open a link it has no connection to read.

ALEX: The tell?

SAM: "Not available to her" on a Team or Enterprise plan. That is an organisation setting, so the answer is the person who owns it. [sting]

## Five to remember

SAM: One: instructions are how Claude behaves in every chat in the Project; knowledge is what it knows. Profile settings reach only you, in every conversation.

ALEX: Two: on paid plans, a Project switches to retrieval as knowledge nears the context limit, up to ten times the capacity. So curate: one current version of each document, nothing superseded.

SAM: Three: upload what never changes; connect what does. A linked Google Doc keeps syncing. Gmail reads and drafts email but not attachment content. Claude sees only what your Google account can.

ALEX: Four: strong instructions name the role, audience, format, the authoritative sources and what to do when knowledge runs out. Keep them concise; manuals belong in knowledge.

SAM: Five: give a shared Project an owner, update on every source change, retest with standard questions, and keep edit access to the maintainers. Connector not available on a Team plan: the Owner enables it.

## Recap: the exam tells

SAM: Recall first. Pause and name the four segments, and the question that ran under all of them. [pause]

ALEX: Instructions and knowledge, uploads and connectors, instructions that work, and keeping it current. The question: where does each piece belong, and who keeps it current?

SAM: Now as exam tells. If a rule applies to every chat in a shared Project, think project instructions. If it is one person's preference everywhere, think profile settings.

ALEX: If the Project quotes an old version, think: link the live source and remove the stale file. Not a louder instruction, not a bigger model.

SAM: If a source changes weekly, connect it. If it never changes, upload it. If the connector is missing on a Team plan, ask the Owner or Primary Owner.

ALEX: If instructions say "be helpful, be accurate", rewrite them with role, format, authority and a fallback. If someone wants to paste a manual into them, it goes in knowledge instead.

SAM: If several people can change a shared Project and it keeps drifting, think owner, edit access and a retest after each change.

SAM: Next, episode six: governance, risk and responsible use.
