from src.indicators.sma import SMA


def test_sma():

    sma = SMA(5)

    prices = [1, 2, 3, 4, 5]

    value = sma.calculate(prices)

    assert value == 3