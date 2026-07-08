class MarketData:

    def __init__(self):
        self.connected = False

    def connect(self):
        self.connected = True
        print("Market Data Connected")

    def disconnect(self):
        self.connected = False
        print("Market Data Disconnected")

    def get_price(self):
        return 100000

    def get_candle(self):
        return {
            "open": 100,
            "high": 105,
            "low": 99,
            "close": 103,
        }
