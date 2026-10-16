# detection-time

Detection time is when a check first notices something, which may be later than when it happened.

Two discoveries three hours apart do not mean two changes happened three hours apart. The checks have their own spacing; the changes may have happened anywhere the evidence permits inside the gaps. A request also takes time, so its start, finish, and the moment a reply was chosen should not be treated as one instant.

**Illustration, not a host measurement — 2026-10-15:** suppose checks at hours 0, 3 and 6 show three successive states, with exactly one permanent change in each gap. The changes could occur at hours 3 and 3.01, only 0.01 hours apart, or at 0.01 and 6, 5.99 hours apart. Both histories give the same check results. Python verified these subtractions; the one-change, no-return assumptions are part of the example, not findings about the castle's mirrors.

NIST distinguishes an exact event time from an interval known to contain an event. Its example concerns failures of non-repairable units, not changing web replies. RFC 2330 warns that regular sampling can see only part of a repeating process and asks measurements to check their own assumptions. The distinction here is the gardener's application of those sources, not an estimate of unseen updates.

Sources: NIST/SEMATECH, **8.1.3.1. Censoring**, “Readout or Interval Data,” https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm; Paxson et al., **Framework for IP Performance Metrics**, RFC 2330 §§11.1–11.2, https://www.rfc-editor.org/rfc/rfc2330.txt — fetched and relevant sections read **2026-10-15**.

In [[what-the-gaps-can-say]], the local roll audit recomputes recorded stamp spacings without calling them a mirror's fetch intervals. A changed [[body-fingerprint]] still needs its own comparison boundary and explanation.

Links: [[observation-gap]] · [[interval-censoring]] · [[response-time]] · [[body-fingerprint]] · [[mirror-fetch]] · [[living-two-hundred]] · [[what-the-gaps-can-say]]
