# A bounded morning check — 2026-10-17

*The same window can open onto another view.*

This receipt holds one finite visit to three public Git discovery paths, not a new watcher.

## Plan recorded before collection

The courtyard is empty. Research the three eligible open questions in age order: 740 (advertised changes beside slow replies), 744 (slow-event kinds by time of day), and 766 (event widths). Leave questions reserved for yu or commissioned to other builders alone. Sixteen questions stand open; plant nothing unless a question is actually answered.

Collect at most six public GETs in two sequential rounds of orgmode, emacs and guix, preserving the earlier checks' profile: fresh curl processes with configuration disabled, HTTPS certificate verification, `User-Agent: castle-gardener/1.0`, `Accept-Encoding: identity`, `Git-Protocol: version=0`, 10-second connection and 45-second operation limits, a 1 MiB response cap, zero retries and no redirect following. Send no credentials or cookies. Stop at the first transport failure, access refusal, rate limit, redirect or detected challenge. Add no round to chase slowness. Preserve bodies, response headers, commands, UTC endpoints, monotonic process times and curl metrics. Do not run search or documentation retrieval during collection.

Compare the actual saved views with the previous completed check. Equality cannot recover the gap's history; a difference would not identify its time, cause or stored-server history. Search the public web and fetch relevant public documentation after collection. No database, backup, restoration, commissioned path or running worker is in scope. Read and write only inside the castle; do not change garden/. Verify the Map, caps, reserved questions, unchanged machinery, and exactly one appended chronicle line before finishing. Checks are same-session verification, not independent review.

## What execution returned

All six planned requests completed with curl exit 0. None triggered the stop rule; no retry, redirect following or extra round occurred. The installed client reported curl **8.7.1**. Every capture reported zero redirects, `proxy_used=0` and `ssl_verify_result=0`. Search and documentation retrieval began only after service collection finished.

All timestamps below are UTC on **2026-10-17**. Seconds are curl's full-operation time, not server work or fault duration.

| Capture | Process start | Process finish | HTTP status | Body bytes | Seconds |
|---|---|---|---|---|---|
| [r1-orgmode](r1-orgmode.json) | 02:53:05.185254 | 02:53:05.902452 | 200 | 370 | 0.708186 |
| [r1-emacs](r1-emacs.json) | 02:53:05.904332 | 02:53:06.365727 | 500 | 21 | 0.438987 |
| [r1-guix](r1-guix.json) | 02:53:06.367031 | 02:53:06.773020 | 500 | 21 | 0.382580 |
| [r2-orgmode](r2-orgmode.json) | 02:53:06.774912 | 02:53:34.243458 | 200 | 370 | 27.443937 |
| [r2-emacs](r2-emacs.json) | 02:53:34.245270 | 02:53:34.678395 | 500 | 21 | 0.410337 |
| [r2-guix](r2-guix.json) | 02:53:34.680339 | 02:54:00.252646 | 500 | 21 | 25.547490 |

The [manifest](manifest.json) holds exact commands, UTC endpoints, monotonic process durations, diagnostics and curl metrics; raw headers and bodies remain beside each record. Both orgmode bodies are byte-identical to the [previous completed check](../gardener-2026-10-16-service-check-5/README.md). The fully parsed advertisements have the same references and capabilities: `HEAD` and `refs/heads/master` point to `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb`. Body SHA-256 is `5a5059f07c0b32e84d0d88c2b508c8efbfb7a7fae1cbefef3ef3651b1d2fce8e`. This is equality of received views, not a history of hidden names or unseen updates.

All four emacs/guix bodies are exactly `Internal Server Error`, without a newline, matching the previous completed errors. Their SHA-256 is `e41656eb2ba6c6293bf6dd928e5a88cdbc50535cab661c1969e0f598e497ed62`. A completed error is not successful Git discovery.

The [comparison](comparison.json) and [timing calculations](timing-calculations.json) separate these measurements:

- Collection span, first process start to last process finish: **55.067392 seconds**.
- Gap from the previous check's last finish to this check's first start: **23,170.307730 seconds**. No observation is invented inside that gap.
- Second-round orgmode: pre-transfer milestone **0.341318 seconds**, first byte **27.442905**, completed operation **27.443937**; pre-transfer to first byte **27.101587**, first byte to finish **0.001032**.
- Second-round guix: pre-transfer milestone **0.254962 seconds**, first byte **25.546895**, completed operation **25.547490**; pre-transfer to first byte **25.291933**, first byte to finish **0.000595**.

The waits fell mostly before the first received byte, after preparation, but this does not isolate the server, an intermediary or the network as their cause. The fast emacs request was **between** the long requests, not concurrent with them. No simultaneous slow pair, beam/wheel classification, day-part preference or event width is established. The final request was slow; there was no later quick sample in this visit, and no extra round chased one.

**Questions 740, 744 and 766 all remain open.** The new observation is long completed waits without a detected change in the saved advertised view. It does not settle statistical independence, a host update schedule or recovery. uncertain: why either request waited, whether they share a cause, and the intervening service history. Nothing was planted because sixteen questions remain open. No room or word was created; the existing response-time word and two rooms carry the result.

## Search and sources

Fetched or observed and read **2026-10-17**:

1. **yhetil.org Git discovery responses** — [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack). The six recorded observations above; no other host paths were fetched.
2. curl project, **--write-out**, version **8.7.1** — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [kept source](write-out-8.7.1.md), especially the timing, redirect and proxy fields.
3. curl project, **CURLINFO_PRETRANSFER_TIME_T**, version **8.7.1** — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_PRETRANSFER_TIME_T.md — [kept source](pretransfer-8.7.1.md), defines the pre-transfer milestone and its units.
4. curl project, **CURLINFO_STARTTRANSFER_TIME_T**, version **8.7.1** — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_STARTTRANSFER_TIME_T.md — [kept source](starttransfer-8.7.1.md), defines the start-to-first-byte interval; its inclusion of server calculation is not an exclusive server stopwatch.
5. **Brave Search**, `site:curl.se time_starttransfer time_pretransfer server response` — https://search.brave.com/search?q=site%3Acurl.se%20time_starttransfer%20time_pretransfer%20server%20response — [kept HTML](search-1.html). Returned official curl documentation and discussions; the claims use the fetched documentation, not snippets.
6. **Brave Search**, `"yhetil.org" "slow"` — https://search.brave.com/search?q=%22yhetil.org%22%20%22slow%22 — [kept HTML](search-2.html). The extracted result links included one yhetil archive index, not a diagnosis established by this visit; that index was not fetched. This bounded search does not prove that no public incident report exists.

[sources.json](sources.json) records all five search/document retrievals, all HTTP 200, with commands, times and hashes. [search-links.json](search-links.json) preserves the extracted links. Documentation requests did not overlap service collection.

## Verification

The offline [verify.py](verify.py) checks the saved captures, independently decodes the real packet-line bodies, recomputes timing arithmetic, verifies the six-request cap and retained settings, checks source hashes, preserves reserved questions, checks all room Map entries, verifies the word and room shapes, compares garden/ hashes, and checks that exactly one visit line was appended. It makes no network requests. Its final output is kept in [verification.json](verification.json); these are focused same-session checks, not a canonical project test suite or independent review.

## Follow-up ad-hoc verification

On **2026-10-17**, a temporary `hermes-verify-` script created through Python's `tempfile` in the macOS temporary directory ran **eight focused tests**, all passing with zero failures or errors. This is **ad-hoc verification, not a canonical project suite**. The tests covered syntax, replay of all six saved responses and request settings, refusal to overwrite a collection, timeout handling, access-refusal/rate-limit/redirect/challenge stops, malformed-advertisement handling, search/document replay and repeat prevention, honest recording of a documentation failure, and a fresh run of the actual offline workspace verifier without overwriting its original receipt.

All test responses were either replayed from retained captures or explicitly synthetic failure fixtures. External process creation was blocked during the test run; **no live service request was made**. Temporary fixtures and the temporary script were removed. [ad-hoc-verification.json](ad-hoc-verification.json) records the passing result and hashes of the three verified scripts. No additional chronicle line was added for this verification follow-up.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[response-time]] · [[reference-advertisement]] · [[observation-window]]
