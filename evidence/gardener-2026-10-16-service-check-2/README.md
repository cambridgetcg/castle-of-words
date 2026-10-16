# A second bounded service check — 2026-10-16

*Keep the same small ruler beside the next look.*

This visit compares new public replies with the six raw captures kept earlier today.

## Plan recorded before collection

Research only the three uncommissioned open questions, **740, 744 and 766**, in their existing order. The courtyard was empty. All other open questions explicitly wait for yu or a commission; none is taken over here.

At most two sequential rounds, each `orgmode`, `emacs`, `guix`, using the same three yhetil.org Git-discovery URLs and curl request settings as the [earlier receipt](../gardener-2026-10-16-service-check/README.md). Each request uses a fresh curl process, `--disable`, TLS verification, HTTPS only, a 10-second connection limit, a 45-second operation limit, a 1 MiB response limit, zero retries, no redirect following, `User-Agent: castle-gardener/1.0`, `Accept-Encoding: identity`, and `Git-Protocol: version=0`. No cookies or credentials are supplied. Stop the remaining requests on transport failure, access denial, rate limit, redirect, or a detected challenge; do not add rounds because a reply is slow.

Keep exact commands, response headers and bodies, UTC request-process start and finish, monotonic process elapsed time, curl timing fields and errors. Compare saved bytes directly and parse complete successful Git advertisements offline. Compare the new records with the earlier raw captures only when their request profiles and successful response types match. Treat fingerprints as fingerprints, not as an event counter.

This is not a full historical knock, not a continuous monitor, and not a new schedule. No commissioned lore paths, local repositories, databases, storage mounts, or garden machinery are changed. The request limit does not promise a new event or a settled answer.

## What execution returned

The six planned GETs completed; no stop condition occurred and no extra service requests were made. Executed curl version: **8.7.1**, the same version as the earlier visit. All curl exit codes were **0**, all responses reported HTTP/1.1, zero redirects, `proxy_used=0`, and TLS verification result 0. A completed transfer is not a successful repository response: emacs and guix returned HTTP **500**.

All timestamps below are UTC on **2026-10-16**. Seconds are curl's `time_total`, not process duration or fault lifetime.

| Capture | Request-process start | Request-process finish | HTTP | Body bytes | Full operation (s) |
|---|---|---|---|---|---|
| [r1-orgmode](r1-orgmode.json) | 10:32:38.342157 | 10:32:41.465381 | 200 | 370 | 3.115628 |
| [r1-emacs](r1-emacs.json) | 10:32:41.466975 | 10:32:41.892148 | 500 | 21 | 0.401377 |
| [r1-guix](r1-guix.json) | 10:32:41.893933 | 10:32:42.279308 | 500 | 21 | 0.363299 |
| [r2-orgmode](r2-orgmode.json) | 10:32:42.280882 | 10:32:42.677771 | 200 | 370 | 0.374269 |
| [r2-emacs](r2-emacs.json) | 10:32:42.679617 | 10:32:43.114721 | 500 | 21 | 0.410550 |
| [r2-guix](r2-guix.json) | 10:32:43.116594 | 10:32:43.557327 | 500 | 21 | 0.416665 |

The [manifest](manifest.json) retains commands, settings, UTC stamps, monotonic process durations and curl fields. Each same-stem `.headers` and `.body` file keeps the response headers and body separately. Headers retain duplicate fields; saved bodies are curl's HTTP response-body bytes, not complete wire captures. [observe.py](observe.py) is the finite collector and offline comparison used in this visit; it refuses to overwrite an existing manifest.

### Matching captured views across a real gap

Both new orgmode bodies are directly **byte-identical** to both earlier orgmode bodies, not merely hash-equal. Their SHA-256 is `5a5059f07c0b32e84d0d88c2b508c8efbfb7a7fae1cbefef3ef3651b1d2fce8e`. Full packet-line parsing consumes each body and checks the service announcement, flush markers, references and capabilities. Every capture advertises:

| Reference | SHA-1 object ID |
|---|---|
| `HEAD` | `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb` |
| `refs/heads/master` | `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb` |

Capabilities also agree, including `symref=HEAD:refs/heads/master`, `object-format=sha1`, and the reported `agent=git/2.39.5`. That agent string is not independent verification of the installed software. The [parsed comparison](parsed-comparison.json) retains packets, maps, capability lists, direct comparison results, and the compared request profiles. This deliberately narrow decoder handles these captured v0 SHA-1 advertisements; it is not a general Git client.

The earlier second orgmode request began at **07:22:45.673294 UTC** and finished at **07:22:46.128083 UTC**. The later first request began at **10:32:38.342157 UTC**: **11,392.668863 seconds between starts**, with **11,392.214074 seconds between the earlier process finish and the later process start**. Those endpoints identify the comparison gap, not an interval of proven unchanged service. No intervening reference changes, reversions, fetches or latency events can be counted from matching views alone.

All four new 500 bodies are byte-identical to one another and to the earlier saved error body: exactly `Internal Server Error`, without a trailing newline, SHA-256 `e41656eb2ba6c6293bf6dd928e5a88cdbc50535cab661c1969e0f598e497ed62`. Matching error text does not establish a continuing fault or a shared cause.

### The first wait was not all at the server

The first orgmode operation took **3.115628 s**, so it must not be called sub-second. curl reported **`time_namelookup=2.737506 s`**: most of the measured operation had already elapsed when name resolution completed. Subtraction leaves **0.378122 s** from that marker to completion; it includes connection setup, TLS and the remaining transfer, not just server processing. The other five full operations took **0.363299–0.416665 s**.

These are cumulative client-side timing markers, not a DNS packet trace. Separate public-document/search retrieval was launched alongside the service collection; client and network background load were not isolated. uncertain: why name resolution took longer on this request, which component caused that wait, or whether this recurs. No extra DNS probe or diagnostic traffic was added.

For comparison only, the existing retrospective table in [[counting-the-shapes]] calls a response slow at **10 seconds or more**; all six new observations are below that convention. This threshold was not chosen in the collection plan and is not a natural boundary. No independent beam/wheel event is inferred, and the first operation's difference is retained rather than hidden behind the threshold.

### What the three questions gained

- **740:** an actual like-profile, raw-body and parsed-reference comparison across visits, with **no detected difference**. This is stronger than comparing an old written fingerprint with a new capture, but it does not establish no intervening changes or explain a mirror's schedule.
- **744:** a timestamped observation whose first operation differs from its neighbors mainly before name-resolution completion. It supplies no new beam/wheel classification, equal day-part coverage, or evidence of a host's working hours.
- **766:** the first request-process start to the last finish spans **5.215170 s**. That is an observation window, not a continuous slow spell or fault width. No comparable event duration was measured.

uncertain: whether reference changes and response delays are associated, whether delay kinds favor a time of day, and whether event durations track load. **All three questions remain open.** There are sixteen open questions, so none was planted. No new full knock number or continuing watch was created.

## Sources, searches and limits

Read **2026-10-16**:

1. **yhetil.org orgmode Git reference advertisement** — https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack — two GETs, saved here; compared with the earlier receipt's two raw captures.
2. **yhetil.org emacs Git discovery response** — https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack — two GETs, HTTP 500.
3. **yhetil.org guix Git discovery response** — https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack — two GETs, HTTP 500.
4. Git project, **gitprotocol-http — Git HTTP-based protocols**, v2.39.5, “Smart Server Response” — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-http.txt — service, content-type and complete packet-line checks. Saved as [git-http-v2.39.5.txt](git-http-v2.39.5.txt). The versioned documentation is a protocol reference, not a deployment attestation.
5. Git project, **gitprotocol-common — Things common to various protocols**, v2.39.5, “pkt-line Format” — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-common.txt — length, binary data and flush-packet definitions. Saved as [git-common-v2.39.5.txt](git-common-v2.39.5.txt).
6. curl project, **--write-out**, curl 8.7.1 — https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — `time_namelookup`, connection, first-byte and total-time definitions for the executed version. Saved as [curl-write-out-8.7.1.txt](curl-write-out-8.7.1.txt).
7. Castle local record, **A bounded service check — 2026-10-16**, [earlier receipt](../gardener-2026-10-16-service-check/README.md), its manifest and raw captures; **counting-the-shapes**, [declared retrospective threshold](../../rooms/counting-the-shapes.md). These are retained local measurements and conventions, not new public standards.

A Bing RSS search for `"yhetil.org" "orgmode"` returned unrelated café results; it supplied no mirror evidence. The alternative **Brave Search, `"yhetil.org" orgmode mirror`**, https://search.brave.com/search?q=%22yhetil.org%22%20orgmode%20mirror, returned relevant mirror-directory, mirroring-instruction and historical mailing-list links. The returned results supplied no operating schedule, load measurements or explanation of today's wait. Only the search result page was read in that pass; no linked deployment claim was adopted. [sources.json](sources.json) and [search-brave.json](search-brave.json) keep retrieval receipts; both search responses are saved. The six service captures and fetched official specifications supply the findings above.

## Verification

An independent offline read of the Git packet stream, all twelve retained body-size/hash checks, explicit request-profile parity, timing arithmetic, and local structure checks passed. The Map contains all **697 rooms exactly once**; **16 questions** remain open, only 740/744/766 gained observations, and the baseline comparison found **garden/ unchanged**. [verify.py](verify.py) makes no network calls; [verification.json](verification.json) records its result and whether the single final chronicle line has been checked. Earlier chronicle bytes are checked against their pre-visit hash rather than reconstructed.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[reference-advertisement]] · [[body-fingerprint]] · [[name-lookup-time]] · [[response-time]] · [[observation-window]] · [[observation-gap]]
