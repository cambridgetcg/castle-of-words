# uri-origin

A web origin names which web address a request belongs to, not just which computer answers it.

**2026-10-11 — HTTP's rule:** an origin is the three-part combination of scheme, host, and port. RFC 9110 normalizes the scheme and host to lowercase, removes leading zeros from the port, and supplies the scheme's default port when it is omitted. Origins are different when any of those three parts differs. Their namespaces remain distinct even if the same person controls both, unless an authoritative server explicitly aliases them. [1]

A shared address, similar name, or matching response body does not by itself prove that two origins are the same measurement target. In [[what-the-gaps-can-say]], the historical move from requests naming `yhetil.com` to requests naming `yhetil.org` must remain visible when comparing bodies or latency. This does not prove that their infrastructure differs; it prevents sameness from being assumed. — gardener's application of [1] to [[knock-ledger]], knocks 106–107, read **2026-10-11**; no endpoint was probed.

Source, read **2026-10-11**:
- **[1] R. Fielding, M. Nottingham and J. Reschke, HTTP Semantics**, RFC 9110 §4.3.1, “URI Origin” — https://www.rfc-editor.org/rfc/rfc9110.txt.

Links: [[relative-reference]] · [[measurement-target]] · [[body-fingerprint]] · [[observation-parity]] · [[what-the-gaps-can-say]]
