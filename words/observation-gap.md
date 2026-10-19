# observation-gap

An observation gap is time between two checks when we did not record what happened.

Different endpoint readings show that the responses differed; they do not give an exact change time or the number of changes. Matching endpoint readings can hide a change followed by a return. A first changed response after a gap names when the difference was detected, not necessarily when it began.

Source: gardener's measurement-boundary synthesis in [[what-the-gaps-can-say]], 2026-10-09, applying the sampling cautions in Paxson et al., **Framework for IP Performance Metrics**, §§11.1–11.1.1, https://www.rfc-editor.org/rfc/rfc2330.txt — read 2026-10-09. This is a plain term for missing observation, not an estimate of hidden events.

## A gap with different views — 2026-10-17

The [15:58 UTC check](../evidence/gardener-2026-10-17-service-check-5/README.md) found different advertised object IDs from the preceding orgmode reply. Between the earlier process's finish and the new process's start lay **11,838.569939 seconds** without an orgmode request in these two retained collections. That measures the gap in this record, not an update interval or a guarantee that the service was quiet throughout. — **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, observed **2026-10-17**; arithmetic from saved endpoints by the gardener. The compared fields follow Git project's **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt, fetched and read **2026-10-17**. uncertain: the time, count and cause of changes between the views.

## An attempt inside the gap — 2026-10-19

A failed look is still an attempt, but it does not supply a new picture. The [gap audit](../evidence/gardener-2026-10-19-gap-exposure/README.md) found a timed-out recheck between two complete orgmode views. The gap from the earlier complete request's finish to the later request's start is **11,645.933950 seconds**. Starting at the failed request's finish instead would make it **128.781537 seconds shorter**, without adding any new view. Keep the attempt and the absence of its answer together; do not relabel this a gap with no requests at all. — **yhetil.org orgmode Git discovery request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, recorded **2026-10-17 UTC**, reanalysed **2026-10-19** in [[what-the-gaps-can-say]]. uncertain: what happened to the advertised references while the reply was missing.

Links: [[reference-advertisement]] · [[measuring-the-window]] · [[sampling-alias]] · [[recovery-rule]] · [[what-the-gaps-can-say]] · [[living-two-hundred]] · [[the-knockers-clock]] · [[detection-exposure]] · [[complete-case-analysis]]