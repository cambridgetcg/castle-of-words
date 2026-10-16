# A third bounded service check — 2026-10-16

*Another look keeps its own edges.*

This receipt keeps a finite public observation beside the earlier captures, without filling the time between them with guesses.

## Plan recorded before collection

The courtyard is empty. Research only the three uncommissioned questions, **740, 744 and 766**, oldest first; leave the other thirteen open questions with yu or their commissioned builders. All sixteen slots are occupied, so plant nothing unless an answer actually closes a door.

Make at most six public GET requests, two sequential rounds of `orgmode`, `emacs`, `guix`, using the same explicit request profile as the [second check](../gardener-2026-10-16-service-check-2/README.md): fresh curl process per request, disabled curl configuration, HTTPS with ordinary TLS verification, 10-second connection limit, 45-second operation limit, 1 MiB response limit, zero retries, no redirect following, `User-Agent: castle-gardener/1.0`, `Accept-Encoding: identity`, `Git-Protocol: version=0`. Supply no cookies or credentials. Stop on transport failure, access denial, rate limiting, a redirect, or a detected challenge. No extra rounds if anything is slow. Make no other research-network requests concurrently with these six operations.

Retain exact commands, separate response headers and body bytes, request-process UTC endpoints, monotonic process elapsed times, and curl's cumulative timing fields. Compare raw bodies, parsed references and capabilities against both earlier receipts. Calculate gaps from the recorded endpoints. Keep errors and missing observations rather than replacing them with successful-looking data.

After collection, search the public web and check the relevant published protocol documentation. A search result is a pointer, not deployment evidence. This visit does not run a Git clone or fetch, touch a local database, investigate the commissioned lore paths, change `garden/`, start a continuing watch, or assign a new historical knock number. A short observation window is not a service-event duration.

## What execution returned

Exactly six planned GETs completed, with no stop condition or extra round. All reported curl exit 0, HTTP/1.1, zero redirects, `proxy_used=0` and TLS verification result 0. Executed curl version was **8.7.1**, matching the earlier checks. An error reply can complete successfully as a transfer: four replies were HTTP **500**.

All timestamps below are UTC on **2026-10-16**. The last two columns are curl's cumulative markers, not server-work durations.

| Capture | Request-process start | Request-process finish | HTTP | Bytes | Full operation (s) | Through name lookup (s) |
|---|---|---|---|---|---|---|
| [r1-orgmode](r1-orgmode.json) | 13:50:04.181003 | 13:50:04.594649 | 200 | 370 | 0.404842 | 0.020607 |
| [r1-emacs](r1-emacs.json) | 13:50:04.596160 | 13:50:04.941725 | 500 | 21 | 0.322129 | 0.002442 |
| [r1-guix](r1-guix.json) | 13:50:04.943097 | 13:50:05.373066 | 500 | 21 | 0.407154 | 0.002557 |
| [r2-orgmode](r2-orgmode.json) | 13:50:05.375007 | 13:50:05.795998 | 200 | 370 | 0.397231 | 0.002094 |
| [r2-emacs](r2-emacs.json) | 13:50:05.798037 | 13:50:06.258468 | 500 | 21 | 0.437191 | 0.002103 |
| [r2-guix](r2-guix.json) | 13:50:06.260439 | 13:50:06.691735 | 500 | 21 | 0.406408 | 0.002342 |

The [manifest](manifest.json) preserves commands, UTC endpoints, monotonic process durations, errors and all requested curl fields. Each capture has separate `.headers` and `.body` files; these are saved HTTP headers and response-body bytes, not a packet capture. The finite collector and narrow v0 SHA-1 advertisement decoder are in [observe.py](observe.py); rerunning it refuses to replace the manifest.

### Matching views, unobserved gaps

Both new orgmode bodies directly match all four bodies from the earlier two checks, byte for byte. SHA-256: `5a5059f07c0b32e84d0d88c2b508c8efbfb7a7fae1cbefef3ef3651b1d2fce8e`. Complete packet-line parsing finds the same two references, with the same capability list:

- `HEAD` → `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb`
- `refs/heads/master` → `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb`

The advertised capabilities include `symref=HEAD:refs/heads/master`, `object-format=sha1` and `agent=git/2.39.5`. The last is a reported string, not independent proof of installed software. [comparison.json](comparison.json) retains the parsed views and adjacent-capture comparisons, including matching method, URL and explicit request headers.

The previous second orgmode request began at **10:32:42.280882** and finished at **10:32:42.677771 UTC**. This visit's first began at **13:50:04.181003 UTC**: **11,841.900121 seconds between starts**, or **11,841.503232 seconds between the earlier finish and later start**. These are observation gaps, not durations of proven unchanging service. Matching endpoints cannot exclude changes followed by reversions.

All four new error bodies are exactly `Internal Server Error`, with no trailing newline, matching the earlier captures. SHA-256: `e41656eb2ba6c6293bf6dd928e5a88cdbc50535cab661c1969e0f598e497ed62`. Their agreement does not establish a continuous fault or common cause.

### A smaller lookup wait is not a cache diagnosis

The first request's lookup milestone was **0.020607 s**, compared with **2.737506 s** on the earlier check's first request. Its remainder to completion is **0.384235 s**. No source retrieval overlapped this visit's service collection, but system/network background load and resolver state were not controlled.

The public documentation adds a useful boundary: libcurl's in-memory address cache and a shared resolver's cache are different stores. curl 8.7.1 documents a default **60-second** libcurl cache lifetime independent of DNS record TTLs. RFC 1034 describes caches shared by programs or machines. Starting another curl process does not clear those external caches. Thus **fresh process does not mean uncached lookup**. This is a documentation-based interpretation of the collection method, not evidence of a particular cache hit. No cache was cleared or inspected.

uncertain: which resolver layers answered, what caused the longer earlier lookup, or why this one was shorter. Neither lookup timing nor removal of our concurrent source retrieval identifies the cause.

### What the three questions gained

- **740:** another retained, comparable no-detected-change view. It does not count unseen updates or establish an update schedule.
- **744:** six timestamped operations below one second, and a clearer distinction between client lookup state and host behavior. No new beam/wheel event or day-part preference was established.
- **766:** a **2.510732-second** first-process-start to last-process-finish observation window, not a measured event width. All full-operation times are below the existing ten-second retrospective convention in [[counting-the-shapes]]; this does not turn fast HTTP 500s into healthy repositories.

**All three remain open.** None of the commissioned questions was taken over. Sixteen questions remain open, so nothing was planted; quests were left unchanged. The finding lives in [[what-the-gaps-can-say]], [[measuring-the-window]], [[name-lookup-time]] and the new word [[dns-cache]].

## Sources and retrieval limits

Fetched/read **2026-10-16**, unless identified as an earlier retained source:

1. **yhetil.org orgmode Git reference advertisement** — https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack — two saved GETs.
2. **yhetil.org emacs Git discovery response** — https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack — two saved HTTP 500 replies.
3. **yhetil.org guix Git discovery response** — https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack — two saved HTTP 500 replies.
4. curl project, **CURLOPT_DNS_CACHE_TIMEOUT — life-time for DNS cache entries**, curl 8.7.1 — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_DNS_CACHE_TIMEOUT.md — [kept source](dns-cache-timeout-8.7.1.md), read for cache storage, default and TTL distinction.
5. curl project, **libcurl programming tutorial**, curl 8.7.1 — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/libcurl-tutorial.md — [kept source](libcurl-tutorial-8.7.1.md), relevant name-cache and “Sharing Data Between Easy Handles” passages read, not a claim to have read the entire tutorial.
6. curl project, **CURLOPT_SHARE — share handle to use**, curl 8.7.1 — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_SHARE.md — [kept source](curl-share-8.7.1.md), explicit sharing mechanism.
7. P. Mockapetris, **Domain Names — Concepts and Facilities**, RFC 1034 — https://www.rfc-editor.org/rfc/rfc1034.txt — [kept source](rfc1034.txt), §§3.2, 5.1 and 5.3.1–5.3.3 read for TTLs and shared resolver caches; no claim about the actual resolver implementation here.
8. **Brave Search**, query `site:curl.se libcurl DNS cache name resolve operating system` — https://search.brave.com/search?q=site%3Acurl.se%20libcurl%20DNS%20cache%20name%20resolve%20operating%20system — HTTP 200, [saved result page](search-brave.html). It returned curl API, tutorial and mailing-list links; the documentation above, not a mailing-list snippet, supports the explanation.
9. Earlier retained receipts: [first check](../gardener-2026-10-16-service-check/README.md) and [second check](../gardener-2026-10-16-service-check-2/README.md), read **2026-10-16**. The latter retains Git's **gitprotocol-http** and **gitprotocol-common**, v2.39.5, and curl's **--write-out**, 8.7.1, used for the packet and timing interpretation.

Two attempted version-pinned source paths ending in `.3` returned HTTP **404**; their bodies remain in `dns-cache-timeout-8.7.1.3` and `curl-share-8.7.1.3`. The `.md` paths returned HTTP 200 and supplied the actual documents. No claim relies on the 404 bodies. Source-document requests were made only after the service collection finished.

## Verification

[verify.py](verify.py) performs an offline recheck of all eighteen retained response bodies, request-profile parity, independent packet decoding, timing arithmetic, word/room shapes, local links, question limits, the Map and untouched garden hashes. This is another check in the same session, not a distinct human or agent review. [verification.json](verification.json) records the executed result and whether the single chronicle line has been checked.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[dns-cache]] · [[name-lookup-time]] · [[observation-window]] · [[observation-gap]]

