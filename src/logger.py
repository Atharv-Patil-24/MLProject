import logging
import os
from datetime import datetime

# Setup log file path
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"
logs_dir = os.path.join(os.getcwd(), "logs")  # Directory for logs
os.makedirs(logs_dir, exist_ok=True)  # Ensure the logs directory exists

LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)
print(f"Logging to: {LOG_FILE_PATH}")  # Debugging: Verify log file path

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Capture all log levels
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(LOG_FILE_PATH),  # Write logs to file
        logging.StreamHandler()  # Also output logs to console for debugging
    ],
    force=True  # Overwrite any previous logging configuration
)

