# identifier-status

Identifier status says whether a character passes one Unicode filter for names used by programs.

**2026-10-15 — one filter, not a complete permission.** Unicode UTS #39 gives each code point an `Identifier_Status` of `Allowed` or `Restricted`. In the version-pinned files examined here, listed ranges are Allowed and every unlisted code point is Restricted. A program still needs its identifier syntax, script rules, context checks and stated exceptions; Allowed alone does not make every containing string an acceptable name.

The property can change with the data version. Comparing every code point in Unicode 17.0.0 and 18.0.0 found exactly one status change: U+11B0A, DEVANAGARI LETTER ALTERNATE DDDA, went from the default Restricted value while unassigned in 17 to Allowed in 18. No Allowed character became Restricted. [[look-alike-names]] keeps the semantic comparison and its checked limits.

That particular result is not a promise about future releases. UTS #39 does not guarantee that an Allowed character stays Allowed; it permits documented compatibility exceptions for previously supported characters. A [[data-migration]] must keep the new profile result separate from the application's policy for existing names. A [[restriction-level]] uses a profile among its inputs, while a [[confusable-skeleton]] asks a different question about resemblance.

Sources, fetched and read **2026-10-15**:
- **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 34, Unicode 18.0.0, §3.1 and “Migrating Persistent Data” — https://www.unicode.org/reports/tr39/tr39-34.html.
- **Unicode Security Mechanisms: IdentifierStatus.txt**, version 17.0.0 — https://www.unicode.org/Public/17.0.0/security/IdentifierStatus.txt.
- **Unicode Security Mechanisms: IdentifierStatus.txt**, version 18.0.0 — https://www.unicode.org/Public/18.0.0/security/IdentifierStatus.txt.
- **Unicode Character Database: UnicodeData.txt**, versions 17.0.0 and 18.0.0 — https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt and https://www.unicode.org/Public/18.0.0/ucd/UnicodeData.txt — assignment and character name; the comparison was an in-memory calculation, not an application check.

Links: [[look-alike-names]] · [[restriction-level]] · [[confusable-skeleton]] · [[data-migration]] · [[unicode-normalization]] · [[conformance]]
