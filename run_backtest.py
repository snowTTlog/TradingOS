from src.engines.backtest_engine import BacktestEngine


def main():

    print("=" * 50)
    print("🚀 TradingOS Backtest Started")
    print("=" * 50)


    engine = BacktestEngine(
        "src/data/historical/DAT_ASCII_EURUSD_M1_2025.csv"
    )


    account = engine.run()


    print("=" * 50)
    print("✅ Backtest Finished")
    print("=" * 50)


if __name__ == "__main__":
    main()