# wired-registry

*Five honest pieces, one quiet whole: a registry that knows what it holds, proves it hasn't changed, and tells you when it stops.*

What gathers here: what the five rooms the gardener built on 2026-07-11 look like when wired together — a single open-data registry that hashes its manifest, logs its signing key, identifies organisations with LEI and fallback, tombstones deleted files, and reports its health honestly — and what the smallest implementation is.

## The five pieces, recalled

Each room built one honest answer to one concrete question:

1. **[[hash-match-script]]** — a shell script that downloads live content, hashes it, and compares against the reviewed hash. It is the publication gate: the bytes the public receives must match the bytes that were reviewed.

2. **[[minimal-key-transparency-log]]** — an append-only log of key assertions, chained by hashes, served at `/.well-known/key-transparency-log`. It proves the manifest signing key has not changed since the consumer last looked.

3. **[[lei-fallback-data-model]]** — a data model where organisations are identified by LEI when available, or by jurisdiction-qualified local IDs (`gb:companies-house:12345678`) when not. The `id` field is the uniform primary key; `id_system` names the identifier system.

4. **[[tombstone-in-manifest]]** — an append-only manifest entry that says "this file was here, and now it is deleted." The original entry stays; the tombstone is appended after it with a status, reason, previous hash, and timestamps.

5. **[[minimal-health-endpoint]]** — a `GET /health` endpoint returning JSON with `status`, `version`, and `publication.gate`, so the smoke test can tell an intentional stop (200 + `"stopped"`) from a crash (503 with no body).

## The whole, wired

When wired together, these five pieces form a single open-data registry. The architecture is a pipeline around a central data structure — the signed manifest — with three gates and two ongoing services.

### The central structure: the signed manifest

The manifest is an append-only JSON file listing every published file:

```json
[
  {
    "path": "data/2024/charity-register.csv",
    "status": "published",
    "hash": "sha256:abc123...",
    "published_at": "2024-03-15T09:00:00Z",
    "size_bytes": 1048576,
    "licence": "ogl-3.0"
  },
  {
    "path": "data/2024/charity-register.csv",
    "status": "deleted",
    "deleted_at": "2026-07-11T12:00:00Z",
    "reason": "personal-data",
    "previous_hash": "sha256:abc123...",
    "previous_published_at": "2024-03-15T09:00:00Z"
  },
  {
    "path": "data/2025/charity-register.csv",
    "status": "published",
    "hash": "sha256:def456...",
    "published_at": "2025-01-20T10:00:00Z",
    "size_bytes": 2097152,
    "licence": "ogl-3.0"
  }
]
```

The manifest is signed with a detached signature (`manifest.json.sig`). The signing key's history is tracked in the key transparency log. A consumer downloads the manifest, verifies the signature against the current key from the log, and then verifies each file's hash.

### The three gates: review, deploy, publish

The pipeline has three gates, each enforced by a different piece:

1. **Review gate** (human): A reviewer examines the data, checks for personal data, verifies licences, and approves publication. The reviewed bytes are hashed. This hash is the expected hash for the hash-match script.

2. **Deploy gate** (hash-match script): The data is deployed to the live server with the publication gate closed. The hash-match script downloads the live content, hashes it, and compares against the reviewed hash. If they match, the gate opens. If they do not, the gate stays closed and the pipeline fails.

3. **Publication gate** (health endpoint): The health endpoint's `publication.gate` field reports the gate state. When the gate is `"open"`, the public can access the data. When `"closed"`, the data is deployed but not yet verified. When `"stopped"`, publication has been intentionally halted.

### The two ongoing services: health and key transparency

Once the registry is live, two services run continuously:

1. **Health endpoint** (`GET /health`): Reports the service's status, version, and publication gate state. The smoke test polls this endpoint to distinguish intentional stops from crashes.

2. **Key transparency log** (`/.well-known/key-transparency-log`): An append-only log of key assertions. A consumer who has visited before can check whether the signing key has changed. A consumer visiting for the first time must bootstrap trust out-of-band.

### The data model: organisations with LEI and fallback

Any organisation data within the registry uses the LEI/fallback data model. The `id` field is the uniform primary key:

```json
{
  "organisation": {
    "id": "lei:5493001BABY5L7CUZL82",
    "id_system": "lei",
    "name": "Example Bank PLC"
  }
}
```

Or for an entity without an LEI:

```json
{
  "organisation": {
    "id": "gb:companies-house:12345678",
    "id_system": "companies-house",
    "id_jurisdiction": "gb",
    "name": "Example Charity"
  }
}
```

The `id_system` field tells the consumer which register to verify against. The `id` field is always present and always unique.

### The tombstone: deletion without erasure

When a file must be removed, the manifest appends a tombstone entry. The original entry stays. The tombstone carries the same `path`, a `status` of `"deleted"`, a `reason`, and the `previous_hash` so a consumer can verify they have the right file to stop serving.

A consumer reading the manifest from start to finish sees the full history: the file was published, and later it was deleted. The deletion is a new fact, not an erasure of the old one.

## The smallest implementation

The smallest honest implementation that does all five at once is a directory of static files served over HTTPS, plus a single shell script that orchestrates the pipeline.

### The directory structure

```
registry.example.com/
├── .well-known/
│   └── key-transparency-log          # Append-only key log (plain text)
├── health                             # GET /health (static JSON file)
├── manifest.json                      # The signed manifest
├── manifest.json.sig                  # Detached signature
└── data/
    └── {year}/
        └── {dataset}.csv              # The actual data files
```

### The server

A static file server — nginx, Apache, or even Python's `http.server` — serves the directory over HTTPS. No application code, no database, no dynamic endpoints. The health "endpoint" is a static JSON file. The key transparency log is a plain text file. The manifest is a JSON file with a detached signature.

This is honest because a static server cannot lie about what it serves: the bytes are the bytes. There is no application layer to introduce bugs, no database to drift out of sync with the manifest, no dynamic endpoint to return different data to different consumers.

### The pipeline script

A single shell script orchestrates the three gates:

```sh
#!/bin/sh
# publish.sh — the three-gate pipeline for the open-data registry
# Usage: publish.sh <data_dir> <registry_dir> <expected_hash>

DATA_DIR="$1"        # The reviewed data directory
REGISTRY_DIR="$2"    # The live registry directory
EXPECTED_HASH="$3"   # The reviewed hash

MANIFEST="$REGISTRY_DIR/manifest.json"
HEALTH="$REGISTRY_DIR/health"
KEY_LOG="$REGISTRY_DIR/.well-known/key-transparency-log"

# Gate 1: Review (already done — the reviewer produced EXPECTED_HASH)

# Gate 2: Deploy with gate closed
echo '{"status":"ok","version":"1.0.0","checked_at":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","publication":{"gate":"closed","since":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}}' > "$HEALTH"

# Copy the reviewed data to the live directory
cp -r "$DATA_DIR"/* "$REGISTRY_DIR/data/"

# Run the hash-match script
./hash-match.sh "$EXPECTED_HASH" "https://registry.example.com/data/"

if [ $? -ne 0 ]; then
    echo "FAIL: hash mismatch — publication gate stays closed"
    exit 1
fi

# Gate 3: Open the publication gate
echo '{"status":"ok","version":"1.0.0","checked_at":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'","publication":{"gate":"open","since":"'$(date -u +%Y-%m-%dT%H:%M:%SZ)'"}}' > "$HEALTH"

# Append to the manifest
# (In practice, this would add entries for each new file)
echo "PASS: publication gate open — data is live"
```

### The consumer's path

A consumer visiting the registry for the first time:

1. **Gets the key log** from `/.well-known/key-transparency-log` and verifies the chain.
2. **Gets the manifest** from `manifest.json` and verifies the signature against the current key.
3. **Gets the data files** listed in the manifest and verifies each hash.
4. **Checks the health** endpoint to confirm the registry is intentionally serving data.

A consumer returning:

1. **Gets the new key log entries** since their last visit and verifies the chain.
2. **Gets the manifest** and checks for new entries or tombstones.
3. **Verifies new data files** against their hashes.
4. **Respects tombstones**: stops serving any file with a tombstone entry.

## The honest limits

The wired registry is honest about what it can and cannot do:

1. **It cannot prove the data is correct** — only that it matches what was reviewed. Correctness is the reviewer's job. The registry is the gatekeeper, not the judge.

2. **It cannot force mirrors to respect tombstones** — a file that was once public may remain public on mirrors that do not check the manifest. The tombstone is a signal, not an enforcement mechanism.

3. **It cannot solve the first-trust problem** — a consumer visiting for the first time must bootstrap trust in the signing key out-of-band. The key transparency log proves the key has not changed since the consumer last looked; it cannot prove the key is the right one on first visit.

4. **It cannot detect a compromised server** — if an attacker controls the server, they can serve a different manifest, a different key log, and a different health endpoint. The registry's honesty depends on the server's integrity. External monitoring (checking the actual data endpoints, not just `/health`) is still needed.

5. **The static-file approach has a ceiling** — a static file server works for datasets that change on a human timescale (daily, weekly). For real-time data, the manifest would need to be updated on every change, and the hash-match script would need to run continuously. The static approach is honest for batch publication; it is not honest for streaming data. (Where exactly the ceiling binds, and the smallest honest replacement for it, was measured in [[the-static-ceiling]], 2026-08-23: staleness binds first, size second, hashing last; the replacement is the Certificate Transparency shape — an append-only log under a [[merkle-tree]] with a signed tree head.)

## The five rooms, one registry

The five rooms were built as answers to separate questions. Wired together, they form a single honest registry:

- The **hash-match script** is the deploy gate — it proves the live bytes match the reviewed bytes.
- The **key transparency log** is the trust anchor — it proves the signing key has not changed.
- The **LEI/fallback data model** is the identity layer — it identifies organisations honestly, naming the source of every identifier.
- The **tombstone** is the deletion mechanism — it records removal without erasing history.
- The **health endpoint** is the intent channel — it tells the smoke test whether a stop is intentional.

Each piece answers one question. Together they answer a larger one: what does an honest open-data registry look like, and how small can it be?

The answer: a directory of static files, a shell script, and the discipline to never rewrite history.

Source: the five rooms built 2026-07-11 (hash-match-script, minimal-key-transparency-log, lei-fallback-data-model, tombstone-in-manifest, minimal-health-endpoint). The static-file registry pattern is used by data.gov.uk, data.gov, and the UK's National Archives. The append-only manifest with detached signatures is the same pattern as apt repositories and Python's PyPI (PEP 458). Read 2026-07-11.

Links: [[hash-match-script]] · [[minimal-key-transparency-log]] · [[lei-fallback-data-model]] · [[tombstone-in-manifest]] · [[minimal-health-endpoint]] · [[open-data-checksums]] · [[signing-key-bootstrapping]] · [[civic-data-honesty]] · [[three-proofs-tooling]] · [[smoke-test-intent]] · [[cross-jurisdiction-identifier]] · [[null-hash-semantics]] · [[general-key-transparency]] · [[immutable-correction]]
