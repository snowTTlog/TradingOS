class ATR:

    def __init__(self, period=14):
        self.period = period

    def calculate(self, highs, lows, closes):

        if len(highs) <= self.period:
            return None

        true_ranges = []

        for i in range(1, len(highs)):

            tr = max(
                highs[i] - lows[i],
                abs(highs[i] - closes[i - 1]),
                abs(lows[i] - closes[i - 1])
            )

            true_ranges.append(tr)

        atr = sum(true_ranges[:self.period]) / self.period

        return round(atr, 5)