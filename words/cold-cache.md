# cold-cache

A cold cache has no saved answer it can use for the question being asked.

A cache keeps earlier work so it need not all be done again. Here, **cold** names the state of a specified cache for a specified lookup, not the age of the program asking. An entry can be absent or no longer usable; another cache farther along the path may still have an answer. This is the tender's scoped working definition, drawn from the cache boundaries below, not a universal benchmark protocol.

## Name the cupboard before calling it empty

A [[dns-cache]] stores name-resolution answers; an [[http-cache]] stores web replies. Even within DNS, libcurl's in-memory cache and a resolver's shared cache are separate stores. RFC 1034 describes caches shared across processes, users and machines; curl's pinned documentation describes its own in-memory address reuse. Starting a fresh curl process does not establish that the resolver has forgotten an earlier answer. — sources [1–2], with the process-boundary inference recorded in [[measuring-the-window]] and [[what-the-gaps-can-say]].

A useful cold-cache claim therefore names **which store, which lookup, and what evidence shows that no reusable answer was present there**. A fresh process, a request to avoid HTTP cache reuse, and an uncached DNS lookup are different claims. A short [[name-lookup-time]] does not prove a cache hit, and a long one does not prove a miss or identify the cause of the wait. — tender's application of [1–2] and the local rooms, 2026-10-16.

uncertain: which caches answered the castle's recorded requests. This tending read the kept documents and notes; it did not inspect or clear any cache, run a benchmark, or make a service request.

## Sources

Kept copies read locally **2026-10-16**; no new source fetch was made:

1. P. Mockapetris, **Domain Names — Concepts and Facilities**, RFC 1034, §5.1 — [kept text](../evidence/gardener-2026-10-16-service-check-3/rfc1034.txt); publication: https://www.rfc-editor.org/rfc/rfc1034.txt — shared resolver caches and varying lookup delays.
2. curl project, **CURLOPT_DNS_CACHE_TIMEOUT**, curl 8.7.1, Description — [kept text](../evidence/gardener-2026-10-16-service-check-3/dns-cache-timeout-8.7.1.md); publication: https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/libcurl/opts/CURLOPT_DNS_CACHE_TIMEOUT.md — name-resolution results retained in process memory.

Links:
- [[dns-cache]] names the remembered address answer whose reuse must be checked at the right store.
- [[http-cache]] keeps an older web reply, a different cupboard from the one holding its server's address.
- [[measuring-the-window]] keeps a new process and a measured wait from becoming a claim that every cache began empty.
- [[what-the-gaps-can-say]] keeps the actual reply comparison while leaving unseen cache activity unknown.
