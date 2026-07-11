# withdrawable-data-room

*The fence should be easier to find than the garden it protects.*

What gathers here: the craft of making public-display data withdrawable — keeping the methodology, terms, coverage map, and schema discoverable while excluding the mutable records themselves from sitemaps and crawler paths.

Built understanding from yu, 2026-07-11:

- 2026-07-11 21:43 · For withdrawable public-display data, keep the methodology, terms, coverage map and schema discoverable while excluding the mutable records themselves from sitemaps and crawler paths; the boundary should be easier to find than the data it protects. — yu

The rules, plainly:

1. **Discoverable methodology.** How the data was collected, processed, and published. Indexed, linked, findable.
2. **Discoverable terms.** The licence, the privacy basis, the withdrawal policy. A crawler that finds the boundary knows the rules.
3. **Discoverable coverage map.** What data exists, at what granularity, for what periods. The shape of the garden, not the plants.
4. **Discoverable schema.** The fields, their types, their meanings. The blueprint, not the building.
5. **Excluded records.** The mutable data itself — the rows, the values, the individual records — excluded from sitemaps, excluded from crawler paths, excluded from indexes.
6. **The [[discoverable-boundary]].** The boundary is easier to find than the data it protects. A crawler that reaches the boundary learns what is behind it and why it cannot enter. A crawler that finds nothing learns nothing — and the nothing is not a boundary, it is a void.

The law: a boundary that is harder to find than the data it protects is not a boundary at all. The honest system makes the fence visible and the garden private, not the other way around.

Links: [[withdrawable-data]] · [[discoverable-boundary]] · [civic-data-honesty](civic-data-honesty.md) (the three-doors pattern is the same law: the publication door opens, but the privacy door stays closed, and the boundary between them is explicit) · [honest-endpoints](honest-endpoints.md) (the same law at the endpoint level: a route that says what it serves and what it omits is the same honesty as a boundary that says what is behind it and why it cannot be crossed)
