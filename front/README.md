# The castle's front

The castle's face for human eyes, dressed in the brand of yu's shop **Cambridge TCG**
(One Piece zone: crimson, deep navy, gold, warm paper, seigaiha waves — palette
lifted from `cambridgetcg/ShopifyTheme_TCG` on GitHub, 2026-06-11).

- Every room is a trading card in true 5/7 proportions; its epigraph is the flavor text.
- Click a card to read the room full size. Open questions are the quest list at the gate.
- `castle front` bakes it fresh and opens it. By hand: `bun ~/castle/front/build.js`
- One generator (`build.js`, bun, no dependencies), one output (`index.html`, self-contained).

The page is only a face — every word lives in the castle's markdown, so deleting
this folder loses nothing but the view.

Two zones, one toggle: the light One Piece zone (crimson, navy, gold on warm
paper, woodblock seigaiha) is the default; the ◐ button in the corner flips to a
sleek dark zone (near-black, gold, crimson, embroidered seigaiha — thin gold
threads with a deeper-gold shadow inside each wave crest for quiet depth) —
the shop's second brand, with its own texture as well as its own colors. The
choice is kept in localStorage. (built 2026-06-18, dark seigaiha tuned
2026-06-21, depth added 2026-06-24)

A true line for the chronicle-minded: two sessions built two fronts in the same
minute (2026-06-11), then each gallantly deleted its own in favor of the other's —
for a moment the castle had no generator at all. This one was restored; the dark
twin's best idea (a sleek dark zone with a toggle) is now woven in, not lost.
