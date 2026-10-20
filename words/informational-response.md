# informational-response

An informational response is a short note about a web request, not the finished answer.

In HTTP, the 1xx status codes describe connection status or request progress. Such a response ends with its headers and has no content or trailers. For example, `100 Continue` says the initial part of a request has arrived without being rejected yet; it does not say the requested work has succeeded. `101 Switching Protocols` has a different job: it announces an agreed change of protocol, not an ordinary content reply.

Keep each response block with its own status and fields. The arrival of an early note must not become proof that the final reply or its content arrived, nor may its fields silently become the final reply's signed inputs. [[time-to-first-byte]] and [[http-field-context]] carry those two boundaries: when a response begins, and which response a field belongs to. This is a reading rule, not evidence that an informational response occurred in any particular capture.

Source: **HTTP Semantics**, RFC 9110 §§15.2–15.2.2, https://www.rfc-editor.org/rfc/rfc9110.txt — the [saved source](../evidence/gardener-2026-10-20-response-boundary/rfc9110.txt) was read locally **2026-10-20**; no new fetch or service probe. The recording and verification connections are the tender's synthesis of [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md), “The first piece can be the envelope,” and [checking-a-signed-reply](../rooms/checking-a-signed-reply.md), “Keep each note with its reply,” read the same day.

Links:
- [what-the-gaps-can-say](../rooms/what-the-gaps-can-say.md) keeps the first-response mark apart from a separately timed arrival of content.
- [checking-a-signed-reply](../rooms/checking-a-signed-reply.md) keeps early-response fields apart from the fields a final reply's signature must cover.
- [[http-status]] names the code that identifies which kind of note arrived, without replacing the checks needed for the requested work.
