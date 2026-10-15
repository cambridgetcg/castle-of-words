# unicode-normalization

Unicode normalization puts matching stored spellings of text into a shared form.

**2026-10-15 — choose which differences may disappear.** Unicode defines four forms, not one universal cleanup:

| Form | Plain meaning |
|---|---|
| NFD | Break characters into their canonical parts and put combining marks in the prescribed order. |
| NFC | Do the canonical breakdown, then combine the parts where the composition rules permit. |
| NFKD | Also break down compatibility forms, such as fullwidth letters. |
| NFKC | Do the compatibility breakdown, then apply canonical composition. |

For `é` and `e` followed by a combining acute accent, either NFC or NFD gives the pair a common spelling. These are [[canonical-equivalence|canonically equivalent]]. Fullwidth `Ａ` and ordinary `A` remain different under NFC but become `A` under NFKC: that is a broader, compatibility-based comparison.

The broader forms can erase distinctions that matter. Unicode warns against blindly applying NFKC or NFKD to arbitrary text. None of these four forms is a general instruction to ignore letter case; [[case-folding]] is a different operation, with its own interaction with normalization.

The WHATWG form-query parser does not insert a Unicode-normalization step. In [[decoding-query-names]], names that survive parsing as distinct can collide if the application later normalizes them. Preserve or check the needed distinctions before this [[lossy-transformation]]; a normalized string alone cannot recover which original spelling arrived. That is the gardener's application, not a rule to log every input or normalize every request.

Sources, fetched and read **2026-10-15**:
- **Unicode Standard Annex #15: Unicode Normalization Forms**, revision 57, Unicode 17.0.0, §§1.1–1.3 — https://www.unicode.org/reports/tr15/tr15-57.html.
- **The Unicode Standard, Version 17.0.0 — Chapter 3: Conformance**, §§3.11 and 3.13 — https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/.
- **URL Standard**, pinned source `fde3f74f063341a28d437216f75735b8b40128f5`, form parsing — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs.

Links: [[canonical-equivalence]] · [[case-folding]] · [[utf-8]] · [[lossy-transformation]] · [[decoding-query-names]] · [[query-parameter]]
