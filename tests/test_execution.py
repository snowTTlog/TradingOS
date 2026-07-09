from src.portfolio.account import Account
from src.execution.simulator import ExecutionSimulator


def test_buy_execution():

    account = Account(10000)

    simulator = ExecutionSimulator(account)

    candle = {
        "close": 1.1000
    }

    result = simulator.execute(
        "BUY",
        candle
    )

    assert result == "BUY executed"

    assert simulator.position.side == "BUY"