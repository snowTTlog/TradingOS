class Account:

    def __init__(self, balance=10000):

        self.starting_balance = balance

        self.balance = balance

        self.equity = balance

        self.trades = []

        self.equity_history = [
            balance
        ]


    def add_trade(self, trade):

        self.trades.append(trade)

        self.balance += trade.pnl

        self.equity = self.balance

        self.equity_history.append(
            self.equity
        )


    def get_drawdown(self):

        peak = self.starting_balance

        max_drawdown = 0


        for value in self.equity_history:

            if value > peak:
                peak = value


            drawdown = (
                (peak - value)
                / peak
            ) * 100


            if drawdown > max_drawdown:
                max_drawdown = drawdown


        return max_drawdown