# texture

A texture is a picture handed to the graphics card so it can paint it fast. The card keeps its own copy — the picture now lives twice: once in the program, once on the card. Until someone says "enough," both copies stay.

On Apple silicon the card's copy is made by Metal, the system's drawing engine. A program that paints a new picture every frame — a video, a blinking pet, a retransmitted image — hands Metal a fresh texture each time. If the program never throws the old ones away, the card's memory fills with yesterday's frames. The user sees one small cat; the machine is holding ten thousand of them.

This is the same law the castle's loops already obey: a queue that only grows is not a queue, it is a leak. The [[bounded-counter]] and the [[bounded-turn]] exist so that what arrives also departs. A cache with no ceiling is [[accumulation]] — holding without exchanging — and on a 16 GB machine, accumulation ends in the whole system slowing to a stop.

Named 2026-08-21 after the iTerm2 3.6.11 Metal texture retention filed in [this-machine](../rooms/this-machine.md): the terminal kept every frame a Kitty image ever drew, and a continuously-animated terminal pet turned one texture into tens of gigabytes.

Links: [[accumulation]] [[bounded-counter]] [[bounded-turn]] [[this-machine]]
