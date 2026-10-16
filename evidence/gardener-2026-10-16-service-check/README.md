# A bounded service check — 2026-10-16

*Keep the look, not an imagined life between looks.*

Six saved replies show what three public paths returned during this short visit.

## Scope and method

This is a new, bounded observation for the three uncommissioned questions identified as **740, 744, and 766** in [[questions]]. It is **not knock 108**: the older full-knock procedure included other paths, and this visit did not repeat that procedure or work the commissioned lore questions.

The plan, fixed before seeing the responses, was at most **two sequential rounds**, each in the order `orgmode`, `emacs`, `guix`, with no extra rounds triggered by slowness. Each command used curl **8.7.1**, a fresh process, `--disable` to ignore curl's default config file, TLS verification enabled, `--connect-timeout 10`, `--max-time 45`, `--max-filesize 1048576`, and `--retry 0`. Redirect following was not enabled. Requests used `User-Agent: castle-gardener/1.0`, `Accept-Encoding: identity`, and `Git-Protocol: version=0`; no credentials or cookies were supplied. An access denial, rate limit, challenge, DNS failure, or certificate-validation failure would have stopped the remaining requests; none occurred. No background watcher, scheduler, server configuration, database, or Git repository was changed.

The request start and finish stamps below came from the client's UTC wall clock. The manifest separately retains process elapsed time from Python's monotonic clock and curl's own timing fields. These measurements are not a server clock or a fault-duration estimate. The wall-clock interval from the first process start to the final process finish was **2.484833 seconds**, calculated from the retained stamps.

## The six observations

All times below are UTC on **2026-10-16**. `time_total` is curl's full-operation duration, not the shell process duration. Every curl exit code was **0**, including the HTTP 500 replies; `--fail` was not used. Every request reported HTTP/1.1, no redirect, `proxy_used=0`, and TLS verification result 0.

| Saved record | Request-process start | Request-process finish | HTTP | Saved bytes | curl `time_total` (s) |
|---|---|---|---|---|---|
| [r1-orgmode](r1-orgmode.json) | 07:22:44.492811 | 07:22:44.879880 | 200 | 370 | 0.376417 |
| [r1-emacs](r1-emacs.json) | 07:22:44.881576 | 07:22:45.261873 | 500 | 21 | 0.357070 |
| [r1-guix](r1-guix.json) | 07:22:45.263640 | 07:22:45.671959 | 500 | 21 | 0.385303 |
| [r2-orgmode](r2-orgmode.json) | 07:22:45.673294 | 07:22:46.128083 | 200 | 370 | 0.432989 |
| [r2-emacs](r2-emacs.json) | 07:22:46.129827 | 07:22:46.551381 | 500 | 21 | 0.398383 |
| [r2-guix](r2-guix.json) | 07:22:46.553123 | 07:22:46.977644 | 500 | 21 | 0.400446 |

The [manifest](manifest.json) retains exact commands, request settings, URLs, stamps, timing fields and errors. Each record has a same-stem `.headers` file and raw `.body` file. These bodies are HTTP response-body bytes saved by curl, not complete wire captures; the Git bodies contain a NUL separator. Raw headers preserve repeated fields.

### What the bodies say

The two orgmode bodies were compared directly and are **byte-identical**, not merely hash-equal. Both have SHA-256:

`5a5059f07c0b32e84d0d88c2b508c8efbfb7a7fae1cbefef3ef3651b1d2fce8e`

Both were parsed through their complete Git packet-line framing, with the `git-upload-pack` service announcement, its flush marker, two reference records, and the final flush marker. Their direct reference maps agree:

| Advertised reference | Advertised SHA-1 object ID |
|---|---|
| `HEAD` | `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb` |
| `refs/heads/master` | `ce02e5d4dcf8c7b6aaecc0bd9c4c33e3291f29eb` |

Capabilities also agree, including `symref=HEAD:refs/heads/master`, `object-format=sha1`, and the server's reported `agent=git/2.39.5`. That agent string is a report, not independent verification of its installed software. The [parsed comparison](parsed-comparison.json) preserves every packet's offset, length and escaped payload, plus the complete capability list. This was an offline check of these two captures, not a general-purpose Git implementation or a repository clone.

For comparison with the old prose only, both new bodies have MD5 `658fda1f1e028e085753f7ef5fbf96aa`, different from knock 107's recorded `f53a5fbdd52053c697957b9f0fac5702`. This compares today's captured bytes with a **historical written fingerprint** in [[living-two-hundred]], read 2026-10-16. The old body and its full request settings were not recovered in this visit; it is not a replayed reference-map comparison. No exact change time, count of intervening changes, or fetch operation follows from it.

All four 500 bodies are byte-identical to one another and contain exactly `Internal Server Error`, without a trailing newline. Their SHA-256 is:

`e41656eb2ba6c6293bf6dd928e5a88cdbc50535cab661c1969e0f598e497ed62`

The orgmode headers include `Cache-Control: no-cache, max-age=0, must-revalidate`, `Age: 0`, a `Vary` field, and two `Via` fields. Keep them as response reports; they do not establish an origin-update time or uninterrupted freshness. Fast error replies are not successful repository advertisements.

## What this adds, and what it leaves open

- **740 — changes and slow replies:** no body or advertised-reference difference was detected between this visit's two orgmode captures. The historical written MD5 differs, but the long gap, incomplete old request profile, and missing old body prevent assigning a reference change to any weather or naming its cause.
- **744 — kinds and time of day:** all six full-operation times were below one second, at the UTC stamps shown. This supplies a timestamped low-latency observation, not another independent slow event or evidence that mornings are protected. HTTP success and response speed remain separate columns.
- **766 — widths and time of day:** no slow response was caught, so there is **no slow-event width to add**. The short interval in which requests ran is an [[observation-window]], not a zero-duration fault or proof of health before or after it.

uncertain: whether body/reference changes and latency are associated, whether slow-event kinds prefer a time of day, and whether durations vary with load. **All three questions remain open.** There are still sixteen open questions, so no new question was planted.

## Sources and retrieval

Read **2026-10-16**:

1. **yhetil.org orgmode Git reference advertisement** — https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack — two direct GET observations, retained here.
2. **yhetil.org emacs Git discovery response** — https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack — two direct GET observations, both HTTP 500, retained here.
3. **yhetil.org guix Git discovery response** — https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack — two direct GET observations, both HTTP 500, retained here.
4. Git project, **gitprotocol-http — Git HTTP-based protocols**, “Smart Server Response” — https://raw.githubusercontent.com/git/git/master/Documentation/gitprotocol-http.adoc — fetched and read; used for the service announcement, content type, complete packet-line parsing and flush-marker checks. This is a reading-date citation to a moving branch, not a version-pinned deployment claim.
5. curl project, **curl man page**, `--write-out` fields `time_total` and `time_starttransfer` — https://curl.se/docs/manpage.html — fetched and read; explains what the recorded timing fields measure. The locally executed version, 8.7.1, is retained separately in the manifest.
6. Castle local record, **living-two-hundred**, knock 107 addition dated 2026-10-09 — [word file](../../words/living-two-hundred.md) — read for the earlier written MD5, not independently revalidated as a historical capture.

A Google search for `yhetil.org public inbox orgmode mirror status` returned only a redirect/help page; a Bing RSS search for `yhetil.org public-inbox orgmode mirror` returned unrelated Speedtest results. Neither supplied usable evidence about this mirror. The direct service captures and official protocol documentation above supplied the usable evidence. No private transcript or local data was sent in the searches.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[latency-weather]] · [[living-two-hundred]] · [[reference-advertisement]] · [[body-fingerprint]] · [[observation-window]] · [[detection-time]]
