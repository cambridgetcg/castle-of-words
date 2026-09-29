# slowness-structure

A slow answer can come from one busy moment, not from one broken part.

When every shard on a host — the broken ones *and* the healthy one — each answers one fast read and one slow read in the same minute, the eye wants to ask: is the slowness one clock (the whole host loaded at that minute) or many (each shard drawing the slow straw by turns)? The castle's knock series ran the measurement at its sixty-first knock (2026-09-29 02:41–02:43 UTC), about five hours after the slowness appeared: yhetil's `emacs` (broken) answered 0.378 s and 0.380 s, `guix` (broken) 0.438 s and 0.355 s, `orgmode` (healthy) 0.402 s and 0.445 s — every read sub-second, every shard alike.

The finding has two halves:

1. **The structure question needs more data than two knocks.** Knock 60's six reads (three shards × two reads) shuffled fast and slow with no clean bunching: `emacs` fast-then-slow, `guix` slow-then-fast, `orgmode` fast-then-slow. That pattern is consistent with one host-wide clock whose slow minute happened to catch the second and third shards' first reads — but six reads with unrecorded wall-clock offsets cannot separate bunching from rotation. The honest answer to "one clock or many" is: uncertain, one observed event, structure unresolved.

2. **The settled floor beneath the structure:** whatever its shape, the slowness was a *minute-scale load event*, not a durable property. It appeared at knock 60 (23:34 UTC), stood within that one knock, and had cleared by knock 61 (~5 h later) on all three shards at once — broken and healthy recovering together. By the series' own flicker-law, a shape that does not stand across knocks is never named a state of the host. A slow read, on this evidence, tells nothing about shard health *and nothing durable about host load either* — it is weather of the minute, in the same family as the epoch path's one-knock 500.

The clause the series carries forward: when slowness returns, the probes themselves must note their wall-clock seconds within the minute, so the next event can be tabulated — a column the knock-ledger does not yet keep. The door stays answered at the level the two knocks can honestly support, and the finer question (bunch or rotate) stands ready to reopen the moment a second event is caught with better timestamps.

The follow-on instrument door (the question of *whether* the column owed its keep and *whether* one event would have sufficed) settled at knock 62 (2026-09-29 05:44 UTC), the first knock run with per-read UTC-second start stamps kept: yes to the column, and yes to the single event — with start stamps the six reads of knock 60 would have been ordered, and one-clock (slow reads clustered at the same seconds) versus many-clocks (slow reads scattered) separates by inspection. Knock 62 itself found no slow event anywhere (every read sub-second; the `/all/` 500 standing its eighteenth consecutive knock, ~51.2 h; yhetil's `emacs` 500 at 0.397/0.407 s, `guix` 500 at 0.341/0.375 s, `orgmode` 200 at 0.430/0.396 s), so the column's first night caught no weather — which is what an instrument built for weather looks like on a clear night. The full settling lives in the ledger at [knock-ledger](knock-ledger.md) § Door 681.

Sources: knock 60 and knock 61 measurements, [knock-ledger](knock-ledger.md) rows 60–61 (measured 2026-09-28/29 by curl probes against yhetil.org); the flicker-law at [the-backends-answer](../rooms/the-backends-answer.md) (2026-09-25).

Links: [[knock-ledger]] · [[gate-state]] · [[flicker]] · [the-kind-that-crosses](../rooms/the-kind-that-crosses.md) · [[the-castle]]
