"""
log_setup.py - Centralized logging configuration
"""

import os
import logging
import sys

def setup_logging(log_file="kis_app.log"):
    """
    Configure logging to file and console.
    
    Args:
        log_file (str): Name of the log file. Defaults to "kis_app.log".
    """
    # Determine the absolute path to the logs directory at the project root
    # This file is in d:\Python\deriv\scripts\
    # Project root is the parent.
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_dir = os.path.join(base_dir, "logs")
    
    # Create logs directory if it doesn't exist
    if not os.path.exists(log_dir):
        os.makedirs(log_dir)
        
    log_path = os.path.join(log_dir, log_file)
    
    # Create handlers
    file_handler = logging.FileHandler(log_path, encoding='utf-8', mode='a')
    stream_handler = logging.StreamHandler(sys.stdout)
    
    # Define formatter
    formatter = logging.Formatter(
        '%(filename)s:%(lineno)d: %(asctime)s - %(levelname)s - %(message)s'
    )
    
    file_handler.setFormatter(formatter)
    stream_handler.setFormatter(formatter)
    
    # Configure root logger
    logging.basicConfig(
        level=logging.INFO,
        handlers=[file_handler, stream_handler],
        force=True # Force reconfiguration to override any existing config
    )
    
    logging.info(f"Logging initialized. Log file: {log_path}")

# Initialize logging when module is imported? 
# Better to let the main script call setup_logging() to allow flexibility if needed.
