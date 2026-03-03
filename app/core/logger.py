import logging
import os

os.makedirs("logs", exist_ok=True)

LOG_FILE = "logs/app.log"

logger = logging.getLogger("address_app")
logger.setLevel(logging.INFO)

# 🚫 Disable propagation to root logger (important)
logger.propagate = False

# Remove existing handlers (important fix)
if logger.hasHandlers():
    logger.handlers.clear()

# File handler only
file_handler = logging.FileHandler(LOG_FILE)
file_handler.setLevel(logging.INFO)

formatter = logging.Formatter(
    "%(asctime)s - %(levelname)s - %(message)s"
)

file_handler.setFormatter(formatter)
logger.addHandler(file_handler)