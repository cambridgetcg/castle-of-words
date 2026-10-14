# replacement-character

A replacement character is a mark a computer can put where it could not read some text.

**2026-10-14 — the mark does not keep the missing bytes.** Unicode names this character U+FFFD, usually displayed as `�`. In WHATWG's replacement decoding mode, each error returned by the decoder adds this character to the output. The decoder's rules decide how much input each error consumes; replacement is not simply one mark for every byte.

For the form-query parser, `%FF` and `%FE` both yield one U+FFFD. But `%EF%BF%BD` is a valid UTF-8 spelling of U+FFFD and yields exactly the same text without an error. Seeing the character afterward therefore cannot tell which input produced it. These hypothetical examples were checked locally; [[decoding-query-names]] records the sources, inputs and bounded test result.

A malformed percent escape is different: `%G1` remains `%G1` under the form parser's percent-decoding step. It is not turned into U+FFFD merely because the escape is malformed.

This technical character is not the castle's [[replacement-mark]]: that word names a dated record of something missing, not a text-decoding rule.

Sources, fetched and read **2026-10-14**:
- **Encoding Standard**, WHATWG, pinned revision `a985b62a9b45c17da3e17a9f0a0b4e30c34c4a8a` — https://raw.githubusercontent.com/whatwg/encoding/a985b62a9b45c17da3e17a9f0a0b4e30c34c4a8a/encoding.bs — “Process an item,” “UTF-8 decode without BOM,” and “UTF-8 decoder.”
- **URL Standard**, WHATWG, pinned revision `fde3f74f063341a28d437216f75735b8b40128f5` — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs — byte percent-decoding and form parsing.

Links: [[utf-8]] · [[percent-encoding]] · [[query-parameter]] · [[decoding-query-names]] · [[replacement-mark]]
