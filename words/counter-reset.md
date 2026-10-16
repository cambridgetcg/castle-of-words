# counter-reset

A counter reset starts a running total over, so its next number may no longer include what happened before the new start.

A counter can remember events across missed checks, but only within the part of its history it still carries. OpenMetrics permits a counter's total to reset to zero. Its `Created` timestamp is recommended, not required; when present, it must change to the reset time. Knowing that new start does not recover an unseen final total from the old run. — **OpenMetrics, a cloud-native, highly scalable metrics protocol**, “Counter,” pinned source revision `6c847344ff49fa6241a35e8b4f65bf098da5a161`, https://raw.githubusercontent.com/prometheus/OpenMetrics/6c847344ff49fa6241a35e8b4f65bf098da5a161/specification/OpenMetrics.md; fetched and read **2026-10-16**. The source identifies itself as an Internet-Draft, not an issued RFC.

Prometheus documents `resets()` for ordinary numeric samples as counting observed decreases. A reset can go unnoticed by that rule if the new total has already overtaken the old one before the next check. Its `increase()` adjusts detected breaks and extrapolates across the requested time range; the result can be fractional even when each event adds one. An estimated increase is not a recovered list of events. — **Query functions**, “resets” and “increase,” https://prometheus.io/docs/prometheus/latest/querying/functions/; fetched and read **2026-10-16**; the hidden-reset consequence is the gardener's deduction.

The checked illustration in [[what-the-gaps-can-say]] shows two histories with the same sampled totals and reset timestamp but different event counts. It is not evidence that either watched service exposes a counter or has reset one.

Links: [[panel-count-data]] · [[observation-gap]] · [[timestamp-provenance]] · [[identifiability]] · [[what-the-gaps-can-say]]
