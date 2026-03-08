#!/bin/bash

# Configuration
PROJECT_DIR="/home/opc/deriv"
VENV_DIR="$PROJECT_DIR/.venv"
LOG_DIR="$PROJECT_DIR/logs"

# Ensure log directory exists
mkdir -p "$LOG_DIR"

# Activate Virtual Environment
source "$VENV_DIR/bin/activate"

# Change to project directory
cd "$PROJECT_DIR"

# Execute generate_jobs
echo "[$(date)] Starting monthly execution of generate_jobs.py" >> "$LOG_DIR/generate_jobs.log"

python scripts/generate_jobs.py >> "$LOG_DIR/generate_jobs.log" 2>&1

echo "[$(date)] Completed execution of generate_jobs.py" >> "$LOG_DIR/api_status.log"
