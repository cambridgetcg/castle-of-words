# The wrapper changed while the list stayed the same — 2026-10-20

This visit researched **question 740**, the oldest unreserved open question. The courtyard was empty. Commissioned questions and decisions reserved for yu were skipped. Questions 744 and 766 were not counted as researched. All **16** questions remain open; no question or quest was planted.

## Scope

Reanalyse the same **28 orgmode attempts from fourteen saved visits** used in the [response-boundary audit](../gardener-2026-10-20-response-boundary/README.md). Compare the kept framing headers with the decoded content bytes. Search the public web and read the HTTP standard and version-pinned curl documentation. Make **no new requests to lore or yhetil**, and do not run a collector or change a schedule.

`before.json` keeps the starting scope, eligible question positions and pre-edit hashes. `edit-boundaries.json` preserves the exact gate lines and word-link line needed to verify that the prose edits left the rest intact. Existing uncommitted work was not reverted.

## Executed result

`python3 -B evidence/gardener-2026-10-20-framing/audit.py` succeeded:

- **28 attempts:** 27 completed responses and one timeout with no headers or body.
- **19** completed responses declare Content-Length; **8** declare chunked transfer coding. None combines the two, and none declares content coding. All saved contents are 370 bytes.
- **13** complete within-visit pairs have identical decoded content; **6** of those pairs have different framing headers.
- **11** distinct saved contents occur across the completed requests; **5** are seen under both framing forms. Equality is checked by direct byte comparison as well as hashes.
- With the inherited descriptive one-second cutoff, Content-Length has **17 below / 2 at-or-above**; chunked has **7 below / 1 at-or-above**. The timeout is kept outside this table because no framing was received.
- **87** inherited input hashes match. `analysis.json` retains the new input manifest, every request, the paired comparisons and all mixed-framing content groups.

For a concrete pair, `gardener-2026-10-17-service-check-3/r1-orgmode` is chunked and `r2-orgmode` declares Content-Length. Their request starts are **09:24:30.093013 UTC** and **09:24:31.293793 UTC**; their saved contents are byte-identical.

Original source: **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, reanalysed **2026-10-20**. Paths and hashes identify local records, not independently authenticated remote history.

Execution note: the first analysis stopped because it assumed every JSON capture had a `method` field. Sixteen older records omit it. The revised check validates the complete recorded command shape and checks the method when present, without adding fields or changing old captures. The results above come from the successful rerun.

## Public research, read 2026-10-20

`research.py` fetched these three sources with **HTTP 200 and curl exit 0**. `sources.json` retains exact titles, URLs, retrieval timestamps, commands, sizes and SHA-256 fingerprints. The search was read for discovery; snippets were not used in place of the standard.

1. **Brave Search: RFC 9112 chunked transfer coding connection property intermediaries decode** — https://search.brave.com/search?q=RFC%209112%20chunked%20transfer%20coding%20connection%20property%20intermediaries%20decode.
2. R. Fielding, M. Nottingham and J. Reschke, **HTTP/1.1**, RFC 9112 — https://www.rfc-editor.org/rfc/rfc9112.txt — §§6.1–6.3 and 7.1–7.1.3: transfer coding belongs to a message; recipients can decode or apply it with matching field changes; framing rules depend on method and status; chunk decoding retains content rather than original chunk layout.
3. curl project, **CURLOPT_HTTP_TRANSFER_DECODING — HTTP transfer decoding control**, **8.7.1** — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_HTTP_TRANSFER_DECODING.md — chunk decoding enabled by default.

## What grew, and the boundary

[[message-framing]] is a new word. [[transfer-coding]] and [[what-the-gaps-can-say]] now carry the observed case: a changed wrapper does not have to be a changed list. The Map summary and current gate glance point to that narrower finding.

**Filed 0, researched 1, planted 0.** No question was marked answered. uncertain: which component selected each wrapper, original chunk boundaries, hidden reference-update times, the cause of waiting, and any update–delay association. Both framing forms appear beside quick and longer waits; this small descriptive table is not a causal test or evidence of independence. A framing header is not a backend identity or a cache-hit receipt.

Reusable checking path: preserve response headers separately from decoded content; validate the recorded command and tolerate explicitly absent metadata without inventing it; compare bytes directly within matched requests; retain failed attempts as missing framing; read the protocol before attributing a wrapper to a machine; verify evidence hashes and old prose, then the full Map and the one-line close. This recipe is local evidence, not a new monitoring policy or installed skill.

## Verification

`python3 -B evidence/gardener-2026-10-20-framing/verify.py` checks the evidence through a separate parser, direct body comparisons, the full Map, unchanged questions/courtyard/quests and machinery, preservation of prior prose, and links in the added writing. Its pre-close output is saved as `preflight.json`. The same command with `--closed` additionally requires exactly one correctly shaped chronicle line and saves `verification.json`. These are same-session checks, not a separate reviewer or a new observation of the service.
