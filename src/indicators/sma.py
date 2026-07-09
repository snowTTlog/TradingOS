class SMA:

    def __init__(self, period):

        self.period = period


    def calculate(self, prices):

        if len(prices) < self.period:
            return None

        window = prices[-self.period:]

        return sum(window) / self.period