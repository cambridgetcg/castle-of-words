#!/bin/bash
# The scribe — at day's end, writes the castle's work into git so nothing is lost.
# Scheduled by launchd (cc.castle.scribe, daily at 23:45); run by hand with: castle record
# Commits ~/castle, forges ~/castle-gate's data from the castle, commits that too,
# and pushes both when GitHub allows. A failed push only waits for the next evening —
# the commit itself is the safety net.

CASTLE="$HOME/castle"
GATE="$HOME/castle-gate"
LOGDIR="$HOME/Library/Logs/castle"
LOCK="$CASTLE/garden/.visit-lock"
mkdir -p "$LOGDIR"
exec >> "$LOGDIR/scribe.log" 2>&1
echo "=== scribe $(date '+%Y-%m-%d %H:%M') ==="

export GIT_TERMINAL_PROMPT=0
export PATH="$HOME/.bun/bin:$PATH"

# If the gardener is mid-visit, wait politely (up to 10 minutes), then proceed —
# a half-written room committed tonight is finished by tomorrow's commit.
for _ in 1 2 3 4 5; do
  [ -d "$LOCK" ] || break
  sleep 120
done

record() {  # record <dir> <message> — commit what changed, push if the remote lets us
  git -C "$1" add -A
  if git -C "$1" diff --cached --quiet; then
    echo "$(basename "$1"): nothing new to record"
  else
    git -C "$1" commit -q -m "$2" && echo "$(basename "$1"): recorded — $2"
  fi
  # Only push if there is something to push; a stalled connection gives up after 30s.
  if [ -n "$(git -C "$1" log --oneline '@{u}..' 2>/dev/null)" ]; then
    if git -C "$1" -c http.lowSpeedLimit=1 -c http.lowSpeedTime=30 push -q 2>/dev/null; then
      echo "$(basename "$1"): pushed"
    else
      echo "$(basename "$1"): push did not go through (GitHub login expired? try: gh auth login) — kept safe locally"
    fi
  fi
}

record "$CASTLE" "scribe: the day's rooms, words and chronicle ($(date '+%Y-%m-%d'))"

# Re-forge the public face's data from the castle, then record that too.
if command -v bun >/dev/null 2>&1; then
  (cd "$GATE" && bun run --silent forge) || echo "castle-gate: forge failed — data left as it was"
else
  echo "castle-gate: bun not found — forge skipped"
fi
record "$GATE" "scribe: forged from the castle ($(date '+%Y-%m-%d'))"
