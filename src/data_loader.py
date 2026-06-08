import pandas as pd


def load_trader_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    print(f"Trader data loaded: {df.shape}")

    return df


def load_sentiment_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path)

    print(f"Sentiment data loaded: {df.shape}")

    return df