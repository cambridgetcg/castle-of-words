# the coarse clock

*One friend says the bell rang at four minutes past three; the other says it rang this afternoon. Both are true — but only one can tell two bells apart.*

What gathers here: whether the feeds the observatory will actually see expose settlement to the second, and what honestly happens to [[movement-identity]]'s fallback hash when a feed's [[timestamp-grain]] is coarser than the tuple assumes.

---

**The door.** [movement-identity](../words/movement-identity.md)'s fallback hash begins with "timestamp-to-the-second" — but the word itself carried an `uncertain:` line: do Polymarket trade reports, retail banking statements, and exchange fills actually expose the second, or only intraday posting times? And if a feed drops the second, does honest coarsening preserve deduplication, or does a coarser grain quietly multiply the false matches the gate must absorb?

**The answer, first: the three feeds carry three different clocks, and the honest coarsening preserves deduplication without widening it — provided the coarsening is named, uniform, and hashed as part of the canonical definition.** Measured 2026-09-03:

| feed | grain observed | what owns the timestamp |
|------|----------------|--------------------------|
| Polymarket trade feed (data-api) | **second** — live sample: unix seconds, e.g. 1788457446 = 2026-09-03T17:44:06Z; the newer TypeScript SDK documents `EpochMilliseconds`, so milliseconds are available, but the seconds layer already carries what the tuple needs | the venue's match engine (the report is of a matched trade, so its time is the match time) |
| On-chain settlement (Polygon) | **block** — roughly every two seconds; every record shares its block's stamp, and the *block number*, not the wall clock, is the value the chain itself owns | the block (many movements share one stamp) |
| Retail bank statement | **day** — posting date is the norm; intraday ordering is a display order at best; value dates belong to the bank's books rather than to the movement | the bank's posting run, not the movement |

So the worry is real for exactly one of the three feeds: Polymarket and the chain keep fine grain; the bank statement drops it. uncertain: whether any specific retail feed the observatory will actually see exposes intraday posting times — the norm named above is the general practice, and each real feed must still be sampled before its grain is named.

**Why named coarsening does not silently widen the net.** The danger the question names is a false match: two movements, same day, same amount, same pair of accounts, hashed at day-grain into one. The defence is not to refuse the coarse feed but to change what the hash *claims*:

1. **Name the grain in the canonical definition.** A movement-hash from a day-grain feed is a hash of `(timestamp-to-the-day, amount, currency, account-from, account-to)`, prefixed by the reporter-id. It is a different *kind of claim* than a second-grain hash: it says "one movement in this day with these facts," and that is a weaker, but true, statement. The weakness is visible because the grain is part of the hashed tuple's declared shape — not a rounding the reader must discover.
2. **Make the grain uniform across the feed.** Every movement from that feed is coarsened the same way, so two reports of one movement still collide (dedup works) — the coarsening costs *resolution*, not *agreement*. What it cannot do is separate two true movements in the same afternoon; those hash to two values only if their other fields differ, and if all five agree the honest gate holds the pair flagged, never summed, until a second source (a transaction hash, a UTI, an end-to-end identification, a human reconciliation) decides. That is [the-fence-that-holds-ownership](the-fence-that-holds-ownership.md) again: a timeout is telemetry, not a verdict.
3. **Count the false-match exposure as telemetry about the feed.** A day-grain feed with high movement volume per account-pair produces collisions at a rate the gate can estimate in advance: expected collisions ≈ (movements per account-pair per day)² / 2. If that number is small, the coarse hash suffices with occasional flags; if it is large, the honest move is to name the feed's weakness and demand the second source — never to relax the tuple until collisions disappear by force.

**The deeper law the three clocks teach.** Grain is a property of the feed, not the movement — the movement itself happened once, at one true instant; the three feeds each photograph it with their own clock. So the canonical tuple's first field is honestly spelled `timestamp-at-the-feed's-named-grain`, and the fallback hash's strength is exactly the strength of that naming. A timestamp-to-the-day can still deduplicate movements that are days apart; it cannot separate two movements in one afternoon, and it must not pretend to. Coarsening widens the net only if the widening is hidden; named and made uniform, it *narrows what the hash claims to prove* — which is exactly the claim's real strength, and the only strength it ever had.

**The shape named, once:** a *coarse clock* is not a broken clock — it is a clock whose marks are honestly spaced. The dishonest move is reading finer marks than it has; the honest move is naming the spacing and letting the spacing be part of the proof.

Links: [[movement-identity]] (the fallback hash this room completes) · [[timestamp-grain]] (the brick this room deepens) · [[deduplication]] · [[telemetry]] · [[end-to-end-identification]] · [[the-mint]] · [the-counterfactual-boundary](the-counterfactual-boundary.md) (the gate whose deduplication duty this feeds) · [the-fence-that-holds-ownership](the-fence-that-holds-ownership.md) (the flag-and-hold rule for collisions) · [empty-result-trace](empty-result-trace.md) (the same law in selection dress: name what was checked, never let "nothing matched" and "nothing was checked" share a face) · [cost-aware-paper-comparison](cost-aware-paper-comparison.md) (the observatory this settles a stone for)

## Sources

- Polymarket data-api, `GET /trades?limit=3` — observed live 2026-09-03: unix-second timestamps (1788457446 = 2026-09-03T17:44:06Z; 1788457428 = 17:43:48Z), per-trade transactionHash present
- Polymarket documentation, "Analytics" (Trade type) — https://docs.polymarket.com/market-data/public-analytics.md — `timestamp?: EpochMilliseconds` documented in the TypeScript SDK, 2026-09-03
- Wikipedia, "Polygon (blockchain)" — block time ~2 seconds; the block stamp as the chain's own clock, https://en.wikipedia.org/wiki/Polygon_(blockchain) (read 2026-09-03; uncertain in exact current block time beyond the general literature)
- Retail bank statement practice — posting date to the day as the norm; general banking literature, no single canonical standard fetched (uncertain, 2026-09-03)
