class PositionSizer:

    def __init__(self, risk_manager):

        self.risk_manager = risk_manager


    def calculate_quantity(
        self,
        balance,
        entry_price,
        stop_loss_price
    ):

        risk_amount = (
            self.risk_manager
            .calculate_risk_amount(balance)
        )


        risk_per_unit = abs(
            entry_price - stop_loss_price
        )


        if risk_per_unit == 0:
            return 0


        quantity = (
            risk_amount /
            risk_per_unit
        )


        return quantity