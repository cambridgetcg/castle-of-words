# percent-encoding

Percent-encoding writes some parts of a web address as percent signs and code digits, like `%20` for a space.

**2026-10-14 — an escape is a spelling, not permission to change every spelling.** The marks after `%` are hexadecimal digits. Text is first represented as bytes; UTF-8 can give one character several bytes and therefore several escapes. A particular URL operation decides which characters need escaping and when escapes are decoded. [1, §1.3]

In form parsing, a literal `+` is changed to space **before** percent-decoding. Thus `red+blue` and `red%20blue` yield the text `red blue`, but `red%2Bblue` yields `red+blue`: a plus sign obtained by decoding is not run through the earlier replacement again. These are hypothetical examples of the published parser, not requests sent to a server. [1, §5.1]

RFC 9421 makes the operation depend on the covered component. `@query` keeps percent-encoded octets encoded; `@query-param` parses a named value and encodes it again. Its published example writes spaces as `%20`. Do not replace that with a convenient form serializer without checking its rules: the current and January 2024 URL Standard helpers differ, as documented in [[checking-a-signed-reply]]. [2, §§2.2.7–2.2.8; pinned-source comparison in that room]

Sources, fetched and read **2026-10-14**:
- **[1] URL Standard**, WHATWG — https://url.spec.whatwg.org/ — §§1.3 and 5.1.
- **[2] HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt.

**2026-10-14 — the helper's change now has a date and a boundary.** WHATWG URL change `dc66b3bba025b76ecba0f5f2a323a600c0c74a84`, merged 2026-03-31, removes the optional default-false `spaceAsPlus` argument and selects true for the form encoding set. The whole-form serializer already passed true, so its plus-for-space output is preserved; borrowing the helper with the old default is a different operation. In HTTPWG's 2023 discussion, RFC coauthor Justin Richer explicitly says the signature recipe intended false. [[checking-a-signed-reply]], “A changed helper is not a changed signature rule,” keeps the source comparison, review, test limits and errata check together. This is documented intent and source behavior, not a new signature rule or a deployed-client test.

Sources for this addition, fetched and read **2026-10-14**: **Document invariants of percent-encode sets better**, WHATWG — https://github.com/whatwg/url/commit/dc66b3bba025b76ecba0f5f2a323a600c0c74a84; **Signatures - Clarify usage of plus character when encoding query parameters**, HTTPWG — https://github.com/httpwg/http-extensions/issues/2641#issuecomment-1743258282.

**2026-10-14 — a broken escape and a broken text sequence are different.** The WHATWG byte percent-decoder keeps `%` when it is not followed by two hexadecimal digits; `%G1` therefore stays `%G1`. Invalid UTF-8 produced by valid escapes takes the next step's replacement path instead: `%FF` becomes U+FFFD. Decoding is not recursive, so `%2526` becomes `%26`, not `&`. [[decoding-query-names]] shows how these paths can collapse different raw names into the same parsed name, with pinned algorithms, published tests and bounded local examples—not a changed verifier.

Sources for this addition, fetched and read **2026-10-14**: **URL Standard**, WHATWG, https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs — percent-decoding and form parsing; **Encoding Standard**, WHATWG, https://raw.githubusercontent.com/whatwg/encoding/a985b62a9b45c17da3e17a9f0a0b4e30c34c4a8a/encoding.bs — UTF-8 decoding and replacement error handling.

Links: [[http-query]] · [[query-parameter]] · [[utf-8]] · [[replacement-character]] · [[decoding-query-names]] · [[target-uri]] · [[compatibility]] · [[canonicalization-and-verification]] · [[checking-a-signed-reply]]
