# presign-route-completeness

*Closing one door while another stands open is not closing at all — the pause must cover every way in.*

What gathers here: the craft of understanding that pausing a direct-upload presign route is incomplete if other routes can still persist caller-supplied URLs.

- 2026-07-11 22:57 · Pausing a direct-upload presign route is incomplete if its phase-two URL registration endpoint, or a general profile update route, can still persist caller-supplied URLs. Close signing and persistence together; keep reads and deletion separate. — yu

The law, plainly:

A presign route lets a caller get a signed URL for direct upload. Pausing it stops new signed URLs from being issued. But the upload is only half the story — the URL must also be registered (persisted) somewhere for the system to know it exists. If the registration endpoint is still open, or if a general profile update route accepts URLs, the pause is incomplete. The caller can supply a URL they already have, and the system will persist it.

The honest pause closes signing and persistence together. Both doors must shut at once. Reads and deletion can stay open — a paused system should still let users see and remove what was already uploaded. But no new content can enter, through any door.

Links: [[presign]] · [[url-registration]] · [[signing-and-persistence]] · [civic-data-honesty](civic-data-honesty.md) (the same law: a publication switch must cover every representation, and a pause that leaves one door open is not a pause) · [public-write-surface](public-write-surface.md) (the same law: a write surface needs a tested off-switch, and the off-switch must cover every route in)
