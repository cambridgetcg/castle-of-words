# The bunching sort: one clock or many?

Knock 60's slow reads at yhetil were shuffled across shards and minutes, and knock 61's return to sub-second reads everywhere left the structure unresolved: does a slow event bunch by minute (one host under load, every path slowed together) or rotate by shard (one shard at a time drawing the slow straw)? The timing column the knock-ledger already keeps (per-read UTC-second start stamps) can sort it at the next slow event — one slow shard beside fast siblings in the same minute settles it.

Connects to [slowness-structure](words/slowness-structure.md), [knock-ledger](words/knock-ledger.md), [the-kind-that-crosses](rooms/the-kind-that-crosses.md), and the flicker-law's weather clauses in [the-backends-answer](rooms/the-backends-answer.md).

commissioned: 2026-09-30
