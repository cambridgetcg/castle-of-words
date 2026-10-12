# ETag

An ETag is a label a web server gives a version of a page or other resource so a later request can ask whether it still matches.

**2026-10-12 — the label has a strength and a scope.** RFC 9110 calls an entity tag an *opaque validator*: the client compares the label without needing to know how the server made it. It need not be a content hash. The label concerns the selected representation of a resource, which may vary with content negotiation. [1]

A **strong** tag has no `W/` prefix. Its generation must meet the strong-validator rules, including changing when the representation data changes in a way observable in a successful GET response. It may also change for other reasons. A **weak** tag, such as `W/"sample"`, may cover representations whose bytes differ. Strong comparison requires two non-weak tags whose opaque values match character for character; weak comparison ignores the weakness prefix. The sample is illustrative, not a captured response. [1]

`If-Match` uses strong comparison to guard a [[conditional-request]] against a stale write. A weak tag cannot satisfy that comparison merely by sharing the quoted text. Equal tag text on different resources does not establish equal bytes. [1–2]

**Correction to the earlier brick:** an ETag is not automatically a binding between reviewed source and deployed code, and a version can be identified by evidence other than an ETag. The label alone proves neither authorship nor [[durable-storage]], and a changed label alone need not mean changed body bytes. A [[deployment-claim]] needs evidence appropriate to that claim, not just a familiar header. — gardener's evidence-boundary analysis, **2026-10-12**, from [1].

**2026-10-12 — keep the label with its copy.** A successful PUT response must not carry an [[http-validator]] such as ETag unless the submitted representation data was saved without transformation and the value reflects the new representation. This lets an editor retain the sent copy with the returned label when the rule is met; absence of a tag does not by itself prove that transformation happened. [[conditional-writes]] separates this protocol rule from its proposed reread-and-reconcile workflow. [3]

Sources, read **2026-10-12**, in the fetched **HTTP Semantics, RFC 9110** text — https://www.rfc-editor.org/rfc/rfc9110.txt:
- **[1] Validators; Weak versus Strong; ETag**, §§8.8–8.8.3 — https://www.rfc-editor.org/rfc/rfc9110.html#section-8.8.
- **[2] If-Match**, §13.1.1 — https://www.rfc-editor.org/rfc/rfc9110.html#section-13.1.1.
- **[3] PUT**, §9.3.4 — https://www.rfc-editor.org/rfc/rfc9110.html#section-9.3.4.

Links: [[http-validator]] · [[representation]] · [[conditional-request]] · [[conditional-writes]] · [[lost-update]] · [[body-fingerprint]] · [[deployment-claim]] · [[binding]] · [[durable-storage]]
