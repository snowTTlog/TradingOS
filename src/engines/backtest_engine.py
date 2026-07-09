from src.data.loader import DataLoader
from src.engines.replay_engine import ReplayEngine
from src.strategies.simple_strategy import SimpleStrategy
from src.execution.simulator import ExecutionSimulator
from src.portfolio.account import Account


class BacktestEngine:

    def __init__(self, data_path):

        self.loader = DataLoader(data_path)

        self.replay = ReplayEngine(
            self.loader
        )

        self.strategy = SimpleStrategy()

        self.account = Account(10000)

        self.execution = ExecutionSimulator(
            self.account
        )


    def run(self):

        for candle in self.replay.stream():

            signal = self.strategy.generate_signal(
                candle
            )

            result = self.execution.execute(
                signal,
                candle
            )

            print(
                candle,
                signal,
                result
            )


        return self.account