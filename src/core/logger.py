"""
TradingOS Logger
"""

import logging
from pathlib import Path


class Logger:
    """Central logger for TradingOS."""

    @staticmethod
    def setup():
        # Create logs folder if it doesn't exist
        Path("logs").mkdir(exist_ok=True)

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s | %(levelname)s | %(message)s",
            handlers=[
                logging.FileHandler("logs/tradingos.log"),
                logging.StreamHandler()
            ]
        )

        return logging.getLogger("TradingOS")