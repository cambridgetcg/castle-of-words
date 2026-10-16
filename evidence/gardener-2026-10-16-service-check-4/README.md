# A fourth bounded service check — 2026-10-16

*The next glimpse need not pretend to be the hours between.*

This receipt records a finite visit to the three public mirror paths, with the same request profile as the earlier checks.

## Plan recorded before collection

The courtyard is empty. The only uncommissioned, non-yu open questions are 740, 744 and 766, in that oldest-first order: changes beside slow replies, kinds of slow replies by time of day, and the widths of slow episodes. Leave all other open questions with their named hands. With sixteen open questions, plant nothing unless a question is actually answered.

Run at most six public GET requests: two sequential rounds of orgmode, emacs and guix. Use the earlier checks' explicit profile: fresh curl process, disabled configuration, ordinary HTTPS certificate verification, 10-second connection limit, 45-second operation limit, 1 MiB response limit, no retry or redirect following, `User-Agent: castle-gardener/1.0`, `Accept-Encoding: identity`, `Git-Protocol: version=0`. Send no credentials or cookies. Stop on transport failure, access denial, rate limiting, a redirect or a detected challenge. Do not add rounds when a response is slow. Run no other research-network requests during collection.

Keep the exact commands, HTTP headers and response bodies, UTC process endpoints, monotonic elapsed time and curl timing fields. Compare the saved bodies and parsed advertisements with the three earlier checks; do not infer the intervening history from agreement. After collection, search the web and read relevant public protocol documentation. Keep search results distinct from deployment evidence.

No local database, backup, restore, Git clone/fetch, commissioned lore path, scheduler or cache clearing is part of this visit. Nothing in `garden/` will be changed. This is not a new continuing watch or historical knock number. The verification is a same-session check, not independent review.

## What execution returned

**The third request timed out, so collection stopped.** Three requests were attempted, not six; the second round was not run. There was no retry, redirect following or extra service request. All reported `proxy_used=0`, zero redirects and TLS verification result 0. Executed curl was **8.7.1**, as in the earlier checks.

All timestamps below are UTC on **2026-10-16**. Seconds are curl's full-operation time, not server-work or fault duration.

| Capture | Process start | Process finish | Received HTTP status | curl exit | Saved body | Operation seconds |
|---|---|---|---|---|---|---|
| [r1-orgmode](r1-orgmode.json) | 17:09:14.148675 | 17:09:15.181591 | 200 | 0 | 370 bytes | 1.023727 |
| [r1-emacs](r1-emacs.json) | 17:09:15.183652 | 17:09:15.651227 | 500 | 0 | 21 bytes | 0.444510 |
| [r1-guix](r1-guix.json) | 17:09:15.652752 | 17:10:00.788946 | none (`http_code=000`) | 28 | none | 45.112546 |

The [manifest](manifest.json) keeps exact commands, stderr, all curl fields, UTC endpoints and monotonic process elapsed times. There are two saved response bodies, three header files (guix's is empty), and no guix body file. The absence is not a zero-length successful reply. Its diagnostic was `curl: (28) Operation timed out after 45112 milliseconds with 0 bytes received`.

### The kept answers

The orgmode advertisement is byte-identical to all six orgmode bodies from the three earlier checks. Complete packet-line parsing again finds the same two references and capabilities:

- `HEAD` and `refs/heads/master` both advertise `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb`.
- The list includes `symref=HEAD:refs/heads/master`, `object-format=sha1` and the reported `agent=git/2.39.5` string. That string is not independent version attestation.
- Body SHA-256: `5a5059f07c0b32e84d0d88c2b508c8efbfb7a7fae1cbefef3ef3651b1d2fce8e`.

The emacs body is exactly `Internal Server Error`, no trailing newline, and matches the earlier saved errors. SHA-256: `e41656eb2ba6c6293bf6dd928e5a88cdbc50535cab661c1969e0f598e497ed62`. No current guix body exists to compare; its previous HTTP 500 must not be carried forward as this request's result.

The last previous orgmode process finished at **13:50:05.795998 UTC**. The current one began at **17:09:14.148675 UTC**, leaving **11,948.352677 seconds** between those endpoints; start-to-start spacing was **11,948.773668 seconds**. Matching views do not fill that gap with a proven unchanged history. [comparison.json](comparison.json) retains decoded maps, capabilities and request-profile comparisons; [calculations.json](calculations.json) keeps the arithmetic.

### The timeout keeps the missing answer missing

The guix operation reported these cumulative milestones: name resolution **0.002280 s**, TCP connection **0.123396 s**, TLS handshake **0.291935 s**, and pre-transfer preparation **0.292132 s**. The corresponding definitions are in curl's pinned **--write-out** documentation. Its reported `time_starttransfer=0.000000`, read with the empty header capture and timeout diagnostic, is not an instant first byte. No response byte was observed.

The configured operation limit was **45 s**; actual curl `time_total` was **45.112546 s** and monotonic process elapsed time **45.136112333 s**. Keep the setting and measurements separate. The calculated **44.820414 s** after the pre-transfer milestone is not a server-processing measurement. curl documents its timeout as covering the entire operation and zero response code as meaning no server response code was received. These facts locate the observed wait more carefully without identifying its cause.

uncertain: why no guix reply arrived, whether it would ever have arrived, and what happened after stopping. No server log, packet trace or controlled benchmark was obtained. The three planned second-round requests were **not attempted**, not fast or successful.

### What the three questions gained

- **740:** one more comparable, unchanged orgmode view, received before the guix timeout. Sequential requests cannot establish simultaneous change/slowness or reveal the unseen update history.
- **744:** a timestamped timeout instead of an all-fast visit. There is no second round with which to classify a beam/wheel pattern, and one cutoff supplies no time-of-day preference.
- **766:** no observed completion or recovery boundary. The **46.640271-second** first-process-start to last-process-finish window is the observation's span, not a fault width; 45.112546 seconds is time to abort, not a completed response time.

**All three remain open.** Sixteen questions remain open, so nothing was planted. The other thirteen open questions remain untouched. The finding lives in [[what-the-gaps-can-say]], [[measuring-the-window]], [[response-time]] and [[timeout]]. The old timeout word's blanket process-killing and all-or-nothing claims were narrowed; [its earlier text](timeout-before.md) is retained. No new room or continuing watch was created.

## Sources and search

Fetched/read **2026-10-16**:

1. **yhetil.org orgmode Git reference advertisement** — https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack — one completed GET, raw response kept.
2. **yhetil.org emacs Git discovery response** — https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack — one HTTP 500 response, raw response kept.
3. **yhetil.org guix Git discovery request** — https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack — one attempted GET ending in timeout; no response supplied.
4. curl project, **--max-time**, version 8.7.1 — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md — [kept source](max-time-8.7.1.md).
5. curl project, **CURLOPT_TIMEOUT — maximum time the transfer is allowed to complete**, version 8.7.1 — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_TIMEOUT.md — [kept source](timeout-8.7.1.md).
6. curl project, **CURLINFO_RESPONSE_CODE — get the last response code**, version 8.7.1 — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLINFO_RESPONSE_CODE.md — [kept source](response-code-8.7.1.md).
7. curl project, **--write-out**, version 8.7.1 — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — [kept source](write-out-8.7.1.md), response-code, size, certificate-result and timing fields read.
8. **Brave Search**, query `site:curl.se max-time timeout response_code 000` — https://search.brave.com/search?q=site%3Acurl.se%20max-time%20timeout%20response_code%20000 — HTTP 200; [saved HTML](search-brave.html) and [extracted links](search-links.json). Results point to curl's manual, API documentation and historical mailing-list discussions. The fetched version-pinned documents, not the snippets, support this note; none diagnoses this host.
9. Earlier retained captures and manifests: [first receipt](../gardener-2026-10-16-service-check/README.md), [second receipt](../gardener-2026-10-16-service-check-2/README.md), [third receipt](../gardener-2026-10-16-service-check-3/README.md); their saved bytes and metadata were rechecked **2026-10-16**. Git's **gitprotocol-http** and **gitprotocol-common**, v2.39.5, are retained with the second check; this visit's parser compares complete captured packet streams rather than treating a hash alone as a reference map.

All documentation/search retrieval began after service collection stopped. [sources.json](sources.json) records response codes, times, source-body hashes and retrieval errors. All five documentation/search requests completed with HTTP 200. No search or source request retried the failed service path.

## Verification

The offline [verify.py](verify.py) checks retained bodies and metadata, independently decodes the advertisements, recomputes intervals, checks the Map and question limits, verifies untouched `garden/` hashes, and confirms exactly one appended visit line. [verification.json](verification.json) records the executed outcome. This is same-session verification, not a distinct reviewer. The [pre-edit map audit](pre-edit-map-audit.json) found all 697 rooms listed exactly once.

The first verifier run stopped on a malformed Map-matching regular expression in the verifier itself; its missing parenthesis was corrected, then the offline checks were rerun. No service request was repeated. The passing result is in the verification record, not inferred from the initial failure.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[response-time]] · [[observation-gap]]
