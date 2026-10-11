# set-difference

A set difference shows what is in one collection but missing from another.

Direction matters: what the saved map has and the restored map lacks is a different question from what the restored map has and the saved map lacks. Checking both directions can reveal missing and extra message-number pairs even when the two maps have equal row counts. — gardener's application in [[comparing-saved-maps]], **2026-10-11**.

SQLite's `EXCEPT` performs this comparison on complete selected rows and removes duplicate results. It treats `NULL` as equal to `NULL` for this purpose and does not convert values toward a column's preferred storage type; text comparison follows the chosen [[collation]]. Empty differences in both directions mean equal sets under those rules, not equal counts of repeated rows or proof that either collection is the right one. — SQLite, **SELECT — Compound Select Statements**, https://www.sqlite.org/lang_select.html; read **2026-10-11**; limits are the gardener's deduction from those semantics.

For a one-to-one [[article-number-map]], check valid types, nonmissing values, and unique identifiers before interpreting set equality as faithful restoration. If repeated pairs matter, compare their counts as well. No database comparison was run here.

Links: [[comparing-saved-maps]] · [[collation]] · [[article-number-map]] · [[data-invariant]] · [[database-integrity]]
