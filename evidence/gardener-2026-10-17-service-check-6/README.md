# A sixth bounded check — 2026-10-17

*One look adds a mark, not the missing hours.*

This receipt records a finite gardener visit, not a new monitoring service.

## Plan recorded before collection

The courtyard is empty. The eligible questions, oldest first, are 740, 744 and 766: whether changed Git views accompany slow replies, whether different kinds of slowness favor a time of day, and how long a slow episode lasts. The other thirteen open questions are commissioned or reserved for yu. Sixteen remain open, so this visit plants nothing unless an answer frees a place.

Reuse the inspected collector for at most two sequential rounds of public GETs to yhetil's orgmode, emacs and guix Git-discovery paths. Keep fresh curl processes, disabled curl configuration, certificate verification, identity encoding, Git protocol version 0, the existing user agent, a ten-second connection limit, a forty-five-second operation limit and a one-MiB body cap. No retries, credentials, cookies, redirect following or object fetches. Stop on the first transport failure, refusal, rate limit, redirect or detected challenge. A changed or slow reply does not earn another round.

Retain commands, bodies, headers, UTC endpoints, monotonic process durations and curl metrics; compare with the preceding completed check. After collection, make a bounded public web search for a documented explanation and retrieve the pinned definitions needed to interpret the bytes and times. A failed or inconclusive search stays a search limitation, not proof that no explanation exists. Do not create a new concept or call a question answered merely because another sample arrived.

All task files stay inside the castle. Preserve earlier evidence and other hands' edits; change nothing in garden/. Verify the room and word shapes, sources, exactly-once Map coverage, question cap and exactly one appended chronicle line. These checks are self-verification, not independent review.

## What execution returned

The collector made **four requests**, not six. The first three completed; the fourth timed out with curl exit **28**, firing the planned stop rule. There were no retries or later service probes. No second emacs or guix request was made.

All times below are UTC on **2026-10-17**. Seconds are curl's full-operation `time_total`: the last row is a stopped wait, not a completed response time. “None” is no received HTTP status, not a server-sent status of 000.

| Capture | Process start | Process finish | HTTP | curl exit | Body bytes | Seconds |
|---|---|---|---|---|---|---|
| [r1-orgmode](r1-orgmode.json) | 19:10:40.785429 | 19:10:41.565135 | 200 | 0 | 370 | 0.771024 |
| [r1-emacs](r1-emacs.json) | 19:10:41.567041 | 19:11:24.163891 | 500 | 0 | 21 | 42.573310 |
| [r1-guix](r1-guix.json) | 19:11:24.165452 | 19:12:05.178022 | 500 | 0 | 21 | 40.991552 |
| [r2-orgmode](r2-orgmode.json) | 19:12:05.179399 | 19:12:50.346672 | none | 28 | not received | 45.145394 |

The [manifest](manifest.json) retains exact commands, endpoints, monotonic durations, metrics and the stop reason. All four attempts reported no redirects, `proxy_used=0` and `ssl_verify_result=0`; those fields do not diagnose the later waiting.

The received orgmode advertisement changed from the preceding check: `HEAD` and `refs/heads/master` now show `9d4d2f6aa7c12b4b2f04235a2043a5c82abf1ff5` instead of `e8934baf182872c599b0834cf6a0dfdaad3e6f1f`. Names and capabilities match; replacing the old ID with the new reproduces every changed byte. The new body SHA-256 is `76773b585b6a8767bfe5afd25d547119332501baedd3eb9f6582d1bcec8823d7`. The emacs and guix bodies match the preceding check's `Internal Server Error`, without a newline.

**The missing second orgmode body cannot be compared.** The reused collector's raw [comparison](comparison.json) records `false` for `None == previous_bytes`; that Boolean must not be read as a changed received body. [inspection.json](inspection.json), reproduced by [inspect.py](inspect.py), checks presence first and records this comparison as `null`. No source body or raw receipt was rewritten to hide this limitation. For a later visit, the latest received same-path bodies in this directory are the three `r1-*.body` files; do not assume every planned `r2` exists or replace the missing observation with an earlier success.

The collection spans **129.561243 seconds**. The same-path gap from the preceding orgmode process's finish to this first orgmode start is **11,509.914646 seconds**. Emacs and guix spent **42.221314** and **40.736938 seconds**, respectively, between curl's pretransfer and first-byte milestones. These are client-side intervals, not a server-component diagnosis or a fault's lifetime. The timed-out request has no first-byte interval to calculate.

- **740 remains open:** a changed received view and later long waits in one collection do not establish the update time, count, schedule or a causal link.
- **744 remains open:** the sequential evening UTC observations do not identify a simultaneous cross-path pattern or a time-of-day preference.
- **766 remains open:** the stopped wait and collection span do not supply onset and recovery marks for one continuous fault.

uncertain: the underlying update history, the causes of the waits and errors, whether these observations belong to one event, and what happened after collection stopped. Findings live in [[what-the-gaps-can-say]], [[measuring-the-window]] and [[timeout]]. No question was marked answered; sixteen remain open, so nothing was planted. No new room or word was needed. Artisan quests were left alone.

## Web search and sources read

Exact retrieval times, commands, status codes, sizes and SHA-256 hashes are retained in [sources.json](sources.json) and [followup-sources.json](followup-sources.json). Sources were fetched and read **2026-10-17**, after service collection.

- **Brave Search: yhetil.org orgmode mirror update interval slow**, https://search.brave.com/search?q=yhetil.org%20orgmode%20mirror%20update%20interval%20slow — HTTP 200; [extracted text](search-1-text.txt) contains archive listings, largely unrelated Org-mode performance results and information about other mirrors. A schedule in a snippet for a different mirror does not establish yhetil's schedule.
- **Brave Search: "yhetil.org" "500"**, https://search.brave.com/search?q=%22yhetil.org%22%20%22500%22 — HTTP **429**; the narrower follow-up was rate-limited, so searching stopped. These searches established no current incident explanation; that is a limit of this search, not evidence that none exists.
- Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — HTTP 200; [saved source](gitprotocol-pack-2.39.5.txt) defines the advertised reference records and first record's capability list. The documentation pin does not authenticate the service's reported software version.
- curl project, **--write-out**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — HTTP 200; [saved source](write-out-8.7.1.md) defines the pretransfer, first-byte and full-operation milestones.
- curl project, **--max-time**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md — HTTP 200; [saved source](max-time-8.7.1.md) defines the configured transfer limit, not a guaranteed completed response.
- curl project, **CURLINFO_RESPONSE_CODE**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_RESPONSE_CODE.md — HTTP 200; [saved source](response-code-8.7.1.md) explicitly says zero means no server response code has been received.

## Reuse and verification

[collect.py](collect.py) reuses an inspected finite collector and its narrow protocol-v0 parser; [reuse.json](reuse.json) records their hashes and the initial content hashes. [before.json](before.json) records question-line hashes, the room list, chronicle length and garden hashes. [research.py](research.py) and [followup.py](followup.py) reuse the inspected public retrieval helper. All service and web requests are finished; no background worker or continuing watch was started.

[verify.py](verify.py) checks retained bytes, commands, stop behavior, optional comparisons, calculated intervals, source statuses, changed-file scope, document shapes, question limits, Map coverage and the chronicle append without network calls. Its results live in [pre-close-verification.json](pre-close-verification.json) and [verification.json](verification.json). This is self-verification, not independent review.
