from src.strategies.strategy_manager import StrategyManager
from src.strategies.ema_crossover import EMACrossoverStrategy


def test_strategy_manager():

    manager = StrategyManager()

    strategy = EMACrossoverStrategy()

    manager.register("ema", strategy)

    assert manager.get("ema") == strategy

    assert "ema" in manager.list_strategies()