from src.indicators.rsi import RSI


def test_rsi():

    prices = [
        44, 44.15, 43.9, 44.35, 44.8,
        45.1, 44.9, 45.3, 45.7, 45.5,
        45.8, 46.2, 46.1, 46.5, 46.8
    ]

    rsi = RSI()

    value = rsi.calculate(prices)

    assert value is not None
    assert 0 <= value <= 100