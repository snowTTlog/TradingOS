"""
TradingOS Historical Data Loader

Loads HistData CSV files and converts each row into a Candle object.
"""

from pathlib import Path
from datetime import datetime

from src.models import Candle


class DataLoader:
    def __init__(self, file_path: str):
        self.file_path = Path(file_path)

    def load(self):
        """
        Read the CSV file and yield Candle objects one at a time.
        """

        if not self.file_path.exists():
            raise FileNotFoundError(f"File not found: {self.file_path}")

        with self.file_path.open("r", encoding="utf-8") as file:

            for line in file:

                line = line.strip()

                if not line:
                    continue

                parts = line.split(";")

                if len(parts) != 6:
                    continue

                timestamp = datetime.strptime(
                    parts[0],
                    "%Y%m%d %H%M%S"
                )

                candle = Candle(
                    symbol="EURUSD",
                    timestamp=timestamp,
                    open=float(parts[1]),
                    high=float(parts[2]),
                    low=float(parts[3]),
                    close=float(parts[4]),
                    volume=float(parts[5]),
                    timeframe="1m",
                )

                yield candle