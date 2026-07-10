from src.intelligence import SignalEngine


def test_buy_signal():
    engine = SignalEngine()

    signals = {
        "ema": "BUY",
        "macd": "BUY",
        "rsi": "BUY",
        "market_structure": "BULLISH",
        "regime": "TRENDING_UP",
    }

    result = engine.analyze(signals)

    assert result["action"] == "BUY"
    assert result["confidence"] == 100


def test_sell_signal():
    engine = SignalEngine()

    signals = {
        "ema": "SELL",
        "macd": "SELL",
        "rsi": "SELL",
        "market_structure": "BEARISH",
        "regime": "TRENDING_DOWN",
    }

    result = engine.analyze(signals)

    assert result["action"] == "SELL"
    assert result["confidence"] == -100


def test_hold_signal():
    engine = SignalEngine()

    signals = {
        "ema": "BUY",
        "macd": "SELL",
        "rsi": "HOLD",
        "market_structure": "BULLISH",
        "regime": "TRENDING_DOWN",
    }

    result = engine.analyze(signals)

    assert result["action"] == "HOLD"


def test_empty_signals():
    engine = SignalEngine()

    result = engine.analyze({})

    assert result["action"] == "HOLD"
    assert result["confidence"] == 0