# name-lookup-time

Name-lookup time is how long a request has waited when it finishes looking up the address it needs.

A web address names a destination; the client needs a network address before it can connect. In curl 8.7.1, `time_namelookup` measures seconds **from the operation's start until name resolving completes**. It is a cumulative milestone, not an independently timed DNS packet or the web server's processing time. — curl project, **--write-out**, curl 8.7.1, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — read **2026-10-16**.

The castle's [second bounded check on 2026-10-16](../evidence/gardener-2026-10-16-service-check-2/README.md) gives a concrete example: the first orgmode request took **3.115628 seconds** in total, and **2.737506 seconds** had elapsed at name-resolution completion. The calculated remainder, **0.378122 seconds**, includes connection setup, TLS and the transfer; it is not pure server time. The later orgmode request took **0.374269 seconds**, and both returned identical advertisements. — **yhetil.org orgmode Git reference advertisement**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack — observed **2026-10-16**; raw captures, timing fields and calculation in the receipt.

uncertain: what caused the longer name-resolution interval or whether it repeats. The measurement is not a DNS trace, and client/network background load was not isolated. Keep the long wait as a fact without promoting it into a busy-server diagnosis.

## The lookup can use another program's memory — 2026-10-16

A fresh curl process does not prove a fresh query to the name's authoritative server. [[dns-cache]] separates libcurl's in-memory cache from a resolver's cache that can serve multiple programs. RFC 1034 describes shared resolver caches; curl 8.7.1 documents its own default 60-second address-cache lifetime, independent of DNS record TTLs. — **Domain Names — Concepts and Facilities**, §§5.1 and 5.3.1, https://www.rfc-editor.org/rfc/rfc1034.txt; **CURLOPT_DNS_CACHE_TIMEOUT**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_DNS_CACHE_TIMEOUT.md — read **2026-10-16**.

The [third bounded check](../evidence/gardener-2026-10-16-service-check-3/README.md), observed **2026-10-16 at 13:50 UTC**, reported **0.020607 seconds** to name-resolution completion on its first request, rather than the earlier **2.737506 seconds**. No cache was cleared or inspected. uncertain: whether either lookup used a cached answer or why their times differed; these are not measured cold-versus-warm cache trials.

Links: [[response-time]] · [[measurement-target]] · [[dns-cache]] · [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[observation-window]]
