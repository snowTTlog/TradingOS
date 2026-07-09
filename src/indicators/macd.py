class MACD:

    def __init__(self, fast_period=12, slow_period=26):

        self.fast_period = fast_period
        self.slow_period = slow_period

    def _ema(self, prices, period):

        if len(prices) < period:
            return None

        multiplier = 2 / (period + 1)

        ema = sum(prices[:period]) / period

        for price in prices[period:]:
            ema = (price - ema) * multiplier + ema

        return ema

    def calculate(self, prices):

        fast_ema = self._ema(prices, self.fast_period)
        slow_ema = self._ema(prices, self.slow_period)

        if fast_ema is None or slow_ema is None:
            return None

        macd = fast_ema - slow_ema

        return round(macd, 5)