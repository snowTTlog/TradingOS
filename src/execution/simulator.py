from src.portfolio.position import Position
from src.portfolio.trade import Trade


class ExecutionSimulator:

    def __init__(self, account):

        self.account = account
        self.position = Position()


    def execute(self, signal, candle):

        # Support dictionary and Candle object
        if isinstance(candle, dict):
            price = candle["close"]

        else:
            price = candle.close


        # Simple risk levels for now
        stop_loss = price * 0.995
        take_profit = price * 1.01


        # Open BUY position
        if signal == "BUY":

            if not self.position.is_open():

                self.position.open(
                    symbol="EURUSD",
                    side="BUY",
                    quantity=1,
                    price=price,
                    stop_loss=stop_loss,
                    take_profit=take_profit
                )

                return "BUY executed"


            return "Already in position"



        # Close position on SELL
        elif signal == "SELL":

            if self.position.is_open():

                trade_data = self.position.close()


                trade = Trade(
                    symbol=trade_data["symbol"],
                    side=trade_data["side"],
                    entry_price=trade_data["entry_price"],
                    quantity=trade_data["quantity"]
                )


                trade.close(price)


                self.account.add_trade(trade)


                return "Trade closed"


            return "No position"



        return "HOLD"