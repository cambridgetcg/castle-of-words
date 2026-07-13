# parity-gate

*A gate that cannot see every door is a gate that lies.*

An SDK parity gate must cover every reachable client namespace — nested clients, language-specific filenames, every surface a caller can touch. A helper that performs no runtime inspection must return `not_checked`, never claim enforcement. A gate that says "all clear" without looking is not a gate — it is a story.

Links: [[enforcement]] · [[not-checked]] · [[boundary]] · [safe-api-design](safe-api-design.md)
