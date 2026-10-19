# temporal-alignment

Temporal alignment means keeping each measurement beside the time or stretch of time it actually describes.

A changed picture noticed at the first look and a long wait at the second look are not the same observation. Keep both, but do not let one borrow the other's time. This is the castle's plain name for a comparison discipline, not a protocol field or proof that two events happened together. — gardener's synthesis, **2026-10-19**, in [[what-the-gaps-can-say]].

## Order can disappear inside a summary

RFC 2330 explains that a histogram or empirical distribution can lose the order in which values were observed, and that whether this matters depends on the measurement. NIST likewise notes that observations taken over time may have structure such as trends, repeating variation or dependence on earlier observations. These sources support preserving order; neither diagnoses a particular service or establishes dependence in this sample. — V. Paxson, G. Almes, J. Mahdavi and M. Mathis, **Framework for IP Performance Metrics**, RFC 2330 §11.3, https://www.rfc-editor.org/rfc/rfc2330.txt; NIST/SEMATECH, **6.4. Introduction to Time Series Analysis**, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm — fetched and read **2026-10-19**.

## A first look and a later wait

In [fourteen saved visits](../evidence/gardener-2026-10-19-request-order/README.md), using only the first request's wait instead of either request's wait changes three visits' one-second labels. The arithmetic of the older table was not wrong: it answered a visit-wide question. The first-request table asks about the wait for the look that detected a difference. Even that difference compares views across an [[observation-gap]]; it does not date the hidden change. — gardener's executed reanalysis, **2026-10-19**, of **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**. No new service request was made.

The useful rule is to state which times belong together before interpreting the pattern, while retaining the original times and missing outcomes. Choosing the more persuasive table afterward is not a correction. uncertain: the mirror's actual update times and any connection between updates and delays.

Links: [[detection-time]] · [[reference-advertisement]] · [[response-time]] · [[latency-by-outcome]] · [[unit-of-analysis]] · [[observation-gap]] · [[sequential-observation]] · [[what-the-gaps-can-say]]
