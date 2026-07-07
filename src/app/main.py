from src.core.settings import Settings
from src.core.logger import Logger
from src.core.event_bus import EventBus


def on_system_start(data):
    print(f"📢 Event Received: {data}")


def main():
    
    print("STEP 1")

    logger = Logger.setup()
    print("STEP 2")

    logger.info("TradingOS Started")

    bus = EventBus()
    print("STEP 3")

    bus.subscribe("system_start", on_system_start)
    print("STEP 4")

    bus.publish("system_start", "TradingOS is now running")
    print("STEP 5")

    print("=" * 50)
    print(f"🚀 {Settings.APP_NAME} Starting...")
    print("=" * 50)


if __name__ == "__main__":
    main()