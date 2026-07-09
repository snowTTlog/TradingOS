"""
TradingOS Replay Engine

Feeds candles one at a time, simulating a live market.
"""


class ReplayEngine:
    def __init__(self, loader):
        self.loader = loader

    def stream(self):
        """
        Yield one candle at a time.
        """
        for candle in self.loader.load():
            yield candle