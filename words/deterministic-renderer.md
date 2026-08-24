# deterministic-renderer

A deterministic renderer is a machine that turns the same input into the same output, every time — no hidden dice, no quiet drift.

In music, a deterministic renderer takes a score (notes, durations, instruments) and produces audio. If the score is the same and the renderer is deterministic, the audio is the same. The renderer is the [[receipt]] that the score's promise was kept. If the renderer is not deterministic — if it samples, improvises, or uses unrecorded state — then two runs of the same score are two different takes, and any claim of repeatability is a lie.

The castle knows this shape in [canonical-wire-action](canonical-wire-action.md): commit the complete wire action before dispatch, compare the same commitment before execution. The deterministic renderer is the same law at the creative layer: the score is the commitment, the renderer is the executor, and determinism is what lets the listener verify that the voice did not invent a new promise mid-song.

Links: [[receipt]] · [[validated-score]] · [[edition]] · [the-score-and-the-engine](../rooms/the-score-and-the-engine.md) · [canonical-wire-action](../rooms/canonical-wire-action.md)
