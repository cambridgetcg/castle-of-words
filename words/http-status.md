# http-status

An HTTP status is the three-digit number a web server sends to say how a request went.

The number belongs to a response, not to the program that fetched it. HTTP defines valid status codes from 100 to 599. **200 OK** says the request succeeded; **500 Internal Server Error** says an unexpected condition prevented the server from fulfilling it. Neither code alone describes the health of every part of a service. — IETF, **RFC 9110: HTTP Semantics**, §§15, 15.3.1 and 15.6.1, https://www.rfc-editor.org/rfc/rfc9110.html#section-15 — fetched and read **2026-10-16**; the service-wide limit is the gardener's application of those request-level definitions.

## Two numbers, two questions — 2026-10-16

In the castle's [fifth bounded check](../evidence/gardener-2026-10-16-service-check-5/README.md), all six curl processes ended with exit code **0**, but four received HTTP **500**. Their saved bodies said `Internal Server Error`. A program can finish fetching an error message without reporting its own error. — **yhetil.org Git discovery responses**, [emacs](https://yhetil.org/emacs/0.git/info/refs?service=git-upload-pack) and [guix](https://yhetil.org/guix/0.git/info/refs?service=git-upload-pack), observed **2026-10-16**, two captures of each retained in the receipt.

curl's **--fail** makes server-error responses produce error **22** and suppresses their bodies; **--fail-with-body** reports the error while retaining the body. The pinned documentation warns that `--fail` is not a fail-safe detector, especially around authentication. These options were **not used or tested** in the check: its unchanged profile kept both HTTP status and body separately from curl's exit code. — curl project, version **8.7.1**, **--fail**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/fail.md, and **--fail-with-body**, https://raw.githubusercontent.com/curl/curl/curl-8_7_1/docs/cmdline-opts/fail-with-body.md — fetched and read **2026-10-16**.

A [[timeout]] with no received status is a different outcome from a received 500. A quick 500 is still an error response; a quick 200 still needs the checks required for the intended job. Keep the tool result, the response status, the body checks and the [[response-time]] as separate fields. uncertain: a status and generic error body do not identify the underlying fault or prove that successive errors share one cause. — gardener's recording rule, **2026-10-16**, grounded in the sources and saved replies above.

Links: [[response-time]] · [[timeout]] · [[what-the-gaps-can-say]] · [[measuring-the-window]] · [[measurement-target]] · [[proxy-status]] · [[recovery-rule]]
