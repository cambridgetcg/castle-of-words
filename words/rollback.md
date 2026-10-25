# rollback

A rollback takes back a change it controls, not everything that happened around it.

In a [[database-transaction]], rollback cancels uncommitted changes. The SQLite Backup API example in [[saving-a-live-database]] makes the boundary concrete: finishing an incomplete backup rolls back its destination write transaction, and successful cleanup alone does not establish that a complete copy exists. This does not undo already committed source work.

In a deployment, rollback can mean returning to an earlier application version. That is a different promise. [[privacy-sensitive-release]] puts read gates before the release's data changes; [[civic-data-honesty]] records why reversing code cannot recall information already copied by people or mirrors. Returning the machine to an older version does not return the outside world to an earlier moment.

Name what is being rolled back, which changes it includes, and what remains outside its reach. A cancelled unfinished transaction, an older executable, and the withdrawal of published data are not interchangeable results.

Sources: the local [[saving-a-live-database]] room's “Finished is a result” section and [[database-transaction]] brick, read **2026-10-25**; the room retains its **2026-10-10** reading of SQLite's [Online Backup API](https://www.sqlite.org/c3ref/backup_finish.html). The release boundary comes from yu's **2026-07-11** account in [[privacy-sensitive-release]] and **2026-07-10** account in [[civic-data-honesty]], read locally **2026-10-25**. This brick gathers those existing accounts; no rollback, database test, deployment or fresh web retrieval was performed.

Links:
- [[saving-a-live-database]] gives rollback a specific unfinished transaction to cancel, rather than treating cleanup as a completed backup.
- [[privacy-sensitive-release]] keeps the protective gate ahead of the change, where a later reversal cannot erase an earlier disclosure.
- [[civic-data-honesty]] separates returning to older code from recalling copies that have already left the door.
- [[database-transaction]] names the unit whose uncommitted changes can be cancelled together.
