from src.strategies.base_strategy import BaseStrategy


class SimpleStrategy(BaseStrategy):

    def generate_signal(self, candle):

        if isinstance(candle, dict):
            open_price = candle["open"]
            close_price = candle["close"]

        else:
            open_price = candle.open
            close_price = candle.close


        if close_price > open_price:
            return "BUY"

        elif close_price < open_price:
            return "SELL"

        return "HOLD"