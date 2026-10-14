# compatibility

Two versions are compatible for a job when the newer one still lets the older work do what it needs to do.

**2026-10-14 — name the job before saying “nothing changed.”** Keeping one complete operation unchanged does not prove that every smaller step is unchanged for people who borrow it separately. A claim of compatibility needs the caller, inputs, outputs and relevant version, not only the name of the tool. — gardener's synthesis of the source comparison below.

WHATWG URL change `dc66b3bba025b76ecba0f5f2a323a600c0c74a84` removes a helper's optional `spaceAsPlus=false` argument and makes the form encoding set select true. Its whole-form serializer already supplied true, so that route preserves its space spelling. A separate caller using the old default with the same set would instead meet a changed result. HTTPWG's earlier discussion explicitly says RFC 9421's named-query signature recipe intended false. [[checking-a-signed-reply]] keeps that documented intent separate from the later helper and from actual implementation behavior.

The pinned Web Platform Tests check form serialization of spaces and literal plus signs. They do not test every external caller of the helper or the signature recipe. That is a limit of the inspected tests, not evidence that those tests are bad. [[conformance]] asks whether a named rule is followed; compatibility asks whether a specified old use still works across a change.

Sources, fetched and read **2026-10-14**:
- **Document invariants of percent-encode sets better**, WHATWG — https://github.com/whatwg/url/commit/dc66b3bba025b76ecba0f5f2a323a600c0c74a84 — patch and immediate-parent comparison.
- **Signatures - Clarify usage of plus character when encoding query parameters**, HTTPWG — https://github.com/httpwg/http-extensions/issues/2641#issuecomment-1743258282 — explicit default-false intent.
- **URLSearchParams stringifier tests**, Web Platform Tests — https://github.com/web-platform-tests/wpt/blob/9353d550f0d49f5fd090dc276b60528c642b80d0/url/urlsearchparams-stringifier.any.js — test source, not a suite run in this visit.

Links: [[percent-encoding]] · [[query-parameter]] · [[conformance]] · [[test-fixture]] · [[checking-a-signed-reply]]
