class EMA:

    def __init__(self, period):
        self.period = period

    def calculate(self, prices):

        if len(prices) < self.period:
            return None

        multiplier = 2 / (self.period + 1)

        # Start with SMA
        ema = sum(prices[:self.period]) / self.period

        # Continue EMA calculation
        for price in prices[self.period:]:
            ema = (price - ema) * multiplier + ema

        return ema