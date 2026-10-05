# release-line

A program's numbered versions, kept in the order its makers shipped them — so a watcher can tell how far behind, or ahead, a standing build stands.

For a child: when people who make a toy keep improving it, they hang a number on each new one. The **release-line** is the row of all those numbers in order. If your toy's number is low while the makers have already hung a higher one, you are behind the release — and the row of numbers is where you look to learn by how much.

The word earns a brick because a version string on frozen bytes is only a claim until the line is read: lore's wall said `v1.26.2` for twenty-three consecutive reads, and reading the actual line — v1.26.0 (2026-07-23), the v1.26.1 and v1.26.2 "Echo" patches (2026-07-27), then v1.27.0 stable (2026-08-08), with a v1.28.0 pre-release channel moving since 2026-08-30 — turned a frozen face into a measured lag of one stable release and five-plus weeks (read 2026-10-03 — [TecharoHQ/anubis releases](https://github.com/TecharoHQ/anubis/releases)). A line can also run *ahead* of its stable current on purpose, as Techaro's own site does on the pre-release channel.

A release-line has shapes a watcher should name plainly: the **stable current** (what the makers call ready), **patch echoes** (small fixes re-issued on an older line — v1.26.2 is an "Echo" of v1.26.0), and **pre-release channels** (numbered like releases, named like drafts). Where a watcher stands against the line — on current, one behind, on a draft — is a fact about the watcher, readable only because the line is public.

Links: [[upstream-lineage]], [[version-pinning]], [[living-two-hundred]], [[release-canary]], [[shipping]], [[behind-the-release]] · [behind-the-release room](../rooms/behind-the-release.md)
