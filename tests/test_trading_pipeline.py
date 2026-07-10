from src.core.trading_pipeline import TradingPipeline


def test_pipeline_buy():
    pipeline = TradingPipeline()

    prices = [
        100, 101, 102, 103, 104,
        105, 106, 107, 108, 109,
        110, 111, 112, 113, 114,
        115, 116, 117, 118, 119,
        120, 121, 122, 123, 124,
        125, 126, 127, 128, 129,
    ]

    result = pipeline.process(
        prices=prices,
        atr=1.5,
    )

    assert result is not None
    assert "action" in result
    assert "confidence" in result
    assert result["action"] in ("BUY", "SELL", "HOLD")


def test_pipeline_sell():
    pipeline = TradingPipeline()

    prices = [
        129, 128, 127, 126, 125,
        124, 123, 122, 121, 120,
        119, 118, 117, 116, 115,
        114, 113, 112, 111, 110,
        109, 108, 107, 106, 105,
        104, 103, 102, 101, 100,
    ]

    result = pipeline.process(
        prices=prices,
        atr=1.5,
    )

    assert result is not None
    assert "action" in result
    assert "confidence" in result
    assert result["action"] in ("BUY", "SELL", "HOLD")