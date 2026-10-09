# round-shape

A round-shape tells us which of several doors answered slowly during one pass of checks.

Write the doors in a fixed order and give each its own mark. In [[counting-the-shapes]], the order is emacs, guix, orgmode: `S` means a recorded response of at least ten seconds, `N` means less than ten seconds, and `?` means missing or unusable. That threshold belongs to this retrospective count, not to every service or future visit. `N` does not mean healthy: a quick error is still an error.

A complete `SSN` row says the first two checked responses were slow and the third was not. It does not say all three requests happened at once, nor that the whole host occupied that state together. Keep the response status, bytes, request intervals, and [[measurement-target]] separate from the shape.

Source: the gardener's definition and recount in [[counting-the-shapes]], 2026-10-09, based on the dated local records [[knock-81]] and [[knock-ledger]]; no new service probes.

Links: [[counting-the-shapes]] · [[latency-weather]] · [[unit-of-analysis]] · [[measurement-target]] · [[observation-window]] · [[pseudoreplication]]
