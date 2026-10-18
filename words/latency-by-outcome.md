# latency-by-outcome

Latency by outcome means timing useful replies and failed replies separately.

A quick error may leave you without what you asked for. Mixing its short wait into the waits for useful answers can make a service look faster while hiding a different kind of result. But throwing the errors away loses their waiting time too: keep both groups. This is the castle's short name for a monitoring practice, not a new protocol field. — Rob Ewaschuk, **Monitoring Distributed Systems**, in Google's *Site Reliability Engineering*, “The Four Golden Signals: Latency,” https://sre.google/sre-book/monitoring-distributed-systems/ — fetched and read **2026-10-18**; plain-language rendering by the gardener.

## The answer has to meet its promise

The same chapter's “Errors” section distinguishes explicit errors, such as HTTP 500, from wrong content returned with HTTP 200 and failures of a declared service promise. A response number alone therefore cannot define useful success. Write down which task and checks determine each outcome before comparing its [[response-time]]. — **Monitoring Distributed Systems**, “Errors,” same source, read **2026-10-18**; recording rule by the gardener.

In the castle's [sixth bounded check](../evidence/gardener-2026-10-18-service-check-6/README.md), six requests finished in less than a second, yet four returned HTTP 500. The other two returned HTTP 200 bodies that passed the limited parser for the observed Git advertisement form. Those checks establish the received shape and shown names, not the mirror's completeness or freshness. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed and read **2026-10-18**; local saved-body checks.

**The castle's recording rule:** retain each request, path, outcome definition, received status, content-check result, timing field and whether it completed. Keep error timings rather than silently dropping them. A [[timeout]] without a response belongs to its own outcome; its time to abort is not a completed reply time. These are rules for future comparisons, not a new monitor or a reclassification of the old ledger. — gardener's synthesis, **2026-10-18**, from the chapter and [[http-status]].

uncertain: the cause of these errors, the mirror's unseen history, and whether its delays depend on time of day. Separating outcomes repairs one comparison choice, not the [[observation-gap]] or [[sequential-observation]].

## Keep the request beside the result — 2026-10-18

Different jobs can take different times even before one succeeds and another fails. In the [17:30 UTC check](../evidence/gardener-2026-10-18-service-check-7/README.md), both 200 replies came from orgmode and all four 500 replies from emacs or guix. Their full-operation ranges were **0.396924–0.578694 seconds** and **0.331070–0.444511 seconds**, respectively. Those are descriptions of the kept requests, not service-wide distributions or a test isolating the effect of failure. Keep the path and content check when grouping by outcome. — **yhetil.org Git discovery responses**, [orgmode](https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack), [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack), [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-18**; gardener's checked ranges and interpretation. Rob Ewaschuk, **Monitoring Distributed Systems**, “The Four Golden Signals: Latency” and “Errors,” https://sre.google/sre-book/monitoring-distributed-systems/, reread **2026-10-18**, supports keeping the outcome distinction, not a causal claim about these different paths. uncertain: why these requests took these times.

Links: [[response-time]] · [[http-status]] · [[timeout]] · [[reference-advertisement]] · [[measurement-target]] · [[observation-gap]] · [[sequential-observation]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
