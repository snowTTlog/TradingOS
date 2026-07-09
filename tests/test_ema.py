from src.indicators.ema import EMA


def test_ema():

    ema = EMA(5)

    prices = [1, 2, 3, 4, 5, 6]

    value = ema.calculate(prices)

    assert value is not None
    assert value > 3