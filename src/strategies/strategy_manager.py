class StrategyManager:

    def __init__(self):
        self._strategies = {}

    def register(self, name, strategy):
        self._strategies[name] = strategy

    def get(self, name):
        return self._strategies.get(name)

    def list_strategies(self):
        return list(self._strategies.keys())