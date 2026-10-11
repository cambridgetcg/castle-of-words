# database-constraint

A database constraint is a rule saying which entries a stored table is allowed to hold.

A rule can require a value (`NOT NULL`), forbid repeated values (`UNIQUE`), or require a value to match a row in another table (a foreign key). The exact wording matters: SQLite's `UNIQUE` can accept several `NULL` values, and a foreign-key rule can accept an absent child value unless a separate rule requires it. A reassuring rule name is not the whole rule.

A [[data-invariant]] names what the application needs to stay true; a constraint writes a particular rule into the database's design. Declaring it, enforcing it during writes, and checking existing data are separate acts. Even correctly enforced constraints do not by themselves show that restored messages kept their old numbers: a different mapping may obey the same rules.

Sources: [[checking-a-restored-map]], especially “Three checks, three boundaries,” and [[comparing-saved-maps]], especially “First, check the assumptions,” read locally **2026-10-11**. Their cited primary references are SQLite's **CREATE TABLE**, https://www.sqlite.org/lang_createtable.html, and **SQLite Foreign Key Support**, https://www.sqlite.org/foreignkeys.html. This brick distills those sourced notes; the web references were not fetched again and no database was opened or tested during this tending.

Links:
- [[data-invariant]] is the promise the application needs, which may require more than the rules written into its tables.
- [[database-integrity]] asks whether the stored pieces obey the particular rules and structural checks being examined.
- [[checking-a-restored-map]] keeps an internally sound table separate from a faithful return of yesterday's work.
- [[comparing-saved-maps]] checks the actual saved pairings and the assumptions a constraint's name cannot settle alone.
