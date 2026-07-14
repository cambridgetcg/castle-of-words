# log

*A log is a witness that never forgets what it saw.*

A log is a record of events in the order they happened. In computing, an append-only log is a data structure where new entries are added at the end and existing entries are never modified or deleted. Log-structured file systems write all data and metadata sequentially to a circular buffer called a log, preserving every change. A blockchain adds cryptographic verification so every transaction in the log is verifiable.

The castle holds the log as the honest form of memory: the bytes that were written are the bytes that were written. A [[migration-craft]] journal is a log — applied migrations are immutable byte history, and the honest record never silences a witness. A [[retention-ledger]] is a log of what may be kept and for how long. The [[append-only]] pattern is the log's law: never erase, only add.

A log is not the same as a story. A log says what happened; a story says what it means. The honest system keeps them separate: the log is the ground, the story is the building, and [[trust]] requires that the ground not shift under the building.

Links: [[append-only]] · [[immutable]] · [[trust]] · [[migration-craft]] · [[witness]]
