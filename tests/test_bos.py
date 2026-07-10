from src.analysis.bos import BOS


def test_bullish_bos():
    bos = BOS()

    highs = [100, 105]
    lows = [95, 98]

    assert bos.detect(highs, lows) == "BULLISH_BOS"


def test_bearish_bos():
    bos = BOS()

    highs = [105, 103]
    lows = [100, 95]

    assert bos.detect(highs, lows) == "BEARISH_BOS"


def test_no_bos():
    bos = BOS()

    highs = [105, 104]
    lows = [95, 96]

    assert bos.detect(highs, lows) == "NONE"


def test_not_enough_data():
    bos = BOS()

    assert bos.detect([100], [95]) == "NONE"