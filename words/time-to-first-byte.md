# time-to-first-byte

Time to first byte is how long we wait, from a named starting point, before the first tiny piece of an answer arrives.

A byte is a small unit of computer data. The first one does not mean the whole answer has arrived, and the wait does not tell us which computer or part of the journey caused it.

## Name where the clock starts — 2026-10-19

curl's `time_starttransfer` measures seconds from the operation's start until the first byte is received. It includes the earlier preparation measured by `time_pretransfer`; `time_total` ends when the full operation finishes. These are marks measured from the same start, not separate durations to add together. — curl project, **--write-out**, **curl 8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/write-out.md — fetched and read **2026-10-19**.

For a completed request whose marks are in order, subtracting the preparation mark from the first-byte mark gives the wait **between those client marks**. It does not isolate server processing: the request and reply still have to travel. Subtracting the first-byte mark from the total gives the remaining part of the operation. These are the gardener's applications of the documented definitions, not measurements from inside a server.

## A real comparison, with its missing answer — 2026-10-19

The [saved-request audit](../evidence/gardener-2026-10-19-first-byte/README.md) examined **28 orgmode requests** from fourteen visits. Of **27 completed replies**, three took at least one second. In each of those three, **more than 98%** of the full operation lay between preparation and the first byte; the remaining time after that byte was at most **0.001174 seconds**. This locates most of those long waits without identifying their cause. — **yhetil.org orgmode Git discovery responses and client request records**, https://yhetil.org/orgmode/0.git/info/refs?service=git-upload-pack, captured **2026-10-17–18 UTC**, reanalysed **2026-10-19**; exact differences retained in the receipt and [[what-the-gaps-can-say]].

The other request timed out without a response. Its zero first-byte field is not an instant answer; no first-byte-to-finish interval can be measured from it. `--max-time` sets a limit on the transfer, not a promised arrival time. — curl project, **--max-time**, **curl 8.7.1**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/max-time.md — fetched and read **2026-10-19**; missing-response interpretation checked against that saved request's exit code, diagnostic and empty header capture.

uncertain: why the waits differed and whether they relate to changes in the advertised names. A place on the client's ruler is not a diagnosis.

Links: [[response-time]] · [[name-lookup-time]] · [[timeout]] · [[temporal-alignment]] · [[reference-advertisement]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
