class RiskManager:

    def __init__(
        self,
        risk_percent=1
    ):

        self.risk_percent = risk_percent


    def calculate_risk_amount(
        self,
        balance
    ):

        return (
            balance *
            self.risk_percent /
            100
        )


    def can_trade(
        self,
        balance
    ):

        risk_amount = self.calculate_risk_amount(
            balance
        )

        return risk_amount > 0
    