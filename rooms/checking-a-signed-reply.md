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

Links: [[http-message-signature]] · [[content-digest]] · [[repr-digest]] · [[nonce]] · [[replay-attack]] · [[http-cache]] · [[agent-claims]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
