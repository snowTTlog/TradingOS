class RSI:

    def __init__(self, period=14):
        self.period = period

    def calculate(self, prices):

        if len(prices) <= self.period:
            return None

        gains = []
        losses = []

        for i in range(1, self.period + 1):

            change = prices[i] - prices[i - 1]

            if change > 0:
                gains.append(change)
                losses.append(0)
            else:
                gains.append(0)
                losses.append(abs(change))

        average_gain = sum(gains) / self.period
        average_loss = sum(losses) / self.period

        if average_loss == 0:
            return 100

        rs = average_gain / average_loss

        rsi = 100 - (100 / (1 + rs))

        return round(rsi, 2)