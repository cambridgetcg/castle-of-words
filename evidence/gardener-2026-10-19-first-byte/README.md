# Put the first byte on the ruler — 2026-10-19

This visit researched **question 740**, the oldest eligible open question. The courtyard was empty. Commissioned work and decisions reserved for yu were skipped; questions 744 and 766 were not counted as researched. Sixteen questions remain open, so no question or quest was planted.

## Scope fixed before calculation

[before.json](before.json) keeps the scope, document before-images and machinery hashes. Use the same fourteen saved October 17–18 visit directories as the [request-order audit](../gardener-2026-10-19-request-order/README.md), not new service traffic. Recheck every orgmode request and its earlier complete comparison; preserve failed requests. Use the inherited one-second descriptive cutoff, not a new classification selected for this result.

For each completed request, calculate three non-overlapping pieces: start to preparation, preparation to first byte, first byte to finish. Their sum must equal the recorded full-operation time. The raw fields are cumulative; do not add them without subtraction. Do not invent a first-byte time for a timed-out request.

## Executed result

`python3 -B evidence/gardener-2026-10-19-first-byte/analyze.py` succeeded. [analysis.json](analysis.json) retains all 28 attempts and **59 input-file hashes**. It checks saved-body hashes and the complete two-reference Git v0 advertisements in this slice; it is not a general Git parser. It also checks the recorded stdout against the parsed curl fields, zero followed redirects and the commands' disabled retries.

- **27 replies completed; one request timed out.** Twenty-four completed operations were below one second; three were at or above it.
- The three longer completed operations took **27.443937**, **20.902406**, and **18.912934 seconds**. Their preparation-to-first-byte intervals were **27.101587**, **20.576147**, and **18.668885 seconds** respectively. Each is **more than 98%** of its operation's total.
- Their first-byte-to-finish intervals were **0.001032**, **0.000904**, and **0.001174 seconds**. This locates the long waits before the first byte, without identifying the responsible component.
- One of those long replies is a first view changed since the preceding complete capture; the other two are rechecks matching their own first replies. The comparison targets stay explicit.
- The failed request lasted **45.145394 seconds** and recorded a preparation mark of **0.253469 seconds**. The difference, **44.891925 seconds**, ends at abort, not first byte. Its zero first-byte field, absent body, empty header capture and exit 28 stay together; the missing stage durations are JSON `null`, not zero or negative durations.

Original public source: **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, with the prior complete baseline on **2026-10-16 UTC**; reanalysed **2026-10-19**. Hashes establish local consistency, not independent authentication of that history. No collector was imported or run and no saved capture was changed.

## Web search and reading — 2026-10-19

All three retrievals returned HTTP 200 with curl exit 0. [sources.json](sources.json) keeps exact URLs, commands, retrieval times, lengths and hashes.

1. **Brave Search: “curl time_starttransfer time_pretransfer first byte timing”**, https://search.brave.com/search?q=curl%20time_starttransfer%20time_pretransfer%20first%20byte%20timing — discovery only; results included curl timing discussions and third-party explanations. No search snippet was used to diagnose this service.
2. curl project, **--write-out**, **curl 8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — read the cumulative timing definitions and redirect count. The timing differences are the gardener's calculation, not internal server measurements.
3. curl project, **--max-time**, **curl 8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md — the configured limit and retry reset rule, not a guarantee of an eventual reply.

## What grew

The room [[what-the-gaps-can-say]], section “Put the first byte on the ruler,” and the new word [[time-to-first-byte]] hold the result. The room's Map line was refreshed. **Filed 0, researched 1, planted 0.** Question 740 remains open; no checkbox was changed merely to free a planting slot.

uncertain: hidden update times, the cause of waiting, and any update–delay association. Client milestone differences locate the measured wait without supplying server work, a fault's lifetime, or an independent causal test.

## Reusable checking path

Fix the slice and cutoff before calculating; name each cumulative mark and its unit; keep failed attempts separate from completed replies; compare a view with its actual reference view; subtract marks rather than adding overlapping spans; recompute with a separate arithmetic path; preserve old prose, verify the Map and unchanged machinery, then append one chronicle line. This is a local evidence recipe, not an installed skill or a new monitoring policy.

`verify.py` checks the numerical result from raw records using exact fractions without importing `analyze.py`, verifies source hashes and document boundaries, and checks the full Map. Run without arguments before closing and with `--closed` afterward. These are same-session checks, not independent review or proof of the service's unobserved history. The saved outputs are `preflight.json` and `verification.json`.

Execution note: the first verification stopped on an ordering comparison: sorting room stems and then adding `.md` can differ from sorting filenames when one stem prefixes another. A direct filename-set check found no additions or removals. The checker now compares sorted filenames on both sides; no room or Map entry was changed to satisfy that test.
