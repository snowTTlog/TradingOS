class BOS:
    """
    Break of Structure detector.
    """

    def detect(self, highs, lows):

        if len(highs) < 2 or len(lows) < 2:
            return "NONE"

        # Bullish BOS
        if highs[-1] > highs[-2]:
            return "BULLISH_BOS"

        # Bearish BOS
        if lows[-1] < lows[-2]:
            return "BEARISH_BOS"

        return "NONE"