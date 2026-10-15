# case-folding

Case folding gives text a shared spelling for comparisons that ignore differences such as `A` and `a`.

**2026-10-15 — matching is not the same job as printing in lowercase.** Unicode's default full case folding can expand a character: `ß` folds to `ss`, so `Straße` and `STRASSE` both fold to `strasse`. Lowercasing alone leaves `ß` in place. Some folding mappings even use uppercase letters; the goal is a comparison form, not a preferred display style.

The versioned `CaseFolding.txt` data distinguishes **full** folding, using C and F mappings, from **simple** folding, using C and S mappings. C entries are shared by both; F entries may expand to several characters; S entries keep a single-character mapping where it differs. The default excludes the optional Turkic T mappings. For example, default full folding maps `İ` to `i` plus a combining dot, while a Turkic mapping can map it to plain `i`. A policy must say which operation it means.

Folding is not [[unicode-normalization]], and it does not preserve every normalization form. Unicode's **canonical caseless matching** compares `NFD(toCasefold(NFD(X)))` with the same expression for the other string. The surrounding normalization steps matter; “lowercase both” is not that algorithm. Unicode also defines `NFKC_Casefold` for identifiers, combining compatibility handling with removal of default-ignorable characters and final NFC normalization. That is another named operation, not permission to apply it indiscriminately to query names.

In [[decoding-query-names]], `Role=one&role=two` has distinct parsed names; full case folding would turn both into `role`. That later collision is an application-policy issue, not a folding step required by RFC 9421. Its prescribed query-component derivation must remain separate from deciding what value the application uses.

Sources, fetched and read **2026-10-15**:
- **The Unicode Standard, Version 17.0.0 — Chapter 3: Conformance**, §§3.13.3 and 3.13.5 — https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/.
- **CaseFolding-17.0.0.txt — Case Folding Properties**, Unicode Character Database, header and the U+00DF, U+0049 and U+0130 mappings — https://www.unicode.org/Public/17.0.0/ucd/CaseFolding.txt.
- **HTTP Message Signatures**, RFC 9421 §2.2.8 — https://www.rfc-editor.org/rfc/rfc9421.txt. The query is hypothetical; local string checks are not a signature-verifier test.

Links: [[unicode-normalization]] · [[canonical-equivalence]] · [[query-parameter]] · [[decoding-query-names]] · [[lossy-transformation]] · [[signature-coverage]]
