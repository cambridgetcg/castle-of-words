# identifier

An identifier is a name or number a system uses to point to a thing.

A label needs its setting. In [[same-mail-same-numbers]], a message's Message-ID, its newsreader article number, and its Git object identifier are different handles; preserving the mail does not by itself preserve every old handle. A [[stable-identifier]] adds a promise of continuity across time, which the word *identifier* alone does not make.

**Say how names are compared.** [[decoding-query-names]] shows that different query spellings can decode to the same name, while names still distinct after parsing can meet under an application's later normalization or case-folding rule. [[comparing-saved-maps]] instead chooses exact stored spelling for its recovery check and applies that choice consistently through its [[collation]]. These are different contracts, not one universal definition of “the same name.”

**A resemblance mark is not a replacement name.** [[look-alike-names]] keeps the original text separate from its [[confusable-skeleton]]: `m` and `rn` can share a skeleton without becoming identical strings. Rebuilding that derived comparison for a new Unicode version does not grant permission to rename accounts, merge them, or decide what their writers intended.

Grounding, read locally **2026-10-15**: [[look-alike-names]] carries the identifier definition and pinned UTS #39 readings; [[decoding-query-names]] carries the WHATWG and RFC 9421 comparison rules; [[comparing-saved-maps]] carries SQLite's exact-text contract; [[same-mail-same-numbers]] carries public-inbox's separate numbering promise. This brick gathers those distinctions; no service, database, or new identifier policy was tested.

Links:
- [[look-alike-names]] separates the name inside the collar from the coat another name may share.
- [[decoding-query-names]] follows the label through reading rules that can erase a difference before it reaches the application.
- [[comparing-saved-maps]] checks whether each saved label still leads to its promised number.
- [[same-mail-same-numbers]] keeps the letter and its familiar shelf mark as two recovery promises.
- [[stable-identifier]] adds the promise that the handle will keep pointing to the same thing over time.
