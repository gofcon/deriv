#!/bin/bash

# Configuration
PROJECT_DIR="/home/opc/deriv"
VENV_DIR="$PROJECT_DIR/.venv"
LOG_DIR="$PROJECT_DIR/logs"

# Cycle argument (e.g., 5min, 1hour, daily)
CYCLE=$1

if [ -z "$CYCLE" ]; then
    echo "Usage: $0 <cycle>"
    exit 1
fi

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Activate Virtual Environment
source "$VENV_DIR/bin/activate"

# Change to project directory
cd "$PROJECT_DIR"

# Execute with cycle filter
echo "[$(date)] Starting execution for cycle: $CYCLE" >> "$LOG_DIR/api_${CYCLE}.log"

python main.py --cycle "$CYCLE" >> "$LOG_DIR/api_${CYCLE}.log" 2>&1

echo "[$(date)] Completed execution for cycle: $CYCLE" >> "$LOG_DIR/api_status.log"
