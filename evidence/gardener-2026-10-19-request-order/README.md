# Keep the first look beside its own wait — 2026-10-19

*The second lantern cannot lend its shadow to the first.*

This is a bounded, offline reanalysis for question **740**, the oldest unassigned open question. The courtyard is empty. Sixteen questions are open; commissioned questions and decisions reserved for yu are not taken over. Questions 744 and 766 are not counted as researched this visit.

## Scope before calculation

Use the same fourteen saved visits as the preceding [missing-read audit](../gardener-2026-10-19-missing-reads/README.md): every `gardener-2026-10-17-service-check` and `gardener-2026-10-18-service-check` directory, including numeric suffixes. Recheck source hashes, manifests, request records and saved bodies. Do not import or run a service collector.

Compare each first complete orgmode advertisement with the preceding complete capture named by its existing receipt. Keep this **between-visit detected-change label** separate from a comparison of the first and second replies **within the visit**. Tabulate the first request's wait, the second request's wait, and the larger of the two beside the same first-view label. Use the inherited one-second descriptive cutoff, not an optimized or natural boundary. Keep the second-request timeout as a client wait without inventing its missing advertisement or completed-response time.

Retain the actual UTC intervals and the elapsed gap between the first orgmode request finishing and the recheck starting. Other requests ran in that gap; it is not an intentional pause or a period known to be quiet. Do not call either wait an update time. Do not choose the table with a more attractive pattern or calculate a p-value on these adjacent, nonrandom visits. A source describing ordered measurements supplies a recording principle, not a host diagnosis.

Search public documentation, read the fetched sources and write the understanding into the existing room and a word file. No service probes, live experiments, database reads, watcher, schedule change, garden edit or write outside the castle. Plant nothing while sixteen questions remain open. Verify the Map and append exactly one chronicle line when the visit is complete.

## Reusable checking path

1. Freeze the input slice and define the comparison before counting.
2. Re-read the saved request records, not just a previous table; verify hashes and each capture's outcome.
3. Keep the look that supplies the change label beside its own wait. Preserve later waits under their own timestamps.
4. Separate a missing reply from an unchanged reply and a measured client wait from a completed response time.
5. Cross-check the arithmetic separately, check scope and links, then preserve the old prose and add the dated finding.

This is a local evidence recipe, not an installed skill, a new monitoring policy or independent review.

## Executed result

`python3 -B evidence/gardener-2026-10-19-request-order/analyze.py` completed successfully. [analysis.json](analysis.json) retains the full row list, exact timestamps, input paths and hashes. It rechecked all **195 inputs** of the preceding missing-read audit and the audit's own output, for **196 input hashes** in this analysis. All fourteen first replies completed; thirteen rechecks completed and one timed out.

Each cell counts **wait ≥ 1 s / wait < 1 s**, grouped by whether the first advertised reference map differed from the preceding complete capture:

| First view | First request | Second request's client wait | Either request |
|---|---:|---:|---:|
| Changed | 1 / 9 | 1 / 9 | 2 / 8 |
| No detected change | 0 / 4 | 2 / 2 | 2 / 2 |

**Three visits change their timing label** when only the first request's wait is used. The second-request column contains the timeout as a client wait; of its completed replies, the changed-view group has **0 at least one second / 9 below**, the no-detected-change group **2 / 2**. The changed-view group also has **one missing reply**, not a tenth completed recheck.

All **13 received recheck bodies are byte-equal to their own first replies**, with equal parsed maps and capabilities. The absent fourteenth body is kept as absent. The first-request and either-request tables answer different descriptive questions; the older table is reproduced, not declared wrong.

### Where the later wait enters

| Visit directory suffix | First-view change | First wait (s) | Second client wait (s) | First-finish to second-start gap (s) |
|---|---|---:|---:|---:|
| `2026-10-17-service-check` | no detected change | 0.708186 | 27.443937 | 0.872460 |
| `2026-10-17-service-check-6` | changed | 0.771024 | 45.145394, timeout | 83.614264 |
| `2026-10-18-service-check` | changed | 20.902406 | 0.524748 | 21.290919 |
| `2026-10-18-service-check-2` | no detected change | 0.483331 | 18.912934 | 18.099631 |

The suffixes belong to directories prefixed `gardener-` in `evidence/`. Directory dates are local-date labels; the exact request times in the JSON are UTC. These are all visits in the slice with either orgmode wait at least one second, not all fourteen visits. The gaps contain intervening emacs and guix requests; they are not scheduled pauses, observation of continuous service behavior or fault lifetimes.

Original public source: **yhetil.org orgmode Git discovery responses**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**. Reanalysis date: **2026-10-19**. Hash and schema checks establish local consistency, not independent authentication of the earlier remote history. No service request was made this visit.

### Execution note

The first run stopped because it expected a `method` field in every record. Inspection showed the October 18 format omits that field while preserving the full curl command. The check now validates the field when present and compares normalized commands across every selected request; absent metadata was not filled in and no source record was rewritten. The subsequent run succeeded. A type-check warning about an optional parsed baseline was also resolved by asserting that the baseline is complete before indexing it.

## Public sources read — 2026-10-19

All **five** fetched pages returned HTTP 200 and curl exit 0. [sources.json](sources.json) records their URLs, commands, retrieval timestamps and SHA-256 hashes.

1. **Brave Search: “NIST time series temporal order lag plot observations”**, https://search.brave.com/search?q=NIST%20time%20series%20temporal%20order%20lag%20plot%20observations — the results located NIST's time-series introduction. Discovery only; search snippets were not used as primary evidence.
2. V. Paxson, G. Almes, J. Mahdavi and M. Mathis, **Framework for IP Performance Metrics**, RFC 2330 §11.3, https://www.rfc-editor.org/rfc/rfc2330.txt — an empirical distribution or histogram loses the observed order; whether that matters depends on the metric. It does not supply a host diagnosis or prescribe this table.
3. NIST/SEMATECH, **6.4. Introduction to Time Series Analysis**, https://www.itl.nist.gov/div898/handbook/pmc/section4/pmc4.htm — observations over time can have internal structure, including autocorrelation, trend or seasonal variation. No time-series model was fitted here.
4. curl project, **--write-out**, **8.7.1**, `time_total`, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — full-operation duration, not a hidden update's time.
5. Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — names, object IDs and capability records. The local parser is deliberately limited to the complete two-reference SHA-1 protocol-v0 form in these saved bodies.

## What grew and what did not

The new [[temporal-alignment]] word and the dated section “Keep the first look beside its own wait” in [[what-the-gaps-can-say]] preserve the order hidden by a visit-wide label. The Map summary and current glance were updated without replacing their historical archive. **Filed 0, researched 1, planted 0.** Question 740 remains open; no existing checkbox, commission or quest was changed.

uncertain: the missing reply, hidden update times, whether request order influences the waits, and any update–delay association. First-only and whole-visit summaries remain retrospective descriptions, not rival proofs or a causal test.

## Verification

**Pre-close verification: PASS.** `python3 -B evidence/gardener-2026-10-19-request-order/verify.py` separately extracted the saved reference pairs and recomputed the counts and gaps with exact fractions. [preflight.json](preflight.json) records **196 input hashes**, **5 public-source hashes**, **13 equal recheck bodies**, **3 changed timing labels**, all **697 rooms** listed exactly once, **11 resolving new wikilinks**, the word's required shape, preserved earlier room prose and gate archive, and unchanged courtyard, questions, quests and `garden/`. `git diff --check` passed.

The closing check is `python3 -B evidence/gardener-2026-10-19-request-order/verify.py --closed`; [verification.json](verification.json) records that check, including the requirement for **exactly one appended chronicle line**. These are same-session checks, not distinct-session review or proof of the earlier service's hidden state.
