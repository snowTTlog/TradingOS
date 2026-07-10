class MarketStructure:

    def trend(self, prices):

        if len(prices) < 2:
            return "UNKNOWN"

        if prices[-1] > prices[0]:
            return "UPTREND"

        elif prices[-1] < prices[0]:
            return "DOWNTREND"

        return "SIDEWAYS"

    def higher_high(self, highs):

        if len(highs) < 2:
            return False

        return highs[-1] > highs[-2]

    def lower_low(self, lows):

        if len(lows) < 2:
            return False

        return lows[-1] < lows[-2]