from src.indicators.ema import EMA


class EMACrossoverStrategy:

    def __init__(self, fast_period=20, slow_period=50):

        self.fast = EMA(fast_period)
        self.slow = EMA(slow_period)

    def generate_signal(self, prices):

        if len(prices) < self.slow.period:
            return "HOLD"

        fast_ema = self.fast.calculate(prices)
        slow_ema = self.slow.calculate(prices)

        if fast_ema > slow_ema:
            return "BUY"

        elif fast_ema < slow_ema:
            return "SELL"

        return "HOLD"