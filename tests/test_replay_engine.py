from src.data.loader import DataLoader
from src.engines.replay_engine import ReplayEngine


def test_replay_engine_streams_data():

    loader = DataLoader(
        "src/data/historical/DAT_ASCII_EURUSD_M1_2025.csv"
    )

    replay = ReplayEngine(loader)

    candles = []

    for i, candle in enumerate(replay.stream()):
        candles.append(candle)

        if i == 4:
            break

    assert len(candles) == 5