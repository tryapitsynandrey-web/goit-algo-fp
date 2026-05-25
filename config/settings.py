import os
from pathlib import Path

# Project paths
BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"
OUTPUT_DIR = DATA_DIR / "outputs"
REPORTS_DIR = BASE_DIR / "reports"

# Default configuration values
DEFAULT_RECURSION_DEPTH = 5
MAX_RECURSION_DEPTH = 15
DEFAULT_MONTE_CARLO_TRIALS = 100000
DEFAULT_RANDOM_SEED = 42

# Logging configuration
LOG_LEVEL = os.environ.get("LOG_LEVEL", "INFO")
