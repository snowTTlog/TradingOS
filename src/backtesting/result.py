class BacktestResult:

    def __init__(self, account, strategy_name):

        self.strategy_name = strategy_name

        self.starting_balance = (
            account.starting_balance
        )

        self.final_balance = (
            account.balance
        )

        self.total_trades = (
            len(account.trades)
        )

        self.profit_loss = (
            account.balance -
            account.starting_balance
        )


        self.win_rate = self.calculate_win_rate(
            account
        )


        self.max_drawdown = (
            account.get_drawdown()
        )


    def calculate_win_rate(self, account):

        if len(account.trades) == 0:
            return 0


        wins = 0

        for trade in account.trades:

            if trade.pnl > 0:
                wins += 1


        return (
            wins /
            len(account.trades)
        ) * 100



    def summary(self):

        return {

            "strategy":
                self.strategy_name,

            "starting_balance":
                self.starting_balance,

            "final_balance":
                self.final_balance,

            "trades":
                self.total_trades,

            "profit_loss":
                self.profit_loss,

            "win_rate":
                round(self.win_rate,2),

            "drawdown":
                round(self.max_drawdown,2)
        }