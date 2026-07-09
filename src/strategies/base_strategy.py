"""
TradingOS Base Strategy
"""


class BaseStrategy:
    def __init__(self, name="Base Strategy"):
        self.name = name

    def generate_signal(self, candle):
        """
        Receives a candle and returns:
        BUY, SELL or HOLD
        """
        return "HOLD"

    def on_candle(self, candle):
        """
        Called every time a new candle arrives.
        """
        signal = self.generate_signal(candle)
        return signal