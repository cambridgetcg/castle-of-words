# The first response is not the first content — 2026-10-20

This visit researched **question 740**, the oldest unreserved open question. The courtyard was empty; commissioned work and decisions reserved for yu were skipped. Questions 744 and 766 were not counted as researched. Sixteen questions remain open, so no question or quest was planted.

## Bounded work

Use the same 28 orgmode attempts from fourteen saved visits as the preceding [first-byte audit](../gardener-2026-10-19-first-byte/README.md). Inspect the saved header blocks and reconsider the timing boundary using curl's version-pinned source. Do not send another request to the service, run a collector, change a schedule, or infer a hidden update time. `before.json` records the scope and pre-edit document/machinery hashes.

## Executed result

`python3 -B evidence/gardener-2026-10-20-response-boundary/audit.py` succeeded:

- **28 attempts: 27 completed responses and one timeout.**
- Every completed header capture has exactly one **HTTP/1.1 200 OK** block; **zero** informational or additional response blocks were found.
- The timeout's header file is empty; its body is absent. It is not an instant reply.
- **19** completed replies declare `Content-Length: 370`; **8** declare chunked transfer coding instead. All saved content bodies are 370 bytes, without a Content-Encoding field.
- **59** preceding audit input hashes agree. All **27** completed timing partitions were independently recomputed using exact fractions rather than importing the earlier Decimal-based analyser. The three long completed waits still spend over 98% of their totals between preparation and the first-response mark.

`analysis.json` keeps per-request results and input hashes. Original source: **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, reanalysed **2026-10-20**. The preceding comparison inputs include an October 16 baseline. Hashes check local consistency, not independent authentication of that history.

Execution note: the first audit stopped because it wrongly assumed every completed response declared Content-Length. The kept headers instead contain two framing forms. The check now handles those forms explicitly, without changing any capture; the counts above are from the successful rerun.

## Public research, read 2026-10-20

`research.py` fetched one web search and six official reference files, all with HTTP 200 and curl exit 0. `sources.json` retains titles, exact URLs, timestamps, commands and hashes. Retrievals began on October 19 UTC; the local reading date is October 20 CEST.

- **Brave Search: “curl time_starttransfer includes HTTP response headers first byte body”**, https://search.brave.com/search?q=curl%20time_starttransfer%20includes%20HTTP%20response%20headers%20first%20byte%20body — discovery only; the result snippets were not used as implementation evidence.
- curl **8.7.1**, **CURLINFO_STARTTRANSFER_TIME**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_STARTTRANSFER_TIME.md — documented first-byte timing and redirect accumulation.
- curl **8.7.1**, **lib/transfer.c**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/transfer.c, and **lib/http.c**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/http.c — response dispatch, header writing and the body-content path.
- curl **8.7.1**, **lib/sendf.c**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/sendf.c — `cw_download_write` calls `TIMER_STARTTRANSFER` before the body-content check, excluding CONNECT responses from that trigger.
- curl **8.7.1**, **lib/progress.c**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/lib/progress.c — repeated calls do not replace the first mark within a transfer.
- **HTTP Semantics**, RFC 9110 §§6.2, 6.4 and 15.2, https://www.rfc-editor.org/rfc/rfc9110.txt — control data, content after headers, transfer framing, and informational responses without content.

The source reading identifies a client timing boundary; it is not a build or instrumented runtime test. No inference about the deployed server's code is made.

## What grew, and what did not

[[time-to-first-byte]] and [[what-the-gaps-can-say]] now distinguish a first-response mark from a separate content-arrival timestamp. The small remainder after the mark is not content-download time alone. No informational reply was found in this slice, so none is invented as an explanation for its waits. The Map line and current gate glance are refreshed without altering the historical archive.

**Filed 0, researched 1, planted 0.** The empirical question stays open. uncertain: content's separately timed arrival, hidden update times, the cause of waiting, and any update–delay association.

Reusable checking path: name the byte boundary before interpreting a timing field; read the version-pinned client path; retain headers separately from content; count every saved response block and failed attempt; let observed framing determine the length check; recompute inherited arithmetic; preserve the old record; verify the Map and unchanged machinery before appending exactly one chronicle line. This is a local evidence recipe, not an installed skill or a monitoring policy.

## Verification

`verify.py` checks the raw header counts through a second path, input and downloaded-source hashes, preservation of old prose, all Map entries, unchanged questions and courtyard, and all 84 saved machinery-file hashes. Its pre-close run passed with **697 rooms, 697 unique Map lines, 16 open questions, zero courtyard insights and no chronicle line yet added**. `preflight.json` retains that result. The after-close command is `python3 -B evidence/gardener-2026-10-20-response-boundary/verify.py --closed`; its output is saved to `verification.json`, and it additionally requires exactly one correctly shaped appended chronicle line. These are same-session checks, not an independent reviewer or proof of remote history.
