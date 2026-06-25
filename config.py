"""
BTC OI Backtester
Configuration
"""

from pathlib import Path

# ======================================================
# PATHS
# ======================================================

BASE_DIR = Path(__file__).resolve().parent

INPUT_DIR = BASE_DIR / "input"
REPORT_DIR = BASE_DIR / "reports"

BTC_FILE = INPUT_DIR / "btc.csv"
OI_FILE = INPUT_DIR / "oi.csv"

TRADES_FILE = REPORT_DIR / "trades.csv"
EQUITY_FILE = REPORT_DIR / "equity.csv"

# ======================================================
# ACCOUNT
# ======================================================

START_BALANCE = 1000.0

LEVERAGE = 20

MARGIN = 50.0

POSITION_SIZE = LEVERAGE * MARGIN

COMMISSION = 0.0004

SLIPPAGE = 0.0

# ======================================================
# POSITION LIMITS
# ======================================================

MAX_LONG = 1
MAX_SHORT = 1

# ======================================================
# STRATEGY
# ======================================================

OI_THRESHOLD = 0.30

USE_CLOSE_FILTER = True

USE_VOLUME_FILTER = True

EXIT_MODE = "profit_reverse"

STOP_PERCENT = None

# ======================================================
# REPORTS
# ======================================================

SAVE_TRADES = True

SAVE_EQUITY = True

PRINT_STATISTICS = True

# ======================================================
# DEBUG
# ======================================================

DEBUG = False