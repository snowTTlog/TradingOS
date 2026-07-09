from src.engines.backtest_engine import BacktestEngine


def test_backtest_engine_runs():

    engine = BacktestEngine(
        "src/data/historical/DAT_ASCII_EURUSD_M1_2025.csv"
    )

    account = engine.run()

    assert account.balance >= 10000