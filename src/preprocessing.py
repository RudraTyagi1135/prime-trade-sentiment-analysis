import pandas as pd


def preprocess_trader_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    # Convert timestamp
    df["Timestamp IST"] = pd.to_datetime(
        df["Timestamp IST"],
        format="%d-%m-%Y %H:%M",
        errors="coerce"
    )

    # Create merge key
    df["trade_date"] = df["Timestamp IST"].dt.date

    # Numeric columns
    numeric_cols = [
        "Execution Price",
        "Size Tokens",
        "Size USD",
        "Start Position",
        "Closed PnL",
        "Fee"
    ]

    for col in numeric_cols:
        df[col] = pd.to_numeric(
            df[col],
            errors="coerce"
        )

    return df


def preprocess_sentiment_data(df: pd.DataFrame) -> pd.DataFrame:

    df = df.copy()

    df["date"] = pd.to_datetime(
        df["date"]
    )

    df["trade_date"] = df["date"].dt.date

    df["value"] = pd.to_numeric(
        df["value"],
        errors="coerce"
    )

    return df


def merge_datasets(
    trader_df: pd.DataFrame,
    sentiment_df: pd.DataFrame
) -> pd.DataFrame:

    merged_df = trader_df.merge(
        sentiment_df[
            [
                "trade_date",
                "value",
                "classification"
            ]
        ],
        on="trade_date",
        how="left"
    )

    print(f"Merged data shape: {merged_df.shape}")

    return merged_df