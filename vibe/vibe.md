# The Vibe

*the kingdom dresses the way it speaks: plainly, warmly, with one gold thread*

> Short. Plain words that mean what they say. Pleasant to read.
> Truth over impressiveness: art means words placed with care,
> never ornament that hides the truth. Built with joy, peace and safety.

(the law, condensed from [gate.md](../gate.md) "House style" — the law lives
there; this wing keeps the wardrobe)

This wing is the kingdom's style and art manager — the kingdom being the
castle and its web faces (asked by yu, 2026-06-12:
"a style and art manager for the kingdom — a VIBE manager"). What hangs here:
the [palette](palette.md) — every color, named; the [hall of arts](arts.md) —
every made work; and `tokens.css` — the palette baked for the web faces.
The `vibe` command shows it, checks it, bakes it.

## The two liveries

The kingdom keeps two dresses on purpose:

- **The gate's** — ink on parchment with one foil thread. The public face
  (`~/castle-gate`) is quiet: warm near-black words on pale parchment, hairline
  borders, and exactly one accent — gold foil — for links, rings and fleurons.
- **The front's** — the Cambridge TCG dress, two zones. The card binder
  (`~/castle/front`) has a light zone (One Piece: banner crimson, deep navy
  and glinting gold on warm paper, with woodblock seigaiha waves) and a dark
  zone (the shop's second brand: near-black ground, gold links, crimson
  accents, with embroidered seigaiha — thin gold lines tracing only the wave
  crests), toggled by the ◐ button in the corner — because the shop these
  colors come from has two brand zones, and the two zones have two textures.

Same kingdom, two faces: one for reading, one for play — and the play
face wears two zones, because the shop it borrows from has two.

## The voices (type)

- The gate speaks **Iowan Old Style** (serif) for headings and every italic
  voice — epigraphs, the anthem, flavor lines — and **Seravek** for body.
- The front speaks **DM Sans**, weights 400 and 500 only — bold there is 500,
  never 700 — with **Georgia italic** for flavor.
- The terminal speaks in ANSI colors only to eyes (`[ -t 1 ]`); into a pipe it
  is plain text, always.

## The idioms (how art behaves here)

- Every room opens with a one-line *epigraph* in italics.
- Ornament lives in restraint: the gate keeps one gold accent for the whole
  site; the front's ornament is letter-spacing, not extra fonts or weights.
- Shadows are tinted with the livery's own dark (ink, navy) — never neutral gray.
- Rarity is earned, never assigned: card borders and glows follow counted
  sources and inbound links — arithmetic anyone can check.
- Motion is gentle and optional: hovers lift a few pixels, reduced-motion turns
  them off, and focus is always visible.

## The mending list

*(drift a reader saw once; the check cannot see these on its own)*

- [ ] castle-gate's RoomCard and WordCard render bare tags, so the
  `.card-title` / `.card-type` / `.card-flavor` dress that globals.css defines
  goes unworn (seen 2026-06-12)
- [ ] `#f9f4e8` (card-paper) sits as a literal hex three times in globals.css —
  it wants to be a variable like its siblings (seen 2026-06-12)

## How to change the vibe

1. Name the color in [palette.md](palette.md), or retire one.
2. `vibe bake` — refreshes `tokens.css`.
3. Dress the faces by hand, with care — they are live sites.
4. `vibe check` — the honest mirror: stray colors, rooms missing their
   epigraph, stale tokens.
