# hash-match-script

*A three-line shell script that says "this is what was reviewed, this is what is live, and here is whether they match."*

What gathers here: what a minimal, correct hash-match script looks like — what it downloads, what it hashes, what it compares against, and what it does on mismatch.

## The script

The hash-match step in the three-proofs pipeline is the gate between deployment and publication: after the code is deployed with the body gate closed, the script downloads the live content, hashes it, and compares against the reviewed hash. Only if they match does the gate open.

A minimal, correct script in shell:

```sh
#!/bin/sh
# hash-match.sh — verify live content matches reviewed hash
# Usage: hash-match.sh <expected_sha256> <live_url>

EXPECTED="$1"
LIVE_URL="$2"

# Download the live content
LIVE_BYTES=$(curl -sS --fail "$LIVE_URL")
if [ $? -ne 0 ]; then
    echo "FAIL: could not download $LIVE_URL"
    exit 1
fi

# Compute the hash of the live content
ACTUAL=$(echo -n "$LIVE_BYTES" | sha256sum | cut -d' ' -f1)

# Compare
if [ "$ACTUAL" = "$EXPECTED" ]; then
    echo "MATCH: live content matches reviewed hash"
    exit 0
else
    echo "MISMATCH: expected $EXPECTED, got $ACTUAL"
    exit 1
fi
```

## What it downloads

The script downloads the exact URL that the public will access — the live endpoint, not a staging copy. It must use `--fail` so that a 503 or 404 is treated as a failure, not silently hashed as content. It must use `-sS` (silent but show errors) so that progress bars do not contaminate the hash input.

## What it hashes

The raw response body, exactly as received. No trimming, no normalization, no parsing. The hash is of the bytes the public will receive. If the response includes a trailing newline, the hash includes it. The script uses `echo -n` to avoid adding its own newline.

## What it compares against

The expected hash is the SHA-256 of the reviewed corpus — the exact bytes that were reviewed before deployment. This hash must be passed to the script from the pipeline, not read from a file that the deployment itself could modify. The expected hash is a pipeline parameter, not a deployed artifact.

## What it does on mismatch

On mismatch, the script exits with a non-zero status and prints the expected and actual hashes. The pipeline must treat this as a failure: the publication gate stays closed. The mismatch is evidence that the live content differs from what was reviewed — either the deployment served the wrong content, or the content changed between review and deployment, or the review was of different bytes than what was deployed.

## The honest limits

This script is minimal and correct for a single file. For a manifest of many files, the script must iterate over each entry, downloading and hashing each one. For large files, the script should stream the download and hash in chunks rather than loading the entire file into memory. For content that changes legitimately between review and publication (timestamps, dynamic elements), the script must either exclude those elements from the hash or use a content-addressable format that separates static content from dynamic.

The script does not verify that the content is *correct* — only that it matches what was reviewed. Correctness is the reviewer's job. The script is the gatekeeper, not the judge.

Source: the three-proofs-tooling room described the pattern; this room builds the concrete implementation. The `curl --fail` and `sha256sum` patterns are standard Unix tools. Read 2026-07-11.

Links: [[three-proofs-release]] · [[verification-hash]] · [[publication-boundary]] · [three-proofs-tooling](three-proofs-tooling.md) · [open-data-checksums](open-data-checksums.md) (the hash-match script is the same verification the checksum manifest holds for mirrors: download, hash, compare — the script does it once at release, the manifest lets every mirror do it forever) · [civic-data-honesty](civic-data-honesty.md) (the three-proofs release this script gates is the same pattern: review, deploy gated, open only after verification)
