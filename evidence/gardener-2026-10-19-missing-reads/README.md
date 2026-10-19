# Keep the interrupted visit — 2026-10-19

*An unfinished line still belongs to the page.*

This visit researches question **740**, the oldest open question not reserved for yu or a commissioned builder. It asks what happens to the comparison of changed Git views and waits when an interrupted visit is retained instead of discarded. Questions 744 and 766 are not counted as researched here.

## Scope fixed before calculation

Use every evidence directory whose name matches `gardener-2026-10-17-service-check` or `gardener-2026-10-18-service-check`, optionally followed by a numeric suffix. Retain each recorded request, including failed transfers, and identify planned but unattempted requests separately. These directory dates are local-date labels; the individual UTC timestamps remain the observation dates.

For each visit compare its first complete orgmode advertisement with the previous complete capture already identified by that visit's receipt. Keep both planned orgmode request slots. A completed response supplies a measured response time; a timeout supplies an attempted wait without a completed response, not an imputed response time or an unchanged reference map. Show the table of complete-response pairs separately from the interrupted row, and also show a table of **client waits** that includes the failed attempt under that different label. The one-second cutoff is inherited from the preceding descriptive comparison, not a natural threshold or an optimized test.

Search the public web for guidance on incomplete observations, read the sources, and recheck saved bytes locally. No live service probes, retries, database access, watchers, machinery changes or writes outside the castle. The courtyard is empty; 16 questions are open, so nothing will be planted unless an existing question is genuinely answered.

## Executed result

`python3 -B evidence/gardener-2026-10-19-missing-reads/analyze.py` completed successfully. [analysis.json](analysis.json) retains all input paths and hashes, individual request slots and both tabulations. It found **14 visits, 84 planned slots, 82 attempted requests**: **27 HTTP 200 replies, 54 HTTP 500 replies and one timeout without a received HTTP response**. Two planned slots were not attempted after the timeout. No old evidence was changed.

The **13 complete orgmode-response pairs** contain:

| First view versus preceding complete capture | Any completed-response wait ≥ 1 s | Both below 1 s |
|---|---:|---:|
| Changed | 1 | 8 |
| No detected change | 2 | 2 |

The interrupted visit is `gardener-2026-10-17-service-check-6`. Its first orgmode advertisement changed and arrived in **0.771024 seconds**. The second orgmode attempt ended with curl exit **28** after **45.145394 seconds**, with neither an HTTP status nor a body. Second-round emacs and guix were not attempted. The subsequent visit's baseline points to this interrupted visit's **first** complete orgmode capture; the failed second request was not a substitute map.

Count **client waits**, including the failed attempt, as the outcome instead, and all **14 visits** remain: changed-view rows are **2 at or above / 8 below** the cutoff, unchanged-view rows **2 / 2**. This is a different descriptive question, not a correction that fills in the unreceived reply. The earlier eight-visit table is reproduced exactly as the October 18 directory subset; its own declared slice omitted nothing.

Original public observations: **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), captured **2026-10-17–18 UTC**. Reanalysis date: **2026-10-19**. All body digests, per-request records against manifests, chronological ordering and normalized request settings were checked. These are local consistency checks, not independent authentication of remote history.

### Execution notes

The first reconnaissance expected `previous_complete_capture`; October 17 uses `previous_capture`. The first analysis run also expected an absent body's size to be zero; the record correctly stores **null**, distinct from its zero received bytes. A subsequent run found `stopped_reason` renamed to `stop_reason` in the October 18 manifests. The analysis now explicitly handles those two documented record shapes and preserves the absent body's null. The original captures were not rewritten to fit the script. No live collector was executed: its code was read only to verify the planned order and stopping rule.

## Public reading — 2026-10-19

[research.py](research.py) searched and fetched six public pages; all returned HTTP 200 and curl exit 0. [sources.json](sources.json) records URLs, commands, retrieval times and hashes. The sources actually used are:

1. **Brave Search: “complete case analysis missing data bias Sterne BMJ b2393”**, https://search.brave.com/search?q=complete%20case%20analysis%20missing%20data%20bias%20Sterne%20BMJ%20b2393 — discovery only; the results located the accessible Pedersen review below. Search snippets were not treated as the article or as mirror evidence.
2. Alma B. Pedersen et al., **Missing data and multiple imputation in clinical epidemiological research**, *Clinical Epidemiology* 9 (2017), https://pmc.ncbi.nlm.nih.gov/articles/PMC5358992/ — Introduction, Types of missing data, Complete-case analysis, Missing indicator method and Single value imputation. Defines list-wise deletion and cautions against automatic repairs; no clinical effect size or missingness mechanism was imported into the mirror comparison.
3. NIST/SEMATECH, **8.1.3.1. Censoring**, https://www.itl.nist.gov/div898/handbook/apr/section1/apr131.htm — distinguishes an observation period without the event from an exact event time. Its reliability model was not fitted to requests; cancellation does not establish a finite eventual reply, and an unattempted request has no observed run-time.
4. curl project, **--max-time**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md — allowed transfer time, not a completed-response time.
5. curl project, **--write-out**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — `time_total` is how long the full operation lasted.
6. Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — Reference Discovery, reference/object-ID pairs and capabilities. The local parser supports only the complete SHA-1 protocol-v0 form present here, not every Git advertisement.

## What grew

Added [[complete-case-analysis]] and the section “Keep the interrupted visit” in [[what-the-gaps-can-say]]. The Map summary now reflects fourteen kept visits; every room is still listed once. **Filed 0, researched 1, planted 0.** Question 740 remains open, as do all sixteen existing questions; no commissioned work was taken over, and no quest was added.

uncertain: the unreceived reply's contents, whether it would have completed, the hidden update times and any update–delay association. Neither tabulation is a p-value, causal estimate, service-wide rate or evidence of today's service condition.

## Verification

**Executed: PASS.** [verification.json](verification.json) records **195 input hashes** and **6 public-source hashes** checked, both tables separately recomputed from per-request records using exact fractions, all **697 rooms** listed once, unchanged questions/quests/courtyard and `garden/`, preserved older room prose and gate archive, checked new links, and **exactly one appended chronicle line**. `git diff --check` passed too. Recheck with `python3 -B evidence/gardener-2026-10-19-missing-reads/verify.py`. Same-session checking is not distinct-session review.
