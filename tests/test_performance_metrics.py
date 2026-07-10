from src.analysis.performance_metrics import PerformanceMetrics


def test_total_trades():
    metrics = PerformanceMetrics([100, -50, 200])

    assert metrics.total_trades() == 3


def test_winning_trades():
    metrics = PerformanceMetrics([100, -50, 200])

    assert metrics.winning_trades() == 2


def test_losing_trades():
    metrics = PerformanceMetrics([100, -50, 200])

    assert metrics.losing_trades() == 1


def test_win_rate():
    metrics = PerformanceMetrics([100, -50, 200])

    assert metrics.win_rate() == 66.67


def test_net_profit():
    metrics = PerformanceMetrics([100, -50, 200])

    assert metrics.net_profit() == 250


def test_average_profit():
    metrics = PerformanceMetrics([100, -50, 200])

    assert metrics.average_profit() == 150


def test_average_loss():
    metrics = PerformanceMetrics([100, -50, 200])

    assert metrics.average_loss() == -50