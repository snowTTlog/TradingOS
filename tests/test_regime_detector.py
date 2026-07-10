from src.intelligence import RegimeDetector


def test_trending_up():
    detector = RegimeDetector()
    assert detector.detect("UP", 1.0) == "TRENDING_UP"


def test_trending_down():
    detector = RegimeDetector()
    assert detector.detect("DOWN", 1.0) == "TRENDING_DOWN"


def test_high_volatility():
    detector = RegimeDetector()
    assert detector.detect("SIDEWAYS", 3.0) == "HIGH_VOLATILITY"


def test_ranging():
    detector = RegimeDetector()
    assert detector.detect("SIDEWAYS", 1.0) == "RANGING"