from src.intelligence.confidence import ConfidenceScore


class SignalEngine:
    def __init__(self):
        self.confidence = ConfidenceScore()

        self.weights = {
            "ema": 20,
            "macd": 20,
            "rsi": 10,
            "market_structure": 30,
            "regime": 20,
        }

    def analyze(self, signals):
        self.confidence.reset()

        for name, signal in signals.items():

            weight = self.weights.get(name, 0)

            if signal in ("BUY", "BULLISH", "TRENDING_UP"):
                self.confidence.add(weight)

            elif signal in ("SELL", "BEARISH", "TRENDING_DOWN"):
                self.confidence.add(-weight)

        score = self.confidence.get_score()

        if score >= 60:
            action = "BUY"
        elif score <= -60:
            action = "SELL"
        else:
            action = "HOLD"

        return {
            "action": action,
            "confidence": score,
        }