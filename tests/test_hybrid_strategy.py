from src.strategies.hybrid_strategy import HybridStrategy


def test_hybrid_strategy():

    prices = list(range(1, 101))

    strategy = HybridStrategy()

    signal = strategy.generate_signal(prices)

    assert signal in ["BUY", "SELL", "HOLD"]