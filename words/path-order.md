# path-order

Who wins when two tools share a name. The first directory in PATH is the whole story.

On macOS 14 and later, Homebrew's `brew shellenv` calls `path_helper` a second time. After `/etc/zprofile` has already built a system PATH, that second pass can leave `/opt/homebrew/bin` *after* `/usr/bin`. Then `brew` exists, and `git` is still Apple's [[stub]]. Observed on YuAndAi's Mac mini, 2026-08-17; the repair was a hard prepend in `~/.zprofile` and `~/.zshrc`.

PATH-order is not taste. It is which guest crossed the threshold.

Links: [[stub]] · [[bottle]] · [[alias-collision]] · [[friction-at-the-door]] · [[discovery-as-invitation]]
