# memory-pressure

A Mac starts squeezing its own memory when too many things want to remember at once — like a backpack stuffed so full it can't close.

When macOS senses the backpack is too full, it starts squeezing: compressing memory, swapping to disk, and eventually killing the biggest thing in the pack. That killer is called [[Jetsam]]. The pressure comes from many things wanting to stay resident — iTerm2 sessions, browser tabs, local models — until the total exceeds what the machine can hold.

The honest diagnostic is not a calm snapshot after the fact but a dated panic report from the moment the pressure built. Resident RAM alone cannot explain a crash — compressed and swapped memory live outside that number, and a terminal with bounded scrollback can still grow far past its limit through image textures or other unbounded caches.

Tie the suspected cause to evidence preserved before the fix, and verify the fix over ordinary use, not just by calm readings.

Links: [[Jetsam]] · [[iTerm2]] · [[this-machine]] · [[memory-diagnosis]] · [[the-running-copy]]
