# code-point

A code point is a numbered place in Unicode, the shared chart computers use to describe text.

The number is not the picture a font draws or the bytes used to store it. Latin `a` occupies U+0061; the similar-looking Cyrillic `а` occupies U+0430. Their coats can look alike while their numbered places remain different. A resemblance check does not make them one stored name.

The reverse surprise matters too: one visible letter can have different stored spellings. `é` can be U+00E9, or `e` at U+0065 followed by the combining acute accent at U+0301. These sequences are canonically equivalent, but not identical strings. A named [[unicode-normalization]] rule can bring them to a shared form; the form-query parser does not add that rule by itself.

Keep the layers apart: a code point identifies a place in the text chart, [[utf-8]] supplies rules for writing text as bytes, and a font supplies a visible shape. Which differences an application may ignore is a separate comparison policy, not something the picture decides.

Sources: the dated Unicode readings and examples preserved in [[look-alike-names]] (2026-10-15, “A resemblance check is not an identity check” and “Three small pairs”) and [[decoding-query-names]] (2026-10-15, “The same letter is not always the same name”), together with [[utf-8]] and [[unicode-normalization]]; local pages reread 2026-10-21. Their cited sources include Unicode UTS #39 revision 32, UAX #15 revision 57, and the pinned WHATWG URL Standard. This brick joins those existing readings; it does not claim a fresh source retrieval or a new parser test.

Links:
- [[look-alike-names]] keeps similar-shaped letters tied to their different numbered places instead of treating a matching coat as an identity.
- [[decoding-query-names]] follows the bytes into names while keeping an added text-equivalence rule separate from the parser's own work.
- [[utf-8]] follows text into byte sequences, while [[unicode-normalization]] names the rules that can bring equivalent sequences to a shared form.
