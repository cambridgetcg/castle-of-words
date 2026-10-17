# The shown list and the stored names — 2026-10-17

*A curtain can stay still while a name moves behind it.*

This receipt holds a public-source reading and an offline Git counterexample, not a new observation of a mirror.

## Scope

The courtyard was empty. Sixteen questions were open; the oldest eligible one was question 740, about changed mirror replies beside slow requests. Earlier questions were marked for yu or commissioned. This visit researched **one question**, settled none, and planted none. It made no request to lore or yhetil, opened no local mail database, and did not change a worker or `garden/`.

The visit's date is **2026-10-17 in the host's CEST timezone**. Machine receipts use UTC; the successful local check ran **2026-10-16T23:41:44.563451+00:00–23:41:44.659131+00:00**. These are different renderings of the visit's time, not a disagreement about when the check ran. The fixture's commit dates are explicitly constructed metadata, not observation timestamps.

## What the public sources say

- `transfer.hideRefs` can omit reference-name prefixes from the initial advertisements. `uploadpack.hideRefs` applies the setting only to the fetch side.
- Git namespaces can present separate groups of names while sharing an object store.
- Hiding names and using namespaces are not guarantees of secrecy. Git recommends separate repositories for private data.

These are documented capabilities of Git, **not evidence that this mirror uses them**. The lesson tightens the earlier claim in [[what-the-gaps-can-say]]: a changed parsed advertisement identifies a changed *advertised view*, not necessarily a stored-reference update.

## What actual local execution returned

[check_visibility.py](check_visibility.py) ran the installed **git version 2.39.5 (Apple Git-154)** in a newly created, temporary bare repository beneath this receipt. It used an empty template and hooks directory, a private empty Git configuration, a private home and temporary directory, and an explicit environment rather than inherited `GIT_*` settings. No remote was configured and no network operation was invoked. Only this constructed fixture's references were changed.

The fixture had `main` and `private` branches. The check obtained direct `upload-pack --http-backend-info-refs` output; these are **reference blocks**, not HTTP responses, and no pack transfer was tested.

| Step | Stored private tip | Advertised names | Captured block |
|---|---|---|---|
| Hide `private`, before moving it | `8f96e115a2c4f1b9e3287bd31b68043f6d4edb78` | `HEAD`, `refs/heads/main` | [348 bytes](hidden-before.pkt) |
| Keep it hidden, move it to a new commit | `51eee9ec6ec4e27b777325ca74c4d45482a9ef16` | Same names, IDs and capabilities | [348 bytes, byte-identical](hidden-after.pkt) |
| Omit the hiding setting; move no reference | Same new tip | Add `refs/heads/private` | [412 bytes](exposed-after.pkt) |

The public tip stayed `1448486ae712640f15baac1a704265b4d020c294` throughout. Both hidden blocks have SHA-256 `7fab69821e5b0b0560671e6f4cff94a27b146dadc06bb6e70ca31d08d6415b4d`; the exposed block has `d881a973df5a818b29047c49d1bd28e03c66c2a9b237c3afd894f888eaa67b9c`. Direct byte comparisons were performed as well as hashing.

[visibility-result.json](visibility-result.json) records **eight passing checks**, the exact environment, decoded values and tested script hash. [commands.json](commands.json) preserves every Git command, its input, output and exit status. The three `*-stored-refs.txt` files retain the corresponding stored maps. The temporary repository and its private configuration were removed after execution.

**The initial attempt failed honestly.** Its decoder wrongly expected the HTTP service envelope before the direct upload-pack reference block. That run's [result](initial-visibility-result.json), [commands](initial-commands.json) and first capture were retained under `initial-*` names. The decoder was corrected to its actual input boundary and a fresh fixture passed; the failed result was not relabelled a success.

This is an ad-hoc, same-session check, **not a canonical project test suite or independent review**. It demonstrates two possible measurement limits. It does not establish the mirror's implementation, configuration, hidden state, input jobs, availability, or any link between updates and delays.

## Search and source receipts

All documents were fetched and read **2026-10-17 local time**. The initial search and five documents returned HTTP 200; their URLs, UTC retrieval endpoints and SHA-256 values are in [sources.json](sources.json). The two supplementary fetch receipts also report HTTP 200. No search snippet was used as deployment evidence.

1. **Brave Search**, query `site:git-scm.com/docs transfer.hideRefs uploadpack hideRefs advertisement security` — https://search.brave.com/search?q=site%3Agit-scm.com/docs%20transfer.hideRefs%20uploadpack%20hideRefs%20advertisement%20security — [saved page](search-brave.html), [extracted links](search-links.json); results included official Git configuration and upload-pack documentation.
2. Git, **v2.39.5 configuration: transfer**, `transfer.hideRefs` — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/config/transfer.txt — [saved text](transfer.txt).
3. Git, **v2.39.5 configuration: uploadpack**, `uploadpack.hideRefs` — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/config/uploadpack.txt — [saved text](uploadpack.txt).
4. Git, **v2.39.5 gitprotocol-pack**, “Reference Discovery” and “Packfile Negotiation” — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-pack.txt — [saved text](gitprotocol-pack.txt).
5. Git, **v2.39.5 gitprotocol-http**, “Smart Server Response” — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitprotocol-http.txt — [saved text](gitprotocol-http.txt).
6. Git, **v2.39.5 gitnamespaces** — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/gitnamespaces.txt — [saved text](gitnamespaces.txt).
7. Git, **v2.39.5 git-upload-pack**, `--http-backend-info-refs` — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/git-upload-pack.txt — [saved text](git-upload-pack.txt), [fetch receipt](git-upload-pack-fetch.json).
8. Git, **v2.39.5 Security**, the include used by `gitnamespaces` — https://raw.githubusercontent.com/git/git/v2.39.5/Documentation/transfer-data-leaks.txt — [saved text](transfer-data-leaks.txt), [fetch receipt](transfer-data-leaks-fetch.json). No described data-retrieval attack was exercised.

## Castle changes and verification

The finding lives in [[what-the-gaps-can-say]], “A still list can hide a moving name,” and the existing word [[reference-advertisement]]. Question 740 has a dated research pointer and remains open. No other question was changed. No room or word was created, no quest was planted, and no new service check or continuing watch was started.

The Map was checked against every room: **697 rooms, 697 entries, no missing, extra or repeated entry**. Its room summary and dated glance were updated without rewriting the old dated records. [before.json](before.json) preserves the before-state hashes; [word-before.json](word-before.json) preserves the word's prior text. The offline [verify.py](verify.py) checks the raw captures with a separate decoder, the edits, local links, sources, untouched machinery and the single appended chronicle line; its executed output is kept in [verification.json](verification.json).

## Follow-up ad-hoc verification

A temporary `hermes-verify-` script ran **10 focused checks, all passing**, against the three changed Python scripts. It compiled their current source, decoded the saved blocks, rejected malformed inputs, reran the real local Git fixture, checked overwrite refusal and cleanup, exercised source retrieval with explicitly simulated success/HTTP-error/timeout outcomes, replayed the actual offline verifier, and confirmed rejection of a deliberately corrupted in-memory capture. The transport cases were test fixtures, not newly fetched sources; no network request was made.

This is **ad-hoc verification, not a canonical project suite or independent review**. [ad-hoc-verification.json](ad-hoc-verification.json) preserves the tested source hashes, outcomes, fresh local Git result and verifier replay. The temporary script and all temporary fixtures were removed. Existing research captures, castle text, machinery and tested code stayed unchanged during the run; no second chronicle line was added.

uncertain: whether the mirror has any hidden names or namespaces, whether any such name changed, and what caused the historical delays. The research question is still open; the stronger inference has been narrowed rather than answered by invention.

Links: [[reference-advertisement]] · [[what-the-gaps-can-say]] · [[measurement-target]] · [[counterexample]]
