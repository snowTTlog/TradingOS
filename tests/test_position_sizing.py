from src.risk.risk_manager import RiskManager
from src.risk.position_sizing import PositionSizer


def test_position_size():

    risk = RiskManager(1)

    sizing = PositionSizer(risk)


    quantity = sizing.calculate_quantity(
        balance=10000,
        entry_price=100,
        stop_loss_price=99
    )


    assert quantity == 100