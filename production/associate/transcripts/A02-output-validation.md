---
episode: "A02"
series: "CCAO-F"
slug: output-validation
title: "Checking what Claude gives you"
description: "The heaviest domain on the Associate paper: judging accuracy and completeness, catching invented details, contradictions and slanted framing, checking against the source, deciding when a person must review, adapting drafts for the reader, and choosing between inline, artifact and structured data."
domain: "Output Evaluation and Validation"
weight: "21%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Associate Foundations. This is episode two: checking what Claude gives you.

ALEX: And what will I be able to do by the end?

SAM: Judge a draft for accuracy and for what it left out, and spot the invented figure, the contradiction and the slanted framing. Pick the checking technique that actually catches the error. Decide when a person has to review before anything goes out, and when a quick self-check is enough. Compare and adapt drafts for the reader who gets them. And choose between an inline answer, an artifact and structured data.

ALEX: This is the heaviest domain on the paper, twenty-one percent, so about thirteen of the sixty items. And it's exactly where I trust a fluent answer too fast.

SAM: Then we start with one. [sting]

## Cold open: the vendor comparison

SAM: An operations lead asks Claude to compare three vendor proposals against her team's twelve-point requirements list and recommend one to the procurement committee. Claude returns a clear table and recommends Vendor B. Reading it over, she notices the table has ten rows. What is the best next action? Option A, send it, since Claude most likely dropped the two requirements that did not separate the vendors. Option B, ask Claude to score the two missing requirements, quoting each proposal, then check those rows and whether the recommendation still holds. Option C, rerun the whole comparison on the most capable model. Option D, send it with a note telling the committee the comparison may be incomplete.

ALEX: D. Honesty with the committee. They see the caveat, and nobody can say I hid anything.

SAM: Hold that. We come back to it at the end.

ALEX: Twenty-one percent. What exactly does the guide test here?

SAM: Six objectives. Evaluate outputs for accuracy and completeness. Identify hallucinations, inconsistencies and biases. Apply fact-checking and validation techniques. Decide when human review or more verification is needed. Edit, adapt and compare outputs for the intended audience. And organise information and choose the format: artifacts, inline or structured data.

ALEX: And what does the right answer tend to look like?

SAM: The diligent, proportionate step. The distractors trust the model's confidence, spend more than the task needs, ask the model to promise something a check should do, give up on the task, or polish the wording without fixing it. Those are the five families from episode zero, and every drill today uses them. [sting]

## Accuracy, hallucinations and bias

SAM: Two questions for any output. Is what it says true? And is everything there that was asked for? Accuracy and completeness, and they fail differently. A wrong figure sits on the page where you can catch it. A missing item leaves no trace, so you only find it by checking against the brief or the source, never by rereading the draft.

ALEX: And a hallucination is the wrong-figure kind.

SAM: A hallucination is content that sounds right and is grounded in nothing: an invented statistic, a quote nobody said, a policy number, a citation to a subsection that does not exist. Anthropic's help centre names two causes: training data that may be out of date, and quotes that look authoritative but are not grounded in fact. Its advice is not to treat Claude as the only source of truth, and to scrutinise high-stakes advice.

ALEX: Here's my actual habit, though. I've used Claude every day for a year. When it sounds sure and the draft reads well, I don't check everything. Mostly it's right.

SAM: Mostly it is, and checking every sentence of every draft would wipe out the time you saved. Being proportionate is the right instinct.

SAM: But confidence and fluency tell you nothing about accuracy. An invented quote reads as smoothly as a real one. The guide's own sample rationale says self-reported confidence is not a reliable accuracy signal, so the exam never rewards "it sounded sure".

ALEX: So where do I look?

SAM: At the specifics: numbers, names, dates, quotes, citations, anything legal or regulatory. And at where the output is going. When a stem gives you a confident specific headed outside the team, the answer checks that specific against the source.

SAM: Inconsistencies next: the draft contradicts itself or its source. The summary says costs fell and the table shows them rising. Regional figures that do not add up to the stated total. A date on page one that differs from page three. These are cheap to catch: read the output against itself and against what you gave it.

SAM: Then bias. One-sided framing, a summary that reports complaints from only one region, a job advert worded to suit one kind of candidate, a recommendation that simply agrees with the option you hinted at.

ALEX: That last one's me. I ask "why is Vendor B the best fit" and I'm surprised when it agrees.

SAM: The prompt leaked the answer. Ask a neutral question, ask for the strongest case against, or have it apply the same criteria to every option. For content about people, swap the name or the group and see whether the wording changes.

SAM: Pause here and answer before we go on. A sales lead asks Claude to turn her call notes into a short customer case study for the company website. The draft includes a quote from the customer's finance director and says onboarding time fell by forty percent. Her notes contain neither. What should she do? A, keep both, since Claude probably inferred them from the context of the call. B, ask Claude whether the quote is accurate, and keep it if Claude says yes. C, remove the quote and the figure unless the customer confirms them, and check every other specific in the draft against her notes. D, soften the figure to "around forty percent" and keep the quote. [pause]

ALEX: C.

SAM: C. Neither detail traces to the source, so both are invented until the customer says otherwise, and a public page with a made-up quote from a named person is a real problem. A trusts the model. B asks the model to vouch for itself. D keeps the invention and makes it vaguer. And note the second half of C: one invented specific is a reason to check the rest. [sting]

## Fact-checking techniques

SAM: Segment two, how you check. The strongest check is the authoritative source: the regulation, the contract, the finance system, the person who said it. Every other technique makes that check faster or narrows what needs checking.

ALEX: Such as?

SAM: Anthropic's prompting guidance lists several. Give Claude permission to say "I don't know", or "the document doesn't cover this". Tell it to use only the documents you provided, not its general knowledge. For long documents, ask it to pull word-for-word quotes first and base its answer on those. Ask it to back each claim with a supporting quote, and to drop any claim it cannot support. And run the same request more than once: if the answers disagree on a fact, that fact needs checking.

ALEX: And when it searches the web it gives me citations. Then it's checked, surely.

SAM: A citation is a real step up. You can see where the claim came from, and for an internal briefing that may be all the evidence you need.

SAM: But a citation is a place to check, not a check. Claude can misread a real page, drop context, or attach a source that does not quite say what the sentence says. The help centre tells you to review cited sources because the original often holds context the summary lost.

ALEX: So the tell?

SAM: If a stem says the output "includes citations" and asks what to do before it reaches an important reader, the answer still opens the source.

SAM: Pause here and answer before we go on. Choose two. A consultant is using Claude to summarise a sixty-page regulatory consultation for a client deck. She wants to reduce the risk of invented details. Which two steps help most? A, tell Claude to use only the uploaded document and to say plainly when it does not cover a point. B, ask Claude to quote the passage that supports each key claim, then check those quotes against the document. C, ask Claude to give each claim a confidence percentage, and drop any under eighty. D, ask for the summary in a more authoritative tone so the client trusts it. E, add "be accurate" in capitals to the prompt. [pause]

ALEX: A and C. C gives me a filter. I keep the claims it's sure about, and it's automatic.

SAM: A is right. C is the trap from the guide's own sample: trusting the model's confidence. A confidence score is more generated text, and an invented claim can arrive at ninety-five percent. It is the distractor that asks the model to promise what a check should do.

ALEX: So B.

SAM: A and B. A limits Claude to the source and makes gaps visible. B gives every claim a quote you can check in seconds. D changes the tone, not the truth. E is a polite instruction, and it gives you nothing to verify. [sting]

## When a human must review

SAM: Segment three, when a person has to review. Four things raise the bar. Stakes: money, health, legal position, someone's job. Audience: anything leaving the team, especially to customers, regulators or the board. Reversibility: a published statement or a sent offer letter cannot be taken back. And specialist content: legal, medical, financial or H R judgements need someone qualified to sign them off.

ALEX: Then my rule's simple. Everything Claude writes gets a second pair of eyes. Safest answer every time.

SAM: Now you've over-applied it. Reviewing a brainstormed list of offsite themes is time nobody gets back, and the exam treats that as disproportionate, just as it treats skipping review as careless. A team that reviews everything soon reviews nothing properly.

ALEX: So what flips it?

SAM: The words in the stem. Customer, patient, regulator, board, contract, offer, published: review by someone accountable. Brainstorm, first pass, draft for myself: a quick self-check is enough. And judge the decision the output feeds, not only who reads it.

SAM: Who reviews matters too. The reviewer is someone who can tell if it is wrong: a clinician for patient guidance, legal for a contract position, the data owner for figures. A colleague skimming for typos is not review. And this is where the domain meets governance, in episode six: some content needs review because policy says so, however good the draft.

SAM: Pause here and answer before we go on. This is a dropdown item: four statements, and for each one choose "human review before use" or "self-check is enough". One: a list of ten possible names for a team offsite. Two: a plain-language summary of a patient's discharge instructions, to be handed to the patient. Three: an internal analysis that will set next year's list prices. Four: Claude's rewording of a paragraph from your own internal newsletter, to make it easier to read. [pause]

ALEX: One, self-check. Two, review, by a clinician. Three, self-check, it's internal. Four, self-check.

SAM: Three out of four. Three needs review. It never leaves the building, but it sets prices for every customer next year, so someone who owns the pricing figures checks it. You judged the reader; judge the decision. Two reaches a patient and carries medical instructions. One and four are low stakes and easy to undo, and for four your check is that the meaning has not changed. [sting]

## Editing for the audience

SAM: Segment four, editing, adapting and comparing for the reader. The same findings go to different people in different shapes. An executive wants the decision and the risk first. A customer wants plain words and no internal jargon. A specialist team wants the detail and the method. Claude can draft each version; the editing judgement is yours: does this version give this reader what they need?

ALEX: And the risk?

SAM: That a rewrite changes the facts while it changes the tone. A finance analyst asks for a friendlier version of a forecast note for the sales team. The original said the forecast "is at risk if fourth-quarter renewals slip". The friendly version says the forecast "looks on track". Same topic, opposite message. When you adapt, compare the new version with the original for figures, commitments and caveats, not just tone.

ALEX: And the caveats go first.

SAM: Usually. "May" becomes "will", and "subject to approval" vanishes. Those are the edits that cause trouble later.

SAM: The other half is comparing drafts. When you have two versions, judge them against the brief and the reader, not against each other's polish. Pause here and answer before we go on. A communications manager asked Claude for a staff announcement about an office move. Staff had raised four questions: the moving date, parking, desk booking, and who to contact. Draft one is warm and polished and answers two of them. Draft two is plainer and answers all four. What should she do? A, send draft one, because tone matters most for staff news. B, ask Claude which draft is better and send that one. C, take draft two, since it meets the brief, and edit its tone for the audience. D, send both and let staff use whichever they prefer. [pause]

ALEX: I'm tempted by A. People remember tone, and a cold announcement about a move lands badly.

SAM: Tone matters, and a clumsy announcement can cost goodwill.

SAM: But tone is the cheap part to fix, and completeness is the expensive part. Draft one leaves half the office asking where to park. So C: start from the draft that meets the brief, then edit the tone. B hands the judgement back to the model with no criteria. D passes the editing job to every reader.

ALEX: The tell?

SAM: When a stem sets polish against completeness or accuracy, choose the draft that meets the brief. Tone gets edited in afterwards. [sting]

## Formats: inline, artifact, structured data

SAM: Last segment, organising and choosing a format. The guide names three. Inline is the ordinary reply in the conversation: right for a quick answer, an explanation, a short back-and-forth. An artifact opens beside the conversation as its own piece of work. The help centre's test is content that is significant and self-contained, typically over fifteen lines, that you are likely to edit, iterate on or reuse outside the conversation, and that you will refer back to: a document, a diagram, a dashboard, a small interactive tool.

ALEX: Then I'd ask for an artifact every time. It looks finished.

SAM: It does, and for anything you will hand to someone, that helps.

SAM: But "what's the deadline in this email" does not need a document beside the chat. Wrapping a two-line answer in an artifact adds a step and nothing else. The tell for an artifact is revise over several rounds, share, reuse, stand-alone. The tell for inline is quick, check, explain.

ALEX: And structured data?

SAM: A table, or data in a fixed shape such as a spreadsheet-ready list, when the output will be compared across rows, sorted, or fed into another tool. A risk register with an owner, likelihood and due date for twenty risks is a table with fixed columns, not twenty paragraphs. Name the columns, and ask for the same columns every week so this week's register lines up with last week's.

ALEX: And curating?

SAM: Deciding what goes in and in what order. Lead with what the reader needs, group related points, drop duplicates, and keep the source next to each claim that someone will check.

SAM: Pause here and answer before we go on. An H R partner needs a two-page onboarding guide for new starters. She will revise it with Claude over several rounds this week, then share it with hiring managers. Which output suits the task best? A, an inline reply, copied into a document after each round. B, an artifact, so the guide stands on its own beside the conversation and can be revised and shared. C, the guide as structured data with one field per section. D, a series of short messages, one per section. [pause]

ALEX: B.

SAM: B. Two pages, self-contained, revised over several rounds, then shared: it meets every part of the artifact test. A works, but she rebuilds the document by hand every round. C is the right shape for data that feeds a tool, not prose that people read. D scatters the guide across the conversation. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Ten rows against a twelve-point list. Alex, you chose D, send it with a caveat.

ALEX: And after segment one I can see it. The caveat tells the committee there's a gap and leaves them to deal with it.

SAM: The answer is B. Have Claude cover the two missing requirements with quoted evidence, check those rows, and check whether Vendor B still comes out ahead. D is a disclosure dressed as a fix: the committee still decides on an incomplete comparison. A assumes Claude dropped them for a good reason, which is trusting the model. C pays for a bigger model, and you would still have to check the new table against the list.

ALEX: What should have stopped me?

SAM: "Twelve-point list" and "ten rows". When the stem tells you what was asked for and shows you less, the answer checks the output against the brief and fills the gap before it reaches the reader. [sting]

## Five to remember

SAM: Five to remember. One: confidence and fluency are not accuracy. Check the specifics, numbers, names, quotes and citations, against the source, and treat one invented specific as a reason to check the rest.

ALEX: Two: completeness is checked against the brief or the source, never by rereading the draft. A missing item leaves no trace.

SAM: Three: the strongest check is the authoritative source. Limiting Claude to your documents, letting it say "I don't know", and asking for a supporting quote per claim make that check faster. A self-rated confidence score is not a check.

ALEX: Four: human review scales with stakes, audience, reversibility and specialist content. Judge the decision the output feeds, not only who reads it, and don't send a brainstorm for review.

SAM: Five: inline for quick answers, an artifact for substantial stand-alone work you will revise, reuse or share, and structured data with fixed columns when it will be sorted, compared or fed into a tool. And when you adapt for an audience, the facts and caveats stay put.

## Recap: the exam tells

SAM: Recall first. Pause and name the five segments, and the check that goes with each. [pause]

ALEX: Accuracy, hallucinations and bias: check the specifics. Fact-checking: go to the source, with quotes. Human review: stakes and audience. Editing: meet the brief and keep the facts. Formats: inline, artifact or structured data.

SAM: Now as exam tells. If a draft contains a precise figure, quote or citation you cannot find in the source, think invented until confirmed, and check the rest.

ALEX: If the stem shows the output covering less than was asked for, think check it against the brief and fill the gap. A caveat is not a fix.

SAM: If an option asks Claude how confident it is, or adds "be accurate" to the prompt, think distractor. If it limits Claude to the source and asks for checkable quotes, think right answer.

ALEX: If the output includes citations and is going to an important reader, still open the sources.

SAM: If the stem says customer, patient, regulator, board, contract or published, think review by someone qualified. If it says brainstorm or first pass, a self-check.

ALEX: If polish competes with completeness, take the complete draft and edit the tone. If a rewrite softens a caveat, the rewrite is wrong.

SAM: If it's quick, inline. If it stands alone and gets revised or shared, an artifact. If it's rows to sort or import, structured data.

ALEX: Next, episode three: choosing the product and the model.
