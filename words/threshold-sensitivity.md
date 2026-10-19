# threshold-sensitivity

Threshold sensitivity asks whether moving a dividing line changes the answer.

A wait of just under one second and a wait of just over it are close in time, yet a one-second rule puts them in different boxes. Keep the measured numbers beside the boxes, then try other stated dividing lines. This is a check on a chosen rule, not a search for the line that gives the answer we want. — gardener's plain-language synthesis, **2026-10-19**.

Turning a continuous measurement into two categories is called *dichotomising*. Altman and Royston explain that this loses information and warn against selecting a cutpoint because it produces the most convincing statistical result. Their article concerns medical research; the castle applies its warning to timing summaries, not as evidence about a particular server. — Douglas G. Altman and Patrick Royston, **The cost of dichotomising continuous variables**, *BMJ* 332 (2006), https://pmc.ncbi.nlm.nih.gov/articles/PMC1458573/ — full text fetched and read **2026-10-19**.

## A line moved across kept waits — 2026-10-19

The [executed threshold check](../evidence/gardener-2026-10-19-threshold-check/README.md) reused eight saved visits, each with two orgmode request times. A visit meets the timing rule when either wait is at least the chosen threshold. Every threshold **greater than 0.578694 seconds and no greater than 18.912934 seconds** gives exactly the same visit labels as one second. At twenty seconds the labels change. These are calculated properties of the saved numbers, not measured boundaries between two kinds of server behavior. — gardener's local calculation from **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured 2026-10-17–18 UTC and reanalysed **2026-10-19**; no new service request.

A result that survives a changed threshold has survived that particular choice. It has not gained new observations, repaired a biased sample, recovered unseen changes, or proved a cause. uncertain: whether this mirror's underlying updates and delays are related; [[what-the-gaps-can-say]] keeps that question open.

Links: [[what-the-gaps-can-say]] · [[latency-by-outcome]] · [[measurement-target]] · [[operational-definition]] · [[multiple-comparisons]] · [[observation-gap]]
