# canonical-equivalence

Canonical equivalence means that two pieces of text represent the same characters even when their stored spellings differ.

**2026-10-15 — the same letter need not have the same stored shape.** Unicode can represent `é` as U+00E9, or as `e` (U+0065) followed by a combining acute accent (U+0301). These are canonically equivalent sequences, but an exact string comparison can still tell them apart. A code point is a character's numbered place in Unicode; the `U+` notation writes that number.

[[unicode-normalization]] gives equivalent strings a common form for comparison. NFC brings this pair to U+00E9; NFD brings it to U+0065 U+0301. Neither the word “equivalent” nor the appearance on a page makes this transformation happen automatically.

Canonical equivalence is narrower than **compatibility equivalence**, which can ignore distinctions such as fullwidth versus ordinary Latin letters. It is also different from [[case-folding]], which supports comparison without case differences. Mere visual resemblance does not by itself establish any of these relations.

In [[decoding-query-names]], `%C3%A9=one&e%CC%81=two` produces two distinct parsed names. A later NFC step makes those names equal. The parsing rule and the application's equality rule therefore need separate names; do not let the second silently replace the first.

Sources, fetched and read **2026-10-15**:
- **Unicode Standard Annex #15: Unicode Normalization Forms**, revision 57, Unicode 17.0.0, §§1.1–1.2 — https://www.unicode.org/reports/tr15/tr15-57.html.
- **Infra Standard**, pinned source `c67ae1fb1d161b23d0f8c9bf9917ea1993f7b19a`, string identity — https://raw.githubusercontent.com/whatwg/infra/c67ae1fb1d161b23d0f8c9bf9917ea1993f7b19a/infra.bs.
- **URL Standard**, pinned source `fde3f74f063341a28d437216f75735b8b40128f5`, form parsing — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs. The query is a hypothetical example checked locally, not a sent request.

Links: [[unicode-normalization]] · [[case-folding]] · [[utf-8]] · [[query-parameter]] · [[decoding-query-names]]
