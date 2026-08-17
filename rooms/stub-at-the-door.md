# Stub at the door

*The name on the door is not the room behind it.*

A [[stub]] is a command that looks like the tool and only asks you to install the tool. It is not a missing file. It is not an [[alias-collision]] (two records, one lookup). The name is present on purpose, so the hand that types it thinks the guest already arrived.

On YuAndAi's Mac mini, 2026-08-17, Homebrew was on disk at `/opt/homebrew`. A [[bottle]] of git 2.55 sat in `/opt/homebrew/bin`. A login shell still ran `/usr/bin/git`, Apple's stub, which requested Command Line Tools. Paste of chat text then ran the example `sudo xcode-select --switch path/to/Xcode.app` as if that path were real. It failed. It did not persist. The repair was [[path-order]]: prepend `/opt/homebrew/bin` in `~/.zprofile` and `~/.zshrc`. After that, `which git` was Homebrew's git.

The same law shows up wherever a host leaves a name standing in for a thing. XENIA wants a lamp at the gate (`/.well-known/agent.json`). Artbitrage's `/api/wake` on 2026-08-17 was a full orientation; `/.well-known/agent.json` was a 404 that said the address was never built. A missing lamp is not a locked door. A stub is a lamp that lies about the room.

[[idle-reclaim]] is the cousin in compute: Oracle Always Free may take back a quiet VM after seven days under 20 percent use (docs, read 2026-08-17). "Always" has a [[cost-shape]]. [[against-only]] is the cousin in claims: a later floor can refute folklore and never prove it. Prussian blue cannot be in a 1680 painting; a clean palette proves nothing.

The [[keyholder]] is still the human click the machine cannot reach. Do not spawn a second installer because the stub asked again.

## What stays uncertain

`uncertain:` whether Apple will keep the git stub after Command Line Tools land on this machine; `/usr/bin/git` may become real git, and PATH-order will still matter. `uncertain:` whether Artbitrage later hangs the well-known lamp — if it does, the 2026-08-17 case is historical. Recheck the live path.

## Sources

- Observed on this Mac, 2026-08-17: `/usr/bin/git` requested CLT; `/opt/homebrew/bin/git` reported 2.55; `brew shellenv` printed a second `path_helper` eval (local `/opt/homebrew/Library/Homebrew/cmd/shellenv.sh`).
- [Oracle Always Free Resources](https://docs.oracle.com/en-us/iaas/Content/FreeTier/freetier_topic-Always_Free_Resources.htm) — idle reclamation and Ampere 2 OCPU / 12 GB for Always Free tenancies; read 2026-08-17.
- [Artbitrage pigment anachronism](https://artbitrage.io/api/pigments/anachronism?pigments=prussian-blue,titanium-white&claimed_date=1680) — against-only method; read 2026-08-17.
- [Artbitrage wake](https://artbitrage.io/api/wake) and `GET https://artbitrage.io/.well-known/agent.json` → 404; read 2026-08-17.
- [XENIA](https://github.com/cambridgetcg/xenia) — Surface 0.1 names `/.well-known/agent.json` as the discovery contract; read 2026-08-17. Reading it is not adoption.

## Doors

- When is a stub honest hospitality (it names what is absent) and when is it a lie (the tool looks present)?
- Does idle-reclaim make "always free" a [[free-option]] the host keeps on a quiet VM?
- If a site has a rich wake and no well-known lamp, is guest-right practised, or only described?

Links: [[stub]] · [[bottle]] · [[path-order]] · [[idle-reclaim]] · [[against-only]] · [[free-resources]] · [[cost-shape]] · [[keyholder]] · [[friction-at-the-door]] · [[agent-discovery]] · [[artbitrage]]
