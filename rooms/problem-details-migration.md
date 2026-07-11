# problem-details-migration

*A safe migration adds the new shape without breaking the old; the old spelling stays as an explicit alias until a versioned contract can retire it.*

What gathers here: the craft of migrating error responses to RFC 9457 Problem Details without breaking existing clients. The law: additive, not destructive.

Built understanding from yu, 2026-07-11:

- 2026-07-11 10:11 · A safe Problem Details migration is additive: keep the published domain error code and recovery fields, add RFC 9457 type/title/status/detail/instance, make nextActions canonical, and retain any old spelling as an explicit compatibility alias until a versioned contract can retire it. — yu

The steps, plainly:

1. **Keep what exists.** The domain error code, the recovery hints, the custom fields — they stay. Existing clients parse them; breaking them is not migration, it is rupture.
2. **Add the standard shape.** RFC 9457's `type`, `title`, `status`, `detail`, and `instance` go alongside, not instead of. The old and new shapes coexist.
3. **Make the canonical field canonical.** If `nextActions` is the right name, make it the one name — but keep the old spelling (`next_actions`, `recovery`) as an explicit compatibility alias, documented and tested.
4. **Retire with a version.** The old spelling is removed only when a versioned API contract says so, and the version number is the client's signal that the alias is gone.

The law: a migration that breaks existing clients is not a migration — it is a new API wearing the old URL. The honest path is additive, explicit, and versioned.

Links: [[problem-details]] · [honest-endpoints](honest-endpoints.md) (the same law at the API layer: a route that changes its contract must say so, and the old contract must survive until the new one is declared) · [civic-data-honesty](civic-data-honesty.md) (the same law at the data layer: a field that changes its meaning must keep the old meaning as an explicit alias)
