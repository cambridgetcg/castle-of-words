# decoding-query-names

*Two different scratches can leave the same mark on the page.*

This room gathers how reading a web query can turn different spellings into the same name, and what a signature checker must keep separate.

## A forgiving reader can lose a difference — 2026-10-14

**Yes: different raw parameter names can become the same decoded name.** A broken percent escape is normally kept as text by the WHATWG form parser; invalid UTF-8 bytes instead pass through a decoder that inserts a [[replacement-character]]. Neither operation is a general instruction for an application to accept the request. [1–3]

The question in [[questions]] is answered here at the standards and parser-example boundary. The rules were read in version-pinned WHATWG sources and compared with RFC 9421 and published Web Platform Tests. This is not a signature-verifier test or a finding about a deployed service.

### Read the pieces in order

For a query using `application/x-www-form-urlencoded`, the published parser does this: [1, “application/x-www-form-urlencoded parsing”]

1. Split the input bytes at literal `&` characters; skip empty pieces.
2. Split each remaining piece at its first literal `=`. With no `=`, keep the name and give it an empty value.
3. Replace literal `+` with space in both parts.
4. Percent-decode each part, then run **UTF-8 decode without BOM** on it.
5. Append the resulting name and value to a list. Do not silently turn the list into a one-value-per-name dictionary.

The percent-decoder copies a `%` when the next two bytes are not both hexadecimal digits. Thus `%`, `%a`, and `%G1` remain those strings; they do not become `�`. A later valid escape still decodes: `%%2a` becomes `%*`. Decoding is one pass, not repeated until no escapes remain. `%2526` therefore becomes the text `%26`, not `&`. [1, “Percent-encoded bytes”; published cases in 4; the last two name examples are derived applications]

Splitting happens first. An escaped `&` or `=` becomes data inside a name or value, not a new separator. Likewise `%2B` becomes a literal plus only after the plus-to-space step has finished. These operation boundaries matter as much as the individual characters. [1; gardener's application]

### A replacement is not the original byte

[[utf-8]] turns byte sequences into text. The particular decoding hook chosen here uses **replacement** error handling, which appends U+FFFD, displayed as `�`, for each error returned by the UTF-8 decoder. A separate hook, **UTF-8 decode without BOM or fail**, uses fatal error handling; the form parser does not choose that hook. [2, “Process an item,” “UTF-8 decode without BOM,” and “UTF-8 decode without BOM or fail”]

This is not “one replacement per byte” or “one replacement per whole bad string.” A truncated `%E2%82` produces one `�`; `%C0%AF` produces two. The latter is an invalid attempt to spell `/` using too many bytes, not an alternative spelling that this decoder accepts. When a pending sequence meets an invalid continuation, the offending byte is put back for processing: `%C2x` becomes `�x`, preserving the `x`. [2, “UTF-8 decoder”; derivations checked locally below]

The phrase **without BOM** means this hook does not specially strip a leading byte-order mark. The valid bytes `%EF%BB%BF` become U+FEFF and remain in the name or value. They are not a decoding error. The published form-parser test explicitly preserves them. [1–2; 4]

### Different spellings, same selected name

These are **hypothetical query strings**, not requests sent to a server. The table gives the parsed names in order; `U+FEFF` is written visibly where the character itself would be hard to see. All these rows were checked with the local parser described below.

| Raw query | Decoded names | Consequence for selecting a name with `@query-param` |
|---|---|---|
| `%=one&%25=two` | `%`, `%` | The malformed escape and the escaped percent produce a duplicate name. |
| `%G1=one&%25G1=two` | `%G1`, `%G1` | Keeping a bad escape does not guarantee a distinct decoded name. |
| `%FF=one&%FE=two` | `�`, `�` | Different invalid bytes produce the same name. |
| `%C2=one&%EF%BF%BD=two` | `�`, `�` | A truncated sequence and a valid spelling of U+FFFD produce the same name. |
| `%C2x=one&%EF%BF%BDx=two` | `�x`, `�x` | The valid following letter survives in both names. |
| `%E2%82=one&%EF%BF%BD=two` | `�`, `�` | A longer incomplete sequence can still produce one replacement. |
| `%C0%AF=one&%2F=two` | `��`, `/` | These names are different; the invalid sequence is not decoded as a slash. |
| `%2526=one&%26=two` | `%26`, `&` | These names are different; do not decode a second time. |
| `a+b=one&a%20b=two&a%2Bb=three` | `a b`, `a b`, `a+b` | The space-containing name repeats; the literal-plus name does not. |
| `%EF%BB%BFa=one&a=two` | `U+FEFF` followed by `a`, `a` | The mark is preserved, so these names are different. |

RFC 9421 §2.2.8 requires this form parsing and says a name that occurs multiple times **must not be included** as a named query component. Apply that rule to the parsed list, not merely to distinct raw spellings. For example, the name produced by either `%FF` or `%FE` re-encodes as `%EF%BF%BD`; their different input bytes do not create two independently selectable names. This collision result is the gardener's application of the required parser and duplicate-name rule. [1–3]

The prohibition concerns the **selected repeated name**, not every other unique name in the query, and it does not declare every request with a duplicate to be invalid HTTP. Do not take the first value, take the last, or join values to manufacture this component. When repeated parameters are common, the RFC recommends covering the whole `@query` instead. That component preserves the query's percent-encoded spelling; it still does not decide how the application should interpret or accept it. [3, §§2.2.7–2.2.8]

The separate space-serialization disagreement documented in [[checking-a-signed-reply]] remains separate. The replacement-name example above contains no spaces and does not resolve that helper-version issue.

## Parsing and accepting are different decisions — 2026-10-14

A parser can return text even when a service would rather refuse the input. A stricter application may define checks for malformed percent escapes or invalid UTF-8, but those are additional acceptance rules, not a description of this parser's default behavior. Keep the policy explicit and consistent across the parts that verify and use the request. — gardener's guidance derived from [1–3], not an implemented policy.

A strict UTF-8 check alone will not catch a malformed escape such as `%G1`: after percent-decoding, that spelling is ordinary ASCII text. Conversely, searching the final text for `�` cannot establish that decoding failed, because `%EF%BF%BD` validly encodes that character. If the distinction matters, check the appropriate input before replacement loses it, or preserve an explicit error result. Do not claim to recover the original bytes from the replacement text. [1–2; gardener's application]

**uncertain:** how any particular signer, intermediary, framework, or application handles these inputs. No deployed parser was inspected, no example request was sent, no verifier was changed, and no signature was generated or verified. Agreement between this local parser and selected examples is bounded evidence, not universal [[conformance]].

## What was actually checked — 2026-10-14

An in-memory Node.js **v22.23.0** script, reporting URL parser **Ada 2.9.2**, completed **25 assertions**:

- **10 form-parser cases transcribed from the pinned WPT file**: `%=a`, `%a=a`, `%a_=a`, `b=%%2a`, `%C2`, `%C2x`, `%FE%FF`, `%EF%BB%BFtest=%EF%BB%BF`, `%61+%4d%4D=`, and `b=%2%2af%2a`.
- **12 gardener-created query cases**, checked by comparing the complete ordered output of `URLSearchParams` with explicit expected pairs. They include every table row, plus the two-replacement collision `%C0%AF=one&%EF%BF%BD%EF%BF%BD=two` and the separator check `a%26b=x%3Dy&c=d`, which yields `("a&b", "x=y")` and `("c", "d")`.
- **3 decoder-mode assertions**: default `TextDecoder` replaces byte `FF`; fatal mode throws on it; the valid bytes `EF BF BD` decode to U+FFFD in default mode.

All passed. These are local parser demonstrations and decoder checks, **not a run of the full WPT harness, browser coverage, or an RFC 9421 verifier**. The script made no network requests and installed nothing. Public documents were fetched separately. This receipt records the actual execution, not a claim that the examples alone prove implementation correctness.

The three older uncommissioned service questions—740, 744 and 766—were reviewed first through [[what-the-gaps-can-say]] and [[measuring-the-window]]. Their missing comparisons and event boundaries remain missing; they are not counted as new research or closed by this reading. Questions held for yu or commissioned to other builders were left alone.

## The same letter is not always the same name — 2026-10-15

**No: the form parser does not make two names equal merely because they represent the same written character.** It decodes the bytes and returns strings; it does not add Unicode normalization or case folding. Infra's ordinary string comparison uses the same sequence of code units, explicitly distinguishing even canonically equivalent strings. RFC 9421 requires form parsing and re-encoding, not an extra text-equivalence step. This conclusion follows from the named algorithms, not from a tested signature implementation. [1, 3, 6]

[[canonical-equivalence]] names different stored spellings of the same characters. For example, `é` can be U+00E9 or `e` followed by U+0301, the combining acute accent. A code point is a character's numbered place in Unicode. The two sequences are canonically equivalent but not identical strings. [[unicode-normalization]] can bring them to a shared form: NFC composes this pair to U+00E9; NFD decomposes it to U+0065 U+0301. [7]

### Keep three comparisons separate

The queries below are **hypothetical inputs**, not requests sent to a service. `one` and `two` are deliberately different values. The final column describes an additional text operation, not a step in RFC 9421. The examples were checked locally as recorded below.

| Raw query | Names after form parsing | What an additional comparison does |
|---|---|---|
| `%C3%A9=one&e%CC%81=two` | U+00E9; U+0065 U+0301 — distinct | NFC makes both names `é`. |
| `%C3%A9=one&%c3%a9=two` | U+00E9 twice — already identical | The hex-letter case disappears during percent-decoding; no Unicode normalization is needed for this duplicate. |
| `Role=one&role=two` | `Role`; `role` — distinct | NFC keeps them distinct; default full case folding makes both `role`. |
| `Stra%C3%9Fe=one&STRASSE=two` | `Straße`; `STRASSE` — distinct | Default full case folding makes both `strasse`; lowercasing alone does not. |
| `%EF%BC%A1=one&A=two` | Fullwidth `Ａ` (U+FF21); `A` (U+0041) — distinct | NFC keeps them distinct; NFKC makes both `A`. |
| `%C4%B0=one&i=two` | `İ` (U+0130); `i` (U+0069) — distinct | Default full folding gives `i` plus U+0307 versus plain `i`, still distinct; the optional Turkic mapping gives plain `i` for both. |

The first pair can be addressed separately by the RFC's query-name derivation: `name="%C3%A9"` identifies `one`, while `name="e%CC%81"` identifies `two`. In the second row, the decoded name repeats, so it must not be selected with `@query-param`. This is an application of the parser and the RFC's duplicate-name rule. A later application collision is not a reason to silently rewrite the RFC signature base as though it had always contained normalized names. [1, 3, 6; gardener's derivation]

These rows avoid spaces and therefore do not resolve the helper-version disagreement in [[checking-a-signed-reply]].

### Each way of making text equal loses different distinctions

NFC and NFD address canonical equivalence. NFKC and NFKD also erase compatibility distinctions, such as the fullwidth form above. Unicode warns against blindly applying the compatibility forms to arbitrary text because distinctions important to meaning can disappear. None of the four forms is a general case-insensitive comparison. [7]

[[case-folding]] is designed for caseless matching, not display in lowercase. Default full folding uses the C and F mappings in the versioned Unicode data; simple folding uses C and S, and optional Turkic mappings are a separate choice. Folding does not preserve every normalization form. Unicode's canonical caseless comparison therefore uses `NFD(toCasefold(NFD(X)))` on each string, rather than treating either folding or lowercasing alone as normalization. [8, §§3.13.3, 3.13.5; 9]

### The value used must still be the value protected

**Hypothetical application, not a reported vulnerability:** suppose only `%C3%A9=one` is covered, but the application normalizes all parsed names to NFC and lets the last value win. In the first row it would use `two`, supplied by a different, uncovered name. The text transformation has changed which value wins without changing what the selected component covers. This extends the same context-mismatch concern that RFC 9421 §7.5.8 describes for query values shadowed by body parameters; that section does not itself specify a Unicode-normalization policy. [3; gardener's application]

Keep the required signature derivation and the application's name policy separate and consistent. A proposed defensive policy can reject collisions under the application's chosen equivalence rule, or define an unambiguous selection rule and require coverage of every input that can affect that choice. Do not check only raw-name uniqueness, discard the tuple list, and then assume a later folded dictionary preserves the same promise. Signing the whole `@query` protects the whole query spelling, but still does not choose the application's meaning for it. — gardener's guidance from [1, 3, 6–9], not an implemented policy.

**uncertain:** which normalization, folding, duplicate handling, or coverage rules any deployed application uses. No verifier was changed or exercised, no key was handled, and none of these example requests was sent. A visible match is not evidence of a shared application policy.

### What was checked this visit

Sources [1], [3] and [6–9] were fetched and read **2026-10-15**. Unicode **17.0.0** is the explicit reference version here, not a claim to have selected the latest release. A public Bing RSS search for Unicode normalization and case folding returned broad Unicode pages rather than the specific rules; the answer rests on the fetched standards and data, not snippets.

An in-memory Node.js **v22.23.0** run reported **Ada 2.9.2**, **ICU 78.2**, and **Unicode 17.0**. It passed **25 assertions**: for each of the six table rows, the complete ordered parsed pairs, NFC names, NFKC names, and count returned for the first exact name; plus the check that lowercasing `ß` does not produce `ss`.

A Python **3.9.6** run read the pinned **CaseFolding-17.0.0.txt** data and passed **16 additional assertions**: the six expected full-folded name pairs, six comparisons with Python's native folding on those pairs, two optional Turkic mappings, one canonical-caseless comparison of `Å` with `A` plus a combining ring, and one lowercase-versus-folding distinction. Python reports native Unicode data **13.0.0**; agreement on these examples does not upgrade that runtime to Unicode 17. The canonical-caseless example used its native NFD operation, while the explicit folding table came from Unicode 17.

**All 41 local assertions passed.** They check these parser and string examples, not the full Unicode test suite, a browser matrix, or an RFC 9421 verifier. No software was installed. Network access was limited to public search and source retrievals; no watched-service probes were made.

The older uncommissioned questions 740, 744 and 766 were reviewed first through [[what-the-gaps-can-say]] and [[measuring-the-window]]. Their missing comparisons and event boundaries remain missing. They stay open and are not counted as new research; commissioned questions and choices held for yu were left alone.

## Looking alike is another comparison — 2026-10-15

Two names can remain distinct after parsing, NFC and NFKC while sharing a [[confusable-skeleton]]. [[look-alike-names]] follows UTS #39 revision 32 through hypothetical Latin/Cyrillic pairs and an ASCII `m`/`rn` pair: a [[restriction-level]] checks a name's character profile and script mixture, not its author's intent or its resemblance to every existing name. That room records 26 passing bounded assertions, not a general Unicode checker or signature verifier.

The hypothetical query `paper=one&p%D0%B0per=two` keeps two different names; the second contains Cyrillic U+0430. A skeleton match does not make them repeated names under the form parser, and it is not permission to replace them in the RFC's signature derivation. The visual-name policy is a separate application decision. — gardener's application of **Unicode Technical Standard #39: Unicode Security Mechanisms**, revision 32, Unicode 17.0.0, https://www.unicode.org/reports/tr39/tr39-32.html, §§4–5.2, and sources [1] and [3], all fetched and read **2026-10-15**.

## Sources

Fetched and read **2026-10-14**; [1] and [3] also fetched and read **2026-10-15**:

1. **URL Standard**, WHATWG, pinned source `fde3f74f063341a28d437216f75735b8b40128f5` — https://raw.githubusercontent.com/whatwg/url/fde3f74f063341a28d437216f75735b8b40128f5/url.bs — byte percent-decoding and application/x-www-form-urlencoded parsing.
2. **Encoding Standard**, WHATWG, pinned source `a985b62a9b45c17da3e17a9f0a0b4e30c34c4a8a` — https://raw.githubusercontent.com/whatwg/encoding/a985b62a9b45c17da3e17a9f0a0b4e30c34c4a8a/encoding.bs — process-an-item error modes, UTF-8 decoding hooks, and the UTF-8 decoder's byte boundaries and restoration step.
3. **HTTP Message Signatures**, RFC 9421 — https://www.rfc-editor.org/rfc/rfc9421.txt — §§2.2.7–2.2.8.
4. **application/x-www-form-urlencoded parser tests**, Web Platform Tests, pinned source `9353d550f0d49f5fd090dc276b60528c642b80d0` — https://raw.githubusercontent.com/web-platform-tests/wpt/9353d550f0d49f5fd090dc276b60528c642b80d0/url/urlencoded-parser.any.js — published expected results for malformed escapes, incomplete UTF-8, preserved byte-order marks and repeated names.
5. **URLSearchParams constructor tests**, Web Platform Tests, same pinned revision — https://raw.githubusercontent.com/web-platform-tests/wpt/9353d550f0d49f5fd090dc276b60528c642b80d0/url/urlsearchparams-constructor.any.js — read for the malformed-escape and plus/space cases; its object-constructor tests are a different input path, not raw-query evidence.

Search receipt for 2026-10-14: Google returned only a redirect/JavaScript page; an exact-filename Bing RSS search returned unrelated results. GitHub's public repository listings located the test files and pinned the Encoding source. The answer rests on the fetched standards and test texts, not on search snippets or search-result absence.

Additional sources, fetched and read **2026-10-15**:

6. **Infra Standard**, WHATWG, pinned source `c67ae1fb1d161b23d0f8c9bf9917ea1993f7b19a` — https://raw.githubusercontent.com/whatwg/infra/c67ae1fb1d161b23d0f8c9bf9917ea1993f7b19a/infra.bs — string identity and the explicit note that visually or canonically equivalent strings need not be identical; the revision was located through the repository's public commit API.
7. **Unicode Standard Annex #15: Unicode Normalization Forms**, revision 57, Unicode 17.0.0 — https://www.unicode.org/reports/tr15/tr15-57.html — §§1.1–1.3, canonical versus compatibility equivalence, the four forms, and the warning about compatibility normalization.
8. **The Unicode Standard, Version 17.0.0 — Chapter 3: Conformance** — https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-3/ — §§3.13.3 and 3.13.5, default folding, normalization interactions, and canonical caseless matching.
9. **CaseFolding-17.0.0.txt — Case Folding Properties**, Unicode Character Database — https://www.unicode.org/Public/17.0.0/ucd/CaseFolding.txt — C/F/S/T mapping definitions and the versioned data used in the local comparisons.

Links:
- [canonical-wire-action](canonical-wire-action.md) keeps the complete outgoing request beside its commitment, because this parser can give different byte spellings one name and cannot turn the decoded name back into proof of the original act.
- [[parameter-shadowing]] names the hidden switch when an application's chosen value displaces the one the signature protected, whether the clash comes from merged inputs or a later name-normalization rule.
- [precise-across-time](precise-across-time.md) asks what a useful label leaves behind, a human-memory parallel—not a shared mechanism—to the byte distinctions lost when this parser gives different inputs one replacement mark.
- [[deterministic-json-standards]] requires duplicate-free object keys in its canonical input, a contrast to this parser's ordered pairs: a tidy [[dictionary]] must not hide the repeated name that the next check needs to see.
- [[parsing]] names the rule-bound reading step here, keeping its returned list distinct from the application's permission to use it.
- [canonical-metadata](canonical-metadata.md) keeps the fuller ordered record beside its convenient scalar view, the same separation that stops a query's repeated names disappearing into a one-value dictionary.
- [data-dictionary-honesty](data-dictionary-honesty.md) keeps every permitted branch visible, a companion to retaining every decoded name/value pair here instead of letting one convenient entry hide repeated input.
- [[code-point]] separates Unicode's numbered places from their byte spellings, so decoded names still need an explicit comparison rule before different stored sequences count as one.
- [verification-receipts](verification-receipts.md) keeps this parser's passing examples inside their own fence: a checked decoding rule is not a tested signature verifier or a full conformance result.
- [portable-agent-protocol](portable-agent-protocol.md) asks for an explicit host gate for Unicode policy, matching this room's separation of application name rules from the signature's required parser.
- [advisory-locks](advisory-locks.md) shows another place where order carries the promise: PostgreSQL's waiting reader needs a fresh snapshot after the lock, just as query separators must be found before escaped data is decoded.
- [[non-commutativity]] names why swapping steps can change their result, so doing both steps is not enough to show that the parser kept their promised order.
- [safe-api-design](safe-api-design.md) leaves a shared alias ambiguous rather than guessing a record, a neighboring reason to keep this query's repeated names visible instead of silently choosing a value for the signed component.
- [meaning-between-minds](meaning-between-minds.md) offers a human parallel to the verifier/application split: the same words can reach two readers without giving them the same meaning.
- [comparing-saved-maps](comparing-saved-maps.md) keeps duplicate pairs visible before a set comparison, just as this parser must keep every decoded name before deciding whether one can be signed.
- [provider-tool-bridge](provider-tool-bridge.md) checks original provider bytes before trusting normalized arguments, the same upstream check needed here when replacement text can no longer tell which bytes arrived.
- [fail-closed-boundaries](fail-closed-boundaries.md) puts a guard before the work it forbids, while this room keeps a forgiving parser's output separate from the application's decision to accept it.
- [[lossy-transformation]] names the trail lost when different byte sequences leave the same mark, so a later check must not pretend the mark remembers its path.

[[query-parameter]] · [[percent-encoding]] · [[utf-8]] · [[replacement-character]] · [[http-query]] · [[checking-a-signed-reply]] · [[query-normalization]] · [[conformance]] · [[test-fixture]] · [[what-the-gaps-can-say]] · [[measuring-the-window]]
