# What table, keys, and uniqueness rules does public-inbox's published Msgmap implementation actually use, and how does it handle missing, repeated, or multiple Message-ID headers when assigning article numbers?

The recovery rooms can compare saved maps, but their example still assumes the message key and its uniqueness. Connect [comparing-saved-maps](../../rooms/comparing-saved-maps.md) and [same-mail-same-numbers](../../rooms/same-mail-same-numbers.md) through [article-number-map](../../words/article-number-map.md), [database-constraint](../../words/database-constraint.md), and [collation](../../words/collation.md), distinguishing raw Message-ID headers from the key actually stored. Read the public implementation and its tests at a named release or commit, alongside the documentation, and say which comparison assumptions hold for missing, repeated, or multiple headers; do not open local databases or run a restore.

commissioned: 2026-10-11
