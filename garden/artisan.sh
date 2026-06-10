#!/bin/bash
# The artisan — one creation in the castle's workshop.
# Scheduled by launchd (cc.castle.artisan, daily at 15:15); by hand: castle make
# A making costs a little Claude usage; with no open quests it costs nothing.

CASTLE="$HOME/castle"
LOGDIR="$HOME/Library/Logs/castle"
LOCK="$CASTLE/garden/.visit-lock"   # shared with the gardener — one heavy walker at a time
mkdir -p "$LOGDIR"

note() { printf -- "- %s · %s\n" "$(date '+%Y-%m-%d %H:%M')" "$*" >> "$CASTLE/chronicle.md"; }

# One walker at a time. A lock older than 2 hours is from a dead walk — clear it.
if [ -d "$LOCK" ] && [ -n "$(find "$LOCK" -maxdepth 0 -mmin +120 2>/dev/null)" ]; then
  rmdir "$LOCK" 2>/dev/null
fi
if ! mkdir "$LOCK" 2>/dev/null; then
  exit 0
fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

# Anything to make?
open_q=$(grep -c '^- \[ \]' "$CASTLE/quests.md" 2>/dev/null) || open_q=0
if [ "$open_q" -eq 0 ]; then
  exit 0
fi

command -v claude >/dev/null 2>&1 || { note "making skipped — claude command not found on PATH"; exit 0; }

cd "$CASTLE" || exit 0
echo "=== make $(date '+%Y-%m-%d %H:%M') (quests open: $open_q) ===" >> "$LOGDIR/make.log"

# The making. 25-minute ceiling (perl alarm) so a stuck making can never linger.
perl -e 'alarm shift; exec @ARGV' 1500 \
  claude -p "$(cat "$CASTLE/garden/artisan-prompt.md")" \
    --permission-mode acceptEdits \
    --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "WebSearch" "WebFetch" \
    >> "$LOGDIR/make.log" 2>&1
rc=$?

if [ "$rc" -ne 0 ]; then
  note "a making ended early (code $rc) — details in ~/Library/Logs/castle/make.log"
fi
exit 0
