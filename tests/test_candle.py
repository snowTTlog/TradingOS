from datetime import datetime

from src.models import Candle

candle = Candle(
    symbol="BTCUSDT",
    timestamp=datetime.now(),
    open=100,
    high=110,
    low=95,
    close=108,
    volume=2500,
)

print(candle)
print(candle.bullish())
print(candle.body)
print(candle.range)
print(candle.upper_wick)
print(candle.lower_wick)