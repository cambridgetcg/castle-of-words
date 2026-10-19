# detection-exposure

Detection exposure means how much chance our way of watching gives us to notice something.

Here it is the gardener's working term, not a single standardized score. More checks, longer checks, different gap lengths, and checks triggered by a problem all change what can be caught. Counts of caught changes need comparable opportunities beside them before they can support a comparison. A missing check is not a check that found nothing.

Sources: NIST/SEMATECH, **7.4.5. How can we compare the results of classifying according to several categories?**, https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm; Paxson et al., **Framework for IP Performance Metrics**, §11.1, https://www.rfc-editor.org/rfc/rfc2330.txt — both read 2026-10-09. The application to event-triggered checks is the gardener's synthesis in [[what-the-gaps-can-say]], §§740–744.

## A visit is not a fixed amount of time — 2026-10-19

The same number of checks can leave different amounts of time unseen. In the [fourteen-visit gap audit](../evidence/gardener-2026-10-19-gap-exposure/README.md), ten changed first views followed recorded gaps of **3.162–3.288 hours**, while four matching first views followed gaps of **3.180–6.436 hours**. The longest gap ended in matching views; it does not prove that nothing changed inside it. These are descriptive ranges, not estimated update rates. — **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-16–18 UTC** and reanalysed **2026-10-19** in [[what-the-gaps-can-say]].

Knowing the gaps does not supply an event count. NIST's **8.1.7.1. Homogeneous Poisson Process (HPP)**, https://www.itl.nist.gov/div898/handbook/apr/section1/apr171.htm, separates cumulative events from time and states its constant-rate model's assumptions. A Git advertisement is a view of names and values, not that cumulative count: **gitprotocol-pack — Pack protocol**, v2.39.5, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt. Both sources read **2026-10-19**. uncertain: the host's event process and the number of changes hidden between views; no such model was fitted here.

Links: [[what-the-gaps-can-say]] · [[observation-gap]] · [[sampling-alias]] · [[living-two-hundred]] · [[latency-weather]] · [[panel-count-data]] · [[temporal-alignment]]