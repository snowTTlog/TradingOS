from src.strategies.base_strategy import BaseStrategy


class SimpleStrategy(BaseStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Simple Strategy"

    def generate_signal(self, candle):
        if candle["close"] > candle["open"]:
            return "BUY"
        if candle["close"] < candle["open"]:
            return "SELL"
        return "HOLD"
