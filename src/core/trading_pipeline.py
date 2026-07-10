from src.indicators.ema import EMA
from src.indicators.macd import MACD
from src.indicators.rsi import RSI

from src.analysis.market_structure import MarketStructure

from src.intelligence import (
    SignalEngine,
    RegimeDetector,
    DecisionEngine,
)


class TradingPipeline:
    """
    Complete Trading Pipeline.

    Responsibilities:
    - Calculate indicators
    - Determine market structure
    - Generate trading signals
    - Detect market regime
    - Produce final BUY / SELL / HOLD decision
    """

    def __init__(self):
        # Indicators
        self.ema = EMA(20)
        self.macd = MACD()
        self.rsi = RSI()

        # Analysis
        self.market_structure = MarketStructure()

        # Intelligence
        self.signal_engine = SignalEngine()
        self.regime_detector = RegimeDetector()
        self.decision_engine = DecisionEngine(
            self.signal_engine,
            self.regime_detector,
        )

    def process(self, prices, atr):
        """
        Process historical prices and return a trading decision.
        """

        # -----------------------------
        # Indicator Calculations
        # -----------------------------
        ema = self.ema.calculate(prices)
        macd = self.macd.calculate(prices)
        rsi = self.rsi.calculate(prices)

        if ema is None or macd is None or rsi is None:
            return None

        current_price = prices[-1]

        # -----------------------------
        # Market Structure
        # -----------------------------
        market_trend = self.market_structure.trend(prices)

        if market_trend == "UPTREND":
            trend = "UP"
        elif market_trend == "DOWNTREND":
            trend = "DOWN"
        else:
            trend = "SIDEWAYS"

        signals = {}

        # -----------------------------
        # EMA Signal
        # -----------------------------
        if current_price > ema:
            signals["ema"] = "BUY"
        else:
            signals["ema"] = "SELL"

        # -----------------------------
        # MACD Signal
        # -----------------------------
        if macd > 0:
            signals["macd"] = "BUY"
        else:
            signals["macd"] = "SELL"

        # -----------------------------
        # RSI Signal
        # -----------------------------
        if rsi < 30:
            signals["rsi"] = "BUY"
        elif rsi > 70:
            signals["rsi"] = "SELL"
        else:
            signals["rsi"] = "HOLD"

        # -----------------------------
        # Market Structure Signal
        # -----------------------------
        if market_trend == "UPTREND":
            signals["market_structure"] = "BULLISH"
        elif market_trend == "DOWNTREND":
            signals["market_structure"] = "BEARISH"

        # -----------------------------
        # Final Decision
        # -----------------------------
        return self.decision_engine.decide(
            signals=signals,
            trend=trend,
            atr=atr,
        )