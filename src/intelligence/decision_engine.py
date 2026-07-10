class DecisionEngine:
    """
    Coordinates the Regime Detector and Signal Engine to produce
    the final trading decision.
    """

    def __init__(self, signal_engine, regime_detector):
        self.signal_engine = signal_engine
        self.regime_detector = regime_detector

    def decide(self, signals, trend, atr):
        """
        Parameters
        ----------
        signals : dict
            Trading signals from indicators.

        trend : str
            "UP", "DOWN", or "SIDEWAYS"

        atr : float
            Current ATR value.
        """

        regime = self.regime_detector.detect(trend, atr)

        # Copy the signals so we don't modify the original dictionary
        final_signals = signals.copy()
        final_signals["regime"] = regime

        return self.signal_engine.analyze(final_signals)