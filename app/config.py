"""
config.py - Application configuration
"""

import os

# Project root directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Database path
# Changed to kis_api_new.db to avoid file lock issues with kis_api.db
DB_PATH = os.path.join(BASE_DIR, "data", "kis_api.db")

# Log directory
LOG_DIR = os.path.join(BASE_DIR, "logs")
