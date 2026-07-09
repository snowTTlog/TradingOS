from src.strategies.ema_crossover import EMACrossoverStrategy


def test_ema_crossover():

    prices = list(range(1, 101))

    strategy = EMACrossoverStrategy()

    signal = strategy.generate_signal(prices)

    assert signal in ["BUY", "SELL", "HOLD"]