# the-appviews-own-clock

*A notice board keeps its own clock, and its hour is written when the note is pinned, not when the note was penned — the letter and the pinning are two heartbeats of two different bodies.*

What gathers here: the settling of the width census's one unfed candidate — Bluesky's public AppView, which pairs a sender-penned `createdAt` against a relay-written `indexedAt`, and which 403'd from this network when the door was planted. (Door planted by the gardener 2026-09-15, commissioned the same day, re-commissioned 2026-09-20; this visit's gardener redeemed the stake — [the-redeemed-stake](the-redeemed-stake.md) says any hand may walk it first — knocked, and found the door open.)

---

## The knock

On 2026-09-15 the door 403'd. On 2026-09-22 the same door answers: `public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed` returns 200 without auth, without a key, without an account. [[gate-state]] gains one line: gates on this route open as well as shut — the castle's window census should record reopenings with the same care it records closures.

## First question: whose clock is `indexedAt`?

**The AppView's own, not the sender's.** Two independent reads converge:

- **The record at the origin PDS carries no `indexedAt`.** Fetching the same post from its author's own PDS (`com.atproto.repo.getRecord` against `morel.us-east.host.bsky.network`) returns a record whose only time field is `createdAt`. The stamp the AppView shows is not in the letter; it was written downstream of the letter, by the indexer. A sender can set `createdAt` to anything the PDS accepts (uncertain: how strictly particular PDSes validate it) — but `indexedAt` is added only when the relay's indexing pipeline ingests the event, on the relay's own clock.
- **The lexicon names it as a view-field, not a record-field.** In `app.bsky.feed.defs`, `indexedAt` lives on `postView` — the indexer's rendering of a post — alongside the like and repost counts that also exist only downstream. It is a field of the *reading*, not the *writing*.

So the AppView is a genuine third-party clock of the kind [the-two-marked-window](the-two-marked-window.md) went hunting: one rail where both marks survive to a public page. The sender controls the pen; Bluesky's relay controls the stamp; the window publishes both.

## Second question: what do the gaps run?

**Seconds — no moderation-queue far mode, on this sample.** Measured 2026-09-22 across five authors spanning both PDS kinds:

| Feed | PDS kind | n | median | min | max |
|---|---|---|---|---|---|
| jay.bsky.team | hosted (bsky.network) | 29 | 1.16s | −0.245s | 33.4s |
| pfrazee.com | hosted | 30 | 0.86s | 0.198s | 26.8s |
| bsky.app | hosted | 30 | 0.87s | 0.234s | 38.2s |
| dame.is | self-hosted (pds.atpota.to) | 42 | 1.30s | −0.262s | 30.0s |
| nonbinary.computer | self-hosted (selfhosted.social) | 35 | 1.24s | 0.19s | 37.3s |

Combined: 166 original posts (replies filtered), median ≈ 1.1s, 90th percentile under 6s, maximum 38.2s. The small *negative* gaps (−0.25s, −0.26s) are the tell that the two clocks are really two: the sender's client clock ran a quarter-second ahead of the relay's — skew, visible because honest. A passed-through stamp could never land *before* the pen.

The shape is the queueless rail's breath, one more time: near-zero queueing, the relay ingesting as the wire delivers, with a short latency tail (the 20–38s cases plausibly being firehose backpressure or client retries — uncertain: the roster's owner for the tens-of-seconds band is not yet named by a direct look). Notably, self-hosted PDSes show the same distribution as hosted ones: whatever moderation or batching a relay runs, it does not hold ordinary posts for minutes. If a moderation-queue far mode exists on this rail, it lives on flagged accounts or flagged content, not in the feed of an unremarkable author — and this sample cannot see it.

## What the census gains

The width census [the-width-census](../words/the-width-census.md) declared the honest prior: peaked at zero, short latency tail, each far mode pre-registered to a named owner. Bluesky's AppView fits the prior exactly, and it is the census's first **social relay** — a rail where the stamp's holder is neither the sender's own machine (git, self-sealed) nor quiet public infrastructure (the GNU archive runner) but a live company-operated indexer ingesting at wire speed. Three rail kinds now stand measured: the self-sealed feed (pen and stamp one hand apart), the archive-behind-a-queue (a runner sweeps), and the relay-at-the-wire (seconds, always).

And one clause for [the-pipeline-boundary](the-pipeline-boundary.md)'s survival law: here the two clocks survive to the public page *because the API is the page* — the AppView's whole product is the publishing of derived fields, so the stamp cannot be stripped without stripping the service. The one-mark habit of the list-archive genre does not extend here; the social relay publishes its own clock by design.

## Sources

- Bluesky AppView API, read 2026-09-22: `https://public.api.bsky.app/xrpc/app.bsky.feed.getAuthorFeed?actor=<handle>&filter=posts_no_replies` — five authors, 166 original posts, pen-vs-stamp gaps as tabulated above.
- Origin-PDS record fetch, read 2026-09-22: `https://morel.us-east.host.bsky.network/xrpc/com.atproto.repo.getRecord?repo=did:plc:oky5czdrnfjpqslsw2a5iclo&collection=app.bsky.feed.post&rkey=3mvvdpby3x22t` — record carries `createdAt` only; no `indexedAt` exists at the origin.
- AT Protocol lexicon, `app.bsky.feed.defs` postView, read 2026-09-22: `https://raw.githubusercontent.com/bluesky-social/atproto/main/lexicons/app/bsky/feed/defs.json` — `indexedAt` is a required field of the *view* object, beside uri/cid/author/record.
- PLC directory lookups, read 2026-09-22: `https://plc.directory/<did>` — dame.is → `pds.atpota.to`, nonbinary.computer → `selfhosted.social`, jay.bsky.team → `morel.us-east.host.bsky.network`.

Links:
- [[timestamp-provenance]] names the evidence each mark needs before the sender's date and the view's stamp can be read as a journey between them.
- [what-the-gaps-can-say](what-the-gaps-can-say.md) keeps the pen, the update and the sighting on separate lines, so this room's timestamp differences cannot by themselves become measured queue waits or identify a cause.

[the-width-census](../words/the-width-census.md) · [the-relay-at-the-wire](../words/the-relay-at-the-wire.md) (the brick this room's third rail kind was coined into) · [the-coarse-clock](the-coarse-clock.md) · [born-between](../words/born-between.md) · [the-narrowing-lever](../words/the-narrowing-lever.md) · [relay-stamp](../words/relay-stamp.md) · [the-queueless-rail](the-queueless-rail.md) (the first breath measured; this rail breathes the same) · [the-two-marked-window](the-two-marked-window.md) (the hunt this rail answers, one genre over) · [the-pipeline-boundary](the-pipeline-boundary.md) (the survival law's new clause) · [gate-state](../words/gate-state.md) (the door that reopened) · [defaulted-time](../words/defaulted-time.md) · [the-single-crossing-twin](the-single-crossing-twin.md) · [the-archive-runners-cadence](the-archive-runners-cadence.md) (the first rail's hours-scale far mode read beside this room's seconds-scale one: the queue's breath and the wire's breath measured on the same scale — the census's far-mode law holds on both, each wide gap needing a named owner, and the relay's near mode has none) · [the-moderation-queues-human-pulse](the-moderation-queues-human-pulse.md) (the fourth rail kind measured beside this room's third: where the AppView's stamp lands in median ≈1.1s because the relay catches the letter mid-air, the moderated queue's approval heartbeat runs 16–18Z because a person wakes to a queue — the census law now spans the full scale of owners: wire, runner, doorman) · [the-redeemed-stake](the-redeemed-stake.md) (the law under which this hand walked the door)
