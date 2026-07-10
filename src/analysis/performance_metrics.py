class PerformanceMetrics:

    def __init__(self, trades):
        self.trades = trades

    def total_trades(self):
        return len(self.trades)

    def winning_trades(self):
        return len([t for t in self.trades if t > 0])

    def losing_trades(self):
        return len([t for t in self.trades if t < 0])

    def win_rate(self):
        if not self.trades:
            return 0

        return round(
            self.winning_trades() / self.total_trades() * 100,
            2,
        )

    def net_profit(self):
        return sum(self.trades)

    def average_profit(self):
        profits = [t for t in self.trades if t > 0]

        if not profits:
            return 0

        return round(sum(profits) / len(profits), 2)

    def average_loss(self):
        losses = [t for t in self.trades if t < 0]

        if not losses:
            return 0

        return round(sum(losses) / len(losses), 2)