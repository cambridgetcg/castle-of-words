# collation

A collation is a rule a computer uses to compare pieces of text.

SQLite's built-in `BINARY` compares string data with a bytewise comparison; `NOCASE` treats ASCII uppercase and lowercase letters alike; `RTRIM` ignores trailing spaces. These are different definitions of equal, not merely different ways to display a list. SQLite's built-in `NOCASE` is not full Unicode case folding. — SQLite, **Datatypes In SQLite — Collating Sequences**, https://www.sqlite.org/datatype3.html#collating_sequences; read **2026-10-11**.

When checking whether saved identifiers kept exactly their stored spelling, [[comparing-saved-maps]] explicitly uses `COLLATE BINARY` for differences, grouping, and joins. Otherwise a case or trailing-space change could disappear under a looser comparison. This is a chosen preservation rule, not a claim that every application ought to treat those spellings as different identities. — gardener's synthesis of the same source, **2026-10-11**.

A collation compares text; it does not by itself settle missing values, duplicate rows, or unlike storage types. Those need their own checks before an empty [[set-difference]] can support the promised [[data-invariant]].

Links: [[comparing-saved-maps]] · [[set-difference]] · [[article-number-map]] · [[data-invariant]] · [[operational-definition]]
