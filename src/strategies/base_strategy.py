class BaseStrategy:
    def __init__(self):
        self.name = "Base Strategy"

    def generate_signal(self, candle):
        """
        This method receives market data and returns a signal.
        """
        return "HOLD"