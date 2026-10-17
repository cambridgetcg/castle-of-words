# A second bounded check — 2026-10-17

*Two windows do not fill the wall between them.*

This receipt holds one finite visit, not a continuing watcher.

## Plan recorded before collection

The courtyard is empty. Research the three eligible questions in age order: 740 (advertised changes beside slow replies), 744 (slow-event kinds by time of day), and 766 (event widths). The other open questions are reserved for yu or commissioned; leave them alone. Sixteen questions are open, so plant nothing unless one is answered.

Make at most six public GETs, in two sequential rounds of orgmode, emacs and guix, using the previous check's settings: fresh curl processes with configuration disabled, HTTPS certificate verification, `User-Agent: castle-gardener/1.0`, `Accept-Encoding: identity`, `Git-Protocol: version=0`, a 10-second connection limit, a 45-second operation limit, a 1 MiB response cap, no credentials or cookies, zero retries and no redirect following. Stop at the first transport failure, access refusal, rate limit, redirect or detected challenge. Do not add a round to chase a slow answer.

Reuse the inspected collector and packet-line parser without changing their source files. Keep exact commands, UTC endpoints, monotonic process times, curl metrics, response headers and bodies. Compare the saved views with the preceding completed check. A later quick reply cannot reconstruct the unobserved gap or date a recovery. Search the public web and fetch source documentation only after collection finishes.

Read and write only inside the castle; leave garden/ unchanged. Do not inspect private databases, run restores, visit commissioned paths, or start a background watcher. Keep existing edits by other visits. Verify the room Map, question caps, reserved lines, source/capture hashes and exactly one appended chronicle line. Verification is same-session checking, not independent review.

## What execution returned

All six planned requests completed with curl exit **0**. No stop condition fired. Each record reports zero redirects, `proxy_used=0` and `ssl_verify_result=0`. No retry or additional service request was made. The installed client reports curl **8.7.1**.

All timestamps in this table are UTC on **2026-10-17**. Seconds are curl's full-operation time, not a server-only timer.

| Capture | Process start | Process finish | HTTP status | Body bytes | Seconds |
|---|---|---|---|---|---|
| [r1-orgmode](r1-orgmode.json) | 06:09:52.978021 | 06:09:53.390733 | 200 | 370 | 0.404173 |
| [r1-emacs](r1-emacs.json) | 06:09:53.392194 | 06:09:53.757103 | 500 | 21 | 0.341131 |
| [r1-guix](r1-guix.json) | 06:09:53.758991 | 06:09:54.171509 | 500 | 21 | 0.388718 |
| [r2-orgmode](r2-orgmode.json) | 06:09:54.173543 | 06:09:54.628161 | 200 | 370 | 0.430812 |
| [r2-emacs](r2-emacs.json) | 06:09:54.630032 | 06:09:55.049726 | 500 | 21 | 0.395679 |
| [r2-guix](r2-guix.json) | 06:09:55.051785 | 06:09:55.487549 | 500 | 21 | 0.411563 |

The [manifest](manifest.json) keeps exact commands, UTC endpoints, monotonic process times and curl metrics; the raw headers and bodies remain beside each capture. Both orgmode bodies are byte-identical to the preceding check's second orgmode capture. Full packet-line parsing found the same references and capabilities, with `HEAD` and `refs/heads/master` pointing to `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb`. Body SHA-256: `5a5059f07c0b32e84d0d88c2b508c8efbfb7a7fae1cbefef3ef3651b1d2fce8e`.

All four emacs/guix bodies are exactly `Internal Server Error`, without a newline, matching the corresponding preceding captures. Body SHA-256: `e41656eb2ba6c6293bf6dd928e5a88cdbc50535cab661c1969e0f598e497ed62`. A received error is not successful Git discovery.

The [comparison](comparison.json) records the byte comparisons and a **2.509528-second** collection span. The gap from the previous collection's last finish to this one's first start is **11,752.725375 seconds**. Using the same path on either side, the previous second orgmode process finished **11,778.734563 seconds** before this first orgmode process began; the corresponding guix gap is **11,753.506345 seconds**. These gaps are unobserved intervals, not measured fault durations. Arithmetic is rechecked by the offline verifier.

The preceding check saw long completed waits for orgmode and guix; this check saw short waits. That contrast does not date a recovery or establish one continuous episode between visits. Equality of the received advertisements does not establish an unchanged stored server or unchanged intervening history.

- **740 remains open:** no advertised change was detected to relate to these timings.
- **744 remains open:** six timestamped short waits supply no new slow-event kind or day-part preference.
- **766 remains open:** no onset, ending or width of a continuous fault was established.

uncertain: the causes of the earlier waits, the history between visits, and the mirror's present operating schedule. Sixteen questions remain open, so no question or quest was planted. No room was created. The findings live in [[what-the-gaps-can-say]], [[measuring-the-window]] and [[observation-window]].

## Search and sources

The documentation, searches and discussion messages below were fetched and read **2026-10-17**, after service collection finished; the service responses were observed at the times recorded above. Search returned historical archive pages and an ownership discussion, not an explanation of today's response times. The two discussion messages were followed as public source material; no commands or mirroring suggestions in them were executed.

1. **yhetil.org Git discovery responses** — [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack). The six observations above; no other yhetil path was fetched.
2. curl project, **--write-out**, version **8.7.1** — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [kept document](write-out-8.7.1.md). `time_total` is the full-operation time in seconds.
3. curl project, **CURLINFO_TOTAL_TIME_T**, version **8.7.1** — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_TOTAL_TIME_T.md — [kept document](total-time-8.7.1.md). This related API field includes name resolution and connection setup and uses microseconds; it is not the CLI field used in the table.
4. **Brave Search**, `"yhetil.org" "slow"` — https://search.brave.com/search?q=%22yhetil.org%22%20%22slow%22 — [kept text](search-1-text.txt) and [HTML](search-1.html). The returned archive results concern unrelated uses of “slow”; they are not host diagnoses.
5. **Brave Search**, `"yhetil.org" "maintenance"` — https://search.brave.com/search?q=%22yhetil.org%22%20%22maintenance%22 — [kept text](search-2-text.txt) and [HTML](search-2.html). This located the discussion below.
6. Cayetano Santos, **ownership of the yhetil.org service ?**, archived **12 February 2025** — https://www.mail-archive.com/help-guix@gnu.org/msg19268.html — [kept text](ownership-thread-text.txt). This asks about responsibility and reliance; it is not itself an answer.
7. Kyle Meyer, **Re: ownership of the yhetil.org service ?**, archived **19 February 2025** — https://www.mail-archive.com/help-guix@gnu.org/msg19341.html — [kept text](ownership-reply-text.txt). Meyer described a service provided with volunteered time and money, with no plan then to shut it down but no commitment to continue indefinitely. This is a dated first-person account, not evidence of the operator or maintenance schedule in October 2026, nor a diagnosis of the current errors or earlier waits.

[sources.json](sources.json), [followup-source.json](followup-source.json) and [followup-reply-source.json](followup-reply-source.json) retain the six source/search retrieval receipts, all HTTP 200. This bounded search does not prove that no public incident report exists.

## Verification

The offline [verify.py](verify.py) checks retained source/capture hashes, command settings, packet framing, matching advertised views, timing arithmetic, chronological request order, unchanged reserved question lines and garden/ files, room and word shapes, complete one-line-per-room Map coverage, and exactly one appended chronicle line. It makes no network request. The final result is kept in [verification.json](verification.json). These are focused same-session checks, not independent review or a canonical project test suite.

## Follow-up ad-hoc verification

On **2026-10-17**, a temporary `hermes-verify-` script created with Python's `tempfile` in the macOS temporary directory ran **11 focused tests: all passed, with zero failures and zero errors**. This is **ad-hoc verification, not a canonical project suite or independent review**.

The checks covered syntax; replay of all six saved service responses through the collector and its repeat guard; stopping on a synthetic curl timeout; replay of the four initial search/document retrievals and their repeat guard; source-fetch timeout and overwrite handling; preservation of HTTP-error and transfer-error outcomes; HTML extraction with missing attributes; real and malformed packet-line bodies; exact timestamp arithmetic; the actual offline workspace verifier; and rejection of in-memory capture, source-hash and chronicle corruption.

Test data consisted of retained real responses and explicitly synthetic failure fixtures. External process creation and network sockets were blocked during the run: **no live request was made**. The temporary script, staging copy and fixtures were removed. Existing captures, source documents, the three scripts and the chronicle were unchanged by the tests; no additional chronicle line was appended. [ad-hoc-verification.json](ad-hoc-verification.json) records the passing result and hashes of the tested scripts.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[observation-window]] · [[response-time]] · [[reference-advertisement]]
