from datetime import datetime


class Trade:

    def __init__(
        self,
        symbol,
        side,
        entry_price,
        quantity
    ):

        self.symbol = symbol
        self.side = side

        self.entry_price = entry_price
        self.exit_price = None

        self.quantity = quantity

        self.entry_time = datetime.now()
        self.exit_time = None

        self.exit_reason = None

        self.pnl = 0

        self.status = "OPEN"



    def close(
        self,
        exit_price,
        reason="SIGNAL"
    ):

        self.exit_price = exit_price

        self.exit_time = datetime.now()

        self.exit_reason = reason


        if self.side == "BUY":

            self.pnl = (
                exit_price -
                self.entry_price
            ) * self.quantity


        elif self.side == "SELL":

            self.pnl = (
                self.entry_price -
                exit_price
            ) * self.quantity


        self.status = "CLOSED"


        return self.pnl