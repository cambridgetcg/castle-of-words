# null

Null is a marker for no value, not the number zero or an empty word.

In the SQLite examples here, `NULL` marks a missing value; it does not explain why the value is missing. A message-number comparison must check for missing identifiers before claiming that the old pairings survived. The `NULL` printed on an absent side of a comparison report is instead an output marker, not a stored message identifier. — [comparing-saved-maps](../rooms/comparing-saved-maps.md), read 2026-10-21.

The operation matters. SQLite's `UNIQUE` rule can allow several nulls, while `EXCEPT` treats nulls as equal when comparing rows. A child foreign key with a null key column can also satisfy its rule without naming a parent row. A clean constraint check therefore need not mean that a relationship is populated. — [comparing-saved-maps](../rooms/comparing-saved-maps.md) and [checking-a-restored-map](../rooms/checking-a-restored-map.md), drawing on SQLite's [SELECT rules](https://www.sqlite.org/lang_select.html), [CREATE TABLE rules](https://www.sqlite.org/lang_createtable.html), and [foreign-key rules](https://www.sqlite.org/foreignkeys.html); local rooms read 2026-10-21, external sources not fetched again.

A manifest's null hash has a different contract: it needs a stated reason to distinguish never published, deleted, and unavailable. Do not borrow SQL comparison rules for that field, or turn its silence into proof that a kept copy is sound. — [null-hash-semantics](../rooms/null-hash-semantics.md), read and qualified 2026-10-21.

Links:
- [[database-constraint]] names the rule whose treatment of missing values must be checked, not assumed.
- [checking-a-restored-map](../rooms/checking-a-restored-map.md) shows how a permitted empty key can leave a relationship unfilled behind a passing check.
- [comparing-saved-maps](../rooms/comparing-saved-maps.md) keeps missing identifiers out of the promised map before comparing its pairs.
- [null-hash-semantics](../rooms/null-hash-semantics.md) asks the blank place to carry its reason rather than a guessed history.
