from src.core.event_bus import EventBus
from src.core.logger import Logger
from src.core.settings import Settings
from src.data.market_data import MarketData
from src.strategies.simple_strategy import SimpleStrategy


def on_system_start(data):
    print(f"📢 Event received: {data}")


def main():
    logger = Logger.setup()
    logger.info("TradingOS Started")

    # Event Bus
    bus = EventBus()
    bus.subscribe("system_start", on_system_start)
    bus.publish("system_start", "TradingOS is now running")

    print("=" * 50)
    print(f"🚀 {Settings.APP_NAME} Starting...")
    print("=" * 50)

    # Market Data
    market = MarketData()
    market.connect()

    # Mock BTCUSDT Data
    market.update_price("BTCUSDT", 100000)

    market.update_candle(
        "BTCUSDT",
        {
            "open": 100,
            "high": 105,
            "low": 99,
            "close": 103,
        },
    )

    # Retrieve Data
    price = market.get_price("BTCUSDT")
    candle = market.get_candle("BTCUSDT")

    print("Current Price:", price)
    print("Current Candle:", candle)

    # Strategy
    strategy = SimpleStrategy()
    signal = strategy.generate_signal(candle)

    print("Strategy Signal:", signal)


if __name__ == "__main__":
    main()