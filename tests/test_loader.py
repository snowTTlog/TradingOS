from src.data.loader import DataLoader


def test_loader_reads_candles():

    loader = DataLoader(
        "src/data/historical/DAT_ASCII_EURUSD_M1_2025.csv"
    )

    candles = list(loader.load())

    assert len(candles) > 0
    assert candles[0] is not None