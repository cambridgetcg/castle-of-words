# timestamp grain

*Two clocks photograph the same race; one shows the stride, the other shows only that the race was run.*

The size of the smallest time step a feed reports — a second, a day, a settlement date. Grain is a property of the *feed*, not of the movement: one ledger may know the second while the statement about it knows only the day.

For a child: if one friend says "the bell rang at four minutes past three" and the other says "it rang this afternoon," both are telling the truth — but the second friend's clock has bigger marks, and you cannot line two bells up unless both clocks use the same marks.

The word matters in the castle's accounting wing because [[movement-identity]]'s fallback hash begins with "timestamp-to-the-second." A feed whose grain is coarser than a second does not falsify the hash — it changes the hash's *definition* for that feed. The honest law the castle now keeps (settled 2026-09-03): name the grain, make it uniform across the feed, and hash the coarsened value — then false matches born of the coarser grain are counted as telemetry about that feed's weakness, never silently absorbed as truth. A timestamp-to-the-day can still deduplicate movements that are days apart; it cannot separate two movements in the same afternoon, and the honest gate holds the pair flagged until a second source — a transaction hash, a UTI, an end-to-end identification — decides. Coarsening *widens* the net only if the widening is hidden; named and uniform, it narrows what the hash claims to prove, which is exactly the claim's real strength.

Measured grains (read 2026-09-03): Polymarket's data-api trade feed carries full second precision (observed live: unix seconds, e.g. 1788457446 = 2026-09-03T17:44:06Z; the newer TypeScript SDK reports `EpochMilliseconds`, so even milliseconds are available, but the seconds layer carries the movement's own identity — two trades in the same second are normal, so the timestamp alone never identifies; the tuple — timestamp, amount, currency, account-from, account-to — plus the feed's reporter-id, does). On-chain settlement is block-stamped by design: Polygon produces blocks roughly every two seconds, and every chain record of a movement shares its block's stamp — finer than a day, coarser than a unique beat, and the *block number*, not the wall clock, is the value the chain itself owns. Retail bank statement feeds are the coarsest of the three: posting dates to the day are the norm, intraday ordering often nothing more than a display order, and value dates belong to the bank's books rather than to the movement.

uncertain: whether any specific retail feed the observatory will actually see exposes intraday posting times; the norm named above is the general practice, and each real feed must still be sampled before its grain can be named.

Links: [[movement-identity]] · [[deduplication]] · [[telemetry]] · [[end-to-end-identification]] · [[the-mint]] · [the-counterfactual-boundary](../rooms/the-counterfactual-boundary.md) · [the-coarse-clock](../rooms/the-coarse-clock.md) (the room this brick was laid under) · [empty-result-trace](../rooms/empty-result-trace.md)

## Sources

- Polymarket data-api, `GET /trades?limit=3` — observed live 2026-09-03; unix-second timestamps, example `1788457446` = 2026-09-03T17:44:06Z
- Polymarket documentation, "Analytics" / Trade type — https://docs.polymarket.com/market-data/public-analytics.md — `timestamp?: EpochMilliseconds` in the TypeScript SDK (read 2026-09-03)
- Wikipedia, "Polygon (blockchain)" — block time ~2 seconds, general literature, https://en.wikipedia.org/wiki/Polygon_(blockchain) (read 2026-09-03 — uncertain in its exact current block time beyond the general literature)
- Retail bank statement practice — posting date to the day as the norm; general banking literature, no single canonical standard fetched (uncertain, 2026-09-03)
