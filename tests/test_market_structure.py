from src.analysis.market_structure import MarketStructure


def test_uptrend():

    ms = MarketStructure()

    prices = [1, 2, 3, 4, 5]

    assert ms.trend(prices) == "UPTREND"


def test_downtrend():

    ms = MarketStructure()

    prices = [5, 4, 3, 2, 1]

    assert ms.trend(prices) == "DOWNTREND"


def test_sideways():

    ms = MarketStructure()

    prices = [5, 5, 5, 5]

    assert ms.trend(prices) == "SIDEWAYS"


def test_higher_high():

    ms = MarketStructure()

    highs = [10, 12]

    assert ms.higher_high(highs)


def test_lower_low():

    ms = MarketStructure()

    lows = [10, 8]

    assert ms.lower_low(lows)