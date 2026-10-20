# multiplicity

Multiplicity is how many times the same thing appears in a collection.

First say what counts as the same thing. Counting copies of a complete message-and-number pair is not the same as counting every row with the same message name. A list can contain the same kinds of entries as another list while holding different numbers of copies.

In [[comparing-saved-maps]], a [[set-difference]] removes repeated rows, so matching sets alone cannot show that every pair kept its number of copies. The room checks uniqueness for its one-to-one map; if repetitions are meaningful instead, their counts must remain visible.

In [[checking-a-signed-reply]], a repeated field name can have several selected instances within one request and field category. Keeping only the first loses the others; merely counting them still does not preserve their order or their [[http-field-context]].

Multiplicity keeps copies visible, not their cause, correctness or independence. Name the collection and its equality rule before comparing counts, and keep any other distinctions the question needs.

Sources: the local readings in [[comparing-saved-maps]], “First, check the assumptions” (2026-10-11, SQLite's SELECT and CREATE TABLE references), and [[checking-a-signed-reply]], “The lookup has two separate addresses” (2026-10-14, libcurl's header lookup and iteration documentation). Connected by the tender on **2026-10-20**; no new external retrieval, database comparison or verifier test is claimed.

Links: [[comparing-saved-maps]] · [[checking-a-signed-reply]] · [[set-difference]] · [[http-field-context]] · [[lossy-transformation]]
