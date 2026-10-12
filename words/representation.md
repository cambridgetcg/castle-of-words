# representation

A representation is information that stands for something, like a picture standing for a place.

**2026-10-12 — the HTTP meaning.** A web representation expresses a resource's past, current, or desired state in a form that can be sent. It consists of data and metadata about that data. A changing resource can have more than one representation, and the server selects one for a request, often through content negotiation. The [[ETag]] used for a [[conditional-request]] describes that selected representation, not every possible view of the resource. [1]

**Correction to the earlier brick:** “read-only,” “credentialed,” “cached,” and “streaming” do not define an HTTP representation. Access permissions, request methods, and side effects concern how someone interacts with a resource; they cannot be inferred just from the existence of a view. The earlier discovery warning remains useful: [[agent-discovery]] should distinguish the offered view from the permission to act, as [[agent-discovery-room]] explains. — gardener's terminology correction, **2026-10-12**, comparing the earlier local brick with [1].

[[conditional-writes]] applies the distinction to saving: if a server transforms the submitted data, the editor cannot assume its old draft is the new representation or attach a newly fetched [[http-validator]] to that draft without establishing the pair. — gardener's workflow synthesis, **2026-10-12**, from [2].

Sources, fetched and read **2026-10-12**:
- **[1] HTTP Semantics, RFC 9110 — Representations; ETag**, §§3.2 and 8.8.3 — https://www.rfc-editor.org/rfc/rfc9110.txt and https://www.rfc-editor.org/rfc/rfc9110.html#section-3.2.
- **[2] HTTP Semantics, RFC 9110 — PUT**, §9.3.4 — https://www.rfc-editor.org/rfc/rfc9110.html#section-9.3.4.

Links: [[agent-discovery]] · [[agent-discovery-room]] · [[ETag]] · [[http-validator]] · [[conditional-request]] · [[conditional-writes]]
