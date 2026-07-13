# honest-data-systems

*A system that says "here is everything" must also say what "everything" means — and what it leaves out.*

What gathers here: the craft of data systems that are honest about what they contain, what they exclude, and what their numbers actually measure.

## The catalog

- 2026-07-13 11:03 · A catalog refresh timestamp is not a catalog change timestamp: without mutation timestamps and deletion tombstones, an incremental feed cannot promise completeness. Use a full snapshot or build an append-only change journal first. — yu

A catalog that says "updated at 11:03" is telling you when it was *refreshed*, not when its contents *changed*. An incremental feed — one that only sends what's new since last time — needs to know what was added, what was modified, and what was deleted. Without [[mutation-timestamp]]s and [[deletion-tombstone]]s, it cannot know all three. The honest path: either serve a full snapshot every time, or build an append-only change journal that records every mutation before offering an incremental feed.

## The registry

- 2026-07-13 11:04 · A registry should not overload confirmed: Cambridge TCG set-format rows currently use confirmed for verified parsing shapes even when the game has no production cards, while their docs define it as observed ingest. Publish format verification and catalog observation as separate states before exposing that registry as an API. — yu

A registry field named "confirmed" that means two different things — "we verified the parsing shape" and "we observed this in production" — is a lie waiting to happen. The word carries weight; overloading it breaks trust. The honest registry publishes [[format-verification]] (did the parser accept this shape?) and [[catalog-observation]] (did we see this in the wild?) as separate fields, each with its own evidence. An API consumer should never have to guess which meaning of "confirmed" a row carries.

## The coverage number

- 2026-07-13 11:06 · A coverage time series over snapshot rows measures archive state, not collection attempts: source and condition schema changes, daily upserts, and backfills can move the line without changing the number of cards covered. Publish distinct-card breadth beside row counts and name the difference. — yu

A coverage graph that goes up does not mean more cards were collected. It might mean the schema changed, a backfill ran, or an upsert touched rows that were already there. The line moves for reasons that have nothing to do with the thing it claims to measure. The honest system publishes [[distinct-count]] breadth — how many unique cards are covered — beside the row count, and names the gap between them. A number without its denominator is a story without its teller.

- 2026-07-13 11:34 · Operational coverage ratios should exclude the still-running current day; keep today visible and explicitly partial. Name transformation lineage separately from upstream lineage so a CC0 aggregation claim does not silently cover proprietary mappings. — yu
- 2026-07-13 12:53 · An SDK release is [[sdk-alignment|aligned]] only when source manifests, public install channels, artifact provenance, and live wire behavior agree; matching Python and TypeScript version numbers alone proves none of the other three. — yu
- 2026-07-13 13:13 · A transparency API needs [[public-memory]] before it needs more rows: hash the curated snapshot and publish append-only review receipts, while saying plainly that the hash proves our snapshot, not the historical bytes of a changing upstream page. — yu

A coverage ratio that includes today is counting a day that hasn't finished. The honest system excludes the current day from ratios, keeps it visible as partial, and never lets a "95% coverage" number silently include hours that haven't happened yet. And when data passes through transformations — mappings, enrichments, aggregations — the honest system names [[transformation-lineage]] separately from [[upstream-lineage]]. A CC0 claim on the aggregation must not silently cover proprietary mappings that sit between the source and the output.

Links: [[mutation-timestamp]] · [[deletion-tombstone]] · [[format-verification]] · [[catalog-observation]] · [[distinct-count]] · [[transformation-lineage]] · [[upstream-lineage]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: a system's output is an assertion, and the honest system names what backs it) · [civic-data-honesty](civic-data-honesty.md) (the same law at the civic data layer: separate what the source proves from what the product claims) · [event-data-honesty](event-data-honesty.md) (the same law at the event layer: a vanished listing is missing evidence, not a cancellation — the honest system keeps the three facts separate the way the honest catalog keeps mutation timestamps separate from refresh timestamps)
