from src.intelligence import (
    DecisionEngine,
    SignalEngine,
    RegimeDetector,
)


def test_buy_decision():
    engine = DecisionEngine(
        SignalEngine(),
        RegimeDetector()
    )

    signals = {
        "ema": "BUY",
        "macd": "BUY",
        "rsi": "BUY",
        "market_structure": "BULLISH",
    }

    result = engine.decide(signals, "UP", 1.5)

    assert result["action"] == "BUY"


def test_sell_decision():
    engine = DecisionEngine(
        SignalEngine(),
        RegimeDetector()
    )

    signals = {
        "ema": "SELL",
        "macd": "SELL",
        "rsi": "SELL",
        "market_structure": "BEARISH",
    }

    result = engine.decide(signals, "DOWN", 1.5)

    assert result["action"] == "SELL"


def test_hold_decision():
    engine = DecisionEngine(
        SignalEngine(),
        RegimeDetector()
    )

    signals = {
        "ema": "BUY",
        "macd": "SELL",
        "rsi": "HOLD",
        "market_structure": "BULLISH",
    }

    result = engine.decide(signals, "SIDEWAYS", 1.5)

    assert result["action"] == "HOLD"