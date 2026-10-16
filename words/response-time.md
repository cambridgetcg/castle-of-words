# response-time

Response time is how long a request takes between the start and finish you choose to measure.

A request is a question sent to another computer. Waiting for its first byte and waiting for its whole answer measure different stretches. Neither is automatically the time that computer spent doing the work.

In libcurl, `CURLINFO_TOTAL_TIME_T` includes name lookup and connection setup as well as the transfer. `CURLINFO_STARTTRANSFER_TIME_T` ends when libcurl receives the first byte; it includes preparation and the server's calculation time. Both add the times of followed redirects. Their documented unit is microseconds. — curl project, **CURLINFO_TOTAL_TIME_T**, https://curl.se/libcurl/c/CURLINFO_TOTAL_TIME_T.html, and **CURLINFO_STARTTRANSFER_TIME_T**, https://curl.se/libcurl/c/CURLINFO_STARTTRANSFER_TIME_T.html — read **2026-10-15**.

**The castle's recording rule:** keep the named timing field, its unit, the request it belongs to, and whether the transfer completed. A long client wait is evidence of a long client wait, not by itself a diagnosis of a busy server. [[what-the-gaps-can-say]] explains the boundary; [[measuring-the-window]] distinguishes a request's wait from the lifetime of a fault. This is a documentation-based rule, not a timing test performed here. — gardener's synthesis, **2026-10-15**.

## A measured example — 2026-10-16

The [second bounded service check](../evidence/gardener-2026-10-16-service-check-2/README.md) returned an orgmode advertisement in **3.115628 seconds**, with **2.737506 seconds** already elapsed at name-resolution completion. The same saved body arrived in **0.374269 seconds** on the next round. [[name-lookup-time]] keeps the cumulative milestone separate from the total wait and from server processing. — **yhetil.org orgmode Git reference advertisement**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, observed **2026-10-16**; curl project, **--write-out**, curl 8.7.1, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, read **2026-10-16**. uncertain: the cause of the longer lookup interval; this was not an isolated-client benchmark.

## A stopped wait is not a finished answer — 2026-10-16

The [fourth bounded check](../evidence/gardener-2026-10-16-service-check-4/README.md) ended its guix request at a [[timeout]]: curl reported **45.112546 seconds**, exit **28**, and zero bytes received, with no saved response body or received HTTP status. That is an observed time to abort, not a completed response time. Its `time_starttransfer=0.000000` must not be read as an instant reply. — **yhetil.org guix Git discovery request**, https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack, observed **2026-10-16**; curl project, **--write-out**, version 8.7.1, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md, relevant timing fields read **2026-10-16**. uncertain: whether or when an answer would have arrived without the cutoff.

Links: [[timeout]] · [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[measurement-target]] · [[name-lookup-time]] · [[observation-window]] · [[http-redirect]] · [[latency-weather]]
