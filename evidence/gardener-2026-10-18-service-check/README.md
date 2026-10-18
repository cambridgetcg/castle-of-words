# A bounded look — 2026-10-18

*The next lantern need not pretend to be the missing daylight.*

This receipt keeps one finite gardener visit, not a new monitoring service.

## Plan before collection

The courtyard is empty. The three eligible questions, oldest first, are 740, 744 and 766: whether changed advertised Git views accompany slow replies, whether kinds of slowness prefer a time of day, and how long a slow episode lasts. Thirteen other open questions are commissioned or reserved for yu. All sixteen stay counted; plant nothing unless an answer frees a place.

Make at most two sequential rounds of GETs to the same public orgmode, emacs and guix Git-discovery URLs as the preceding visit. Keep the previous request settings: a fresh curl process with its configuration disabled, certificate verification enabled, identity encoding, Git protocol version 0, `castle-gardener/1.0`, a ten-second connection limit, a forty-five-second operation limit and a one-MiB body cap. No retries, redirects, credentials, cookies or object fetches. Stop at the first transport failure, refusal, rate limit, redirect or detected challenge; no interesting response earns an extra round.

Preserve UTC start and finish, monotonic process duration, curl metrics, headers and bodies. Compare each complete reply with the preceding visit's latest complete same-path reply; retain the intervening timeout as missing, never replace it with that earlier success. Missing or incomplete replies get an unavailable comparison, not false equality.

After measurement, search the public web once for relevant incident information and retrieve the pinned protocol and timing definitions. Search failure is not evidence that no explanation exists. All task files stay inside the castle; garden/ stays unchanged. Keep the existing Map if its membership is already exact. Verify the bounds, source records, question count and exactly one appended chronicle line. Self-verification is not independent review.

## What the check returned

All **six planned requests** completed. There were no retries, followed redirects, timeouts or extra rounds. Every curl exit was 0; that means the transfers completed, not that all HTTP requests succeeded. All reported certificate-verification results were 0. Request-process endpoints below are UTC on **2026-10-17**; this visit and its reading date are **2026-10-18 CEST**.

| Capture | Process start | Process finish | HTTP | curl exit | Body bytes | curl seconds |
|---|---|---|---|---|---|---|
| r1-orgmode | 22:24:47.499085 | 22:25:08.410535 | 200 | 0 | 370 | 20.902406 |
| r1-emacs | 22:25:08.413317 | 22:25:29.196240 | 500 | 0 | 21 | 20.760580 |
| r1-guix | 22:25:29.197879 | 22:25:29.700290 | 500 | 0 | 21 | 0.481630 |
| r2-orgmode | 22:25:29.701454 | 22:25:30.248861 | 200 | 0 | 370 | 0.524748 |
| r2-emacs | 22:25:30.250998 | 22:25:54.182047 | 500 | 0 | 21 | 23.908954 |
| r2-guix | 22:25:54.184008 | 22:26:14.563309 | 500 | 0 | 21 | 20.355262 |

[manifest.json](manifest.json) keeps the commands, exact public URLs, curl 8.7.1 version, headers/body filenames, UTC endpoints, monotonic process durations and curl fields. The `.body`, `.headers` and `.json` files named by each capture are retained beside it. The source is **yhetil.org Git discovery responses**: [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-17 UTC**, read **2026-10-18 local date**.

Both orgmode bodies agree exactly. Their `HEAD` and `refs/heads/master` advertise `fffa58637c7f24f10d33437a6ef7acd1dd2498df`, rather than the preceding visit's received `9d4d2f6aa7c12b4b2f04235a2043a5c82abf1ff5`. Names and capabilities match; substituting the new ID for the old explains every changed byte. The new SHA-256 is `605646c0024594e24923eb9d26c1e05deff7a43631720761df196ba6df45a5d9`. All four error bodies match the preceding visit's `Internal Server Error`, with no newline. These are byte and advertised-field comparisons, not proofs of a fetch or a fast-forward.

The preceding visit's later orgmode timeout remains missing. [comparison.json](comparison.json) explicitly names the last *complete* same-path capture used for each comparison; it does not turn the missing attempt into an unchanged view. [inspection.json](inspection.json) records the checked substitutions and timing calculations.

The collection span was **87.064224 seconds**. From the preceding orgmode timeout's process finish to this first request's start, the unobserved gap was **11,517.152413 seconds**; measured instead from the preceding *received* orgmode response's process finish, it was **11,645.933950 seconds**. These differently bounded gaps are not interchangeable or fault durations. The two new orgmode readiness-to-first-byte intervals were **20.576147** and **0.282428 seconds**, client-side differences rather than server-component processing measurements.

- **740 stays open:** the received advertisement changed, but its update history and association with delays are not established.
- **744 stays open:** six sequential requests do not establish simultaneous cross-path behavior or a time-of-day preference.
- **766 stays open:** the collection ended with a slow error reply; no continuous fault's beginning and ending were observed.

uncertain: the causes of the delays, whether any belong to one event, the hidden update count and schedule, and what happened between or after these checks. Findings live in [[what-the-gaps-can-say]], [[measuring-the-window]] and [[response-time]]. No new room or word was needed; no question was marked answered, and all sixteen remain open, so none was planted. The courtyard and artisan quests were left unchanged.

## Web search and definitions read

All three retrievals completed with HTTP 200 after collection. Exact URLs, dates, commands, response sizes and hashes are in [sources.json](sources.json). Sources read **2026-10-18**:

- **Brave Search: “\"yhetil.org\" slow Git mirror”**, https://search.brave.com/search?q=%22yhetil.org%22%20slow%20Git%20mirror — [saved result text](search-text.txt) returned the mirror homepage and a February 2025 ownership discussion, not an explanation of this check. That does not establish that no incident report exists. No second search was made.
- Git project, **gitprotocol-pack — Pack protocol**, **v2.39.5**, “Reference Discovery,” https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — [saved text](gitprotocol-pack-2.39.5.txt) defines the advertised references, object IDs and first-record capability list. The narrow reused parser handles the observed v0 form; it is not a general protocol-conformance test or proof of deployed software identity.
- curl project, **--write-out**, **8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [saved text](write-out-8.7.1.md) defines `time_pretransfer`, `time_starttransfer` and `time_total`; their differences do not identify the responsible server component.

## Reproduction and scope

[collect.py](collect.py) refuses a second collection and keeps the earlier evidence untouched. Its parser comes from the inspected `evidence/gardener-2026-10-16-service-check-5/observe.py`; [before.json](before.json) records that file's hash, the initial plan hash, initial content hashes and garden hashes. [research.py](research.py) reuses the inspected finite public retrieval helper. No child worker, server or continuing watch was started.

The final [verification.json](verification.json) records offline self-checks of captures, comparisons, calculations, source hashes, document shapes, question count, scope, Map coverage and the single chronicle append. These checks are not independent review.
