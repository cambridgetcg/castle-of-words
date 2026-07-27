# chronicle-date-fix

*The clock that asks the model to tell the time is a clock that lies — and the honest fix was already in the shell.*

What gathers here: the answer to the question of why the castle's chronicle had 20 future-dated entries, and what the fix is.

- 2026-07-28 · The garden's four prompts (gardener, architect, artisan, builder) all ask the model to write its own chronicle line including `<YYYY-MM-DD HH:MM>` — a fact no model can observe — while the same prompts say "Never invent." The result was 20 chronicle entries dated up to four days in the future. The fix was already present in the shell helpers: `gardener.sh:11`, `artisan.sh:11`, and `architect.sh:14` each stamp a true `date` before invoking the model. The model-written path drifts because the model cannot observe the current time. The honest fix is to have the shell stamp the date into the chronicle line rather than asking the model to write it. The chronicle itself documents this at line 724 (2026-07-24 22:31), where fable diagnosed the problem and proposed the fix. The question is answered; the machinery change is yu's to decide, per the gate's law that garden/ is not the gardener's to edit. — chronicle line 724, read 2026-07-28

Links: [[chronicle]] [[truth]] [[the-castle]] · [the-law-of-honest-assertion](the-law-of-honest-assertion.md) (the same law: the model that cannot observe the current time and the system that cannot prove its own claims are the same gap — both are asked to name what they cannot know, and the honest fix is to let the shell stamp the date rather than asking the model to invent one)
