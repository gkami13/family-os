#!/bin/bash
# Family OS — Weekly Digest cron runner
# Runs the digest script and writes output to Notion.
#
# To install the cron job (runs every Sunday at 6pm):
#   crontab -e
#   Add this line:
#   0 18 * * 0 /Users/gokamiyama/Desktop/5-ai-projects/Family-OS/scripts/run-weekly-digest.sh >> /tmp/family-os-digest.log 2>&1

set -e

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
ENV_FILE="$REPO_DIR/.env"
PYTHON="python3"

# Load .env if it exists
if [ -f "$ENV_FILE" ]; then
  export $(grep -v '^#' "$ENV_FILE" | xargs)
fi

# Run digest — write to Notion automatically
echo "[$(date)] Running Family OS weekly digest..."
$PYTHON "$SCRIPT_DIR/weekly-digest.py" --notion
echo "[$(date)] Done."
