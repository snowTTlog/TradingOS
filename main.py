from src.core.config import Config


def main():
    print("=" * 50)
    print("TradingOS Starting...")
    print("=" * 50)

    config = Config()

    print("Mode:", config.get("mode"))
    print("Symbol:", config.get("symbol"))
    print("Timeframe:", config.get("timeframe"))


if __name__ == "__main__":
    main()
