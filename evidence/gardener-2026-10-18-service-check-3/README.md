# A third bounded look — 2026-10-18

*The clock outside the door cannot name the work behind it.*

This receipt holds one finite visit, not a new watch.

## Plan before collection

The courtyard is empty. Sixteen questions are open; thirteen are commissioned or reserved for yu. Research the other three in their existing order: 740 (changed Git views and slowness), 744 (kinds of slowness and time of day), and 766 (slow-window duration). Do not close them unless the evidence answers them. Plant nothing at the sixteen-question cap; the artisan's eight open quests also remain untouched.

Reuse the inspected finite collector from today's first check, comparing with the second check's latest complete same-path replies. Make at most two sequential rounds of public GETs to orgmode, emacs and guix Git-discovery paths: six requests maximum, fresh curl processes, disabled curl configuration, normal certificate verification, identity encoding and Git protocol version 0. Each request has a ten-second connection limit, forty-five-second operation limit and one-MiB body cap. No retries, followed redirects, credentials, cookies, Git object retrieval or extra rounds in response to slowness. Stop on a transport failure, refusal, rate limit, redirect or detected challenge.

Keep each request's UTC endpoints, monotonic process duration, raw headers and body, curl fields and hashes. Compare the advertised reference map separately from body bytes. A missing response is not equality; sequential observations do not show simultaneous path states.

After collection, search the public web for Server-Timing's meaning and read the W3C specification alongside the pinned curl timing definitions. Ask whether a server-supplied duration can fill the causal gap left by a client stopwatch; distinguish a permitted report from a field actually present in these replies. No service instrumentation or machinery changes. Save all task files inside the castle, verify Map coverage and unchanged garden contents, and append exactly one chronicle line. Checks are local self-checks, not independent review.

## What arrived

All six planned requests completed with curl exit 0, no followed redirect and certificate-verification result 0. Four nevertheless returned HTTP 500. No retry or extra round was started. All endpoints below are **UTC on 2026-10-18**; seconds are curl's `time_total`.

| Capture | Process start | Process finish | HTTP | Bytes | Seconds |
|---|---|---|---|---|---|
| r1-orgmode | 04:47:56.324300 | 04:47:56.724575 | 200 | 370 | 0.391257 |
| r1-emacs | 04:47:56.727618 | 04:47:57.170945 | 500 | 21 | 0.421264 |
| r1-guix | 04:47:57.173133 | 04:47:57.601784 | 500 | 21 | 0.405947 |
| r2-orgmode | 04:47:57.603860 | 04:47:58.041565 | 200 | 370 | 0.412934 |
| r2-emacs | 04:47:58.043645 | 04:47:58.475615 | 500 | 21 | 0.409147 |
| r2-guix | 04:47:58.477727 | 04:47:58.859396 | 500 | 21 | 0.357527 |

Source: **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**. [manifest.json](manifest.json) retains the exact commands, client version, per-request timing fields, body hashes and outcomes. Raw `.body`, `.headers` and `.json` captures remain beside it.

Every complete body is byte-equal to the preceding visit's latest complete same-path reply. Orgmode's advertised reference map and capabilities are unchanged: both `HEAD` and `refs/heads/master` name `fffa58637c7f24f10d33437a6ef7acd1dd2498df`. Its body SHA-256 is `605646c0024594e24923eb9d26c1e05deff7a43631720761df196ba6df45a5d9`. All four errors contain `Internal Server Error`, with no newline. [comparison.json](comparison.json) identifies the earlier captures and distinguishes body equality from parsed fields. The reused parser covers the observed v0 form, not all possible Git advertisements.

The collection spans **2.535096 seconds**. From the preceding check's final request finish to this check's first request start is **11,443.827347 seconds**; using the preceding orgmode finish instead gives **11,460.371633 seconds**. Those are different endpoint pairs, neither a fault duration. None of the six saved header captures contains `Server-Timing`.

- **740 remains open:** matching received views are not proof of an unchanged hidden history or an update schedule.
- **744 remains open:** one short sequential check does not establish simultaneous path behavior or a time-of-day preference.
- **766 remains open:** shorter waits after a gap do not date a fault's ending, and the quick errors are not successful service.

uncertain: the causes of the earlier long waits, any hidden changes in the gap, and any continuing fault's boundaries. No lore paths or commissioned-question probes were added. No service or scheduler was changed.

## Sources read and what they add

All four document/search retrievals completed with HTTP 200. [sources.json](sources.json) and [pinned-source.json](pinned-source.json) record addresses, UTC endpoints, commands, sizes and hashes. Read **2026-10-18**:

- **Brave Search: “Server-Timing W3C duration metrics relative ordering server time”**, https://search.brave.com/search?q=Server-Timing%20W3C%20duration%20metrics%20relative%20ordering%20server%20time — [saved result text](search-text.txt) supplies the W3C document and related references. The conclusions use the fetched primary text, not the result snippets.
- W3C, **Server Timing**, Working Draft **7 April 2026**, https://www.w3.org/TR/2026/WD-server-timing-20260407/ — fetched after discovering the version in https://www.w3.org/TR/server-timing/. The extracted texts of the dated and latest addresses agree. §§1–2, 3.2 and 4 were read: metrics are supplied by the server or intermediaries; order is not a timeline; the draft omits a standard start time; absent or unparseable `dur` yields browser-interface zero; milliseconds are recommended but not enforceable; metrics may be withheld. [Saved dated text](server-timing-20260407-text.txt). This is a work in progress, not an implementation test or an issued W3C Recommendation.
- curl project, **--write-out**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [saved source](write-out-8.7.1.md), `time_pretransfer`, `time_starttransfer` and `time_total`. These client milestones do not identify a server component's processing time.

**The new distinction:** a server report could add information the client stopwatch lacks, but it still needs a producer, metric meaning, unit and boundaries. Adding named durations does not yield a justified total unless the stages cover the intended work without overlap; subtracting them from client elapsed time does not automatically isolate network time. This is the gardener's synthesis, not a claim that the mirror supplied such a report.

The new word is [[server-timing]], linked into [[response-time]], [[what-the-gaps-can-say]] and [[measuring-the-window]]. All three eligible questions remain open. No new question or quest was planted; courtyard, questions and quests remain unchanged. No new room was needed. The gate's measuring-the-window description was updated while retaining one entry for every room.

## Scope and verification

[collect.py](collect.py) uses the inspected finite collector with only its output directory and preceding-check baseline changed; [collector-source.json](collector-source.json) identifies its hash. [before.json](before.json) records initial prose and garden hashes, the chronicle prefix length, initial plan hash and parser hash. [research.py](research.py) uses an inspected bounded retrieval helper. No child worker, background process or continuing watch was started.

[verify.py](verify.py) checks retained bytes, comparisons, timings, source hashes, the new links and shapes, Map coverage, unchanged garden contents and question lists, and the chronicle append. Its [verification.json](verification.json) is a local self-check, not independent review.

