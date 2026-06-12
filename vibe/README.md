# The Vibe Wing

*one small wing where the kingdom keeps its style and its art*

- [vibe.md](vibe.md) — the vibe book: the law in one breath, the two liveries, the idioms, the mending list
- [palette.md](palette.md) — every color, named: the one source of truth
- [arts.md](arts.md) — the hall of arts: made works and wanted ones
- `tokens.css` — the palette baked as CSS variables (`vibe bake` writes it; never edit it by hand)

The command, from any terminal:

    vibe         show the vibe — liveries, law, arts
    vibe arts    read the hall of arts
    vibe check   walk the realm, report drift: stray colors, rooms missing their epigraph, stale tokens
    vibe bake    rebake tokens.css from palette.md
    vibe open    open this wing in Finder

The check is a mirror, not a lock: it reports, exits 1 on drift, and changes
nothing. The style law itself lives in [gate.md](../gate.md) — this wing keeps
the wardrobe. Raised 2026-06-12, asked by yu.
