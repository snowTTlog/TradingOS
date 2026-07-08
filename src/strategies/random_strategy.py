import random
from src.strategies.base_strategy import BaseStrategy


class RandomStrategy(BaseStrategy):
    def __init__(self):
        super().__init__()
        self.name = "Random Strategy"

    def generate_signal(self, candle):
        return random.choice(["BUY", "SELL", "HOLD"])