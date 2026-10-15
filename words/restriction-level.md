# restriction-level

A restriction level says how tightly a name follows rules about allowed characters and mixing writing systems.

**2026-10-15 — classify one name, not its author's purpose.** Unicode UTS #39 revision 32 defines six levels: ASCII-Only, Single Script, Highly Restrictive, Moderately Restrictive, Minimally Restrictive and Unrestricted. The most restrictive level a name meets depends on the chosen identifier syntax and character profile, not on its appearance alone.

All levels require the applicable syntax to be satisfied. Levels 1–5 also require the character profile; Unrestricted may include characters outside that profile but does not mean arbitrary invalid text is accepted. With no further profile, Minimally Restrictive and Unrestricted coincide.

Single Script uses a nonempty [[resolved-script-set]], not merely a count of obvious alphabets. Highly Restrictive permits specified combinations of Latin with Japanese, Korean, or Han/Bopomofo writing. Moderately Restrictive also allows Latin with one other Recommended script, **except Cyrillic or Greek** in this pinned revision. Minimally Restrictive puts no additional limit on script mixtures.

Under the General Security Profile and default identifier syntax used for the examples in [[look-alike-names]], Latin `paper` is ASCII-Only, mixed `pаper` with Cyrillic U+0430 is Minimally Restrictive, and all-Cyrillic `ѕсоре` is Single Script. Yet the last name has the same [[confusable-skeleton]] as Latin `scope`. A strict script policy alone therefore does not remove all look-alike pairs; even ASCII `m` and `rn` can be confusable.

A level is not a probability of deception or a universal safety verdict. An application's choice of threshold, extra checks, warnings or registration rules is a separate policy. WHATWG form-query parsing does not automatically apply these levels.

**2026-10-15 — the profile has a version too.** [[identifier-status]] names the Allowed/Restricted character filter used by the General Security Profile. The semantic 17-to-18 comparison in [[look-alike-names]] found one newly Allowed code point and no Allowed-to-Restricted changes. That does not establish that every complete restriction-level or identifier-acceptance result is unchanged: syntax, script properties, context rules and application exceptions are additional inputs. UTS #39's migration guidance requires a strategy for saved results and permits documented compatibility overrides; it does not authorize renaming existing identifiers.

Source for this addition: **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 34, §§2–5 and “Migrating Persistent Data,” https://www.unicode.org/reports/tr39/tr39-34.html, fetched and read **2026-10-15**; pinned data and the comparison receipt live in [[look-alike-names]].

Sources, fetched and read **2026-10-15**:
- **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 32, Unicode 17.0.0, §§3.1, 4–5.2 — https://www.unicode.org/reports/tr39/tr39-32.html.
- **Unicode Security Mechanisms: IdentifierStatus.txt**, version 17.0.0 — https://www.unicode.org/Public/17.0.0/security/IdentifierStatus.txt. The examples' syntax, script and Allowed-status checks are recorded in [[look-alike-names]].
- **URL Standard**, WHATWG, pinned source `fde3f74f063341a28d437216f75735b8b40128f5`, form parsing — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs.

Links: [[resolved-script-set]] · [[confusable-skeleton]] · [[look-alike-names]] · [[decoding-query-names]] · [[query-parameter]] · [[conformance]] · [[identifier-status]] · [[data-migration]]
