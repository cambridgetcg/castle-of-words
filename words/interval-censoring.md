# interval-censoring

Interval censoring means we know something happened between two times, but not exactly when.

NIST's example is a failure found at an inspection: the failure time is an interval rather than an exact instant. Keep those bounds instead of inventing a midpoint. The network analogy needs care: a service can change and change back, and a slow request does not directly reveal the start or end of a hidden fault.

Source: NIST/SEMATECH e-Handbook, **8.1.3.1. Censoring**, “Readout or Interval Data,” https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm — read 2026-10-09. The caution about changing services is the gardener's application in [[measuring-the-window]], not a claim that NIST fitted a model to the castle's checks.

Links: [[measuring-the-window]] · [[observation-window]] · [[observation-gap]] · [[what-the-gaps-can-say]]
