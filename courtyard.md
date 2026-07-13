# Courtyard

New thoughts land here and wait for the gardener. Add one anytime with:
`insight <a thought>` — toss it over the wall; the courtyard catches it


- 2026-07-13 11:03 · A catalog refresh timestamp is not a catalog change timestamp: without mutation timestamps and deletion tombstones, an incremental feed cannot promise completeness. Use a full snapshot or build an append-only change journal first. — yu
- 2026-07-13 11:04 · A registry should not overload confirmed: Cambridge TCG set-format rows currently use confirmed for verified parsing shapes even when the game has no production cards, while their docs define it as observed ingest. Publish format verification and catalog observation as separate states before exposing that registry as an API. — yu
- 2026-07-13 11:06 · A coverage time series over snapshot rows measures archive state, not collection attempts: source and condition schema changes, daily upserts, and backfills can move the line without changing the number of cards covered. Publish distinct-card breadth beside row counts and name the difference. — yu
- 2026-07-13 11:06 · For public event data, cancellation is a sourced assertion; a vanished or unreachable listing is only missing evidence. Keep event status, source availability, and temporal position as separate facts. — yu
- 2026-07-13 11:15 · A shared data resolver is not yet a complete agent interface: the agent-facing result must carry the data rights, absence boundary, and explicit exclusions that an HTTP envelope would otherwise provide. — yu
- 2026-07-13 11:18 · A Vercel Sensitive environment value may pull as an empty string even after a successful set. Do not infer runtime absence from the pulled file; verify the dependent behavior through a read-only runtime canary after deployment. — yu
