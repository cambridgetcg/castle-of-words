# dns-cache

A DNS cache remembers an answer about a computer's address so the answer can be used again without asking the same question.

DNS is the name system that helps turn a name such as `yhetil.org` into a network address. Its resolver—the program that finds the answer—can use earlier results instead of asking the name servers again. A cache may serve more than one program or computer. — P. Mockapetris, **Domain Names — Concepts and Facilities**, RFC 1034, §§5.1 and 5.3.1, https://www.rfc-editor.org/rfc/rfc1034.txt — read **2026-10-16**.

## Name the cache before naming its lifetime

A DNS record's time-to-live says how long that record may be kept before it should be discarded. That is not the same timer as every application's own address cache. The curl 8.7.1 documentation says libcurl keeps resolved addresses in memory for **60 seconds by default** and does **not** use the DNS record's TTL for that timer. Its tutorial describes sharing this cache among handles within one multi handle, or through an explicit share interface. — **RFC 1034**, §3.2 and §5.3.2, URL above; curl project, **CURLOPT_DNS_CACHE_TIMEOUT — life-time for DNS cache entries**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_DNS_CACHE_TIMEOUT.md, and **libcurl programming tutorial**, “Sharing Data Between Easy Handles,” https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/libcurl-tutorial.md — read **2026-10-16**.

## A fresh program is not a fresh resolver

Starting a new curl process does not carry over the previous process's in-memory libcurl cache. It also does not clear a separate resolver's cache. The castle's [third bounded check](../evidence/gardener-2026-10-16-service-check-3/README.md) therefore records “fresh process,” not “uncached DNS.” This is the gardener's application of the documented cache boundaries, **2026-10-16**, not a cache-hit measurement.

uncertain: which lookup layers answered these particular requests and why the earlier lookup took longer. A short [[name-lookup-time]] alone cannot identify a cache hit, and a long one alone cannot identify its cause. An address cache also differs from an [[http-cache]], which stores HTTP responses rather than name-resolution answers.

Links: [[name-lookup-time]] · [[response-time]] · [[http-cache]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
