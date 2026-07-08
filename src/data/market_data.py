class MarketData:

    def __init__(self):
        self.connected = False
        self.last_price = {}
        self.last_candle = {}

    def connect(self):
        self.connected = True
        print("✅ Market Data Connected")

    def disconnect(self):
        self.connected = False
        print("❌ Market Data Disconnected")

    def update_price(self, symbol, price):
        self.last_price[symbol] = price

    def get_price(self, symbol):
        return self.last_price.get(symbol)

    def update_candle(self, symbol, candle):
        self.last_candle[symbol] = candle

    def get_candle(self, symbol):
        return self.last_candle.get(symbol)