class Position:

    def __init__(self):

        self.symbol = None
        self.side = None
        self.quantity = 0
        self.entry_price = 0
        self.stop_loss = 0
        self.take_profit = 0


    def is_open(self):

        return self.symbol is not None


    def open(
        self,
        symbol,
        side,
        quantity,
        price,
        stop_loss,
        take_profit
    ):

        self.symbol = symbol
        self.side = side
        self.quantity = quantity
        self.entry_price = price
        self.stop_loss = stop_loss
        self.take_profit = take_profit


    def close(self):

        data = {

            "symbol": self.symbol,
            "side": self.side,
            "quantity": self.quantity,
            "entry_price": self.entry_price

        }


        self.symbol = None
        self.side = None
        self.quantity = 0
        self.entry_price = 0
        self.stop_loss = 0
        self.take_profit = 0


        return data