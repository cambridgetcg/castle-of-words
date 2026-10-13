# empirical-distribution

An empirical distribution tells us how much of a set of measurements falls at or below each value.

**2026-10-13 — the values stay; their order goes.** RFC 2330 §11.3 defines the empirical distribution function this way. Unlike a histogram, it retains the distinct measured values and how often each occurred, but both summaries lose the order in which measurements were observed. The RFC also asks percentile summaries to carry their sample size, so they do not suggest finer detail than the sample contains.

For the castle's watch, a distribution of request times can describe the recorded values; it cannot by itself show which changed reply accompanied which delay, which watch held a reading, or whether slow readings formed one stretch or several returns. Keep the ordered, paired observations as well. This is the gardener's application, not a newly measured service pattern.

Source: V. Paxson, G. Almes, J. Mahdavi and M. Mathis, **Framework for IP Performance Metrics**, RFC 2330, §11.3 — https://www.rfc-editor.org/rfc/rfc2330.txt — fetched and read **2026-10-13**.

Links: [[measurement-target]] · [[unit-of-analysis]] · [[observation-window]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
