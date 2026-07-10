class RegimeDetector:
    """
    Detects the current market regime.
    """

    def detect(self, trend, atr):
        """
        Parameters
        ----------
        trend : str
            "UP", "DOWN", or "SIDEWAYS"
        atr : float
            Average True Range

        Returns
        -------
        str
            Market regime
        """

        if trend == "UP":
            return "TRENDING_UP"

        if trend == "DOWN":
            return "TRENDING_DOWN"

        if atr > 2:
            return "HIGH_VOLATILITY"

        return "RANGING"