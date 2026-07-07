"""
TradingOS Settings
------------------
This file stores the global settings used by the application.
"""

class Settings:
    """Application settings."""

    # Application
    APP_NAME = "TradingOS"
    VERSION = "0.0.1"
    MODE = "Development"

    # Trading
    DEFAULT_EXCHANGE = "Binance"
    DEFAULT_MARKET = "Crypto"

    # Risk
    MAX_RISK_PER_TRADE = 1.0  # Percent

    # Logging
    LOG_LEVEL = "INFO"