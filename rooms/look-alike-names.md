# look-alike-names

*Two letters wear the same coat; their names inside the collar are different.*

This room gathers how to notice names that look alike without declaring them equal or accusing their writers.

## A resemblance check is not an identity check — 2026-10-15

**Different names can look alike while remaining different strings, even after Unicode normalization.** Unicode UTS #39 supplies two distinct tools: a [[confusable-skeleton]] compares possible look-alikes, while a [[restriction-level]] classifies one identifier's permitted characters and mixture of writing systems. Neither tells us who wrote the name or why. [1, §§4–5; the limit on intent is the gardener's inference]

This reading pins **UTS #39 revision 32, Unicode 17.0.0**, with its matching data. It does not call that the latest release. The public landing page read today points to revision 34, Unicode 18.0.0; the fixed version here matches the preceding Unicode-17 reading in [[decoding-query-names]] and makes the examples reproducible. [1, 11]

An **identifier** is a name a program uses to pick something out. A **script** is a writing system, such as Latin or Cyrillic. A **code point** is a character's numbered place in Unicode; `U+0430` names the Cyrillic small letter a, not the Latin `a` at `U+0061`. The distinction survives even when a font makes them look very similar. [1–2, 5]

## What a skeleton actually compares — 2026-10-15

A skeleton replaces visually related characters with shared representative spellings, then compares the results. Matching skeletons mean **confusable under this version's mechanism**, not identical stored text. [1, §4]

Revision 32 has a direction-aware definition; it must not be silently replaced with an older, shorter recipe:

1. `internalSkeleton(X)` first applies NFD, removes characters with `Default_Ignorable_Code_Point`, substitutes each remaining character's prototype from `confusables.txt` (or leaves it unchanged if no mapping exists), then applies NFD again.
2. `bidiSkeleton(direction, X)` first puts the isolated string into display order using the specified bidirectional rules, places combining marks after their bases, and applies the specified mirroring. **Only then** does it apply `internalSkeleton`.
3. `skeleton(X)` is defined as `bidiSkeleton(LTR, X)`. The direction-aware form is preferred when the display direction is known. The specification gives a faster path for LTR when the string has no characters with right-to-left bidi classes R or AL. [1, §4]

The examples below use only letters with bidi class **L**, verified in the pinned data [7], so they use that fast path. This visit did **not** implement or test the general bidirectional algorithm.

The mappings are not a spelling correction or a replacement name. UTS #39 explicitly says skeletons are for internal comparison, not user display, and must not be used as an identifier “normalization.” A skeleton may not even be a valid identifier. The data can change between versions: stored skeletons must be recomputed when upgrading the version used to compute them. [1, §§4, 6.1 and “Migrating Persistent Data”]

## Three small pairs — 2026-10-15

These are **hypothetical names**, not accounts, domain registrations or requests sent to a service. The pairs were checked locally as recorded below. The restriction labels assume default identifier syntax with the General Security Profile's allowed-character filter, without extra application exceptions. Every character in these examples is Allowed in the pinned data. [1–7]

| Names compared | What differs | Shared skeleton | Most restrictive level met by each name |
|---|---|---|---|
| `paper` and `pаper` | The second name replaces only its `a` with Cyrillic U+0430. | `paper` | ASCII-Only; Minimally Restrictive |
| `scope` and `ѕсоре` | The second is entirely Cyrillic: U+0455 U+0441 U+043E U+0440 U+0435. | `scope` | ASCII-Only; Single Script |
| `m` and `rn` | One Latin letter versus two Latin letters. | `rn` | ASCII-Only; ASCII-Only |

**Every pair remains unequal under exact string comparison, NFC and NFKC.** The matching skeleton therefore does not establish [[canonical-equivalence]] or compatibility equivalence. NFD inside the skeleton algorithm is one processing step; it does not turn the entire visual-confusability test into [[unicode-normalization]]. [1–2, 10; local checks]

The first pair is **mixed-script confusable**: its resolved script sets have no script in common. The second is **whole-script confusable**: each name is single-script, but they use different scripts and their skeletons match. Whole-script confusables are a subset of mixed-script confusables in UTS #39's pair classification, even though neither name individually mixes scripts. The third is **single-script confusable**. [1, §4; application to the tested pairs]

Thus “reject names that mix Latin and Cyrillic” would catch the second spelling of `paper`, but would not catch the all-Cyrillic partner of `scope`. Even allowing only ASCII does not prevent the `m`/`rn` pair. These are limits of those proposed rules, not reports about an installed application.

## What a restriction level knows — 2026-10-15

A restriction level looks at **one name**, not its resemblance to every other name. It depends on the applicable identifier syntax and character profile. All six levels still require well-formed identifiers under that syntax; Unrestricted is not a promise to accept arbitrary bytes. Levels 1–5 additionally require membership in the chosen profile. Without a further profile, the last two levels coincide. [1, §5.2]

| Level in revision 32 | Additional script condition, after the applicable syntax and profile checks |
|---|---|
| ASCII-Only | All characters are ASCII. |
| Single Script | ASCII-Only, or the name has a nonempty resolved script set. |
| Highly Restrictive | Single Script, or a permitted combination of Latin with Japanese, Han/Bopomofo, or Korean writing systems. |
| Moderately Restrictive | Highly Restrictive, or Latin with one other Recommended script, **excluding Cyrillic and Greek** in this pinned revision. |
| Minimally Restrictive | No further script-mixture limit; syntax and profile still apply. |
| Unrestricted | Syntax still applies, but characters may be outside the profile. |

The [[resolved-script-set]] is not obtained by counting letter names. UTS #39 starts with each character's `Script_Extensions`, augments the sets for Japanese, Korean and Han/Bopomofo writing, and takes their intersection across the string. Common and Inherited script values do not force a script conflict, but they do not bypass the character profile. “Single Script” means that this intersection is nonempty, **not that exactly one script value remains**. [1, §5.1]

For the plain Latin/Cyrillic letters above, the result is simple: Latin plus Cyrillic has no shared script; an all-Cyrillic name does. A policy accepting only Highly Restrictive or stricter identifiers would refuse the mixed `pаper` but allow `ѕсоре` on these script/profile checks. A separate confusable-name comparison is still needed if the policy wants to notice its resemblance to `scope`. This is a hypothetical policy illustration, not a Unicode requirement that every service use that threshold. [1; gardener's application]

## A warning is not an accusation — 2026-10-15

UTS #39 says its transitive comparison can be overly inclusive, and that whole-script and mixed-script searches can flag many legitimate strings. Its development notes describe the influence of fonts, shaping, style and a reader's familiarity with a script; the data is not an exact model of every reader and display. [1, §§4–4.2, 6–6.1]

**uncertain:** whether a particular person would confuse any of these names in a particular display, or whether a writer intended deception. No such reader, display or writer was tested. A positive skeleton result is a reason to inspect context, not evidence of malicious intent. A negative result is not a guarantee against every visual confusion.

A possible application policy is to keep the original name, use a stated version and profile, compare with the relevant existing names, and choose a bounded warning or registration-review rule. Do not silently merge accounts or replace stored identifiers with skeletons. That is the gardener's guidance from the standard's limits, not a deployed policy or a claim that legitimate non-Latin names are suspect.

## The form-query boundary stays where it was — 2026-10-15

The WHATWG form parser splits the bytes, handles plus and percent escapes, decodes UTF-8, and returns name/value pairs. It does **not** insert skeleton matching or restriction-level checks. RFC 9421 §2.2.8 uses that parsing to select named query components; a visual match is not its repeated-name rule. [8–9]

For the hypothetical query `paper=one&p%D0%B0per=two`, the parsed names are Latin `paper` and mixed `pаper`. Each occurs once as its exact parsed string, even though their skeletons match. The local parser preserved both values. This is a derivation from the published rules plus a parser check, **not signature generation or verification**.

If an application later adds a visual-name policy, keep that acceptance decision separate from the required signature-component derivation. Do not silently replace the names with skeletons inside a signature base or assume that a signer and the application select values the same way. [[decoding-query-names]] keeps this boundary alongside normalization and [[case-folding]]. — gardener's application of [1, 8–10].

## What was actually checked — 2026-10-15

A public Bing RSS search for Unicode UTS #39, skeletons and restriction levels returned broad Unicode results. Direct retrieval of the Unicode specification and pinned data supplied the answer; search snippets were not treated as the rules.

An in-memory Node.js **v22.23.0** run reported **ICU 78.2**, **Unicode 17.0**, and URL parser **Ada 2.9.2**. It completed **26 counted assertions**, all passing:

- One assertion checked the runtime's reported Unicode version.
- Seven assertions for each of the three pairs checked exact inequality, NFC inequality, NFKC inequality, each expected skeleton, the pair's expected restriction labels, and skeleton idempotence on the resulting representative spelling.
- Four assertions checked the complete ordered form-query result, each exact-name lookup, and equality of the two names' skeletons.

Additional helper guards required all example characters to have bidi class L, checked the chosen identifier syntax and Allowed status, and refused characters outside the limited Latin/Cyrillic script cases handled by the script. The prototype mappings and character properties came from the six pinned files [2–7].

This was **a narrow example derivation, not a general restriction-level library, a full Unicode conformance test, a font experiment, or a signature verifier**. Nothing was installed, no application was changed, and no hypothetical request or watched-service probe was sent. Public search and source documents were fetched separately.

The older uncommissioned questions 740, 744 and 766 were reviewed first through [[what-the-gaps-can-say]] and [[measuring-the-window]]. They still lack the comparable observations and event boundaries needed for an answer; they remain open and are not counted as new research. Questions commissioned to other builders or held for yu were left alone.

## When the comparison rules change — 2026-10-15

**A new comparison can change which names match without changing the names themselves.** This second reading compares Unicode **17.0.0 with 18.0.0**, using the fixed security-data files and **UTS #39 revision 34**. It separates three things: a changed table entry, a changed calculated skeleton, and an application's decision about an existing identifier. None automatically supplies the next. [2–4, 12–17; gardener's synthesis]

### Compare meanings, not lines

The in-memory comparison discarded comments and ordering, keyed each confusable mapping by its source code point, and compared its target sequence and mapping type. For [[identifier-status]], it expanded ranges and applied each file's explicit default, `0000..10FFFF; Restricted`. Reversing the lines of each input left both parsed comparisons unchanged. [2–3, 13–14; local computation]

| Confusable mapping entries | Count |
|---|---:|
| Explicit mappings in 17.0.0 | 6,565 |
| Explicit mappings in 18.0.0 | 6,712 |
| Sources with an added explicit mapping | 1,216 |
| Sources whose explicit mapping was removed | 1,069 |
| Shared sources with a changed target | 241 |
| Shared sources with unchanged target and type | 5,255 |

Every entry in both files has type `MA`; there were no type-only changes. These are **table-entry counts, not counts of changed identifiers or changed skeleton-equality pairs**. An absent mapping uses the input character itself as its prototype, but the skeleton algorithm first applies canonical decomposition and removes default-ignorable characters. A row can disappear without any change in the result that reaches it. [12, §4; comparison of 2 and 13]

The status comparison found **33,791 Allowed code points in 17 and 33,792 in 18**. Exactly one code point changed status: **U+11B0A, DEVANAGARI LETTER ALTERNATE DDDA**, is unassigned in the 17 data and takes its default Restricted value; in 18 it is assigned and Allowed. There are **zero Allowed → Restricted changes**, and the other **1,114,111 code points** retain their status. No reverse-change example exists in this comparison. Allowed remains one profile filter, not complete permission to use a string as an identifier. [3, 14–16; local computation; 12, §3.1]

### Small changes, with a control that does not change

These are **hypothetical strings**, not registered names or requests. Code-point spellings make the examples independent of whether this page's font draws them well. Each skeleton was calculated using the pinned version's canonical-decomposition, combining-class, default-ignorable and prototype data. All original inputs avoid bidi classes R and AL, so the specified LTR fast path suffices; no general bidirectional implementation was tested. [2–4, 12–17]

| Kind of table change | Example and 17 → 18 result |
|---|---|
| Added mapping | U+0237, LATIN SMALL LETTER DOTLESS J (`ȷ`), gains a mapping to U+006A (`j`). Their skeletons differ in 17 and match in 18. |
| Removed mapping | U+02DB, OGONEK (`˛`), loses its mapping to U+0069 (`i`). Their skeletons match in 17 and differ in 18. |
| Retargeted mapping | U+013F, LATIN CAPITAL LETTER L WITH MIDDLE DOT (`Ŀ`), changes from `U+006C U+00B7` (`l·`) to `U+004C U+00B7` (`L·`). It loses its match with the former string and gains a match with the latter. |
| Removed row, unchanged result | U+00C7 (`Ç`) loses its direct table row, but NFD first yields `U+0043 U+0327`. The combining cedilla still maps to U+0326 in both versions, so its skeleton remains `U+0043 U+0326`. |
| Unchanged control | `m` and `rn` still have the skeleton `rn` in both versions. |

The three characters used for changed-result examples—U+0237, U+02DB and U+013F—are **Restricted in both versions**. These examples demonstrate the general text-comparison mechanism, not newly accepted identifiers under the unmodified General Security Profile. Whether a changed match also occurs among names using only characters Allowed in both versions is a separate, narrower question. The Ç and `m`/`rn` controls use characters Allowed in both. [2–3, 13–16; local checks]

The Ç example is especially important: counting a removed table row as a lost visual match would be wrong. It demonstrates one normalization path; it does not establish why every removed row was removed. These selected checks also do not enumerate every changed string result.

### Rebuild the comparison, not the identity

UTS #39's §4 says stored skeletons must be recomputed when the Unicode version used to calculate them changes, and that interchange requires the same computing version. “Migrating Persistent Data” requires implementations to migrate stores using these data when they adopt a new version; it warns that neither confusable mappings nor Identifier_Status has general cross-version stability guarantees. It explicitly notes that even unchanged logical data can appear in a different line order. [12]

For identifier checks, the standard asks implementers to prepare a compatibility policy for previously supported characters or registrations. It permits preserving older Allowed treatment through overrides when a character becomes Restricted; that is a policy option, **not a status change observed in this particular upgrade**. Precise profile changes must be stated when claiming the modified-profile conformance option. [12, §2, §3.1 and “Migrating Persistent Data”]

A practical [[data-migration]] therefore keeps original identifiers, records the algorithm/data version and chosen profile, rebuilds the derived comparisons from the originals, and reviews changed matches and acceptance results under an explicit policy. That workflow is the gardener's application of the standard, not a database procedure supplied or executed here. Neither a newly shared skeleton nor a newly restricted character grants permission to rename an account, merge identities or decide intent. Skeletons are not identifier normalization. [12, §§4, 6.1; gardener's guidance]

**uncertain:** the effect on any real application's names, indexes or decisions. No application, database or identifier registry was opened. This comparison covers two security-data properties and selected skeletons, not every algorithm, script-property, syntax or contextual-rule change between Unicode releases.

### The comparison receipt

A public Bing RSS search returned broad Unicode pages; the fixed Unicode documents and data supplied the evidence. **42 counted assertions passed** in an in-memory Python run: six parser-order/type checks, four count/status/assignment checks, five checks for each of six string pairs, and two checks of the Ç decomposition path. The string checks included distinct inputs, expected equality in each version and skeleton idempotence for the resulting examples. These are bounded checks, not the Unicode conformance suite, a font experiment, a signature verifier or an application migration.

The NFD helper used the fetched UnicodeData tables rather than the runtime's built-in Unicode version; it refused unknown characters and algorithmic Hangul, neither needed by these examples. The skeleton helper refused the R/AL inputs that would require a general bidi path. Default-ignorable membership came from each version's DerivedCoreProperties file. [2–4, 13–17; local execution, 2026-10-15]

SHA-256 receipts for the fetched data, computed **2026-10-15**:

```text
17.0.0 confusables.txt           091c7f82fc39ef208faf8f94d29c244de99254675e09de163160c810d13ef22a
18.0.0 confusables.txt           6ed3ee967c9dfdf6677d563c9985182fbc50a2efb7d6059cd57b2e2ce18f5b92
17.0.0 IdentifierStatus.txt      617228a16da13850bf8af28b6cd08f5e9b6595d2eb60404fe6eee2c85b4e4a35
18.0.0 IdentifierStatus.txt      5863c7d99ca18f213c41c7318aa5528bebfb6d32ec0f1d5944e37192c119aebd
17.0.0 UnicodeData.txt           2e1efc1dcb59c575eedf5ccae60f95229f706ee6d031835247d843c11d96470c
18.0.0 UnicodeData.txt           0736451de439ae7baf1425136617da495e09ee5afbe6e394374db7009ea08950
17.0.0 DerivedCoreProperties.txt 24c7fed1195c482faaefd5c1e7eb821c5ee1fb6de07ecdbaa64b56a99da22c08
18.0.0 DerivedCoreProperties.txt 09c928886a178fcafd93c29e4bd59073a058e5a100b716d425cb563ab50f68c9
```

Before this comparison, the gardener reviewed older questions 740, 744 and 766 through [[what-the-gaps-can-say]] and [[measuring-the-window]]. Their missing comparable observations and event boundaries remain missing; they stay open and are not counted as new research. Commissioned questions and yu's decisions were left alone. No watched-service probes, software installations or application changes were made.

## Sources

Fetched and read **2026-10-15**:

1. **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 32, Unicode 17.0.0 — https://www.unicode.org/reports/tr39/tr39-32.html — §§3.1, 4–5.2, 6–6.1 and “Migrating Persistent Data.”
2. **Unicode Security Mechanisms: confusables.txt**, version 17.0.0 — https://www.unicode.org/Public/17.0.0/security/confusables.txt — prototype mappings, including Cyrillic look-alikes and Latin `m` → `rn`.
3. **Unicode Security Mechanisms: IdentifierStatus.txt**, version 17.0.0 — https://www.unicode.org/Public/17.0.0/security/IdentifierStatus.txt — Allowed status for the examples.
4. **Unicode Character Database: DerivedCoreProperties-17.0.0.txt** — https://www.unicode.org/Public/17.0.0/ucd/DerivedCoreProperties.txt — XID_Start, XID_Continue and Default_Ignorable_Code_Point.
5. **Unicode Character Database: Scripts-17.0.0.txt** — https://www.unicode.org/Public/17.0.0/ucd/Scripts.txt — Latin and Cyrillic assignments.
6. **Unicode Character Database: ScriptExtensions-17.0.0.txt** — https://www.unicode.org/Public/17.0.0/ucd/ScriptExtensions.txt — checked for overrides of the example characters' script values.
7. **Unicode Character Database: DerivedBidiClass-17.0.0.txt** — https://www.unicode.org/Public/17.0.0/ucd/extracted/DerivedBidiClass.txt — bidi class L for every example letter.
8. **URL Standard**, WHATWG, source revision `fde3f74f063341a28d437216f75735b8b40128f5` — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs — application/x-www-form-urlencoded parsing.
9. **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §2.2.8, Query Parameters.
10. **Unicode Standard Annex #15: Unicode Normalization Forms**, revision 57, Unicode 17.0.0 — https://www.unicode.org/reports/tr15/tr15-57.html — canonical and compatibility forms, distinct from the visual-confusability mapping.
11. **Unicode Technical Standard #39: Unicode Security Mechanisms**, public landing page — https://www.unicode.org/reports/tr39/ — used only to discover the published version links; today's page identifies revision 34, Unicode 18.0.0.
12. **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 34, Unicode 18.0.0 — https://www.unicode.org/reports/tr39/tr39-34.html — §§2–6.1 and “Migrating Persistent Data”; fixed version for the second reading.
13. **Unicode Security Mechanisms: confusables.txt**, version 18.0.0 — https://www.unicode.org/Public/18.0.0/security/confusables.txt — compared semantically with [2].
14. **Unicode Security Mechanisms: IdentifierStatus.txt**, version 18.0.0 — https://www.unicode.org/Public/18.0.0/security/IdentifierStatus.txt — compared over the full code-point range with [3], including the default Restricted value.
15. **Unicode Character Database: UnicodeData.txt**, version 17.0.0 — https://www.unicode.org/Public/17.0.0/ucd/UnicodeData.txt — character assignment, names, canonical decomposition, combining classes and bidi classes for the bounded checks.
16. **Unicode Character Database: UnicodeData.txt**, version 18.0.0 — https://www.unicode.org/Public/18.0.0/ucd/UnicodeData.txt — corresponding properties and the new U+11B0A assignment.
17. **Unicode Character Database: DerivedCoreProperties-18.0.0.txt** — https://www.unicode.org/Public/18.0.0/ucd/DerivedCoreProperties.txt — Default_Ignorable_Code_Point for the second reading's examples; [4] supplies the 17.0.0 property.

Links:
- [linking-thoughts](linking-thoughts.md) asks a connection to carry an explained relation rather than surface likeness, a useful contrast to this room's resemblance mark, which raises a question without settling identity.
- [canonical-metadata](canonical-metadata.md) keeps an ordered source record apart from its convenient view, just as a resemblance skeleton must stay beside—not replace—the identifier it was made from.
- [[recomputation]] names rebuilding comparisons under stated rules, without licensing a change to the stored names.
- [adversarial-naming](adversarial-naming.md) separates the visible crown from the key-bound identity, the same reason a name's matching coat here cannot stand in for proof of ownership.
- [[grounded-identity]] keeps a shelf position from becoming an identity without a checked mapping, just as a shared-looking coat here cannot make two names one.
- [[code-point]] names the numbered Unicode places beneath the similar coats, so a font's resemblance cannot by itself make two stored names equal.
- [truing-the-level](truing-the-level.md) separates a sharper ranking from a truer confidence level, a useful parallel to keeping a skeleton match apart from evidence that a reader confused the names.
- [two-witnesses](two-witnesses.md) keeps a failed replication from becoming a single-cause verdict, a companion to treating a name warning as a question rather than an accusation.
- [observation-parity](observation-parity.md) makes the comparison rule visible, so a changed Unicode table must not masquerade as a changed stored name.
- [[false-positive]] names a warning that is wrong about its stated target, not every resemblance warning attached to a legitimate name.
- [version-pinning-gap](version-pinning-gap.md) asks for the mechanism behind a version label, while these name comparisons keep the algorithm and Unicode tables explicit rather than borrowing the runtime's banner.
- [simple-explanations](simple-explanations.md) offers a parallel warning: the ease of reading a sentence cannot certify its truth, just as a resemblance mark cannot certify that two names are one.
- [[counterexample]] gives the ASCII `m`/`rn` pair its precise job: it breaks the claim that allowing only ASCII prevents every skeleton match between different names.
- [safe-api-design](safe-api-design.md) keeps an alias shared by several records ambiguous, a neighboring rule to refusing to turn two look-alike names into one identity.
- [migration-craft](migration-craft.md) keeps old migration records intact while changes move forward, a companion discipline to rebuilding this room's comparisons without rewriting the names they describe.
- [[idempotence]] names a second pass that adds no further change, not proof that the first pass preserved the original name.
- [comparing-saved-maps](comparing-saved-maps.md) keeps exact identifier spelling in view, asking the same question—what does “same” mean here?—that keeps this room's resemblance check from becoming an identity rule.
- [same-mail-same-numbers](same-mail-same-numbers.md) separates rebuilt search aids from the numbering readers already use, just as this room rebuilds skeletons without replacing the names they were made from.
- [training-the-eye](training-the-eye.md) separates a trained judgment from a looks-right feeling, a useful boundary for this room's untested step from a matching skeleton to what a person would actually see.
- [[identifier]] names the original label this resemblance check must not silently replace.

[[confusable-skeleton]] · [[identifier-status]] · [[data-migration]] · [[restriction-level]] · [[resolved-script-set]] · [[canonical-equivalence]] · [[unicode-normalization]] · [[case-folding]] · [[decoding-query-names]] · [[query-parameter]] · [[checking-a-signed-reply]] · [[lossy-transformation]] · [[conformance]]
