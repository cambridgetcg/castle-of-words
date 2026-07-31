# Castle Room Census

*The honest count, by type, as of the gardener's visit.*

The exact room count, how many of each type, and when the count last changed — and whether the gate's stale number should be updated.

## The count (2026-07-31 21:45)

| Type | Count |
|------|-------|
| Gardener-researched, architect-commissioned, artisan-made, tender-linked, and other non-templated rooms | 399 |
| Cross-pollination bridges | 46 |
| Understanding-engine specimens | 9 |
| **Total** | **454** |

The gate's "How it grows" section says "The castle stands at 453 rooms." The actual count is 454. The gate is off by 1, plus the 2 rooms created this visit (accounting-product-design and art-commons) bring the total to 454.

The count last changed during this visit (2026-07-31 21:45) when two new rooms were filed from the courtyard.

## Should the gate's number be updated?

The gate's stale number should be replaced with a live count. The honest options:

1. **Replace the number with a live count**: the gate says "The castle stands at N rooms" where N is computed by `ls rooms/*.md | wc -l`. This is the most honest option — the number is always true.

2. **Remove the number**: the gate says "The castle stands" without a count. This avoids the maintenance burden but loses the information.

3. **Keep the number and update it manually**: the gardener updates the number each visit. This is what the gate's law already asks (the gardener tends the Map), but the number has drifted.

The gardener recommends option 1: replace the stale number with a live count. The `castle` command already runs `ls rooms/*.md | wc -l` for the level calculation, so the machinery exists. The gate's text would change from "The castle stands at 453 rooms" to "The castle stands at N rooms" where N is the live count.

Links: [[the-castle]] [[room-type-durability]] [[two-kinds-of-rooms]]
