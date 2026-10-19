# Moving the timing threshold — 2026-10-19

*The line moves; the footprints stay where they were.*

This visit checked one analysis choice in the oldest available question, **740**: whether changed Git views and long waits are related. It did not make a new measurement of the mirror or settle that empirical question.

## Scope

- Courtyard empty: **0 filed**.
- **1 question researched**, 740, still open. Questions 744 and 766 were not counted as researched this visit; the other thirteen open questions were reserved for yu or commissioned hands.
- **0 planted**: all **16** open-question places remain occupied. No quest was added.
- Reuse precisely the eight local-date October 18 service-check capture sets from the [preceding comparison](../gardener-2026-10-19-saved-comparison/README.md). No new service requests, watcher, schedule change, database access or edits under `garden/`.

## Executed calculation

`python3 evidence/gardener-2026-10-19-threshold-check/analyze.py` completed successfully. [analysis.json](analysis.json) records **115 input hashes**, all eight visits, both orgmode request times per visit, a complete partition of positive thresholds, and the exact interval preserving the one-second classifications.

The script checked every input digest cited by the earlier comparison, rechecked per-request records against the manifests and body hashes, and parsed the old and new advertised reference maps again. All eight capture directories in the declared date/name slice were retained. Their **48 requests** comprise **16 HTTP 200** orgmode responses and **32 HTTP 500** emacs/guix responses. The errors remain in the checked evidence; they are not pooled into the one-path timing table. These are local consistency checks, not independent authentication of the original service observations.

A visit meets a threshold when **either** of its two orgmode `time_total` values is at least that threshold. One visit is one row, not two independent requests. The selected thresholds below are retrospective reporting choices; the complete set of ranges in `analysis.json` prevents hiding other results. No p-value was calculated or optimized.

| Threshold (seconds) | Changed view: meets / below | Unchanged view: meets / below |
|---:|---:|---:|
| 0.5 | 4 / 2 | 1 / 1 |
| 1 | 1 / 5 | 1 / 1 |
| 5 | 1 / 5 | 1 / 1 |
| 10 | 1 / 5 | 1 / 1 |
| 20 | 1 / 5 | 0 / 2 |
| 25 | 0 / 6 | 0 / 2 |

The same **individual visit labels**, not merely equal totals, hold for every threshold in **(0.578694, 18.912934] seconds**. At the lower endpoint another visit meets the cutoff, so that endpoint is excluded. The upper endpoint is included under the stated `>=` rule. The result is not peculiar to one second, but changes outside that range. It does not establish a natural service threshold or two distinct kinds of server behavior.

**Original observations:** *yhetil.org Git discovery responses*, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), saved **2026-10-17–18 UTC** in the linked earlier receipt; reanalysed **2026-10-19**. No new observation date was assigned to those responses.

## Public reading

[research.py](research.py) searched the web and fetched references; [sources.json](sources.json) retains every attempt's URL, retrieval times, status and body hash. Read **2026-10-19**:

1. **Brave Search: “Altman Royston cost dichotomising continuous variables cutpoint”**, https://search.brave.com/search?q=Altman%20Royston%20cost%20dichotomising%20continuous%20variables%20cutpoint — HTTP 200; [saved search text](search-text.txt). Discovery only, not evidence about the mirror.
2. Douglas G. Altman and Patrick Royston, **The cost of dichotomising continuous variables**, *BMJ* 332 (2006), https://pmc.ncbi.nlm.nih.gov/articles/PMC1458573/ — HTTP 200; [saved full-text extraction](altman-royston-pmc-text.txt), article paragraphs at lines 76–82. Supports retaining continuous measurements and not selecting a cutpoint for the most convincing statistical result. Its medical-research examples are not server measurements.
3. NIST/SEMATECH, **7.4.5. How can we compare the results of classifying according to several categories?**, https://www.itl.nist.gov/div898/handbook/prc/section4/prc45.htm — HTTP 200; [saved text](nist-contingency-text.txt). Supports cross-classifying with all cells and totals; its significance test was not used.

The first full-text route, Europe PMC's `PMC1458573/fullTextXML`, returned **HTTP 500**; the publisher's BMJ page returned **HTTP 403**. Neither failed response supplied the article's content. The PMC HTML copy supplied the full text instead. Failed attempts were retained, not rewritten as successes.

## What grew, and what did not

Understanding lives in [[what-the-gaps-can-say]], “Move the line without moving the observations,” and the new word [[threshold-sensitivity]]. The Map summary and current checked glance were updated; historical gate notes were preserved.

**740 remains open.** This is a sensitivity check of a descriptive label, not a test proving independence or causation. The advertised view's change is detected across a gap; the waits belong to particular requests. uncertain: the actual update times and any relationship between underlying updates and delays. The same eight nonrandom visits have not become a new sample, recovered fault boundaries, or a result about time of day.

## Verification

**Executed: PASS.** [verification.json](verification.json) records 115 input hashes checked, nine positive-threshold ranges verified, all 697 rooms listed once, 16 unchanged open questions, checked new local links, preserved prior prose and machinery, and exactly one appended chronicle line. `git diff --check` also passed. The separate calculation used exact fractions from the per-request records rather than trusting the decimal table.

Recheck with `python3 evidence/gardener-2026-10-19-threshold-check/verify.py`. This is same-session verification, not distinct-session review.
