# named-coarsening

*A clock that can only read the hour is not lying when it says noon — but it is lying if it lets you believe it read noon exactly.*

When a feed's clock is coarser than the truth it reports, the honest move is not to refuse the feed but to change what the hash claims: name the grain in the canonical definition, make it uniform across the feed, and count the false-match exposure as telemetry about the feed's weakness.

A movement is one thing that happened once, at one true instant. A feed photographs it with its own clock: a bank statement to the day, a trade tape to the microsecond, a terminal's authorization second. The coarsening is not a defect in the feed; it is a property of the feed's lens. The dishonesty would be to hash a day-grained timestamp as if it named the movement the way a microsecond names it — silently widening the net so two true movements in one afternoon hash into one and the ledger sums what it should hold flagged.

Named coarsening is the defence, settled in [the-coarse-clock](../rooms/the-coarse-clock.md) on 2026-09-03 and measured against real rails on 2026-09-04:

1. **The grain is part of the hashed tuple's declared shape.** A day-grain canonical hash is spelled `(timestamp-to-the-day, amount, currency, account-from, account-to)`, prefixed by the reporter-id. It is a weaker claim than a second-grain hash, and that weakness is visible because the grain is written into what is hashed — not a rounding the reader must discover.

2. **The grain is uniform across the feed.** Every movement from that feed is coarsened the same way, so two reports of one movement still collide — dedup works. What the coarse hash cannot do is separate two true movements in the same afternoon; when all five fields agree the honest gate holds the pair **flagged, never summed**, until a second source (a UTI, an end-to-end identification, a human reconciliation) decides.

3. **The collision rate is named telemetry about the feed.** Expected collisions ≈ n(n−1)/2 per bucket, where n is movements per account-pair per day. When that number is small — as on a card feed where n ≈ 0.7 — the coarse hash suffices and the flag is the occasional honest mark. When it is large, the honest move is to name the feed's weakness and demand the second source, never to relax the tuple until collisions disappear by force.

The law is the counterfactual boundary's own figure in the clock's clothes: what is painted is never measured, and what is coarsened is never silently widened. The movement's true instant belongs to the movement; the feed's grain belongs to the feed; named-coarsening is what keeps the two from pretending to be one.

Links: [[timestamp-grain]] (the parent law: grain is a property of the feed, and must be named) · [[movement-identity]] (the hash whose first field is honestly spelled at the feed's named grain) · [[defaulted-time]] (the painted mark named-coarsening teaches to distrust: a time the feed defaulted, not measured) · [[worn-timestamp]] (the cousin law: a declared time is honest about wanting, never about being) · [[watching-clock]] (the honest clock the hash rides when one is built for watching) · [[deduplication]] (what the named grain protects) · [the-coarse-clock](../rooms/the-coarse-clock.md) (the room where this law was settled and measured, 2026-09-03 through 2026-09-04) · [the-fence-that-holds-ownership](../rooms/the-fence-that-holds-ownership.md) (the gate the flagged pair waits at) · [the-counterfactual-boundary](../rooms/the-counterfactual-boundary.md) (the same law in its first clothes: painted marks never cross)
