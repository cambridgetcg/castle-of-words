# checking-a-signed-reply

*The seal holds a letter; the address and the day still matter.*

This room gathers the checks that keep a signed web reply tied to the right content, trusted key, request and occasion.

## A valid signature is one check, not the whole answer — 2026-10-13

A protected mark is useful only when it belongs to the thing being accepted. An [[http-message-signature]] over [[content-digest]] does not, by itself, authenticate the entire reply or show that it answers this request. RFC 9421 requires applications to define their required components, signature parameters, key lookup, allowed algorithms and message context; its verification process must enforce those requirements. [1, §§1.4, 3.2–3.2.1]

For the question planted on 2026-10-13, the checks are:

1. **Check the content against its mark.** Recompute the digest over the actual message content with the chosen acceptable algorithm. A signature over the field can remain valid while an attacker substitutes the body, if nobody compares the two. Use the right byte layer: [[content-coding]] remains inside Content-Digest's input; an unpacked file cannot borrow the compressed content's successful check. [[repr-digest]] has a different input and is not a substitute for this comparison. [1, §7.2.8; 2, §§2, 6.1–6.5]
2. **Check the parts that give the reply its meaning.** Require the coverage the application needs, rather than accepting whatever the sender happened to sign. Response status, media type and content encoding can matter alongside the digest. An unsigned field is not protected just because it sits next to a signed one. Which fields must be covered is a profile decision, not one universal list supplied by the RFC. [1, §§1.4, 7.2.1, 7.2.3; 2, §6.3]
3. **Check whose key is acceptable here.** Resolve `keyid` through the application's trusted rules, and reject a key not known or trusted for this context. Use an allowed algorithm appropriate to that key; conflicting algorithm declarations fail verification. A mathematically valid signature with an attacker's key is not the expected server's reply. Shared-secret methods also let the verifier make valid marks, so they do not establish exclusive authorship. [1, §3.2 steps 5–6; §§7.3.3–7.3.6]
4. **Rebuild the signed input from the right messages.** Match the chosen `Signature` entry with its `Signature-Input` entry, apply the standard's component and serialization rules, and derive values from the received message and trusted context—not an untrusted ready-made signature base. A missing required component or an unrecognized component parameter is an error. Signature labels pair the fields but are not themselves protected identity claims. [1, §§2.5, 3.2, 7.2.5–7.2.6, 7.4.2–7.4.4]
5. **Bind the reply to the relevant request.** The `req` parameter tells a response signature to use a component from its triggering request. For example, a profile can cover `"@method";req` and `"@target-uri";req`, alongside the response's `"@status"` and `"content-digest"`. Include request content or selection fields when the application's meaning depends on them. The requester must keep the original request values long enough to verify this binding. This example is a coverage sketch, not a complete secure profile or a signed message. [1, §§1.4, 2.4, 7.2.8]

Binding a method and address distinguishes many requests, but not repeated requests with identical covered values. **The occasion needs its own check.** — gardener's synthesis of [1, §§2.4, 7.2.2].

## A time limit is not a one-use rule — 2026-10-13

RFC 9421 protects signature metadata through the required `@signature-params` line. What the metadata means still needs an enforced policy. The RFC recommends including `created`; it does not make every application require `created`, `expires` and `nonce` together. [1, §§2.3, 3.2.1]

| Item | What the verifier needs to do | What the item alone does not prove |
|---|---|---|
| `created` | Apply the application's allowed signature age and clock policy; use the signature timestamp rather than silently substituting HTTP `Date`. | That the resource was freshly measured, or that the signature has not already been used. |
| `expires` | Enforce the application's expiry rule; the verifier may reject earlier than the signer's offered expiry. | Uniqueness of a use before expiry. |
| Signer-generated [[nonce]] | Enforce the application's uniqueness rule, with enough retained state to detect repeats. | That merely seeing a random-looking string stopped a replay. |
| Verifier-chosen nonce | Require the returned signed nonce to match the outstanding challenge, and apply the application's one-use/lifetime policy. | That a signature request was honored, or that newly signed content is newly gathered data. |

Sources for the parameter and challenge rules: [1, §§2.3, 3.2.1, 5.1–5.2, 7.2.2, 7.2.4]. The state, clock-policy and one-use requirements are the gardener's application guidance; the RFC does not prescribe one retention period or clock tolerance. A recipient may ignore an `Accept-Signature` request that does not fit its application parameters, so a verifier requiring a challenge cannot treat the request's presence as success.

These checks constrain a [[replay-attack]]. They do not prove that a trusted signer reports the truth. [[agent-claims]] keeps that further limit visible. Message signatures provide no confidentiality and do not replace TLS. [1, §7.1.2; distinction about truth is the gardener's synthesis]

## Three clocks must not borrow one another's verdict — 2026-10-13

The signature's acceptable lifetime is not HTTP cache freshness, and neither is the age of the underlying information. RFC 9111 calls a stored response fresh while its calculated age is below its freshness lifetime; it can then satisfy another request without contacting the origin. [3, §4.2]

Consequently, a cache-fresh reply can fail an application's signature-age or nonce requirement, while a still-acceptable signature does not by itself permit cache reuse. Even a new, request-bound signature can authenticate a statement containing old data. Record these verdicts separately rather than calling them all “fresh.” — gardener's comparison of [1, §§3.2.1, 7.2.2] and [3, §4.2].

## What this reading establishes — 2026-10-13

The standards question is answered: protecting a digest requires checking its content, required coverage, trusted key and algorithm, correct request context, and the application's time and replay rules. This is a public-document answer, not a tested verifier. RFC 9421 §7.1.1 explicitly warns that successful examples cannot reveal a verifier that silently skips checking; rejection tests matter too. No such implementation tests were run here.

uncertain: whether any historical castle service capture contained or verified a signature, or which key and replay policy it would have used. No watched service was contacted, no configuration changed, and no keys were handled by signing or verification code. The older observation questions in [[what-the-gaps-can-say]] and [[measuring-the-window]] remain open; a standard does not fill an unwatched interval.

## Sources

Fetched and read **2026-10-13**:

1. A. Backman, J. Richer and M. Sporny, **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — especially §§1.4, 2.3–2.5, 3.2–3.2.1, 5.1–5.2 and 7.
2. R. Polli and L. Pardue, **Digest Fields**, RFC 9530 — https://www.rfc-editor.org/rfc/rfc9530.txt — §§2 and 6.1–6.5.
3. R. Fielding, M. Nottingham and J. Reschke, **HTTP Caching**, RFC 9111 — https://www.rfc-editor.org/rfc/rfc9111.txt — §4.2.

Retrieval note: DuckDuckGo returned an HTTP 202 page without usable results, and Bing's RSS searches returned unrelated pages. Direct retrieval from the RFC Editor succeeded; the answer rests on the standards, not search snippets.

## The seal at the end must wait for the end — 2026-10-14

Some checks arrive after the letter. Until they arrive and pass, receiving the letter is not the same as verifying it.

An [[http-trailer]] is a field sent after the content rather than in the opening header section. It can carry a digest or signature calculated during sending. HTTP keeps these sections distinct, and RFC 9421 makes that distinction part of the signed component's name and parameters. [T1, §2.1.4; T3, §6.5]

### The place is part of the check

These are **component sketches, not a signed message or a tested profile**:

| Covered component | Where its value comes from | What it does not cover |
|---|---|---|
| `"content-digest"` | The response's header section. | A same-named trailer. |
| `"content-digest";tr` | The response's trailer section. | A same-named header, even if its value matches. |
| `"trailer"` | The opening `Trailer` header's list of anticipated field names. | The values of those later fields, or proof that they arrived. |

The signer must use the Boolean `tr` parameter when covering a trailer. If both sections contain the same field name, both values may be signed, **but separately; they must not be combined for the signature**. The parameter also appears in the constructed signature base: it is not an optional hint the verifier may discard. [T1, §§2.1.4, 2.5]

There is an important seam here. RFC 9530 permits a Content-Digest trailer to be merged into the header section under HTTP's rules. But that permission does not make a flattened header value a substitute for the trailer context required by an original `;tr` signature. If that context was lost, do not guess it back from the field's name or remove `tr` to make verification pass. — [T2, §2; T3, §6.5.1; T1, §§2.1.4, 2.5]; the final instruction is the gardener's application of those rules.

`Signature` and `Signature-Input` may themselves be sent as trailers; the RFC recommends putting them in headers to reduce the risk of stripping. Their placement is a separate question from `tr`, which chooses the location of a **covered field**. [T1, §§4.1–4.2]

### Receive, check, then accept

For a profile requiring a signed Content-Digest over streamed content, the following is **application guidance derived from the standards**, not an implementation tested here:

1. **Keep the required context.** Retain header and trailer sections distinctly, the matching `Signature` and `Signature-Input` entries, and any covered original-request values. Enforce the expected coverage rather than accepting a sender's weaker list. [T1, §§2.4–2.5, 3.2–3.2.1]
2. **Calculate over the right arriving bytes.** Content-Digest covers message content after [[transfer-coding]] is removed, but before [[content-coding]] such as gzip is unpacked. Trailer bytes are not part of this digest input. Incremental hashing can do work during receipt; it does not make the final comparison available early. [T2, §2, §6.4; T3, §§6.4, 8.1]
3. **Reach the protocol's complete message, including its trailer section if present.** A useful-looking prefix, a pause, or the last content byte is not by itself proof that every required field arrived. The boundaries below differ by HTTP version. [T3, §6.1; T4–T6]
4. **Require all the checks to pass.** Compare the digest with the actual complete content, rebuild the signature base using each field's correct section, and verify the signature under the trusted-key, allowed-algorithm, request-binding and time/replay rules already set out above. A missing required field or unsupported component parameter is an error, not a component to skip. [T1, §§2.5, 3.2–3.2.1, 7.2.8]

| Protocol | What ends the message and where trailers fit |
|---|---|
| HTTP/1.1 with chunked transfer coding | The zero-sized last chunk is followed by the trailer section, which may be empty, and the final empty line. Read the whole ending, not just the zero. [T4, §7.1] |
| HTTP/2 | Trailers are a final field block beginning with a HEADERS frame carrying `END_STREAM`; any following CONTINUATION frames still have to complete that block. HTTP/2 does not use HTTP/1.1 chunk framing. [T5, §8.1] |
| HTTP/3 | An optional trailing HEADERS frame follows content; normal closure of the response's sending direction marks its end. A premature abort is not a substitute for a complete response and its required fields. [T6, §§4.1–4.1.2] |

When the signature material is also already available, a signature containing only already-available header components can be checked earlier. That earlier result does **not** certify all the streamed content before its digest comparison finishes. Likewise, a connection ending does not certify a signature. Keep **message complete**, **digest matched**, and **required signature verified** as separate verdicts. — gardener's synthesis of [T1–T6].

If downstream actions depend on verified content, hold those actions until the required checks pass—for example by staging the result before committing it. This is a proposed application boundary, not an RFC command to buffer every message in memory. Incremental receipt and parsing are different from accepting content as verified. RFC 9530 specifically warns that eager processing before trailer receipt can process invalid data. [T2, §6.4]

### A missing last note is not a passed check

`Trailer` names fields the sender anticipates; RFC 9110 explicitly says the sender might not follow through. `TE: trailers` declares willingness not to drop trailers, but does not promise to process any particular field. Neither proves that the client's application API actually exposed and checked them. [T3, §§6.5.1, 6.6.2, 10.1.4; last sentence is the gardener's evidence distinction]

An intermediary can discard trailers. RFC 9421 therefore recommends against signing them unless the signer knows the verifier can access their values as sent. When a required covered trailer is unavailable, signature-base construction fails; when required signature material is absent, the application's signature requirement has not been met. Do not silently downgrade either to success. A response can be complete as an HTTP message yet fail this stronger acceptance rule. [T1, §§2.1.4, 2.5, 3.2; T2, §6.4; T4, §7.1.2]

uncertain: whether a missing trailer was never sent, discarded in transit, or hidden by a client interface. Absence alone does not choose the cause or prove malicious alteration. Report the narrower result—**required verification unavailable or failed because an input is missing**—rather than claiming a cryptographic mismatch that was never calculated.

**The trailer question is answered at the standards boundary.** No watched service was contacted, no client changed, and no key, signature-generation code or verifier was exercised. The older questions about body changes, time of day and event widths remain open: this reading supplies no missing service observations.

### Sources for the trailer reading

All fetched from the RFC Editor and read **2026-10-14**:

- **[T1] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §§2.1.4, 2.4–2.5, 3.2–3.2.1, 4.1–4.2 and 7.2.8.
- **[T2] Digest Fields**, RFC 9530 — https://www.rfc-editor.org/rfc/rfc9530.txt — §§2 and 6.4.
- **[T3] HTTP Semantics**, RFC 9110 — https://www.rfc-editor.org/rfc/rfc9110.txt — §§6.1, 6.4–6.6.2, 8.1 and 10.1.4.
- **[T4] HTTP/1.1**, RFC 9112 — https://www.rfc-editor.org/rfc/rfc9112.txt — §§7.1–7.1.2 and 8.
- **[T5] HTTP/2**, RFC 9113 — https://www.rfc-editor.org/rfc/rfc9113.txt — §8.1.
- **[T6] HTTP/3**, RFC 9114 — https://www.rfc-editor.org/rfc/rfc9114.txt — §§4.1–4.1.2.

Retrieval note, 2026-10-14: Google's ordinary and basic search views returned redirect/JavaScript pages without usable results. The IETF Datatracker's **Document Search** returned RFC 9421 for “HTTP Message Signatures” (https://datatracker.ietf.org/doc/search/?name=HTTP+Message+Signatures&rfcs=on); the six direct standards fetches succeeded. No search snippet substitutes for the rules above.

## Keep each note with its reply — 2026-10-14

A field's words are not enough: keep which reply carried them and whether they came before or after its content. [[http-field-context]] names that record. libcurl offers both a stream of arriving lines and a lookup interface with separate request and field-location labels. Those labels describe receipt, not the sender's trustworthiness. [C1–C3]

### The arriving lines need a bookkeeper

`CURLOPT_HEADERFUNCTION` installs a **callback**, a function libcurl calls as header data arrives. It receives complete lines, including HTTP status lines and the empty line ending a header section. Its buffer has an explicit length, not a terminating zero byte. The callback receives headers from all responses in the transfer, including authentication exchanges—not only the final reply. [C1]

For a callback-based recorder, preserve status-line boundaries, each header-section ending, the body stage, and the transfer's completion or error. An informational reply, such as `100 Continue`, is an early response, not the final answer; a redirect or authentication exchange can lead to another request. Fields arriving after the final response's header section and content can be trailers. The callback signature itself has no origin-category argument, so the caller needs a stateful account rather than one growing name-to-value dictionary. This is recording guidance derived from [C1–C3], not a parser exercised here.

The callback documentation lists an opening `Trailer` announcement as one clue. It is not sufficient evidence of arrival or section identity: the standards reading above explains that announced trailers can be absent and unannounced fields cannot be classified merely by matching a name. Preserve the actual message sequence. [C1; T3, §§6.5–6.6.2]

A proxy can first answer a **CONNECT** request that opens a tunnel through it. That answer is not the destination's later reply, even if both status codes are 200. `CURLOPT_SUPPRESS_CONNECT_HEADERS`, available since **7.54.0** and off by default, suppresses CONNECT response headers from the header and write callbacks. Record that setting; callback silence under suppression is not proof that the proxy sent no fields. Its documented promise concerns those callbacks, not a universal erasure from every interface. [C4]

### The lookup has two separate addresses

`curl_easy_header` selects a **request number** and an **origin category**. Request 0 is the first; redirects and multi-stage authentication can advance the number. Request `-1` means the last request **so far** when called during a transfer, not a guarantee that no later request will follow. The function can be called before all headers arrive and reports the state at that moment. [C2]

| Origin category | What it selects |
|---|---|
| `CURLH_HEADER` | Ordinary server-response headers for the selected request. |
| `CURLH_TRAILER` | Fields delivered as trailers. |
| `CURLH_1XX` | Fields from informational responses, kept apart from the ordinary response headers. |
| `CURLH_CONNECT` | Fields from the proxy's CONNECT response. |
| `CURLH_PSEUDO` | HTTP/2 or HTTP/3 control fields called pseudo-headers, not ordinary header fields. |

Here **origin means the API's source category, not an authenticated network origin**. After a successfully completed transfer, selecting `CURLH_HEADER` with request `-1` asks for the last request's ordinary headers; use `CURLH_TRAILER` separately for its trailers. It does not mean the status was successful or the signature passed. Combining the two masks and then forgetting each result's category would lose the distinction required by `;tr`. [C2; T1, §2.1.4; application by the gardener]

For repeated names, retain every selected instance: `nameindex`, returned `index`, and `amount` distinguish them within the requested scope. A first instance is not necessarily the whole field. `curl_easy_nextheader` can iterate within a fixed origin/request scope; begin a fresh iteration with `prev = NULL` and copy retained data before later calls or handle reuse invalidate it. Both interfaces own their returned storage; `curl_easy_header` reuses its returned structure on subsequent calls. [C2–C3]

**Test known origin bits, not equality with a lone flag.** The documentation reserves other bits. The pinned implementation deliberately adds a reserved bit to returned `origin`, while matching requests and origin masks separately. This is direct source evidence for that implementation, not a claim about every deployed library. [C2, C7: `copy_header_external`, `curl_easy_header`]

An origin category does not preserve every boundary. `curl_header` has no status-line or individual informational-response identifier; the inspected store labels entries by request and category. If the identity of each of several 1xx replies matters, keep the callback's separate response boundaries rather than inferring them from a combined `CURLH_1XX` lookup. The lookup also omits the HTTP status line: retain status separately. `CURLINFO_RESPONSE_CODE` reports the last server response code; CONNECT has its own `CURLINFO_HTTP_CONNECTCODE`. [C2, C5–C7; boundary limitation is the gardener's inference from the documented fields and inspected source]

### Preserve the meaning, and name any lost detail

Neither interface is a promise of a verbatim wire transcript. `curl_easy_header` strips surrounding whitespace and line endings, unfolds old multiline fields, and documents that it provides the headers libcurl actually uses where one instance overrides another. The callback's current documentation likewise says old HTTP/1 folded lines are unfolded before delivery **since 8.18.0**. Older captures therefore need their version's behavior, not today's documentation silently applied backward. [C1–C2]

These transformations do not automatically prevent verification: RFC 9421 §2.1 itself specifies trimming and unfolding for its list-field construction. But the required instance order, selected message, header/trailer boundary, and component parameters still matter. Do not invent discarded values or apply arbitrary extra normalization. A signed field with `sf`, `key` or `bs` has its own rules; a convenient lookup is not itself a signature-base builder. [C8, §§2.1–2.1.4, 2.5]

A **proposed verification record**, not an installed collector, therefore keeps:

- The actual libcurl version, enabled HTTP/header-API support, relevant redirect/proxy/header settings, and transfer completion or error. `CURLOPT_HEADERFUNCTION` dates from **7.7.2**; `curl_easy_header` and `curl_easy_nextheader` from **7.83.0**. A newer version number is not proof that the header API was built in. [C1–C3, C7, C9]
- A request identity and response-block identity, the relevant status, and the selected field's category, name, ordered instances and values. Keep the request scope alongside returned structures; it is a lookup argument, not a member of `curl_header`. [C1–C3, C7]
- The triggering request values needed by `req`, rather than assuming the initial URL and method still describe a reply after redirects. Keep covered request values in their appropriate protected context, not indiscriminately in a public log. Preserve the body byte layer required by [[content-digest]] separately. [C8, §§2.4–2.5; T2, §2; recording guidance by the gardener]
- What was unavailable. `CURLHE_MISSING`, `CURLHE_NOHEADERS`, `CURLHE_NOREQUEST` and `CURLHE_NOT_BUILT_IN` are different results; a missing required field, incomplete transfer, or unsupported extraction path must not silently become a verified reply. [C7, C9; acceptance guidance follows T1, §§2.5, 3.2]

**The libcurl documentation question is answered.** The three older uncommissioned observation questions—740, 744 and 766—were reviewed first and remain open: their existing rooms already name the missing observations and measurement limits. This API reading neither fills those gaps nor merits another claimed service measurement.

uncertain: which libcurl version, settings, response boundaries or verification checks any particular historical client retained. Official documentation and public source establish an available interface and one implementation's behavior, not proof that a client uses it. No watched service was probed, no software installed, no client changed, and no verifier run.

### Sources for the libcurl reading

All fetched and read **2026-10-14**:

- **[C1] curl project, CURLOPT_HEADERFUNCTION — callback that receives header data** — https://curl.se/libcurl/c/CURLOPT_HEADERFUNCTION.html — Description, Limitations and Availability.
- **[C2] curl project, curl_easy_header — get an HTTP header** — https://curl.se/libcurl/c/curl_easy_header.html — request/origin selection, returned data, Origins and Availability.
- **[C3] curl project, curl_easy_nextheader — get the next HTTP header** — https://curl.se/libcurl/c/curl_easy_nextheader.html — iteration, ownership and Availability.
- **[C4] curl project, CURLOPT_SUPPRESS_CONNECT_HEADERS — suppress proxy CONNECT response headers** — https://curl.se/libcurl/c/CURLOPT_SUPPRESS_CONNECT_HEADERS.html.
- **[C5] curl project, CURLINFO_RESPONSE_CODE — last response code** — https://curl.se/libcurl/c/CURLINFO_RESPONSE_CODE.html.
- **[C6] curl project, CURLINFO_HTTP_CONNECTCODE — CONNECT response code** — https://curl.se/libcurl/c/CURLINFO_HTTP_CONNECTCODE.html.
- **[C7] curl project, HTTP header collection implementation and public header API declarations**, pinned at `9a6d4ffc1b6c184fb2ec7c6e4879c835cb367689` — https://github.com/curl/curl/blob/9a6d4ffc1b6c184fb2ec7c6e4879c835cb367689/lib/headers.c and https://github.com/curl/curl/blob/9a6d4ffc1b6c184fb2ec7c6e4879c835cb367689/include/curl/header.h — read through the corresponding `raw.githubusercontent.com` files; inspected origin bits, request selection, storage, and disabled-build paths. The callback and lookup manuals at this same revision were also read.
- **[C8] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — especially §§2.1–2.1.4 and the context requirements already recorded above.
- **[C9] curl project, libcurl-errors — error codes in libcurl** — https://curl.se/libcurl/c/libcurl-errors.html — `CURLHcode` results.

Retrieval note: Google returned a redirect page, DuckDuckGo a challenge, and Bing RSS unrelated results. Direct curl documentation and GitHub public-source retrieval succeeded; the findings rely on those fetched sources, not on the unsuccessful search results.

## The last address is not the journey — 2026-10-14

A reply belongs to the request it answers, not automatically to the first request the client planned. An [[http-redirect]] can change the address, the method, and the fields of the next request. RFC 9421's `req` parameter selects the request that triggered **this particular response**. [R1, §15.4; R2, §2.4]

### What may change on the way

A redirect's `Location` can be an absolute address or a relative reference. Resolve a relative one against the target of the request that received that redirect—not always the transfer's starting URL. The result can change the path, query, or network authority. Following is optional; a `Location` is a proposed next destination, not proof that a client visited it. [R1, §§10.2.2, 15.4]

| Status | HTTP's rule for a follow-up request |
|---|---|
| `301` / `302` | A client may change POST to GET. This historical permission is not a rule to turn every method into GET. |
| `303` | The next resource can supply an indirect answer through retrieval, using GET or HEAD. Its URI is not considered equivalent to the original target. |
| `307` / `308` | These are method-preserving redirects; `307` explicitly forbids changing the method during automatic redirection. |

Source: [R1, §§15.4–15.4.9]. A `304` belongs to the 3xx class but directs reuse of a stored representation, not an ordinary new-address hop. The RFC also calls for updating request fields for the new destination and removing content-specific fields when switching to GET or HEAD. Thus preserving a method does not mean copying every header unchanged. [R1, §§15.4, 15.4.5]

**libcurl's documented behavior needs its settings beside it.** `CURLOPT_FOLLOWLOCATION` is off by default. When enabled, it follows successive locations subject to the redirect limit and allowed target protocols. Normally POST becomes GET on `301`, `302`, or `303`, without the old request body; `303` also switches other methods to GET except HEAD. The appropriate `CURLOPT_POSTREDIR` bits can retain an internally configured POST for these codes. That option does not create a POST transfer merely because a custom method string says `POST`. [R3, R6]

`CURLOPT_CUSTOMREQUEST` changes the method string sent, **not the underlying transfer behavior by itself**. For custom methods, the documented follow modes must not be collapsed into a single “follow redirects” Boolean: [R3, R7]

- **`CURLFOLLOW_ALL` (`1`)** keeps the custom method on later requests. This is the named form of the older `1L` setting; the method string alone still does not tell us whether libcurl retained the original body behavior.
- **`CURLFOLLOW_OBEYCODE` (`2`)** lets redirect semantics override the custom method where applicable: POST or a custom POST changes on `301`/`302`, while `303` switches to GET except for HEAD. The custom method remains on `307`/`308`; POST-retention settings can affect the applicable conversions.
- **`CURLFOLLOW_FIRSTONLY` (`3`)** uses the custom method only for the first outgoing request; later requests use libcurl's internally selected method under its redirect handling.

The last two modes were added in **8.13.0**. Record the actual version and selected mode, the internal transfer type, custom method, and POST-retention settings before explaining a capture. These are documented library controls, not proof that every custom configuration obeys the protocol's method-preservation rule or that any specific client used them. — [R3, R6–R7]; recording guidance by the gardener.

### The final lookups are not a request ledger

| Lookup | What it documents | What it does not retain for the caller |
|---|---|---|
| `CURLINFO_EFFECTIVE_URL` | The last used effective URL, which may differ from `CURLOPT_URL`; available since **7.4**. | The ordered intermediate destinations, their methods, or all request fields. |
| `CURLINFO_EFFECTIVE_METHOD` | The last used HTTP method, which may differ from the first request's method; available since **7.72.0**. | Earlier methods, their pairing with responses, or the request content and covered fields. |

Sources for the outputs and versions: [R4–R5]. The missing-history limits follow from those last-value interfaces; they are not claims that all other libcurl interfaces lack history. Check return codes and the transfer outcome rather than treating the word “effective” as evidence of a successful or verified response. Returned strings are library-owned; copy values that must survive handle reuse, and do not free them. The URL documentation explicitly warns that another call involving the same handle can invalidate its returned string. [R4–R5]

Nor should an effective URL be blindly pasted into a signature base. RFC 9421 defines `@target-uri` from the request's target URI, assembled from the available components including authority; RFC 9110 excludes the client-side fragment from that target. libcurl's `CURLOPT_REQUEST_TARGET` can replace the request target it would otherwise extract from the URL. The retained request context therefore matters even when the final URL is known. [R1, §7.1; R2, §2.2.2; R8]

The existing [[http-field-context]] lookup preserves some **response** history: `curl_easy_header` can select a request number. But that number can advance through redirects or multi-stage authentication, and a response-field lookup is not a copy of the corresponding outgoing method, target, and fields. Pair those records explicitly rather than treating the request number as a redirect count. [R9; gardener's inference from the documented interface]

### Bind each checked reply to its own question

For a final response covering `"@method";req` and `"@target-uri";req`, use the method and target of the **final triggering request**. If an intermediate redirect response is itself signed and checked, its `req` values come from the earlier request that triggered it. Keeping a final response's values under the first request's label would join the wrong pair. — application of [R2, §§2.2.1–2.2.2, 2.4].

RFC 9421 requires keeping the relevant original request component values long enough to verify the response. This does **not** impose a universal duty to log every hop merely to verify one final response: a correctly paired final request record may suffice for that response's required coverage. A full journey record serves the additional job of checking intermediate responses or auditing how the client got there. The two final-state getters can supply useful values, but cannot replace any other covered request fields or content evidence the profile requires. [R2, §§1.4, 2.4; R4–R5]

A proposed record therefore keeps each checked response with its triggering request identity, actual method and target, required covered request fields, response status and field sections, relevant client settings, and completion or error. Keep sensitive values in an appropriately protected verification context, not an indiscriminate public trace. The request can be changed by an intermediary; RFC 9421 warns that signing altered request values can leave the requester unable to verify them. Do not invent a lost value or silently weaken coverage to make the mark pass. [R2, §§2.4, 7.4.1; recording guidance by the gardener]

**The redirect question is answered at the documentation boundary.** A final signature's request binding is not, by itself, authentication of every earlier redirect or proof that the starting resource and final resource are equivalent. Required coverage and trusted-key policy still apply. — gardener's synthesis of [R1–R2].

The older uncommissioned questions **740, 744, and 766 were reviewed first** and remain open in [[what-the-gaps-can-say]] and [[measuring-the-window]]: this reading supplies no new comparable service observations or event boundaries. It is counted as one newly researched question, not four new measurements.

uncertain: the redirect route, method changes, or retained request record of any historical client. No watched service was probed, no live redirect chain followed, no credentials handled, no client changed, and no signature verifier exercised.

### Sources for the redirect reading

All fetched and read **2026-10-14**:

- **[R1] HTTP Semantics**, RFC 9110 — https://www.rfc-editor.org/rfc/rfc9110.txt — §§7.1, 10.2.2 and 15.4–15.4.9.
- **[R2] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §§2.2.1–2.2.2, 2.4 and 7.4.1; application requirements are also discussed earlier in this room.
- **[R3] curl project, CURLOPT_FOLLOWLOCATION — follow HTTP 3xx redirects** — https://curl.se/libcurl/c/CURLOPT_FOLLOWLOCATION.html.
- **[R4] curl project, CURLINFO_EFFECTIVE_URL — last used URL** — https://curl.se/libcurl/c/CURLINFO_EFFECTIVE_URL.html.
- **[R5] curl project, CURLINFO_EFFECTIVE_METHOD — last used HTTP request method** — https://curl.se/libcurl/c/CURLINFO_EFFECTIVE_METHOD.html.
- **[R6] curl project, CURLOPT_POSTREDIR — how to act on an HTTP POST redirect** — https://curl.se/libcurl/c/CURLOPT_POSTREDIR.html.
- **[R7] curl project, CURLOPT_CUSTOMREQUEST — custom request method** — https://curl.se/libcurl/c/CURLOPT_CUSTOMREQUEST.html.
- **[R8] curl project, CURLOPT_REQUEST_TARGET — alternative target for this request** — https://curl.se/libcurl/c/CURLOPT_REQUEST_TARGET.html.
- **[R9] curl project, curl_easy_header — get an HTTP header** — https://curl.se/libcurl/c/curl_easy_header.html.

Retrieval note: the IETF Datatracker's **Document Search**, https://datatracker.ietf.org/doc/search/?name=HTTP+Semantics&rfcs=on, returned RFC 9110. The direct RFC and curl documentation requests returned HTTP 200 with automatic redirect following disabled in the research reader; their examples were read, not run.

## The address in the request outranks the saved URL — 2026-10-14

Check the address on the letter, not only the address written in the sender's notebook.

**Answered:** when the URL record and the outgoing request differ, derive the signature's address components from the request that actually triggered the signed reply, using its HTTP version's reconstruction rules and trusted context. `CURLINFO_EFFECTIVE_URL` is useful client state, not a replacement for those rules. The [[http-request-target]] and the complete [[target-uri]] are different things. [U1, §§2.2.2–2.2.3, 2.4; U2, §7.1; U3, §§3.2–3.3; U6]

### Build the whole address before taking its host

- **Ordinary direct HTTP/1.1 request, origin-form:** the request line carries the path and query, while `Host` supplies the authority. A configured fixed scheme or one supplied by a trusted outbound gateway takes precedence; otherwise a secured connection supplies `https` and an unsecured one `http`. Combine these parts to reconstruct the target URI. An arbitrary forwarded header is not automatically that trusted context. [U3, §3.3; final caution is the gardener's application]
- **Ordinary HTTP/1.1 proxy request, absolute-form:** the request-target already is the target URI. Both a proxy and an origin server receiving this form must use its host information instead of the received Host value. A forwarding proxy must generate Host from that request-target. The proxy's own network address is not the requested resource's authority. [U3, §§3.2.2, 3.3]
- **`@target-uri`:** use the whole target URI assembled from the available components, including authority. A fragment after `#` is excluded by HTTP's target definition. A path-and-query alone is not a full target URI. [U1, §2.2.2; U2, §7.1]
- **`@authority`:** use the target URI's host and optional port, normalized as RFC 9421 requires: lowercase the hostname and omit the scheme's default port. Keep a non-default port. For example, an HTTP target authority written `Tenant.Example:80` gives `tenant.example`; `tenant.example:8080` keeps its port. These are imaginary derivations, not captured requests. [U1, §2.2.3; U2, §4.2.3]

The last rule is not permission to lowercase an entire URL, sort its query, or otherwise invent a convenient signature input. Follow each covered component's own derivation. `@request-target` is another component: in HTTP/1.1 it uses the request-line target, and is not interchangeable with `@target-uri`. RFC 9421 does not recommend it when other HTTP versions might be in use. [U1, §§2.2, 2.2.5, 2.5]

### Four paper examples, no requests sent

**Every example below is hypothetical.** The displayed request lines and Host fields are givens, not a claim that every libcurl version and option combination produces them. For the two direct cases, assume plaintext HTTP with no fixed-scheme or gateway override. Omitted fields are outside this address-only illustration; these are neither complete signed messages nor tested verification profiles. The results are the gardener's application of [U1–U3].

| Case | Request line and Host field | `@target-uri` | `@authority` |
|---|---|---|---|
| Ordinary direct request | `GET /planned?x=1 HTTP/1.1`; `Host: route.example` | `http://route.example/planned?x=1` | `route.example` |
| Direct request with a different target and custom Host | `GET /sent?x=2 HTTP/1.1`; `Host: tenant.example:8080` | `http://tenant.example:8080/sent?x=2` | `tenant.example:8080` |
| Ordinary proxy absolute-form request | `GET http://resource.example/sent?x=2 HTTP/1.1`; `Host: resource.example` | `http://resource.example/sent?x=2` | `resource.example` |
| Absolute-form request with a conflicting Host | `GET http://resource.example/sent?x=2 HTTP/1.1`; `Host: tenant.example:8080` | `http://resource.example/sent?x=2` | `resource.example` |

If the client's URL record still says `http://route.example/planned?x=1` in the second case, pasting that string into the signature base would name the wrong target. In the absolute-form cases, blindly using Host can likewise choose the wrong authority; the full URI in the request line controls reconstruction. For a response signature, these request-derived identifiers carry `;req`. [U1, §2.4; U3, §3.3]

**The fourth row is deliberately inconsistent, not a recommended or conforming sender behavior.** RFC 9112 requires a client's Host value to match the target authority, excluding userinfo. Its recipient rule for absolute-form prevents a conflicting Host from replacing that target; it does not bless the sender's mismatch or promise that every server will accept the request. Missing, repeated, or invalid Host fields have separate mandatory 400 rules. [U3, §§3.2–3.2.2]

### What the libcurl controls establish—and what they do not

`CURLOPT_REQUEST_TARGET` replaces the target libcurl would normally extract from the URL. Its documentation says the supplied string is passed verbatim, without safeguards, including for whitespace and control characters. That is a warning to validate inputs, not permission to treat any supplied string as a valid HTTP request-target. HTTP/1.1 forbids whitespace there. [U4; U3, §3.2]

`CURLOPT_HTTPHEADER` can replace an internally generated Host field. For HTTP/2 or HTTP/3, libcurl documents that the custom hostname goes into `:authority` instead and Host is not sent on the wire. Therefore a verifier must retain the actual protocol and authority-bearing values, not assume the original URL's host won. The HTTP/1.1 paper examples above are not a full HTTP/2 or HTTP/3 reconstruction algorithm. [U5; U2, §7.2]

`CURLINFO_EFFECTIVE_URL` documents the **last used effective URL**, which can differ from the configured one after redirects. It does not document a reconstructed transcript of custom request-target and Host values. Nor should its name be confused with HTTP's older term “effective request URI”: RFC 9110 notes that the protocol's recomposed URI is now called the target URI. Similar names do not make the library getter and the protocol derivation the same contract. [U6; U2, §7.1; comparison by the gardener]

For a checked response, keep its triggering request identity, protocol, request-target form and value, actual Host or `:authority`, the trustworthy scheme context, and whatever other components the profile covers. A final URL can help this record but cannot stand in for missing pieces. If an intermediary changes a covered request value, the server's signature can become unverifiable to the requester; RFC 9421 explicitly warns about this. Do not guess the altered value or weaken coverage to make a check pass. [U1, §§2.4–2.5, 7.4.1; proposed recording rule by the gardener]

If a required derived value cannot be obtained, RFC 9421 requires an error and no signature base—not a fallback to the closest saved URL. This establishes a verification input boundary, not proof that a particular client retained it, that a signature passed, or that the destination was authorized. [U1, §2.5; limits are the gardener's synthesis]

The three older eligible questions, **740, 744 and 766**, were reviewed first. Their existing rooms already record the missing comparable observations and event boundaries; they remain open. This visit adds one researched answer, not another service knock. Commissioned work and choices reserved for yu were left untouched.

uncertain: what any historical client actually sent, retained, or verified. No example request was sent, no watched service was contacted, no credentials handled, no client changed, and no signature verifier run.

### Sources for the target reconstruction reading

All fetched and read **2026-10-14**:

- **[U1] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §§2.2–2.2.5, 2.4–2.5 and 7.4.1.
- **[U2] HTTP Semantics**, RFC 9110 — https://www.rfc-editor.org/rfc/rfc9110.txt — §§4.2.3 and 7.1–7.2.
- **[U3] HTTP/1.1**, RFC 9112 — https://www.rfc-editor.org/rfc/rfc9112.txt — §§3.2–3.3.
- **[U4] curl project, CURLOPT_REQUEST_TARGET — alternative target for this request** — https://curl.se/libcurl/c/CURLOPT_REQUEST_TARGET.html.
- **[U5] curl project, CURLOPT_HTTPHEADER — set of HTTP headers** — https://curl.se/libcurl/c/CURLOPT_HTTPHEADER.html — Description and “Specific HTTP headers.”
- **[U6] curl project, CURLINFO_EFFECTIVE_URL — last used URL** — https://curl.se/libcurl/c/CURLINFO_EFFECTIVE_URL.html.

Retrieval note: Google returned a JavaScript/redirect page without usable search results. The IETF Datatracker's public document search, https://datatracker.ietf.org/api/v1/doc/document/?name=rfc9421, returned **HTTP Message Signatures**; the direct RFC and curl documentation fetches succeeded. The answer rests on those documents, not the failed general search or execution of their examples.

## The whole query and one named value protect different things — 2026-10-14

Keeping the whole note preserves its spelling and order; keeping one labeled answer does not preserve the rest of the note.

**Answered at the published-RFC boundary:** `@query` covers the whole query representation, whereas `@query-param` covers a selected, parsed and re-encoded name-value pair. They are not interchangeable shortcuts. The named form also exposes a source-version mismatch over spaces, recorded below rather than silently resolved. [Q1, §§2.2.7–2.2.8]

### Keep the whole string, or follow the named-value recipe

An [[http-query]] is the address information after `?`. It need not be a form with named fields. **`@query` includes the leading `?` and uses simple string comparison; percent-encoded octets are not decoded.** Do not sort parameters, collapse repetitions, change escape spelling, or translate `+` while deriving it. The RFC calls this the normalized query string but explicitly points to simple comparison, not a license to apply arbitrary URL cleanup. An absent query produces `?`; so does an explicitly empty query. [Q1, §2.2.7; Q2, §§3.4, 6.2.1]

**`@query-param` is available for the form-encoded format, not for every possible query syntax.** Its parser makes a list of name-value pairs: split on `&`, skip empty pieces, split at the first `=`, and use an empty value when no `=` is present. Replace literal `+` with space, then percent-decode and UTF-8-decode names and values. Re-encode the selected name and value for the component identifier and value. [[percent-encoding]] gives that spelling operation a name. [Q1, §2.2.8; Q3, §5.1]

The component's `name` parameter is required and contains the **encoded name**; the component value contains only the encoded value, with no added `?`, `name=`, or separating `&`. A present empty value is valid. A requested name that is absent is an error. If the parsed name occurs more than once, it **must not** be selected with `@query-param`: choosing the first, last, or a joined value is not the RFC's rule. Where repeated parameters are common, the RFC recommends `@query`. Another, unique name can still be selected. [Q1, §§2.2.8, 2.5]

The parser, not the original escape spelling, determines repeated names: hypothetical `q=one&%71=two` contains two occurrences of `q`. A dictionary that discards one occurrence loses evidence needed to enforce the rule. Parameter names are not lowercased by this recipe. — gardener's application of [Q1, §2.2.8; Q3, §5.1].

### Paper examples, not sent requests

**Every target below is hypothetical**, with valid UTF-8 form data where named parameters are used. The named-value column follows **RFC 9421's published `%20` examples and the January 2024 helper's default**, not today's whole-form serializer. These are component values, not complete signature bases or verified signatures. [Q1; Q4]

| Hypothetical request-target | `@query` value | Selected encoded name | `@query-param` value or failure |
|---|---|---|---|
| `/books` or `/books?` | `?` | `q` | Error: name absent. |
| `/books?q=&flag` | `?q=&flag` | `q` or `flag`, each selected separately | Empty string for either. |
| `/books?q=red+blue` | `?q=red+blue` | `q` | `red%20blue` |
| `/books?q=red%20blue` | `?q=red%20blue` | `q` | `red%20blue` |
| `/books?q=red%2bblue` | `?q=red%2bblue` | `q` | `red%2Bblue` — the decoded plus is not a space. |
| `/books?q=%41%2f` | `?q=%41%2f` | `q` | `A%2F` |
| `/books?q=one&q=two` | `?q=one&q=two` | `q` | Cannot select this repeated name. |
| `/books?q=one&%71=two` | `?q=one&%71=two` | `q` | Cannot select this repeated parsed name. |
| `/books?b=2&a=1` | `?b=2&a=1` | `a` | `1`; this component does not protect `b` or their ordering. |
| `/books?fa%C3%A7ade=a%0Ab` | `?fa%C3%A7ade=a%0Ab` | `fa%C3%A7ade` | `a%0Ab`; the newline stays escaped in the signature base. |

An empty component value does not remove its line. RFC 9421 §2.5 still places a colon and one space after the identifier. Written with `(SP)` as a visible notation for that single space, the line is `"@query-param";name="q":(SP)`. The notation itself is not sent. [Q1, §§2.2.8, 2.5]

A local, in-memory Python check reproduced **14 hypothetical derivation cases**, including each alternative above, a unique `v` beside repeated `q`, and the form encoding set's treatment of `~` and `*`. A separate byte-level parser and Python's `parse_qsl` agreed on this bounded valid-input set. This is an example/transcription check, **not a conformance suite**, an independent proof of the recipe, or a signature-verification test. No example request was sent.

### The referenced helper has changed

**The two public texts must not be blended into an invented agreement.** RFC 9421 §2.2.8 explicitly shows `with+plus+whitespace` becoming `with%20plus%20whitespace`. Its `[HTMLURL]` reference names the URL Living Standard, **January 2024**. In the inspected January source, the low-level “percent-encode after encoding” operation has an optional `spaceAsPlus` argument defaulting to false. The whole-form serializer separately passes true. Calling the helper and serializing a whole form were already different operations. [Q1; Q4]

The current published URL Standard, checked against pinned source `fde3f74f063341a28d437216f75735b8b40128f5`, has no such optional argument: it sets `spaceAsPlus` to true whenever the form percent-encode set is used. That current helper would emit `+` for a space in that mode, not the RFC's illustrated `%20`. The old source is pinned at `94b844771cc5bb2569dd2663768d123f7ff416c6`; the two helper contracts were read directly. This comparison establishes a **reference-version mismatch**, not an official change to HTTP signature behavior. [Q3–Q5; conclusion by the gardener]

The RFC Editor's errata listing retrieved today contains corrections for §§7.2.8 and 7.5.3, neither resolving this query-encoding seam. **uncertain:** whether a particular signature library follows the RFC's examples, a historical helper, or a newer serializer; no implementation was inspected for that question. Keep the expected signature-input spelling explicit and check the implementation against it rather than assuming the similarly named helpers agree. That is application guidance, not authority to invent a new normalization rule. [Q6; guidance by the gardener]

### Protection stops where the chosen component stops

- Named components can appear in a different order from their parameters in the URL. They do not protect the ordering among other names, the original escape spelling, or unselected values. The signature base still follows its declared covered-component order. Whole-query coverage preserves distinctions the named recipe removes, except for its specified absent/empty-query case. [Q1, §§2.2.7–2.2.8, 2.5]
- Neither query component alone covers the method, host, path, request content, trusted-key policy or replay rule. A response uses `;req` to draw a component from its triggering request; it does not borrow a convenient last URL. Required but unavailable or unsupported components fail signature-base generation, not just that one line. [Q1, §§2.5, 7.2.1–7.2.2]
- `@query-param` reads **only the target URI's query**, not form fields in the request body. RFC 9421 §7.5.8 warns that frameworks can merge those sources: verifying a signed query value and then acting on an unsigned body override defeats the intended protection. Keep the application's consumed value and the signature's source consistent, and cover content when its meaning matters. [Q1, §§7.2.8, 7.5.8]

The older uncommissioned observation questions **740, 744 and 766** were considered first. [[what-the-gaps-can-say]] and [[measuring-the-window]] already explain their missing comparisons and boundaries; they remain open. No watched-service probe, verifier change or new service observation was made. One standards question is answered here; the implementation behavior at the encoding seam is a separate, bounded question for a later visit.

### Sources for the query reading

All fetched and read **2026-10-14**:

- **[Q1] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §§2.2.7–2.2.8, 2.5, 7.2.1–7.2.2, 7.2.8, 7.5.8 and the `[HTMLURL]` reference.
- **[Q2] Uniform Resource Identifier (URI): Generic Syntax**, RFC 3986 — https://www.rfc-editor.org/rfc/rfc3986.txt — §§3.4 and 6.2.1.
- **[Q3] URL Standard**, WHATWG — https://url.spec.whatwg.org/ — percent-encode sets, “percent-encode after encoding,” and §§5.1–5.2.
- **[Q4] URL Standard source**, WHATWG, January 2024 snapshot `94b844771cc5bb2569dd2663768d123f7ff416c6` — https://raw.githubusercontent.com/whatwg/url/94b844771cc5bb2569dd2663768d123f7ff416c6/url.bs — the helper's `spaceAsPlus` default and the serializer's explicit true argument.
- **[Q5] URL Standard source**, WHATWG, snapshot `fde3f74f063341a28d437216f75735b8b40128f5` — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs — the helper's encoding-set-based choice and the serializer's call.
- **[Q6] RFC Errata — RFC 9421**, RFC Editor — https://errata.rfc-editor.org/search/?rfc_number=9421&presentation=records — returned records 8102 and 8103; this is a dated registry reading, not proof that no discussion exists elsewhere.

Search receipt: the IETF Datatracker's **Document Search**, https://datatracker.ietf.org/doc/search/?name=HTTP+Message+Signatures&rfcs=on, returned RFC 9421. GitHub's public commit API identified the January snapshot and current `url.bs` revision; both pinned source fetches succeeded. A commit-message search for `spaceAsPlus` returned an older 2021 fix and did not identify the later helper change; no date or reason for that change is inferred from that search.

## A library can agree with itself and still miss the rule — 2026-10-14

Two people can read the same misspelled word alike. Their agreement does not make the spelling match the book. A signature library likewise needs checks against the standard, not only against its own other half. [[conformance]] names that distinction.

**This reading selects pyauth/http-message-signatures v2.0.1**, pinned to `40be7e490b3ba227263d3f6381f4097f42097e2d`. It concerns the release's **default component resolver**, not every application using the package: the handler permits a replacement resolver class. The public README calls the project an RFC 9421 implementation; the claim does not settle which components this particular version implements. [I1–I4]

### Check the component's name before its spelling rules

The default resolver recognizes **`@query-params`, plural**, and dispatches it to `get_query_params`. RFC 9421 names **`@query-param`, singular**. The singular name is absent from the resolver's allowed set and follows its “Unknown covered derived component name” error path. Thus this release's default path does **not** derive RFC 9421's named-query component; the table below describes the separate plural path, not successful standard-component results. [I1, lines 9–37; I5, §2.2.8]

That plural path calls `urllib.parse.parse_qs(..., keep_blank_values=True)`, checks that the selected decoded name has exactly one value, and returns that value **without re-encoding it**. The signature-base builder inserts the returned value into its line; it adds no query-specific escaping afterward. Python documents `parse_qs` as returning unique names mapped to lists of decoded values, with empty values retained when requested. [I1, lines 68–74; I2, lines 36–60; I6]

**Hypothetical query inputs, compared with the published RFC recipe:** ordinary ASCII names such as `q` are selected unless noted. Error rows for the RFC describe an unavailable or forbidden selection, not an observed implementation run.

| Query and selection | Pinned library's plural-path result | RFC 9421's singular component |
|---|---|---|
| `q=red+blue` or `q=red%20blue` | `red blue`, with a literal space | `red%20blue` |
| `q=red%2Bblue` | `red+blue`, with a literal plus | `red%2Bblue` |
| `q=`; or `flag` selected as `flag` | Empty string | Empty string |
| `v=1`, selecting absent `q` | Missing-name error | Missing-name error |
| `q=one&q=two`, or `q=one&%71=two` | Multiple-values error: the decoded names coincide | The repeated parsed name must not be selected |
| `q=&%71=two` | Multiple-values error; the blank is not dropped | The repeated parsed name must not be selected |
| `v=1&v=2&q=ok`, selecting `q` | `ok`; the repeated unselected name does not block it | `ok` |
| RFC example `bar=with+plus+whitespace` | `with plus whitespace` | `with%20plus%20whitespace` |
| RFC example `var=this%20is%20a%20big%0Amultiline%20value` | Spaces and an actual newline in the returned text | `this%20is%20a%20big%0Amultiline%20value` |
| RFC example `fa%C3%A7ade%22%3A%20=something`, selecting its encoded name | Missing-name error: the dictionary key is decoded | `something`, with the encoded name in the component identifier |

Sources: [I1–I2, I5–I6]. The library's method can find that last value when directly given the decoded name `façade": `, but this does not establish that such a name is valid in a complete structured signature field. Nor does a literal newline returned by the resolver become the RFC's escaped value merely because signing and verifying share the same code. These are source-path distinctions, not a claim that an exploit or deployed failure was observed.

### What its own query test covers

The pinned `test_query_parameters` uses **`Pet=dog`** from the common request fixture. It expects a `Signature-Input` containing the plural name, checks a fixed expected HMAC signature, and calls the project's verification helper. That helper also checks altered, malformed and missing signatures. These are real assertions in the published test source—not test passes witnessed during this visit. [I3, lines 71–107, 402–419]

The fixed expected signature checks more than a bare sign-then-verify round trip, but `dog` needs no escaping. This query test does not distinguish literal spaces from `%20` or `+`, nor does it exercise empty values, decoded-name collisions, encoded names, or the singular identifier. Its negative signature checks do not supply those missing query cases. **A passing simple example would not certify the untested transformations.** — gardener's comparison of [I1, I3, I5]; RFC 9421 §7.1.1 separately recommends testing both valid and invalid signatures.

### No documented choice between the two helpers was found

The January 2024 URL Standard helper and the later pinned helper still differ as recorded above: the former has optional `spaceAsPlus=false`, while the latter chooses true for the form encoding set. Both source versions were fetched again. [I7–I8]

**This resolver uses neither encoding choice: it stops after decoding.** Its introduction commit, “Support query parameter addressing,” already returned the parsed value directly. The pinned README, generated-documentation entry point and changelog do not explain a choice about the changed WHATWG helper. Bounded repository issue searches for `query`, `spaceAsPlus` and `encoding` supplied no such explanation. The code establishes an omitted re-encoding step, not a documented decision to prefer one helper version. [I1–I2, I4, I9]

uncertain: whether a rationale exists elsewhere, whether later or customized code repairs these paths, and how any deployed caller behaves. No absence claim is made beyond the inspected documents and searches. This finding does not resolve the standard-reference mismatch or authorize quietly accepting both byte spellings.

### The small check actually made

The gardener extracted the original `resolve` and `get_query_params` methods and their allowed-name set from the pinned source, using lightweight component objects and an exception substitute. **Fifteen local cases passed their stated source-path expectations on Python 3.13.13**: the table's alternatives, direct decoded-name lookup, and rejection of the singular identifier. An earlier run on Python 3.9.6 also matched, but that interpreter is below this package's declared Python 3.10 minimum; it is not evidence of supported-package operation. [I10 for the declared minimum]

These are **isolated source checks**, not a run of the installed package, structured-field parser, upstream test suite, signer or verifier. No package was installed, no keys were used, no example request was sent, and no client was changed. The fetched resolver's SHA-256 was `cf8696a0558481ba5b4d712d2cf8a8933f3cd30cd086891c251f553c1e793874`; the second extraction checked the same bytes. — local execution receipt, 2026-10-14.

**The implementation-reading question is answered for this named release.** The older observation questions 740, 744 and 766 were reviewed first and stay open: [[what-the-gaps-can-say]] and [[measuring-the-window]] still lack the observations and comparable boundaries needed to settle them. This visit adds no watched-service measurement.

### Sources for the implementation reading

All fetched and read **2026-10-14**. Library source links below are pinned to the v2.0.1 commit rather than a moving branch.

- **[I1] pyauth/http-message-signatures — component resolver**, `resolvers.py` — https://github.com/pyauth/http-message-signatures/blob/40be7e490b3ba227263d3f6381f4097f42097e2d/http_message_signatures/resolvers.py.
- **[I2] pyauth/http-message-signatures — signature-base construction**, `signatures.py` — https://github.com/pyauth/http-message-signatures/blob/40be7e490b3ba227263d3f6381f4097f42097e2d/http_message_signatures/signatures.py.
- **[I3] pyauth/http-message-signatures — tests**, `test/test.py` — https://github.com/pyauth/http-message-signatures/blob/40be7e490b3ba227263d3f6381f4097f42097e2d/test/test.py.
- **[I4] pyauth/http-message-signatures — README and release notes** — https://github.com/pyauth/http-message-signatures/blob/40be7e490b3ba227263d3f6381f4097f42097e2d/README.rst and https://github.com/pyauth/http-message-signatures/blob/40be7e490b3ba227263d3f6381f4097f42097e2d/Changes.rst; `docs/index.rst` at the same pin includes these two documents.
- **[I5] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §§2.2.8, 2.5 and 7.1.1.
- **[I6] urllib.parse — Parse URLs into components**, Python 3.14 documentation — https://docs.python.org/3.14/library/urllib.parse.html#urllib.parse.parse_qs — the documented parser contract, not the local interpreter's version.
- **[I7] URL Standard source**, WHATWG, January snapshot — https://raw.githubusercontent.com/whatwg/url/94b844771cc5bb2569dd2663768d123f7ff416c6/url.bs — helper's optional argument.
- **[I8] URL Standard source**, WHATWG, later snapshot — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs — helper's encoding-set-dependent argument.
- **[I9] Support query parameter addressing**, pyauth source change — https://github.com/pyauth/http-message-signatures/commit/cccaa66780e9eeeb266ae3400b864b634de4be2a — inspected commit message and resolver/test patch.
- **[I10] pyauth/http-message-signatures — package metadata**, `pyproject.toml` — https://github.com/pyauth/http-message-signatures/blob/40be7e490b3ba227263d3f6381f4097f42097e2d/pyproject.toml.

Search receipt: GitHub's public repository search found the project, its tags API identified v2.0.1's commit, and its pinned tree listed the source and tests. The IETF Datatracker's **Document Search**, https://datatracker.ietf.org/doc/search/?name=HTTP+Message+Signatures&rfcs=on, returned RFC 9421. Public repository issue searches used https://api.github.com/search/issues with `repo:pyauth/http-message-signatures` and each term named above; the helper-name query returned zero results. Raw source fetches succeeded. These searches establish the scope of this reading, not an exhaustive search of all discussion.

## A changed helper is not a changed signature rule — 2026-10-14

A recipe can keep making the same whole cake while changing what happens when another cook borrows just one step. [[compatibility]] must name the job it preserves.

**Answered:** the helper changed in WHATWG URL pull request **896**, “Document invariants of percent-encode sets better,” merged on **2026-03-31** as `dc66b3bba025b76ecba0f5f2a323a600c0c74a84`. Its immediate parent is `8f0372b95d3cefde807efe662999f46968034867`. Both source versions, the patch, and the public review were read. An older HTTPWG discussion also explicitly documents the signature author's intended `%20` spelling; the answer is no longer limited to inferring intent from the RFC's example. [H1–H3, H6]

### The same form output, a different borrowed step

Before the change, “percent-encode after encoding” accepted an optional `spaceAsPlus` argument, defaulting to false. The whole-form serializer deliberately passed **true** for names and values. After the change, the helper has no such argument: it selects true when its encoding set is `application/x-www-form-urlencoded`, otherwise false. The form serializer drops its explicit true argument because the helper now makes that choice. [H1–H2]

The distinction is concrete:

| Operation on decoded text | Before | After |
|---|---|---|
| Borrow the helper with the form set for `with plus whitespace`, previously leaving the optional argument at its default | `with%20plus%20whitespace` | `with+plus+whitespace` |
| Serialize a whole form containing name `a` and value `b c` | `a=b+c` | `a=b+c` |
| Encode the literal plus in value `b+c` with that set | `b%2Bc` | `b%2Bc` |

These are source-derived examples, not captured requests. A bounded local Python transcription checked six UTF-8 input pairs—spaces in a value and a name, literal plus, empty text, a literal percent, and the RFC's decoded phrase—and two complete-form outputs. All matched their stated expectations. This checks the transcription, **not a browser, upstream test suite, signer or verifier**. [H1–H2, H4–H5; local check, 2026-10-14]

### What the review and tests actually support

The originating issue reported a bad ISO-2022-JP/userinfo example: its stated encoding set included a backslash that the example left unescaped. The revision gives encoding sets an explicit type, restricts which sets accompany non-UTF-8 encodings, and changes examples to the special-query or form set. The author calls the revision a “more drastic change.” The review catches the need to escape a literal `+` and `%` in the revised form example; those are different from plus signs produced from spaces. This is documented work on the helper's supported combinations and examples, not a documented decision to revise HTTP signatures. [H1, H3]

The pinned, pre-change Web Platform Test **urlsearchparams-stringifier.any.js** already asserts `a=b+c` for a space and `a=b%2Bc` for a literal plus, including corresponding name cases. Thus plus-for-space in the **whole-form output** was not introduced by this 2026 change. Those tests exercise `URLSearchParams`, not RFC 9421's selected-component recipe or every outside caller of the helper. [H4]

The review also discusses full-range form/URL encoding coverage and reports additional cross-tests passing in Firefox, Chromium and Servo while finding WebKit encoding failures. These are the reviewer's reports, **not runs witnessed here**. The inspected URL change modifies only `url.bs`; its discussion does not demonstrate a signature-library compatibility test. Preserving the form serializer's outputs follows from the before-and-after calls; extending that conclusion to every borrowed use of the helper would exceed the evidence. [H1–H3]

### The signature intent was said aloud before the change

In HTTPWG issue **2641**, “Signatures - Clarify usage of plus character when encoding query parameters,” a reader raised the same helper-versus-whole-serializer ambiguity in September 2023. RFC coauthor Justin Richer explicitly clarified on **2023-10-02** that the intended operation had **“space as plus set to false, its default value.”** The earlier reply says the example was chosen to demonstrate parsing `+` as space and re-encoding it as `%20`. This is direct evidence of author intent, not a new erratum or permission to reinterpret the current helper. [H6]

RFC 9421 §2.2.8 still prints `with%20plus%20whitespace`, and its reference to the serializing section still needs that distinction between a whole serializer and its borrowed step. The RFC Editor listing read today contains only records **8102** and **8103**, concerning the `@signature-params` name in §§7.2.8 and 7.5.3; neither changes query encoding. The 2023 discussion resolves the intended old default but predates the 2026 helper revision. [H5–H7]

**uncertain:** whether later discussion outside the bounded search formally reconciles the changed reference, and which deployed implementations follow which spelling. No RFC-9421-specific treatment was found in the inspected WHATWG change or its review. This visit neither proposes accepting both spellings silently nor claims the RFC has been amended. The useful boundary is narrower: the old signature intent is documented, the helper change is pinned, and unchanged form tests do not prove unchanged signature inputs.

The older uncommissioned observation questions **740, 744 and 766** were considered first. [[what-the-gaps-can-say]] and [[measuring-the-window]] still leave their missing comparisons and event boundaries open. They were not counted as new research or answered by these standards. No watched service was probed, no example request was sent, and no verifier was changed.

### Sources for the helper-history reading

All fetched and read **2026-10-14**:

- **[H1] Document invariants of percent-encode sets better**, WHATWG URL change — https://github.com/whatwg/url/commit/dc66b3bba025b76ecba0f5f2a323a600c0c74a84 — commit, parent, patch and associated pull-request metadata.
- **[H2] URL Standard source, immediately before and after the change**, WHATWG — https://raw.githubusercontent.com/whatwg/url/8f0372b95d3cefde807efe662999f46968034867/url.bs and https://raw.githubusercontent.com/whatwg/url/dc66b3bba025b76ecba0f5f2a323a600c0c74a84/url.bs — helper, encoding sets and whole-form serializer.
- **[H3] Percent encoding examples seem to be wrong**, WHATWG issue 895 — https://github.com/whatwg/url/issues/895; and **Document invariants of percent-encode sets better**, pull request 896 — https://github.com/whatwg/url/pull/896 — issue comments, review comments, reviews and changed-file list. In particular: https://github.com/whatwg/url/pull/896#discussion_r2724087780 for literal plus/percent escaping and https://github.com/whatwg/url/pull/896#issuecomment-3832078991 for the attributed cross-test report.
- **[H4] URLSearchParams stringifier tests**, Web Platform Tests, pinned revision `9353d550f0d49f5fd090dc276b60528c642b80d0` — https://github.com/web-platform-tests/wpt/blob/9353d550f0d49f5fd090dc276b60528c642b80d0/url/urlsearchparams-stringifier.any.js — “Serialize space,” “Serialize +,” and their name cases; fetched through the corresponding raw source. The repository's path-history API identified this as the latest file change before the URL revision.
- **[H5] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §2.2.8 and its encoded-name and encoded-value examples.
- **[H6] Signatures - Clarify usage of plus character when encoding query parameters**, HTTPWG issue 2641 — https://github.com/httpwg/http-extensions/issues/2641 — especially Richer's explicit default-false clarification, https://github.com/httpwg/http-extensions/issues/2641#issuecomment-1743258282, and the preceding example explanation, https://github.com/httpwg/http-extensions/issues/2641#issuecomment-1741177200.
- **[H7] RFC Errata — RFC 9421**, RFC Editor — https://www.rfc-editor.org/errata/rfc9421 — returned records 8102 and 8103; a dated registry check, not proof that no other discussion exists.

Search receipt: Google again returned an unusable JavaScript/redirect view. GitHub's public web API supplied the useful search: `repo:whatwg/url percent encode committer-date:>2024-01-01` identified the change, and `repo:httpwg/http-extensions spaceAsPlus in:body,comments` found the explicit signature discussion. The narrower WHATWG search for `9421` returned no results. Conclusions above rest on the fetched primary texts, not on search-result absence alone.

Links:
- [[reserved-value]] keeps the spare places in an API's number under that API's rules, so the reserved origin bit documented here must not turn a known flag into an apparent mismatch.
- [[dictionary]] names the keyed lookup that can hide a repeated query value, so this verifier needs the full parsed list before deciding whether a named component may be selected.
- [[profile]] names the application's required checks, so the sender cannot choose a weaker seal and have it accepted merely because that seal verifies.
- [[exception]] names the signal substituted in the isolated resolver checks, keeping that small harness distinct from an exercised package or verifier.
- [auditing-over-reputation](auditing-over-reputation.md) offers a research parallel to the seal's limit: identifying a trusted source still leaves the evidence for its claim to be examined.
- [agent-addressing](agent-addressing.md) separates the postman's route from the signing hand, keeping this reply's trusted-key check distinct from both arrival at an address and permission to act afterward.
- [[parsing]] finds message parts under a stated rule; it does not by itself establish that the required signature checks passed.
- [deterministic-json-standards](deterministic-json-standards.md) fixes the byte spelling of JSON, while this verifier needs RFC 9421's own [[serialization]] rules: a tidy copy in the wrong format still cannot supply the signed input.
- [[honest-data-systems]] separates a catalog's refresh clock from its change clock, just as a newly sealed reply can still carry yesterday's news.
- [comparing-saved-maps](comparing-saved-maps.md) shows what a flattened list can hide: equal sets may carry different numbers of copies, just as a first field value is not the whole record of repeated fields.
- [[multiplicity]] counts the instances of a selected field without replacing the order and message context that verification may also need.
- [[informational-response]] keeps an early progress note apart from the final reply, so fields from one response block cannot silently stand in for another's signed inputs.
- [fail-closed-boundaries](fail-closed-boundaries.md) keeps the gate shut when required evidence is missing, the same refusal this verifier needs when a covered trailer never becomes available.
- [wire-contract-honesty](wire-contract-honesty.md) brings this check to the wire: a helper that passes its own tests can still build a query component differently from the signature's required rule.
- [[test-oracle]] names the expected answer used to judge the check, which must not be borrowed unquestioned from the same code being tested.
- [portable-comparison](portable-comparison.md) keeps expected values outside the candidate's reach, a companion to checking this signature library against the named rule rather than only against its agreeing other half.
- [closing-the-loop](closing-the-loop.md) offers a human parallel to testing the checker: a reassuring yes can hide a missed check, so a signature test must also show that a known bad mark is refused.
- [checking-a-restored-map](checking-a-restored-map.md) finds the same gap between passing a check and keeping the intended promise: a sound database can hold the wrong old map, just as a valid signature can belong to the wrong request.
- [canonical-metadata](canonical-metadata.md) keeps an ordered source record beside its convenient view, the same separation this verifier needs when flattening fields would discard which reply and section carried each value.
- [[lossy-transformation]] explains why a convenient field map cannot reconstruct discarded header or trailer context merely because the names and values still look right.
- [[decoding-query-names]] traces malformed escapes and invalid UTF-8 through the required parser: different raw names can become one repeated name, so distinct spellings do not guarantee a selectable signed component (pinned-source reading and local parser checks, 2026-10-14).
- [[compatibility]] asks which old job still works, separating unchanged whole-form output from a changed helper used by another standard.
- [query-normalization](query-normalization.md) prepares an application's allowed query, but this verifier must keep that tidying separate from rebuilding the precise query spelling the signature covers.
- [correlated-witnesses](correlated-witnesses.md) explains why two agreeing halves can still share one mistake: a signer and verifier using the same resolver are not independent checks of its rules.
- [truing-the-level](truing-the-level.md) offers a learning parallel for this checker: compare each part with an outside standard rather than trusting an answer because it agrees with itself.
- [ordered-release](ordered-release.md) asks the producer's real bytes to reach the consumer's check, the missing crossing between this room's isolated resolver checks and a full signing-and-verifying test.
- [[test-fixture]] holds a prepared query still while its result is checked, without making one easy case a test of all query rules.
- [[conformance]] asks whether a named rule is followed; a library's internal agreement cannot supply an untested spelling rule.
- [[http-query]] keeps the whole query representation distinct from a form parser's selected values.
- [[query-parameter]] names the single parsed field, whose repetition, emptiness and encoding must be checked rather than guessed.
- [[percent-encoding]] explains why a plus sign, an escaped plus sign and a space can travel differently.
- [[target-uri]] names the whole address the verifier must reconstruct, rather than borrowing the last URL in a client record.
- [[http-request-target]] names the address information actually carried in a request, whose form determines where the remaining pieces come from.
- [saving-a-live-database](saving-a-live-database.md) separates a finished copy from successful cleanup, just as this reply separates the last content byte from a complete message and a passed verification.
- [canonicalization-and-verification](canonicalization-and-verification.md) sets a stricter reading order for signed snapshots: verify the whole chain before parsing, while this streamed reply may be received incrementally but must wait for all required checks before acceptance as verified.
- [canonical-wire-action](canonical-wire-action.md) keeps each result tied to the action actually dispatched, the same pairing this verifier needs when a redirect changes the request that the final reply answers.
- [conditional-writes](conditional-writes.md) keeps a version label with the copy it describes, a neighboring form of this room's rule that a seal must stay with its own request and response.
- [[request-binding]] keeps the answer beside the question it is checked against, without mistaking that match for proof of a new or one-time use.
- [[http-redirect]] names the next-address instruction whose follow-up can ask a different question; a final URL is not the route that reached it.
- [[http-field-context]] keeps each note with its request, response and section before a signature can say what it protected.
- [[signing-key-bootstrapping]] asks where the first trusted key comes from, a question this reply checker cannot answer merely by finding that the mark fits the offered key.
- [[validity-vs-identity]] offers a legal parallel: a real citation can name the wrong law, just as a valid signature can belong to the wrong key or request.
- [[stored-observation]] keeps the age of the news separate from the age of its envelope: an acceptable new signature can still carry an old observation.
- [[verification-receipts]] shares the need to challenge the checker: matching successful examples cannot show that a verifier would refuse a bad signature.
- [[signature-coverage]] draws the edge of the seal, leaving unsigned neighbors outside its protection even when the signed digest checks out.
- [[negative-test]] asks the verifier to refuse a known bad case, so a green light cannot come merely from a checker that always says yes.
- [portable-workflow-authorization](portable-workflow-authorization.md) keeps a checked record from taking the reins: even an authentic, request-bound reply cannot replace the current permission needed for a later provider call.
- [[parameter-shadowing]] names the switch from a checked query value to a different value the application uses, so checking one value must not certify an unsigned substitute.

[[http-message-signature]] · [[content-digest]] · [[repr-digest]] · [[nonce]] · [[replay-attack]] · [[http-cache]] · [[agent-claims]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
