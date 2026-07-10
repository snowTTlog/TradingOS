from src.analysis.choch import CHoCH


def test_bullish_choch():
    choch = CHoCH()

    assert choch.detect(
        "DOWNTREND",
        "UPTREND"
    ) == "BULLISH_CHOCH"


def test_bearish_choch():
    choch = CHoCH()

    assert choch.detect(
        "UPTREND",
        "DOWNTREND"
    ) == "BEARISH_CHOCH"


def test_no_change():
    choch = CHoCH()

    assert choch.detect(
        "UPTREND",
        "UPTREND"
    ) == "NONE"


def test_sideways():
    choch = CHoCH()

    assert choch.detect(
        "SIDEWAYS",
        "SIDEWAYS"
    ) == "NONE"