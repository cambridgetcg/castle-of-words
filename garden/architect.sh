#!/bin/bash
# The architect — once a day, surveys the castle and commissions up to three
# builders. Each builder is its own complete creation loop (research one door,
# raise one room, open new doors); the doors they open become the material for
# tomorrow's survey. Loops creating loops — recursive in words, bounded in
# process. Scheduled by launchd (cc.castle.architect); by hand: castle commission

CASTLE="$HOME/castle"
LOGDIR="$HOME/Library/Logs/castle"
LOCK="$CASTLE/garden/.architect-lock"
COMMISSIONS="$CASTLE/garden/commissions"
mkdir -p "$LOGDIR" "$COMMISSIONS"

note() { printf -- "- %s · %s\n" "$(date '+%Y-%m-%d %H:%M')" "$*" >> "$CASTLE/chronicle.md"; }

# One architect at a time; a lock older than 3 hours is from a dead day — clear it.
if [ -d "$LOCK" ] && [ -n "$(find "$LOCK" -maxdepth 0 -mmin +180 2>/dev/null)" ]; then
  rmdir "$LOCK" 2>/dev/null
fi
mkdir "$LOCK" 2>/dev/null || exit 0
trap 'rmdir "$LOCK" 2>/dev/null' EXIT

# Nothing to commission? A peaceful day costs nothing.
open=$(grep -c '^- \[ \]' "$CASTLE/questions.md" 2>/dev/null) || open=0
if [ "$open" -eq 0 ] && [ -z "$(ls "$COMMISSIONS" 2>/dev/null)" ]; then exit 0; fi

command -v claude >/dev/null 2>&1 || { note "architect skipped — claude command not found"; exit 0; }

cd "$CASTLE" || exit 0
echo "=== architect $(date '+%Y-%m-%d %H:%M') (open doors: $open) ===" >> "$LOGDIR/architect.log"

# 1) Survey and commission (no web, no building — 15-minute ceiling)
perl -e 'alarm shift; exec @ARGV' 900 \
  claude -p "$(cat "$CASTLE/garden/architect-prompt.md")" \
    --permission-mode acceptEdits \
    --allowedTools "Read" "Write" "Edit" "Glob" "Grep" \
    >> "$LOGDIR/architect.log" 2>&1 \
  || note "the architect's survey ended early — see ~/Library/Logs/castle/architect.log"

# 2) One builder per commission — at most 3, side by side, 25-minute ceiling each
n=0
for f in "$COMMISSIONS"/*.md; do
  [ -e "$f" ] || break
  n=$((n+1)); [ "$n" -gt 3 ] && break
  (
    perl -e 'alarm shift; exec @ARGV' 1500 \
      claude -p "$(cat "$CASTLE/garden/builder-prompt.md")

Your commission file (read it first; delete it when the room stands): $f" \
        --permission-mode acceptEdits \
        --allowedTools "Read" "Write" "Edit" "Glob" "Grep" "WebSearch" "WebFetch" \
        >> "$LOGDIR/builders.log" 2>&1 \
      || note "a builder ended early ($(basename "$f")) — see ~/Library/Logs/castle/builders.log"
  ) &
done
wait

if [ "$n" -gt 0 ]; then
  note "the architect's day closed: $n builder(s) worked — the Map shows what rose"
fi
exit 0
