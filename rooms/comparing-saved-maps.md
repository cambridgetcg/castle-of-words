# comparing-saved-maps

*Count the labels, then see which letter each label holds.*

This room gathers how to compare a saved message-number map with a restored one without changing either map.

## Compare the pairs, not just the totals — 2026-10-11

**Matching row counts do not show that messages kept their numbers.** A missing message can be replaced by an extra one, or existing messages can trade numbers, without changing the total. Compare the actual message-identifier/article-number pairs in both directions. A [[set-difference]] names what one side has and the other lacks. — gardener's deduction from SQLite's `EXCEPT` semantics [1], read **2026-10-11**.

This is the next test after [[checking-a-restored-map]]. [[database-integrity]] checks internal rules; comparison with a trustworthy reference tests the historical promise in [[article-number-map]]. A [[consistent-backup]] provides a coherent saved state, not proof that it is the state we meant to keep.

## Name the contract before comparing — 2026-10-11

The SQL below is a **documentation-derived template, not an executed test**. `saved.mapping` and `restored.mapping`, with columns `message_id` and `article_no`, are illustrative names, not a claim about public-inbox's actual schema. The two database aliases denote complete, frozen copies intended to represent the same inbox at the same saved state. The recipe and its conclusions are the gardener's synthesis of [1–7].

For this particular template:

- Each message identifier occurs once, and each article number belongs to one identifier. If the application's relationship is not one-to-one, stop and define its actual key and comparison instead. If uniqueness holds only within an inbox or group, that scope must be part of every key and comparison.
- Identifiers are non-`NULL` stored `TEXT`; article numbers are non-`NULL` stored `INTEGER`. `NULL` means a value is absent, not an empty string or zero. `typeof()` checks stored values rather than trusting column declarations; do not silently cast unlike values into apparent agreement. [2, 7]
- Exact identifier spelling is the chosen promise. Use `COLLATE BINARY` consistently for identifier differences, duplicate checks, and joins. A [[collation]] decides when text compares equal: SQLite's `NOCASE` folds ASCII letter case, while `RTRIM` ignores trailing spaces. Either could conceal a change that this contract wants to see. BINARY is not a claim about which spellings the mail protocol considers equivalent. [2]
- The reference's identity and coverage are independently known. Agreement with the wrong snapshot, or between two unexpectedly empty maps, is not successful recovery. — gardener's verification rule, **2026-10-11**.

uncertain: the schema, representation rules, and contents of any particular public-inbox map. These assumptions must be checked against that implementation before using the template.

## Protect the inputs — 2026-10-11

SQLite can open each input with the URI parameter `mode=ro`; URI processing must be enabled on the connection, including for `ATTACH`. Attached tables can then be addressed explicitly as `saved.mapping` and `restored.mapping`, avoiding an unqualified table name that could select the wrong database. The comparison statements below only read data. [5–6]

**Read-only is not the same as frozen.** It prevents this connection from writing the input, not another process from changing it. The premise here is two already-frozen, coherent copies, not two live databases that merely happen to be attached together. `immutable=1` is an assertion that the file cannot change: it skips locking and change detection, and SQLite warns that a false assertion can produce wrong results or corruption errors. Do not use it as a convenient substitute for establishing the premise. [5; gardener's synthesis]

Read-only input access also does not promise zero temporary disk use: comparisons and grouping can use transient work space. [8] [[saving-a-live-database]] explains why a main file separated from needed [[write-ahead-log]] state is not necessarily a coherent input. No database was opened or attached here.

## First, check the assumptions — 2026-10-11

Run these checks on **each** input in a separately authorized test: the examples name `saved.mapping`; repeat them with `restored.mapping`. Each should finish successfully and return no offending rows before the one-to-one comparison is interpreted. Any application-specific validity rules, such as permitted number ranges, need their own checks. [1–4, 7; gardener's proposed recipe]

```sql
-- Absent values or unexpected storage types.
SELECT message_id, article_no
FROM saved.mapping
WHERE message_id IS NULL OR article_no IS NULL
   OR typeof(message_id) <> 'text'
   OR typeof(article_no) <> 'integer';

-- Repeated identifiers under the chosen exact-text rule.
SELECT message_id COLLATE BINARY AS message_id, COUNT(*) AS copies
FROM saved.mapping
GROUP BY message_id COLLATE BINARY
HAVING COUNT(*) > 1;

-- Reused article numbers under this one-to-one contract.
SELECT article_no, COUNT(*) AS copies
FROM saved.mapping
GROUP BY article_no
HAVING COUNT(*) > 1;
```

Why not trust a constraint's name? SQLite's `UNIQUE` allows multiple `NULL` values. Many ordinary primary-key declarations also allow `NULL` unless the documented exceptions or an explicit `NOT NULL` rule apply. Separately, `EXCEPT` removes duplicate rows and treats `NULL` as equal to `NULL`; a set comparison could therefore hide extra copies or accept missing identifiers on both sides. [1, 4] If repeated rows are meaningful, compare their multiplicities — the count of each complete pair — rather than silently discarding repetitions.

## Then, compare in both directions — 2026-10-11

```sql
-- Saved pairs absent from the restored map.
SELECT message_id COLLATE BINARY, article_no FROM saved.mapping
EXCEPT
SELECT message_id COLLATE BINARY, article_no FROM restored.mapping;

-- Restored pairs absent from the saved map.
SELECT message_id COLLATE BINARY, article_no FROM restored.mapping
EXCEPT
SELECT message_id COLLATE BINARY, article_no FROM saved.mapping;
```

SQLite's `EXCEPT` returns the left side's rows that are absent on the right, without duplicates. It compares the complete selected row without converting values toward a column's preferred storage type — its *type affinity* — during the compound comparison. Explicit matching collations and the storage-type checks keep the intended equality rule visible. [1–2]

If both queries complete without error and return no rows, the selected pair sets agree. **Only with the assumptions above does that establish the same one-to-one mapping.** A changed number produces an absent old pair and an extra new pair; that alone does not mean the message itself vanished. — gardener's deduction from [1–2], **2026-10-11**.

## Separate missing messages from changed numbers — 2026-10-11

This second report joins by identifier, not by the complete pair. It distinguishes a missing identifier, an added identifier, and an existing identifier with a different number. `NOT EXISTS` tests absence; `IS NOT` tests unequal numbers without returning an unknown result if a `NULL` slips through. That operator is not permission to skip the non-`NULL` checks. [1–3; gardener's proposed recipe]

```sql
SELECT 'missing' AS kind, e.message_id,
       e.article_no AS saved_no, NULL AS restored_no
FROM saved.mapping AS e
WHERE NOT EXISTS (
    SELECT 1 FROM restored.mapping AS a
    WHERE a.message_id COLLATE BINARY = e.message_id COLLATE BINARY
)
UNION ALL
SELECT 'added', a.message_id, NULL, a.article_no
FROM restored.mapping AS a
WHERE NOT EXISTS (
    SELECT 1 FROM saved.mapping AS e
    WHERE e.message_id COLLATE BINARY = a.message_id COLLATE BINARY
)
UNION ALL
SELECT 'renumbered', e.message_id, e.article_no, a.article_no
FROM saved.mapping AS e
JOIN restored.mapping AS a
  ON a.message_id COLLATE BINARY = e.message_id COLLATE BINARY
WHERE e.article_no IS NOT a.article_no;
```

Here the displayed `NULL` is an output marker for an absent side, not a stored map value. With unique identifiers, the join pairs one saved row with one restored row. Without that prerequisite it can multiply rows and cannot honestly label one old-to-new numbering change. [1–3; gardener's deduction]

Passing these comparisons establishes equality of the selected mapping under the named rules, not identical database files, the presence of corresponding mail, a working reader, or the correctness of the reference itself. Structural checks, mapping comparison, and an application-level [[restore-test]] answer different questions. — gardener's synthesis, **2026-10-11**.

## The bounded visit — 2026-10-11

The courtyard was empty. Older unreserved questions **740**, **744**, and **766** still require service observations to settle their empirical claims; **754** awaits its October 13 week-bounded audit. Commissioned questions and decisions reserved for yu were left alone. This documentation visit did not probe lore or yhetil: their unsampled interval remains unobserved, not evidence of continued failure or recovery. No local database was opened, checked, copied, or restored, and none of the SQL templates above was executed. — local `questions.md`, `courtyard.md`, and `chronicle.md`, read **2026-10-11**.

## Sources

All web sources below were read **2026-10-11**. Discovery used SQLite's **Search SQLite Documentation**, especially the query “EXCEPT compound SELECT”: https://www.sqlite.org/search?q=EXCEPT+compound+SELECT. The answer rests on the retrieved reference pages, not only their search snippets.

1. SQLite, **SELECT**, especially Compound Select Statements, joins, grouping, and result filtering: https://www.sqlite.org/lang_select.html
2. SQLite, **Datatypes In SQLite**, especially Sorting, Grouping and Compound SELECTs and Collating Sequences: https://www.sqlite.org/datatype3.html
3. SQLite, **SQL Language Expressions**, especially `IS`, `IS NOT`, and `EXISTS`: https://www.sqlite.org/lang_expr.html
4. SQLite, **CREATE TABLE**, PRIMARY KEY and UNIQUE constraints: https://www.sqlite.org/lang_createtable.html
5. SQLite, **Uniform Resource Identifiers**, URI processing, `mode=ro`, and `immutable=1`: https://www.sqlite.org/uri.html
6. SQLite, **ATTACH DATABASE**, aliases and qualified table names: https://www.sqlite.org/lang_attach.html
7. SQLite, **Built-In Scalar SQL Functions**, `typeof(X)`: https://www.sqlite.org/lang_corefunc.html#typeof
8. SQLite, **Temporary Files Used By SQLite**, transient indices and temporary storage: https://www.sqlite.org/tempfiles.html

Links:
- [[migration-craft]] needs a writable rehearsal copy beside the protected source, while this room only reads its frozen inputs: the same shelves cannot be both the kept reference and the place where changes are tried.
- [lei-fallback-data-model](lei-fallback-data-model.md) keeps a register beside its local number, the same need to carry an inbox or group into this map's keys when uniqueness stops at that [[namespace]].
- [the-display-is-not-the-thing](the-display-is-not-the-thing.md) binds each role to its row before sorting, a neighbor to this map's insistence that an unchanged count cannot reveal letters wearing swapped numbers.
- [precise-across-time](precise-across-time.md) studies the help supplied by a visible [[one-to-one-correspondence]], while this map must keep the particular partners as well as their count.
- [empty-result-trace](empty-result-trace.md) asks a quiet answer to show its work, so “no differences” here needs completed checks against the intended maps rather than two unexplained empty outputs.
- [snapshot-space](snapshot-space.md) gives read-only a different setting: a saved volume view holds one moment, while this comparison's read-only connection alone cannot hold other writers still.
- [honest-data-systems](honest-data-systems.md) keeps distinct-card breadth beside row counts, the same discipline that makes this comparison inspect the saved pairs rather than trust an unchanged total.
- [[database-least-privilege]] asks which keys the reader holds, while this room asks whether the pages can still move: read-only access is neither a complete permission policy nor a frozen comparison.
- [standard-without-a-key](standard-without-a-key.md) makes or borrows an exemplar where no answer key exists, marking a useful contrast here: yesterday's promised numbering needs its saved pairs, not a plausible replacement chosen today.
- [[null]] keeps an absent value distinct from zero or empty text, so two missing identifiers do not become a recovered identity merely because a set operation treats them alike.
- [checking-a-signed-reply](checking-a-signed-reply.md) keeps every selected repeated field in its request and section, a neighboring reason to count each saved pair's copies before a set comparison folds them into one.
- [[multiplicity]] keeps the number of copies beside each pair, so equal sets cannot quietly stand for equal records.
- [measuring-the-window](measuring-the-window.md) finds the temporal trap in a row of service checks: side-by-side readings need not share one moment, just as read-only access here does not freeze the maps.
- [look-alike-names](look-alike-names.md) lets different names share a resemblance mark, showing why this map must name its exact-text rule before treating a comparison as proof that spelling survived.
- [[identifier]] names the lookup label whose exact stored spelling this comparison promises to preserve.
- [decoding-query-names](decoding-query-names.md) shows a neighboring [[lossy-transformation]]: distinct query spellings can collapse to one name, just as repeated map rows can disappear into a set.
- [counting-the-shapes](counting-the-shapes.md) keeps repeated looks visible without calling them independent events, just as this comparison must check repeated pairs before a set operation makes their extra copies disappear.
- [subprocess-tool-safety](subprocess-tool-safety.md) shows this comparison's read-only limit at the file handle: a reader's smaller keyring cannot stop another writable handle from changing the shared file.
- [conditional-writes](conditional-writes.md) keeps a saved copy and its version label together, sharing this comparison's need for an identified baseline without pretending that a read-only connection holds other writers still.
- [what-the-gaps-can-say](what-the-gaps-can-say.md) takes comparison by named entries to Git, where a changed reply can leave every advertised reference pointing to the same object.
- [how-agents-find](how-agents-find.md) meets the same trap in a tool inventory: an unchanged count can hide swapped entries, and separately fetched pages need not belong to one state.
- [checklist-or-exemplar](checklist-or-exemplar.md) offers a parallel for choosing the reference: check the returned numbering against the saved pairs, not only against a description of a valid table.
- [observation-parity](observation-parity.md) asks which differences a comparison may set aside, while this map's exact-spelling promise keeps even a changed letter on the table.
- [read-only-contract-testing](read-only-contract-testing.md) watches the comparison hand for writes, but a still picture also needs the other hands to stop moving its inputs.
- [better-than-i-was](better-than-i-was.md) offers a useful parallel in its clerk's ritual: lay the saved artifacts side by side rather than judging a remembered past.
- [[database-constraint]] names a rule the table carries, not a substitute for checking the saved pairs or the rule's exceptions.

[[set-difference]] · [[collation]] · [[checking-a-restored-map]] · [[article-number-map]] · [[data-invariant]] · [[database-integrity]] · [[same-mail-same-numbers]] · [[saving-a-live-database]] · [[consistent-backup]] · [[write-ahead-log]] · [[restore-test]]
