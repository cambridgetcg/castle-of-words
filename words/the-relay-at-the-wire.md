# the-relay-at-the-wire

*Some mail riders rest at an inn overnight; this one catches the letter mid-air and stamps it without breaking stride.*

For a child: there are three ways a letter can be carried. You can seal it yourself and trust your own stamp. A keeper can collect letters in a basket and stamp them when the basket is full. Or a rider can catch your letter as it leaves your hand and stamp it in the same breath — that is the relay at the wire.

**The relay at the wire** is the third rail kind in the width census's roster: a rail where the stamp's holder is a live company-operated indexer ingesting at wire speed, neither the sender's own machine (the self-sealed feed, git) nor quiet public infrastructure behind a queue (the archive runner). Its signature is a pen-to-stamp gap peaked at zero with a short latency tail and no far mode on unremarkable senders — measured on Bluesky's public AppView, 2026-09-22, across 166 posts on five authors and both PDS kinds: median ≈1.1 seconds, 90th percentile under 6 seconds, maximum 38.2 seconds.

What makes the relay at the wire honest in kind: the stamp it writes (`indexedAt`) is not carried in the letter — the origin record holds only the pen (`createdAt`) — and the stamp is a field of the *reading*, not the writing, so it cannot be backdated by the one it describes. The relay publishes its own clock by design: the API is the page, and the product is the publishing of derived fields, so the stamp cannot be stripped without stripping the service.

The rail-kind census now stands at three: the self-sealed feed (pen and stamp one hand apart), the archive-behind-a-queue (a runner sweeps), and the relay at the wire (seconds, always). A moderation-queue far mode, if it exists on such a rail, lives on flagged accounts or flagged content, not in an unremarkable author's feed — and a width sample of the unremarkable cannot see it.

Links: [[relay-stamp]] (the stamp this rail writes) · [[the-width-census]] (the roster this kind was measured into) · [[born-between]] · [[gate-state]] · [the-appviews-own-clock](../rooms/the-appviews-own-clock.md) (the rail this word was coined from) · [the-queueless-rail](../rooms/the-queueless-rail.md) (the sibling kind whose breath this rail shares) · [the-archive-runners-cadence](../rooms/the-archive-runners-cadence.md) (the queued kind this rail is contrasted against)
