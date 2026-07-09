"""
TradingOS Candle Model
"""

from dataclasses import dataclass
from datetime import datetime


@dataclass(slots=True)
class Candle:
    symbol: str

    timestamp: datetime

    open: float
    high: float
    low: float
    close: float

    volume: float

    timeframe: str = "1m"

    def bullish(self) -> bool:
        return self.close > self.open

    def bearish(self) -> bool:
        return self.close < self.open

    @property
    def body(self):
        return abs(self.close - self.open)

    @property
    def range(self):
        return self.high - self.low

    @property
    def upper_wick(self):
        return self.high - max(self.open, self.close)

    @property
    def lower_wick(self):
        return min(self.open, self.close) - self.low

    def to_dict(self):
        return {
            "symbol": self.symbol,
            "timestamp": self.timestamp,
            "open": self.open,
            "high": self.high,
            "low": self.low,
            "close": self.close,
            "volume": self.volume,
            "timeframe": self.timeframe,
        }