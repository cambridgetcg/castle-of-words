# tombstone-in-manifest

*You cannot delete from an append-only log — but you can say "this was here, and now it is gone."*

What gathers here: whether you can delete a file from an append-only manifest without rewriting history, and what a tombstone entry looks like.

## The problem

An append-only manifest is a list of files, each with a hash, that grows over time. When a file is published, it gets an entry. When a new file is published, it gets another entry. The manifest is a historical record: it says what was published and when.

But what happens when a file must be removed? The file was published, mirrors copied it, and now it must be taken down — because it contained personal data, because the licence was revoked, because it was published in error. The manifest must record this removal, but it cannot delete the original entry without rewriting history — and rewriting history breaks the append-only property that makes the manifest trustworthy.

## The tombstone entry

The solution is a **tombstone entry**: a new entry in the manifest that says "the file at this path, which was published at this time, is now deleted." The original entry stays. The tombstone is appended after it.

A tombstone entry in a manifest:

```json
{
  "path": "data/2024/charity-register.csv",
  "status": "deleted",
  "deleted_at": "2026-07-11T12:00:00Z",
  "reason": "personal-data",
  "previous_hash": "sha256:abc123def456...",
  "previous_published_at": "2024-03-15T09:00:00Z"
}
```

The tombstone carries:

- **path**: The same path as the original entry, so a consumer can find both.
- **status**: `"deleted"` — the key field that distinguishes a tombstone from a live entry.
- **deleted_at**: When the deletion happened.
- **reason**: Why the file was deleted (`"personal-data"`, `"licence-revoked"`, `"published-in-error"`, `"superseded"`).
- **previous_hash**: The hash of the file when it was published, so a consumer can verify they have the right file to delete.
- **previous_published_at**: When the original file was published, so a consumer can find the original entry.

## How a consumer reads it

A consumer reading the manifest from start to finish:

1. Sees the original entry: `{"path": "data/2024/charity-register.csv", "status": "published", "hash": "sha256:abc123...", "published_at": "2024-03-15T09:00:00Z"}` — the file was published.
2. Sees the tombstone: `{"path": "data/2024/charity-register.csv", "status": "deleted", ...}` — the file is now deleted.
3. Knows: the file was published on 2024-03-15, and it was deleted on 2026-07-11 because it contained personal data. Any mirror that has the file should stop serving it. Any mirror that does not have the file should not try to obtain it.

A consumer that only reads the last entry for each path sees the tombstone and knows the file is deleted. A consumer that reads the full history sees the complete story.

## The honest limits

The tombstone pattern is honest about what it can and cannot do:

1. **It cannot un-publish**: The file was published. Mirrors copied it. The tombstone tells mirrors to stop serving it, but it cannot force them to. A file that was once public may remain public on mirrors that do not respect the manifest.
2. **It preserves history**: The original entry stays. Anyone can see that the file was once published. This is honest — the deletion is a new fact, not an erasure of the old fact.
3. **It requires consumer cooperation**: The tombstone only works if consumers read the manifest and respect the deletion. A consumer that caches the original entry and never checks for updates will continue serving the deleted file.
4. **It does not solve the "right to be forgotten"**: A tombstone records that a file was deleted, but the file itself may still exist on mirrors. The manifest can say "this should not be served," but it cannot reach into every mirror and delete the bytes.

The tombstone is the manifest's face of the same principle the [[immutable-correction]] word holds: corrections are appended, never overwritten. The history of what was published remains visible; the deletion is a new fact, not an erasure of the old one.

Source: Wikipedia, "Append-only" — the property that new data can be appended but existing data is immutable. The tombstone pattern is used in distributed systems (Cassandra, Kafka) and version control (Git's "deleted" entries in tree objects). Read 2026-07-11.

Links: [[immutable-correction]] · [[publication-boundary]] · [[verification-hash]] · [null-hash-semantics](null-hash-semantics.md) · [open-data-checksums](open-data-checksums.md) (the tombstone is the manifest's answer to the null-hash ambiguity: a null hash with no reason is silence, a tombstone is silence with an explanation) · [civic-data-honesty](civic-data-honesty.md) (the publication boundary that cannot be recalled is the same law: once published, the bytes are out; the tombstone is the honest record of the attempt to call them back)
