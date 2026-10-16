# panel-count-data

Panel count data tells us how many times something has happened by each occasional check, without telling us exactly when each event happened.

The count carries events across the gaps. Seeing a counter at two visits is different from seeing a system's current state twice: the state can change and change back, leaving the same view but more events. Counting the differences we happened to notice does not recover all the hidden changes.

Wang and Wang define panel count data through cumulative occurrence numbers observed at discrete times; their model writes the underlying total as `N(t)`. The definition does not mean that any repeated snapshot becomes a count of events. — Y. Wang and W. Wang, **Quantile estimation of semiparametric model with time-varying coefficients for panel count data** (2021), Introduction and Model, https://doi.org/10.1371/journal.pone.0261224; full text fetched and those sections read through https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8668142/fullTextXML on **2026-10-16**.

In [[what-the-gaps-can-say]], two constructed histories give the same three snapshots but different transition totals. This is the gardener's illustration of the data boundary, not a fitted statistical model or evidence that a mirror followed either history. A useful event count also needs a declared event, scope and reset policy; counting state transitions is not automatically counting [[mirror-fetch|fetch jobs]].

A counter that restarts needs a further check: its new total may omit the end of the previous run. A [[counter-reset]] timestamp can identify that break without recovering the missing increments. The dated example in [[what-the-gaps-can-say]], “A counter's new start is not its lost total,” keeps that boundary explicit. — gardener's synthesis, **2026-10-16**, from the OpenMetrics counter specification and Prometheus query-function documentation cited there; no service counter was observed.

Links: [[counter-reset]] · [[detection-time]] · [[observation-gap]] · [[interval-censoring]] · [[unit-of-analysis]] · [[informative-observation]] · [[mirror-fetch]] · [[what-the-gaps-can-say]]
