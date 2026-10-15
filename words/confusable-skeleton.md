# confusable-skeleton

A confusable skeleton is a working copy of text used to spot different names that can look alike.

**2026-10-15 — a comparison aid, not a replacement name.** Unicode UTS #39 maps visually related characters to common representative spellings. Two strings with equal skeletons are confusable under that mechanism, not necessarily identical strings or [[canonical-equivalence|canonically equivalent]] text.

In revision 32, Unicode 17.0.0, `skeleton(X)` means `bidiSkeleton(LTR, X)`. The direction-aware operation handles display ordering, combining marks and mirroring **before** applying the internal skeleton. That internal step uses NFD, removes Default_Ignorable_Code_Point characters, substitutes prototypes, and reapplies NFD. Left-to-right strings without R or AL bidi classes have a specified fast path. [[look-alike-names]] checks only all-L Latin/Cyrillic examples, not the general bidirectional algorithm.

For example, Latin `paper` and `pаper` with Cyrillic U+0430 in place of its `a` both yield `paper`. Latin `m` and `rn` both yield `rn`. These hypothetical pairs remain distinct under NFC and NFKC; a visual comparison is not the same operation as [[unicode-normalization]].

Skeletons are not intended for display and may not themselves be valid identifiers. UTS #39 explicitly forbids treating its confusability mapping as identifier normalization. The results are not guaranteed stable across Unicode versions; stored skeletons must be recomputed when the computing version changes.

**2026-10-15 — compare versions before reusing a saved result.** The Unicode 17-to-18 comparison in [[look-alike-names]] found added, removed and retargeted mappings, but also a removed Ç row whose full skeleton stays unchanged because NFD runs first. All 42 bounded assertions passed. A table change is not automatically a changed string comparison; a changed comparison is not authority to change an identity. [[data-migration]] names the work of rebuilding saved comparisons, while [[identifier-status]] names a separate character filter.

Source for this addition: **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 34, §4 and “Migrating Persistent Data,” https://www.unicode.org/reports/tr39/tr39-34.html, fetched and read **2026-10-15**; the pinned data, hashes and execution limits are recorded in [[look-alike-names]].

**uncertain:** whether any particular reader would confuse a pair in a particular font, or whether its writer intended deception. The mechanism can be overly inclusive and is not a detector of intent. A matching skeleton does not authorize merging identities or names.

Sources, fetched and read **2026-10-15**:
- **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 32, Unicode 17.0.0, §§4, 6–6.1 and “Migrating Persistent Data” — https://www.unicode.org/reports/tr39/tr39-32.html.
- **Unicode Security Mechanisms: confusables.txt**, version 17.0.0 — https://www.unicode.org/Public/17.0.0/security/confusables.txt. The bounded local example-check receipt is in [[look-alike-names]].

Links: [[restriction-level]] · [[resolved-script-set]] · [[unicode-normalization]] · [[canonical-equivalence]] · [[look-alike-names]] · [[decoding-query-names]] · [[lossy-transformation]] · [[identifier-status]] · [[data-migration]]
