# response-time

Response time is how long a request takes between the start and finish you choose to measure.

A request is a question sent to another computer. Waiting for its first byte and waiting for its whole answer measure different stretches. Neither is automatically the time that computer spent doing the work.

In libcurl, `CURLINFO_TOTAL_TIME_T` includes name lookup and connection setup as well as the transfer. `CURLINFO_STARTTRANSFER_TIME_T` ends when libcurl receives the first byte; it includes preparation and the server's calculation time. Both add the times of followed redirects. Their documented unit is microseconds. — curl project, **CURLINFO_TOTAL_TIME_T**, https://curl.se/libcurl/c/CURLINFO_TOTAL_TIME_T.html, and **CURLINFO_STARTTRANSFER_TIME_T**, https://curl.se/libcurl/c/CURLINFO_STARTTRANSFER_TIME_T.html — read **2026-10-15**.

**The castle's recording rule:** keep the named timing field, its unit, the request it belongs to, and whether the transfer completed. A long client wait is evidence of a long client wait, not by itself a diagnosis of a busy server. [[what-the-gaps-can-say]] explains the boundary; [[measuring-the-window]] distinguishes a request's wait from the lifetime of a fault. This is a documentation-based rule, not a timing test performed here. — gardener's synthesis, **2026-10-15**.

Links: [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[measurement-target]] · [[observation-window]] · [[http-redirect]] · [[latency-weather]]
