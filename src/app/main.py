from src.core.event_bus import EventBus
from src.core.logger import Logger
from src.core.settings import Settings
from src.data.market_data import MarketData
from src.strategies.simple_strategy import SimpleStrategy


def on_system_start(data):
    print(f"Event received: {data}")


def main():
    logger = Logger.setup()
    logger.info("TradingOS Started")

    bus = EventBus()
    bus.subscribe("system_start", on_system_start)
    bus.publish("system_start", "TradingOS is now running")

    print("=" * 50)
    print(f"{Settings.APP_NAME} Starting...")
    print("=" * 50)

    market = MarketData()
    market.connect()

    candle = market.get_candle()

    print("Current Price:", market.get_price())
    print("Current Candle:", candle)

    strategy = SimpleStrategy()
    signal = strategy.generate_signal(candle)

    print("Strategy Signal:", signal)


if __name__ == "__main__":
    main()
