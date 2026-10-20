---
episode: "D01"
series: "CCDV-F"
slug: api-mechanics
title: "The Claude API: messages, streaming, thinking, caching and batch"
description: "How a Messages A P I call really works: stop reasons, tool results, streaming events, images, thinking blocks, how data reaches Claude, cloud platforms, realtime versus batch, and how to track tokens and place cache breakpoints that actually hit."
domain: "Applications and Integration; Model Selection and Optimization"
weight: "6.8% and 2.8%"
target_minutes: 22
---

## In this episode

SAM: Welcome to Pass the Architect, Developer Foundations. This is episode one: the Claude A P I.

ALEX: What do I walk away able to do?

SAM: Read a response by its stop reason and close a tool call properly. Choose when to stream, how to send an image, and what to do with thinking blocks. Pick how data reaches Claude, and what changes when you call it through a cloud platform. Choose between realtime and batch. And track tokens, model the cost, and put a cache breakpoint where it actually hits.

ALEX: Two skills, close to ten percent of the exam, and every one of them is a parameter I half remember.

SAM: Then we start with an item. [sting]

## Cold open: the cache that never hits

SAM: A retail chain's support assistant sends the same eight thousand tokens of returns policy in its system prompt on every request. To cut cost, a developer puts a cache control breakpoint on the user message at the end of the request, and that message begins with the current timestamp. A week later, every response shows cache creation input tokens, and cache read input tokens is always zero. What should the developer change? Option A, switch the breakpoint to the one-hour cache lifetime. Option B, move the breakpoint to the last block of the system prompt, the end of the content that is identical on every request. Option C, call the token counting endpoint before each request to confirm the prompt meets the minimum cacheable length. Option D, shorten the policy text until the cost is acceptable.

ALEX: A. Support traffic is bursty. Entries expire after five minutes, so give them an hour.

SAM: Hold that. We come back to it at the end.

SAM: Why this matters. Claude A P I mechanics is six point eight percent of the exam, and cost and token management another two point eight. About five items. The guide lists messages, tools, streaming, vision, thinking, caching, third-party vendors, data access patterns, and realtime versus batch; then token tracking, cost modelling and cache checkpoints. [sting]

## Segment one: messages and tools

SAM: Segment one. A Messages call needs a model, max tokens, and a list of messages alternating between user and assistant. The system prompt is its own top-level field, not a message.

ALEX: And the A P I keeps the conversation for me?

SAM: No. The Messages A P I is stateless. Every request carries the full history you want Claude to see.

ALEX: That feels wasteful. Turn ten resends turns one to nine. I'd send only the new message and keep a session on the server.

SAM: The waste is real; the last segment deals with it. And managed agent harnesses do hold sessions for you.

SAM: But on the Messages A P I there is no session to lean on. Drop the history and Claude never sees it. The fix for the cost of resending is prompt caching, not trimming what Claude needs.

ALEX: So the tell?

SAM: "Claude forgot what the user said two turns ago." The application didn't send it.

SAM: Now the response. Its content is a list of blocks: text, tool use, thinking. Alongside it, a stop reason. End turn means Claude finished. Max tokens means it hit your ceiling, mid-answer. Stop sequence means one of your stop strings fired. Tool use means Claude wants you to run a tool. Pause turn means a server-side tool loop paused, and you send the content back to continue. Refusal means Claude declined.

ALEX: So when contract summaries end mid-sentence...

SAM: Read the stop reason before you touch the prompt. If it says max tokens, raise max tokens. Adding "keep it brief" is a polite request aimed at a ceiling you set yourself.

SAM: Tools. You pass a tools array. Each tool has a name, a description, and an input schema written in JSON Schema. When Claude calls one, the stop reason is tool use, and the response holds a tool use block with an I D, the tool's name and an input object. Your code runs it.

ALEX: Then I send the answer back.

SAM: As a new user message whose content starts with a tool result block carrying the same tool use I D. Results come first in that message; any text goes after them. If the tool failed, you still send a tool result, with the error text and is error set to true, so Claude can retry or explain.

ALEX: And forcing a tool?

SAM: Tool choice. Auto, the default, lets Claude decide. Any means it must use one of the tools. Tool means it must use the one you name. None means no tools. Those are client tools, run by your code. Server tools, such as web search, run on Anthropic's infrastructure and return results in the same response.

SAM: Two costs to remember. Tool definitions are input tokens on every request. And a point episode nine returns to: content a tool fetches from outside stays inside the tool result, treated as untrusted, never pasted into the system prompt. [sting]

## Segment two: streaming, vision and thinking

SAM: Segment two. Set stream to true and the response arrives as server-sent events. Message start first. Then, for each content block, a content block start, a run of content block deltas, and a content block stop. Then a message delta, carrying the stop reason and usage. Then message stop. Pings can appear anywhere, and an error event, such as overloaded, can arrive mid-stream.

ALEX: Text deltas I just print. What about a tool call?

SAM: Its input arrives as partial JSON strings. Accumulate them and parse once the block stops. Parse each fragment and your parser fails on half an object. The S D K helpers do the accumulation for you.

ALEX: I stream everything anyway. It makes the app faster.

SAM: It makes the app feel faster, and that matters: users see the first words in moments.

SAM: But the model generates, and bills, the same tokens. Streaming fixes perceived latency, and it keeps long requests alive: the S D Ks reject a non-streaming request expected to run past ten minutes, so large max tokens means streaming.

ALEX: Tell?

SAM: "Users stare at a blank screen" or "long outputs time out": stream. "Cut the cost": streaming is not the answer.

SAM: Vision. An image goes in as an image content block, from one of three sources: base sixty-four data inside the request, a U R L, or a file I D from the Files A P I. Formats are J peg, P N G, GIF and WebP. Put the image before your question. Large images are scaled down, and token cost grows with image size, so downsample when you don't need the detail. P D Fs go in as document blocks, and each page costs its text plus an image of the page.

SAM: Thinking. With thinking on, thinking blocks come before the text. Each carries a signature, an encrypted copy of the full reasoning. Thinking tokens are billed as output tokens and count toward max tokens, even when you see only a summary, or nothing.

ALEX: And the modes?

SAM: Adaptive thinking lets Claude decide whether and how much to think, with an effort setting for depth. Manual extended thinking sets budget tokens, at least one thousand and twenty-four and below max tokens, on the models that support it. Episode five covers choosing. Today is the plumbing.

SAM: Pause here and answer before we go on. A field-service company's agent uses thinking and tools. To cut input tokens, a developer's code deletes the thinking blocks from each assistant message before sending the tool results back. Since then, the agent's multi-step reasoning has degraded. What is the best fix? A, pass the thinking blocks back complete and unmodified, alongside the tool use blocks they came with. B, raise the effort level so Claude rebuilds its reasoning from the tool results. C, copy the thinking text into a text block so the reasoning stays in context. D, turn thinking off for every request that carries tool results. [pause]

ALEX: D. Thinking earns its keep on the first decision. A tool result turn is just reading data. Turn it off there and you save output tokens too.

SAM: That's the blunt cut. When you return a tool result, Claude is continuing the same response, so its earlier reasoning has to be there. The answer is A. Within a tool use turn, thinking blocks go back complete and unmodified. C edits the block, and the A P I rebuilds the reasoning from the signature, not from your copy. B pays for more thinking to replace thinking you threw away.

ALEX: And the token saving the developer wanted?

SAM: Not by editing blocks. Pass every thinking block back; depending on the model, the A P I either drops thinking from earlier turns or keeps it in context, and you are billed for what Claude is actually shown. [sting]

## Segment three: data in, and where you call from

SAM: Segment three, data access patterns. Data reaches Claude four ways. Inline: text, or base sixty-four images and P D Fs inside the request. By reference: a U R L, or a file I D from the Files A P I, uploaded once and referenced many times. On demand: a tool, whether your own tool querying your database, a server tool such as web fetch, or the M C P connector to a remote M C P server. And history, which you resend every turn.

ALEX: Why bother with the Files A P I?

SAM: Because history is resent. A base sixty-four scan in turn one rides along in every later request. A file I D keeps the payload under the thirty-two megabyte request limit. One caution: uploaded files are visible to the whole workspace, not to one end user, so a file I D is not access control.

ALEX: Here's my shortcut. Context windows are huge now. I'd paste the whole product catalogue into every request. No tool code, no retrieval.

SAM: For a fixed document Claude needs on every call, putting it in context and caching it is exactly right.

SAM: But catalogue prices change during the day. A pasted snapshot is stale once it's sent, and you pay for all of it on every request. A tool fetches the current price for the one product being asked about.

ALEX: So the tells.

SAM: "Current", "live", "changes hourly": a tool. "The same large document on every request": context plus caching. "The same file across many turns": the Files A P I.

SAM: Now third-party vendors. Claude also runs on Amazon Bedrock, Google Cloud's Vertex A I, and Microsoft Foundry. Teams choose them to keep data inside their cloud's security boundary, to authenticate with cloud identity, such as A W S I A M roles, instead of an Anthropic A P I key, and to bill through an existing cloud agreement.

ALEX: Same A P I?

SAM: Close, and the S D Ks support each. But model I Ds follow each platform's format, and features arrive at different times. The documentation lists images on Bedrock and Google Cloud as base sixty-four only, and lists the Files A P I and Anthropic's Message Batches endpoint as unsupported there. Check the platform's feature list before you design around a feature.

SAM: Pause here and answer before we go on. Choose two. A healthcare company moves its document-intake service from the first-party Claude A P I to Amazon Bedrock, so that patient data stays inside its A W S account. After the switch, requests that reference scanned forms by U R L fail, and the service's Anthropic A P I key is rejected. Which two changes fit? A, authenticate with A W S credentials through I A M instead of the Anthropic A P I key. B, send the scanned forms as base sixty-four image data instead of U R L sources. C, route the image requests back through the first-party A P I and keep the rest on Bedrock. D, rewrite the prompts, because Bedrock needs a different prompt format. E, raise max tokens so the image tokens fit. [pause]

ALEX: A and B.

SAM: Both. A matches how Bedrock authenticates. B matches the source types Bedrock accepts. C breaks the constraint the stem gave you: the data stays in the A W S account. D invents a problem. E answers a token ceiling nothing here hit. [sting]

## Segment four: realtime or batch

SAM: Segment four. The Message Batches A P I takes up to a hundred thousand requests, or two hundred and fifty-six megabytes, whichever comes first. Each request has a custom I D and the usual Messages parameters. Most batches finish within an hour. Results are ready when every request is done, or after twenty-four hours, and anything not processed by then expires. Input and output cost half the standard price. Results stay downloadable for twenty-nine days.

ALEX: And what comes back?

SAM: One result per request, of four types: succeeded, errored, canceled or expired. You aren't billed for the last three. Results can arrive in any order, so you match them on custom I D. Batch requests can't stream. And parameters are validated asynchronously, so a malformed request only shows up when the whole batch ends. Test one request shape against the Messages A P I first.

ALEX: A retailer needs descriptions for forty thousand new products by next week. I'd fan out parallel calls from async code. Done in minutes, no polling.

SAM: Async fan-out is the right tool when a user is waiting on many calls at once.

SAM: Here nobody is waiting. Synchronous calls pay full price, and the fan-out runs into rate limits: requests, input tokens and output tokens per minute, each enforced with a four twenty-nine error. Batch halves the bill and absorbs the volume.

ALEX: The tell.

SAM: "Overnight", "by morning", "not urgent", "cost is the priority": batch.

ALEX: Then I'd batch everything. Half price is half price.

SAM: Not the chat assistant. A customer can't wait an hour for a reply. "While the customer waits", "in the app", "within seconds": realtime, streamed if the answer is long.

SAM: Caching stacks with the batch discount, best effort. Batches can outlast five minutes, so shared context in a batch does better on the one-hour lifetime.

SAM: Pause here and answer before we go on. A public-sector team batch-processes twenty thousand benefit applications each night. Their code writes each result to the database in the order the results were downloaded, assuming it matches submission order. Auditors find summaries attached to the wrong applications. What fixes it? A, set each request's custom I D to the application's I D, and match every result on it. B, submit smaller batches so that order is preserved. C, sort the results by completion time before writing them. D, switch to synchronous calls so each response returns to the code that sent it. [pause]

ALEX: A.

SAM: A. Results come back in any order; the custom I D is how you join them. B and C still rely on an order nobody promised. D works, but it gives up the half-price discount a nightly job was built for. [sting]

## Segment five: counting tokens and caching

SAM: Segment five, cost. Every response has a usage block: input tokens and output tokens, plus, with caching, cache creation input tokens and cache read input tokens.

ALEX: Input tokens is my input.

SAM: Only the part after your last cache breakpoint. Total input is all three input fields added together. Read input tokens alone and a cached request looks almost free.

SAM: Before you send, the token counting endpoint takes the same inputs as a Messages call and returns an estimate. It's free, with its own rate limit.

ALEX: And the cost model?

SAM: Tokens times the price per million. On current models, output costs about five times input. With caching, a five-minute cache write costs one and a quarter times base input, a one-hour write twice base input, and a cache read about a tenth on most models. Batch halves all of it, and the discounts stack. Count the hidden tokens too: tool definitions, thinking billed as output, images, and resent history.

SAM: Now the mechanism. A cache control field on a block marks a breakpoint. The cache covers the prefix in a fixed order, tools, then system, then messages, up to and including that block. You get up to four breakpoints. A write happens only at a breakpoint, and on later requests the A P I looks back up to twenty blocks for an earlier write.

ALEX: How long does an entry live?

SAM: Five minutes by default, refreshed free each time it's read. A one-hour lifetime is available. Each model has a minimum cacheable length, often between one and four thousand tokens. Below it, nothing is cached and there is no error: both cache fields simply read zero.

ALEX: What breaks a hit?

SAM: Any change before the breakpoint. Edit a tool definition and every level is invalidated. Edit the system prompt and system and messages go. Change tool choice, add or remove an image, or change the thinking settings, and the message cache goes. And an entry only exists once the first response begins, so for a fan-out, send one request first, then the rest.

SAM: Checkpointing is the design side. Give parts that change at different rates their own breakpoints: tools, instructions, today's retrieved documents, the conversation. A document refresh then rewrites only from the documents onward. In a long agent conversation, if one turn adds twenty or more blocks, the lookback misses the last write, so place a second breakpoint earlier.

ALEX: I'd put everything on the one-hour lifetime and stop thinking about expiry.

SAM: Simpler, and sometimes right.

SAM: But a one-hour write costs twice base input instead of one and a quarter. If traffic reads the prefix every few minutes, the five-minute cache refreshes for free on every hit. The tell for one hour is a gap longer than five minutes but under an hour: a user who replies slowly, a long side task, a batch.

SAM: Pause here and answer before we go on. For each statement, say true or false. A retail chatbot caches its tools and system prompt. One: on a cache hit, input tokens in the usage block counts everything Claude read. Two: if the cached prefix is shorter than the model's minimum, the A P I returns an error. Three: editing one tool's description also invalidates the cached system prompt and messages. Four: on most models, cache reads don't count toward the input-tokens-per-minute rate limit. [pause]

ALEX: False, false, true, true.

SAM: All four. One is false: input tokens is only what follows the last breakpoint. Two is false: it's silently uncached, with both cache fields at zero. Three is true: tools sit at the front of the prefix, so everything after them goes. Four is true, which is why caching raises effective throughput as well as cutting cost. [sting]

## Cold open: the verdict

SAM: Back to the cold open. Alex, you picked A, the one-hour lifetime.

ALEX: And now I can see it. The timestamp changes on every request, so the hash at the breakpoint never matches.

SAM: So the answer is B: move the breakpoint to the last block that is identical across requests, the end of the system prompt. A treats a hashing problem as an expiry problem; a one-hour write costs twice base input and still never hits. C checks something the usage already answered: cache creation tokens mean the prefix was long enough to cache. D cuts content the assistant needs.

ALEX: And the clue in the stem?

SAM: Creation on every request, reads always zero, and a breakpoint on something that changes. Put the breakpoint at the end of what stays the same. [sting]

## Five to remember

SAM: Five to remember. One: the Messages A P I is stateless; you send the history. Read the stop reason before you touch the prompt. Max tokens means raise the ceiling.

ALEX: Two: answer a tool use block with a tool result carrying the same I D, first in the next user message, with is error for failures. Thinking blocks go back complete and unmodified.

SAM: Three: streaming fixes perceived latency and long-request timeouts, not cost. Tool input streams as partial JSON; parse when the block stops.

ALEX: Four: live data, a tool. The same big document, context plus caching. The same file over many turns, the Files A P I. Data that must stay in your cloud, that cloud's platform, after checking its feature list.

SAM: Five: batch is half price, up to twenty-four hours, matched on custom I D. Cache from the front, tools, system, messages, with the breakpoint on the last stable block; input tokens is only what follows it.

## Recap: the exam tells

SAM: Recall first. Pause and name the five segments. [pause]

ALEX: Messages and tools; streaming, vision and thinking; data access and cloud platforms; realtime or batch; tokens and caching.

SAM: Now as exam tells. If answers end mid-sentence, check for a max tokens stop reason before editing the prompt. If a tool fails, send a tool result with is error set to true.

ALEX: If users stare at a blank screen, stream. If an agent's reasoning degraded after someone trimmed tokens, look for stripped thinking blocks.

SAM: If data changes during the day, give Claude a tool. If the same file rides along every turn, upload it once. If data must stay in the cloud account, use that cloud's platform, cloud credentials, and base sixty-four images.

ALEX: If the stem says overnight and cost first, batch, joined on custom I D. If a customer is waiting, realtime.

SAM: If cache reads sit at zero, look for a breakpoint on content that changes. If gaps run past five minutes, one hour. If input tokens looks tiny, add the cache fields.

ALEX: Next, episode two: software engineering for Claude applications.
