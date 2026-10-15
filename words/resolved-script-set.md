# resolved-script-set

A resolved script set lists the writing systems that can account for every character in a piece of text.

**2026-10-15 — look for a shared writing system.** A script is a writing system, such as Latin or Cyrillic. Unicode UTS #39 revision 32 begins with each character's `Script_Extensions`: the scripts with which that character is used. It augments those sets for Japanese, Korean and Han/Bopomofo writing, then keeps only script values shared across every character's augmented set. This shared part is the intersection.

Characters whose script set contains Common or Inherited are treated as permitting all script values for this intersection. That prevents shared punctuation or inherited marks from automatically making a name mixed-script. It does not exempt them from the application's permitted-character profile or syntax checks.

If the intersection is empty, the string is mixed-script; if nonempty, it is single-script in the standard's defined sense. “Single-script” does **not** require the result to contain exactly one script value. The standard's Japanese Hiragana/Katakana example `ねガ` shares the augmented Japanese writing-system value even though the characters' individual script labels differ.

In the simpler examples in [[look-alike-names]], Latin `paper` has the Latin result, all-Cyrillic `ѕсоре` has the Cyrillic result, and `pаper` mixing Latin with Cyrillic U+0430 has an empty result. Script sets help classify [[restriction-level|restriction levels]] and kinds of confusable pairs; they do not by themselves decide visual resemblance, language, identity or intent.

Sources, fetched and read **2026-10-15**:
- **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 32, Unicode 17.0.0, §§4 and 5.1, especially Table 1a — https://www.unicode.org/reports/tr39/tr39-32.html.
- **Unicode Character Database: Scripts-17.0.0.txt** — https://www.unicode.org/Public/17.0.0/ucd/Scripts.txt.
- **Unicode Character Database: ScriptExtensions-17.0.0.txt** — https://www.unicode.org/Public/17.0.0/ucd/ScriptExtensions.txt. The Latin/Cyrillic examples were checked against these data; the Japanese example above is taken from the specification, not a locally tested script resolver.

Links: [[restriction-level]] · [[confusable-skeleton]] · [[look-alike-names]] · [[unicode-normalization]] · [[canonical-equivalence]]
