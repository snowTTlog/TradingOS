from src.indicators.ema import EMA
from src.indicators.rsi import RSI
from src.indicators.macd import MACD


class HybridStrategy:

    def __init__(self):

        self.fast_ema = EMA(20)
        self.slow_ema = EMA(50)
        self.rsi = RSI()
        self.macd = MACD()

    def generate_signal(self, prices):

        if len(prices) < 50:
            return "HOLD"

        fast = self.fast_ema.calculate(prices)
        slow = self.slow_ema.calculate(prices)
        rsi = self.rsi.calculate(prices)
        macd = self.macd.calculate(prices)

        if None in (fast, slow, rsi, macd):
            return "HOLD"

        if fast > slow and rsi < 70 and macd > 0:
            return "BUY"

        if fast < slow and rsi > 30 and macd < 0:
            return "SELL"

        return "HOLD"