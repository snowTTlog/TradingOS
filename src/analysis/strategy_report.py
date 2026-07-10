class StrategyReport:

    def __init__(self, name, balance):

        self.name = name
        self.balance = balance

    def summary(self):

        return {
            "strategy": self.name,
            "balance": self.balance
        }