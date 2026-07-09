from src.strategies.simple_strategy import SimpleStrategy


def test_simple_strategy():

    strategy = SimpleStrategy()

    candle = {
        "open": 100,
        "close": 105
    }

    signal = strategy.generate_signal(candle)

    assert signal == "BUY"