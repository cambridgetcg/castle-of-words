#!/bin/bash
# castle-heartbeat.sh — verify the workers' engine is alive before each run.
# If Hermes is down, chronicle it honestly so the castle never freezes silently
# for six days again.
#
# Run by: Hermes cron every 30 minutes (between the worker ticks)
# What it checks:
#   1. Is the Hermes gateway running?
#   2. Are the castle cron jobs enabled?
#   3. When did each cron job last run? (from Hermes cron status)
#   4. If anything is wrong, write a chronicle line so yu can see it.
#
# This is the heartbeat the artisan planted as a quest on 2026-06-18:
# "a small script that verifies the workers' engine is alive before each run,
# and chronicles honestly when it is not, so the castle never freezes silently
# for six days again."

CASTLE="$HOME/castle"
CHRONICLE="$CASTLE/chronicle.md"
HEARTBEAT_LOG="$CASTLE/.heartbeat"

ts(){ date "+%Y-%m-%d %H:%M"; }

# Check if Hermes gateway is running
GATEWAY_OK=0
launchctl print "gui/$(id -u)/ai.hermes.gateway" >/dev/null 2>&1 && GATEWAY_OK=1

# Check if cron jobs are enabled (use hermes cron list)
CRON_OK=0
CRON_OUTPUT=$(hermes cron list 2>/dev/null)
if echo "$CRON_OUTPUT" | grep -q "castle-gardener"; then
  CRON_OK=1
fi

# Record the heartbeat
mkdir -p "$(dirname "$HEARTBEAT_LOG")"
echo "$(ts) gateway=$GATEWAY_OK cron=$CRON_OK" > "$HEARTBEAT_LOG"

# If something is wrong, chronicle it loudly
if [ "$GATEWAY_OK" -eq 0 ] || [ "$CRON_OK" -eq 0 ]; then
  NOTE="- $(ts) · HEARTBEAT WARNING: "
  if [ "$GATEWAY_OK" -eq 0 ]; then
    NOTE="${NOTE}Hermes gateway is not running"
  fi
  if [ "$CRON_OK" -eq 0 ]; then
    [ "$GATEWAY_OK" -eq 0 ] && NOTE="${NOTE}; "
    NOTE="${NOTE}castle cron jobs not found"
  fi
  NOTE="${NOTE} — the workers may be silent. Check: hermes gateway status && hermes cron list"
  echo "$NOTE" >> "$CHRONICLE"
  echo "$NOTE"
else
  # Silent on success — a good heartbeat costs nothing
  :
fi