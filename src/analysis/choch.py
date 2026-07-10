class CHoCH:
    """
    Change of Character detector.
    """

    def detect(self, previous_trend, current_trend):

        if previous_trend == "DOWNTREND" and current_trend == "UPTREND":
            return "BULLISH_CHOCH"

        if previous_trend == "UPTREND" and current_trend == "DOWNTREND":
            return "BEARISH_CHOCH"

        return "NONE"