from src.analysis.liquidity import Liquidity


def test_buy_side_liquidity():
    detector = Liquidity()

    highs = [100, 105, 105]
    lows = [95, 96, 97]

    assert detector.detect(highs, lows) == "BUY_SIDE_LIQUIDITY"


def test_sell_side_liquidity():
    detector = Liquidity()

    highs = [100, 101, 102]
    lows = [95, 90, 90]

    assert detector.detect(highs, lows) == "SELL_SIDE_LIQUIDITY"


def test_no_liquidity():
    detector = Liquidity()

    highs = [100, 101, 103]
    lows = [95, 94, 93]

    assert detector.detect(highs, lows) == "NONE"


def test_not_enough_data():
    detector = Liquidity()

    assert detector.detect([100], [95]) == "NONE"