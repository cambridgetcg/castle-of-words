# utf-8

UTF-8 is a way to write text as bytes so computers can store and send it.

**2026-10-14 — bytes need rules before they become letters.** A character can take one or several bytes. Not every possible byte sequence is valid UTF-8: the decoder checks which leading and following bytes are allowed, including limits that prevent a character being written in an overly long form. The name of the encoding does not, by itself, choose what to do with invalid input.

WHATWG's **UTF-8 decode without BOM** hook uses replacement error handling; its separately named **UTF-8 decode without BOM or fail** hook uses fatal error handling. The form-query parser chooses the former. It can therefore turn different invalid inputs into the same text, as [[decoding-query-names]] demonstrates. “Without BOM” means no special removal of a leading byte-order mark in this hook: valid bytes for U+FEFF remain that character.

Sources, fetched and read **2026-10-14**:
- **Encoding Standard**, WHATWG, pinned revision `a985b62a9b45c17da3e17a9f0a0b4e30c34c4a8a` — https://raw.githubusercontent.com/whatwg/encoding/a985b62a9b45c17da3e17a9f0a0b4e30c34c4a8a/encoding.bs — UTF-8 decoder and the two decoding hooks.
- **URL Standard**, WHATWG, pinned revision `fde3f74f063341a28d437216f75735b8b40128f5` — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs — application/x-www-form-urlencoded parsing.

Links: [[replacement-character]] · [[percent-encoding]] · [[query-parameter]] · [[decoding-query-names]]
