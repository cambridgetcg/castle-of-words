#!/bin/bash
# The gardener — one visit to the castle of understanding.
# Scheduled by launchd (cc.castle.gardener, every 4 hours); run by hand with: castle visit
# A visit costs a little Claude usage; an idle visit (nothing waiting) costs nothing.

CASTLE="$HOME/castle"
LOGDIR="$HOME/Library/Logs/castle"
LOCK="$CASTLE/garden/.visit-lock"
mkdir -p "$LOGDIR"

note() { printf -- "- %s · %s\n" "$(date '+%Y-%m-%d %H:%M')" "$*" >> "$CASTLE/chronicle.md"; }

# One gardener at a time. A lock older than 2 hours is from a dead visit — clear it.
if [ -d "$LOCK" ] && [ -n "$(find "$LOCK" -maxdepth 0 -mmin +120 2>/dev/null)" ]; then
  rmdir "$LOCK" 2>/dev/null
fi
if ! mkdir "$LOCK" 2>/dev/null; then
  exit 0
fi
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

# Anything to do? (insights waiting in the courtyard, or questions open)
waiting=$(grep -c '^- ' "$CASTLE/courtyard.md" 2>/dev/null) || waiting=0
open=$(grep -c '^- \[ \]' "$CASTLE/questions.md" 2>/dev/null) || open=0
if [ "$waiting" -eq 0 ] && [ "$open" -eq 0 ]; then
  exit 0
fi

command -v claude >/dev/null 2>&1 || { note "visit skipped — claude command not found on PATH"; exit 0; }

cd "$CASTLE" || exit 0
echo "=== visit $(date '+%Y-%m-%d %H:%M') (waiting: $waiting, open: $open) ===" >> "$LOGDIR/visit.log"

# The visit. 25-minute ceiling (perl alarm) so a stuck visit can never linger.
perl -e 'alarm shift; exec @ARGV' 1500 \
  claude -p "$(cat "$CASTLE/garden/gardener-prompt.md")" \
    --permission-mode acceptEdits \
    --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "WebSearch" "WebFetch" \
    >> "$LOGDIR/visit.log" 2>&1
rc=$?

if [ "$rc" -ne 0 ]; then
  note "visit ended early (code $rc) — details in ~/Library/Logs/castle/visit.log"
fi
exit 0
