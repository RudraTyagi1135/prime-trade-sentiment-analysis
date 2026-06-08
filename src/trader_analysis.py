import pandas as pd


# ============================================================
# Trader Summary
# ============================================================

def trader_summary(df: pd.DataFrame) -> pd.DataFrame:

    temp = df.copy()

    temp["win"] = (
        temp["Closed PnL"] > 0
    ).astype(int)

    return (
        temp.groupby("Account")
        .agg(
            total_pnl=("Closed PnL", "sum"),
            total_volume=("Size USD", "sum"),
            trades=("Trade ID", "count"),
            avg_position_size=("Size USD", "mean"),
            win_rate=("win", "mean")
        )
        .reset_index()
    )


# ============================================================
# Top vs Bottom Traders
# ============================================================

def top_bottom_traders(df: pd.DataFrame):

    summary = trader_summary(df)

    summary = summary.sort_values(
        "total_pnl",
        ascending=False
    )

    n = max(
        int(len(summary) * 0.20),
        1
    )

    top_traders = summary.head(n)

    bottom_traders = summary.tail(n)

    return top_traders, bottom_traders


# ============================================================
# Performance By Sentiment
# ============================================================

def trader_performance_by_sentiment(
    df: pd.DataFrame
) -> pd.DataFrame:

    return (
        df.groupby(
            ["Account", "classification"]
        )
        .agg(
            total_pnl=("Closed PnL", "sum"),
            total_volume=("Size USD", "sum"),
            trades=("Trade ID", "count")
        )
        .reset_index()
    )