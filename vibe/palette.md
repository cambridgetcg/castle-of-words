# The Palette

*every color the kingdom wears, named and numbered*

One table per livery, one source of truth for all of them. The faces (the gate
site, the front binder) should wear only these colors; `vibe check` tells on
any stray. Change a color here, then `vibe bake` to refresh `tokens.css`.
Tints are allowed: an `rgba()` of a named color is that color wearing alpha —
the check reads only solid hexes.

## The gate's livery — ink on parchment, one foil thread

Worn by `~/castle-gate`, the public face. Read from its `globals.css`, 2026-06-12.

| livery | name | hex | role |
|--------|------|-----|------|
| gate | ink | #1a1612 | the words themselves — warm near-black |
| gate | ink-soft | #3d352b | quieter prose: quotes, epigraphs, card text |
| gate | ink-faint | #6e6354 | footnotes and flavor |
| gate | parchment | #f5efe2 | the page |
| gate | parchment-deep | #ece3cf | the chip behind code |
| gate | parchment-edge | #e0d4b8 | every hairline border |
| gate | card-paper | #f9f4e8 | the card's brighter face |
| gate | foil | #b8902e | the one gold accent: underlines, rings, fleurons |
| gate | foil-dark | #8a6d1f | gold deepened — hovers and small-caps labels |
| gate | foil-light | #e3c45e | gold lifted — the ring when a card rises |
| gate | foil-gleam | #f6e7ae | the bright heart of the foil gradient |

## The front's livery — the Cambridge TCG dress

Worn by `~/castle/front`, the baked card binder. Crimson, navy and gold on warm
paper with seigaiha waves (the Japanese overlapping-wave pattern) — lifted
from cambridgetcg/ShopifyTheme_TCG (the One Piece zone). Read from
`front/build.js`, 2026-06-12.

| livery | name | hex | role |
|--------|------|-----|------|
| front | crimson | #c41e3a | the banner red: names, headings, rare cards |
| front | navy | #1e3a5f | the frame: header, panels, common borders |
| front | gold | #f5d742 | glints: underlines, hover rings, rewards |
| front | paper | #fff8f0 | warm paper ground |
| front | ink | #1a1a1a | main text |
| front | muted | #4a4a4a | secondary text |
| front | white | #ffffff | card and room faces |
| front | art-shade | #f3e9da | the card art panel's deeper edge |
| front | hairline | #eee2d0 | foot borders and the progress track |
| front | room-edge | #eadfce | the soft outline around full rooms |
| front | code-cream | #f6efe2 | inline code ground |
| front | chronicle-ice | #e9eef6 | pale words on the navy chronicle panel |
| front | steel | #5a7a9f | the uncommon tier's steel blue |
| front | trophy-gold | #b8860b | the legendary tier's border — trophy gold |
