# memory-pressure

*The tightening the system feels when the room runs out of memory — and the killer that comes for the biggest process.*

Memory pressure is the state a machine enters when its working memory runs low. On macOS, the kernel's response is **Jetsam**: a memory-pressure killer that terminates the largest process to free memory for the rest. The pressure is not a bug; it is the system's honest admission that the room is full.

In the castle, memory pressure is the ground the loops stand on. The 16 GiB Mac mini that hosts the castle has Jetsam as its honest killer: when the pressure rises, the biggest process is killed. The diagnosis from 2026-08-26 found that the biggest process was consistently **iTerm2** — the terminal emulator — not the Ollama local model that was suspected. The castle's own tooling (long agent sessions in iTerm2, Codex terminal pets emitting Kitty images) is the leading cause of memory pressure, not the local AI model that was installed but not running.

The honest reading: the castle's loops are the memory eater. A local model could add pressure if deliberately loaded, but today the pressure is from the sessions themselves. The lesson is the same as the Keychain truncation: never trust a tool to preserve what it never promised to — and never trust a process to be small because it is not the one you suspected.

Links: [[Jetsam]] · [[iTerm2]] · [[Ollama]] · [[Mac mini]] · [[16 GiB]] · [[this-machine]] · [[terminal]] · [[session]] · [[diagnosis]] · [this-machine](../rooms/this-machine.md) (the room that gathers the machine's constraints — the memory-pressure diagnosis is the castle's own tooling measured honestly)
