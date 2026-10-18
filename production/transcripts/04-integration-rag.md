---
episode: 4
slug: integration-rag
title: "Integration II: RAG, retrieval strategy, accuracy-latency, observability"
description: "The second half of Integration, the heaviest domain on the exam: chunking by document structure, indexing by query pattern, retrieval versus live tool calls, silent retrieval drift, defending a cost-latency configuration, and monitoring at scale."
domain: "Integration"
weight: "19%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect. Episode four: Integration, part two.

ALEX: And by the end?

SAM: You'll be able to choose chunking by the structure of the documents and indexing by how queries are phrased. You'll tell live state, which needs a tool call, from stable knowledge, which suits retrieval. You'll catch retrieval drift that never shows in the output, defend a cost and latency configuration, and pick what to monitor once the system runs at scale.

ALEX: It's the other half of the nineteen percent, the heaviest domain on the paper. The trap is tuning retrieval when the broken part is somewhere else, or adding a bigger model that can't reason over a chunk it never received. Confident and wrong is the signature failure here.

SAM: Then start with a choose-two. [sting]

## Cold open: service manuals

SAM: Here's a scenario. Choose two. A field service company gives its technicians an assistant over twelve years of equipment service manuals. The manuals are numbered, section by section, one section per fault procedure. The pipeline splits every manual into fixed five-hundred-token chunks and uses a dense embedding index only. Two complaints come in. First, when a technician types an exact fault code, say E four one seven, the answer often describes a different code. Second, the repair steps that come back are cut off halfway, with no sign of which compressor model they belong to.

SAM: Which two changes best fix both complaints? Option A: re-chunk the manuals hierarchically, keeping each numbered section and its parent model heading together. Option B: add a sparse keyword index alongside the dense one and merge the two ranked lists with reciprocal rank fusion. Option C: move to the most capable model tier. Option D: raise the number of retrieved chunks to fifty so the right one is somewhere in there. Option E: add a banner telling technicians to double-check fault codes against the printed manual.

ALEX: My gut says A and D. A for the cut-off steps, and D because if the right chunk isn't coming back, pull more chunks.

SAM: Hold that. We'll come back to it at the end.

SAM: This is Domain three, Integration, nineteen percent of the exam, the biggest single slice. Last episode covered capability bloat, auth, protocol choice and progressive discovery. Today is the other four task statements: design a rag pipeline with the right chunking and indexing, apply retrieval strategies matched to data shape and query pattern, evaluate accuracy-latency trade-offs and justify the configuration, and analyse observability challenges and select monitoring strategies at scale.

ALEX: One thing from episode three before we start. Identity gets injected by the server, never asserted by the user in their message.

SAM: And that carries straight into rag. In a retrieval system the retrieval layer enforces access control before anything reaches Claude. If a consultant isn't on a client's engagement, that client's confidential documents never get retrieved for them. The model is not the gate.

SAM: Segment one, chunking. A chunk is the unit that gets retrieved. The exam's rule: choose the chunking approach by the structure of the source material, not by a default chunk size. There are three to know.

ALEX: Fixed, semantic, hierarchical.

SAM: Fixed-size splits text into uniform spans, usually with overlap, ignoring structure. It earns its place on homogeneous, unstructured text where natural boundaries are weak, and it's the simplest to operate. Semantic splits on meaning boundaries and topic shifts, so it fits prose where each retrieved chunk has to stand on its own. Hierarchical preserves sections and subsections and retrieves at the level that fits, which suits contracts, manuals and policies where the section context carries meaning.

ALEX: So a hospital's clinical policy library, numbered sections, is hierarchical. A pile of free-text nurse handover notes with weak structure might be fixed-size. And long incident write-ups in prose are semantic.

SAM: That's the mapping. The trap is fixed-size on structured, section-numbered documents. It cuts across section boundaries and throws away the context the query depended on. Watch for the other chunking failure too: a split that breaks a semantic unit, like a table, a code block or a multi-paragraph argument, across two chunks.

SAM: Segment two, indexing. Chunking is chosen by what the corpus is. Indexing is chosen by how queries are phrased, because indexing decides what similar means when a query arrives.

ALEX: Before you tell me. Dense is embeddings, matches meaning. Sparse is keywords, matches exact terms.

SAM: Right. Dense fits queries phrased differently from the source: paraphrase, intent, concept matching. Sparse, keyword-based, B M twenty-five for example, fits queries that hinge on specific tokens: part numbers, statute citations, error codes. Hybrid runs both and combines the results. It fits mixed query patterns, which the course calls the common production case, and it recovers the exact-match results that dense alone misses.

ALEX: And when you have two ranked lists, you need one answer.

SAM: Reciprocal rank fusion. Each result is scored by its rank in each list, so the combined score favours items that rank well in both. The course calls it the standard, low-tuning default. If an exam option says merge dense and sparse with reciprocal rank fusion, that's a defensible design choice, not exotic engineering.

ALEX: Where's the trap here?

SAM: Two traps, pulling opposite ways. One is dense-only on a query set full of identifiers: a retail returns desk where half the questions are SKU numbers. The other is over-building. The course says size the pipeline's sophistication to the query patterns you actually have, not to the most thorough design imaginable. If every query is a paraphrased concept question, hybrid adds compute and a fusion step for nothing. [sting]

## Segment three: retrieval versus live state

SAM: Segment three, retrieval strategy by data shape, and the one mistake the course calls the most common in reference architectures: retrieval used where a tool call belongs.

ALEX: Live state.

SAM: Live state is data that changes during a conversation: order status, inventory, a price, a calendar slot, an account balance. An index captures what was true when it was built, not what's true now. So for live transactional state, call the system of record directly. Retrieval is for stable knowledge that was true yesterday and will be true tomorrow: policies, manuals, regulatory text.

ALEX: How do I spot it in a scenario?

SAM: Three symptoms: stale-looking chunks, results that shift with each index refresh, and answers that contradict the database. And operationally it looks healthy. Normal latency, no errors. Nothing signals a problem until a user notices the answer doesn't match reality.

ALEX: And the distractors will be retrieval tuning.

SAM: Exactly. A better chunker, a shorter refresh interval, a better embedding model or a higher similarity threshold will not fix it. This is a data-architecture problem, not a retrieval-quality problem. And remember similarity is not truth: a high similarity score means the text is close to the query, not that it's current.

SAM: Two more data-shape points. Separate live-state queries from static-knowledge queries, because a shared index refresh schedule that suits one creates staleness for the other. And know where retrieval itself breaks: a recall failure where the right document never enters the top-k, and questions that need synthesis across many documents, because the retriever scores each document independently.

SAM: Pause here and answer before we go on. A retail pharmacy chain runs a patient assistant. It answers questions about refill policy and also tells patients whether their prescription is ready. Both come from one vector index refreshed nightly from the pharmacy system. Patients are arriving to collect prescriptions the assistant said were ready, and they aren't. What's the best fix? Option A: refresh the index every fifteen minutes. Option B: switch to a stronger embedding model. Option C: answer prescription status with a tool call to the pharmacy system, and keep refill policy in retrieval. Option D: raise the similarity threshold so only close matches are used. [pause]

SAM: C. Prescription status is live state owned by the pharmacy system, so it gets a direct call. Refill policy is stable knowledge, so it stays in retrieval. Two kinds of data, two mechanisms. A narrows the staleness window but keeps a snapshot doing a live job. B and D tune retrieval, which was never the broken part.

ALEX: Got it. And I'll admit A looked reasonable.

SAM: It's the most tempting one because it does help a bit. The exam wants the answer that removes the cause. [sting]

## Segment four: silent drift

SAM: Segment four, silent drift. A rag pipeline that was correct at launch can degrade silently as documents are added. The course names three causes of retrieval quality drift: documents added or removed without reindexing, the query and document representations falling out of alignment, and an index refresh schedule that creates staleness for live-state queries.

ALEX: Why silent? Wouldn't output quality drop?

SAM: Because the failure mode is a confident answer built on the wrong chunk. Retrieval quality is not visible in the output. It has to be measured against a labelled set. So the course says track retrieval precision as its own metric, separate from output quality, in both the eval suite and production observability, and keep retrieval quality in the eval loop.

ALEX: Give me the concrete version.

SAM: The course's internal-knowledge-assistant example logs per-request retrieval precision measured against the grounding documents, and alerts when retrieval precision drops below threshold, alongside an alert on p ninety-five latency crossing the SLA. And it documents index coverage and freshness as the load-bearing boundary condition in the statement of work.

ALEX: That's the Domain four link too. Every retrieval configuration change goes through the eval gate before production.

SAM: Yes, and if you want to test a new retrieval configuration against real traffic without exposing users, that's shadow testing. Keep that for episode five.

SAM: Pause here and answer before we go on. Choose two. A public-sector benefits agency runs a caseworker assistant over its policy library. New policy circulars are added every week. Four months in, the model-graded score on final answers is flat, but caseworkers are revising more drafts, and several revisions cite policies that changed recently. Which two actions best address this? Option A: log retrieval precision per request against a labelled grounding set and alert when it falls below threshold. Option B: keep the model-graded answer score as the single quality signal, since it hasn't moved. Option C: add queries about newly added circulars to the labelled retrieval eval set and run it on every index update. Option D: add an alert when cost exceeds one hundred and fifty percent of the seven-day average. Option E: move to a larger model. [pause]

SAM: A and C. The pattern is silent retrieval drift as the corpus grows. A measures retrieval separately in production, C puts retrieval quality in the eval loop for exactly the documents that are changing. B is the mistake that hid the problem: output scores don't show which chunk came back. D is a good alert in general, but it watches cost, not retrieval. E is the bigger-model distractor. A model can only reason over what it was handed.

ALEX: And the caseworker revisions, that's the outcome signal.

SAM: Right. Capturing the user's acceptance or revision of a draft is the course's outcome signal. Hold that thought for observability. [sting]

## Segment five: accuracy and latency

SAM: Segment five, accuracy-latency trade-offs. Every retrieval design trades three things: retrieval quality, meaning does the right chunk come back; latency, meaning how much time retrieval adds; and maintenance, meaning the work to keep the pipeline correct as the corpus changes.

ALEX: And the directions?

SAM: Smaller chunks and hybrid indexing tend to raise quality and latency together. Larger chunks and dense-only lower latency and maintenance but miss exact-match queries. There's no universally right point, only the one that fits this corpus and these queries, stated as a trade-off you can defend.

ALEX: How do I justify a configuration on the exam?

SAM: Name the load-bearing constraint. In the course's design exercise, query variety is what justifies hybrid: the fusion step costs compute and latency, but it earns its place because the queries genuinely need both modes. Then the wider budget rules. Design to p ninety-five latency, not the median, because SLA breaches live in the slow tail. When there's a cost ceiling and a latency budget, both must hold at once. Being well under one buys no slack against the other.

ALEX: And the levers.

SAM: When the system prompt is long and stable, prompt caching is usually the most effective cost and latency lever. Static content first, volatile content after the cached prefix. That's the Domain two rule showing up again. Model tier routing is the other big lever: cheap fast tiers for routine work, stronger tiers for the hard calls. A fallback chain from a stronger, slower model to a faster one absorbs latency spikes. Stream anything user-facing. And raising the max output tokens cap never helps either target; it raises both cost and latency.

ALEX: Time to first token versus time to completion?

SAM: Track them separately. Time to first token governs how responsive it feels. Time to completion governs total duration and cost.

SAM: Pause here and answer before we go on. A bank's contact-centre assistant is breaching its p ninety-five latency target. It sends a long, stable policy prompt on every call, runs every query on the top model tier, and uses a hybrid index. About forty percent of queries are exact product codes. The cost is within budget. What's the best first change? Option A: drop the sparse index to save retrieval time. Option B: cache the stable policy prompt and route routine queries to a faster tier, keeping the hybrid index. Option C: raise the max output tokens cap so fewer answers get cut short. Option D: stop logging requests to shave time off each call. [pause]

SAM: B. It attacks the latency where it's coming from without losing anything required. A buys speed by losing the exact-match recall that forty percent of queries depend on, a blunt cut. C makes latency worse. D is a real trade the course names, less logging detail for a faster response, but you lose visibility into each interaction, and nothing in the scenario says logging is the bottleneck. [sting]

## Segment six: observability at scale

SAM: Segment six, observability at scale. An LLM system doesn't crash when it's wrong. It gives a subtly wrong answer. Standard logging catches errors and timeouts, not that.

ALEX: The course had four things to log.

SAM: Request: model version, input token count, prompt identifier. Response: output token count, latency, stop reason. Context: user role, session ID, whether caching applied. Outcome: whether the downstream system accepted the output and any rejection signals. Request-level traces also capture any tool calls. For a rag system, add retrieval precision per request and cache hit or miss.

ALEX: And the layers above the trace?

SAM: The four questions: what is the system doing, how well, when did it change, and why. That maps to request tracing, metric aggregation, anomaly detection and change attribution. Aggregate cost per request, p fifty and p ninety-five latency, task success rate if there's an acceptance signal, and error rate by type. Threshold alerts: the course's example is a cost spike over one hundred and fifty percent of the seven-day average, or p ninety-five crossing the SLA. Gradual model drift is harder to catch with thresholds and needs periodic distribution comparison.

ALEX: Change attribution. Model drift, data drift, model update effect.

SAM: Quick check. A claims assistant's success rate drops the week after a regional flood. Model version is pinned and unchanged. Which is it?

ALEX: Data drift. The input mix changed, flood claims, not the model.

SAM: Correct. Model drift is a change in output behaviour on stable inputs. A model update effect needs a version change, which the pinning rules out. Mixing them up gives the wrong fix.

SAM: Now the trap the exam loves: aggregate-only dashboards. A system can look healthy on averages while a small fraction of requests consumes most of the budget and produces wrong outputs. Aggregates catch obvious failures; per-request decomposition catches the rest. Two more scale points. A multi-tenant system on one shared API key can't attribute a rate-limit breach to the tenant that caused it, so isolate tenants in Workspaces, each with its own keys, spend and rate limits. And in multi-agent systems, use a shared trace ID across orchestrator and subagents.

ALEX: And the business people?

SAM: They read KPIs, not traces. Build a translation layer at design time: task success rate maps to first-contact resolution, latency maps to handle time. And build observability before the first incident, because afterwards you're reconstructing root cause from logs that were never designed to answer the question.

SAM: Back to the cold open. Fault codes answered wrong, repair steps cut off mid-procedure, fixed chunks, dense-only index. You said A and D.

ALEX: Having heard all that, A and B.

SAM: A and B. A, hierarchical chunking, fixes the cut-off steps: the manuals are section-numbered, and fixed-size chunks were slicing procedures and dropping the model heading. B, a sparse index merged with reciprocal rank fusion, fixes the fault codes: exact tokens are sparse territory, and dense-only misses them. C is the bigger-model distractor; the model can't reason over a chunk it was never given. D adds noise and latency and doesn't fix how chunks are split or matched. E is a compensating control dressed as a fix. [sting]

## Five to remember

ALEX: Five to remember. One: chunk by what the corpus is. Fixed for weak structure, semantic for prose, hierarchical for numbered documents.

SAM: Two: index by how queries are phrased. Sparse for exact tokens, dense for paraphrase, hybrid for mixed queries, merged with reciprocal rank fusion as the low-tuning default.

ALEX: Three: live state gets a tool call to the system of record. Better chunkers, faster refreshes and higher thresholds don't fix a snapshot doing a live job.

SAM: Four: retrieval drift is silent. Measure retrieval precision separately against a labelled set, in evals and in production, and alert on it.

ALEX: Five: defend a configuration by naming the load-bearing constraint, design to p ninety-five, meet cost and latency together, and monitor per request, not just in aggregate.

## Recap: the exam tells

SAM: Before the tease, a test. Pause and name the six segments, or the giveaway for each. [pause]

ALEX: Chunking. Indexing. Retrieval versus live state. Silent drift. Accuracy-latency trade-offs. Observability at scale.

SAM: Now as exam tells. If documents are section-numbered and answers come back cut off mid-procedure, think hierarchical chunking.

ALEX: If exact codes, part numbers or citations come back wrong on a dense-only index, think sparse alongside dense, merged with reciprocal rank fusion.

SAM: If answers contradict the database while latency is normal and nothing errors, think live state in an index. A tool call fixes it; a faster refresh doesn't.

ALEX: If output scores are flat but users revise more drafts as the corpus grows, think silent retrieval drift. Measure retrieval precision on its own.

SAM: If p ninety-five is breaching with a long, stable prompt on the top tier, think caching and tier routing, keeping the index that exact-match queries need.

ALEX: If dashboards look healthy on averages but the budget is burning, think per-request decomposition. And if the model is pinned but the input mix changed, think data drift.

SAM: And if an option raises the max output tokens cap to fix latency, think wrong direction. It raises cost and latency together, and it never helps either target.

SAM: Next episode: Evaluation, Testing and Optimization, where evals become the gate for every change we talked about today.
