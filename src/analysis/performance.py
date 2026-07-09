class PerformanceAnalyzer:

    def __init__(self, account):

        self.account = account


    def report(self):

        total_trades = len(
            self.account.trades
        )

        total_profit = 0

        winning_trades = 0

        losing_trades = 0


        for trade in self.account.trades:

            total_profit += trade.pnl


            if trade.pnl > 0:
                winning_trades += 1


            elif trade.pnl < 0:
                losing_trades += 1


        win_rate = 0


        if total_trades > 0:

            win_rate = (
                winning_trades /
                total_trades
            ) * 100


        return {

            "starting_balance":
                self.account.starting_balance,


            "final_balance":
                self.account.balance,


            "total_trades":
                total_trades,


            "winning_trades":
                winning_trades,


            "losing_trades":
                losing_trades,


            "win_rate":
                round(win_rate, 2),


            "profit_loss":
                round(total_profit, 2),


            "max_drawdown":
                round(
                    self.account.get_drawdown(),
                    2
                )
        }