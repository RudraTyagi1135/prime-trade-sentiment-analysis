import pandas as pd


# ============================================================
# QUESTION 1
# How does market sentiment affect trader profitability?
# ============================================================

def profitability_by_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate profitability metrics across sentiment regimes.

    Metrics:
    - Total PnL
    - Average PnL
    - Median PnL
    - Win Rate
    """

    temp = df.copy()

    temp["win"] = (
        temp["Closed PnL"] > 0
    ).astype(int)

    return (
        temp.groupby("classification")
        .agg(
            total_pnl=("Closed PnL", "sum"),
            avg_pnl=("Closed PnL", "mean"),
            median_pnl=("Closed PnL", "median"),
            win_rate=("win", "mean"),
            trades=("Trade ID", "count")
        )
        .reset_index()
    )


# ============================================================
# QUESTION 2
# How does market sentiment affect trading activity?
# ============================================================

def trading_activity_by_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze trader activity under different
    sentiment conditions.
    """

    return (
        df.groupby("classification")
        .agg(
            trade_count=("Trade ID", "count"),
            total_volume=("Size USD", "sum"),
            avg_position_size=("Size USD", "mean")
        )
        .reset_index()
    )


# ============================================================
# QUESTION 3
# Do traders behave differently?
# ============================================================

def trader_behavior_by_sentiment(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze behavioral changes under
    different sentiment regimes.
    """

    return (
        df.groupby(
            ["classification", "Direction"]
        )
        .agg(
            trades=("Trade ID", "count"),
            total_volume=("Size USD", "sum"),
            avg_fee=("Fee", "mean"),
            avg_position_size=("Size USD", "mean")
        )
        .reset_index()
    )


# ============================================================
# QUESTION 5
# Long vs Short Performance
# ============================================================

def long_short_performance(df: pd.DataFrame) -> pd.DataFrame:
    """
    Compare profitability of long and short
    trades across sentiment regimes.
    """

    return (
        df.groupby(
            ["classification", "Direction"]
        )
        .agg(
            total_pnl=("Closed PnL", "sum"),
            avg_pnl=("Closed PnL", "mean"),
            trades=("Trade ID", "count")
        )
        .reset_index()
    )


# ============================================================
# QUESTION 6
# Risk Analysis
# ============================================================

def risk_analysis(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analyze trading efficiency and risk.
    """

    result = (
        df.groupby("classification")
        .agg(
            total_pnl=("Closed PnL", "sum"),
            total_volume=("Size USD", "sum"),
            total_fee=("Fee", "sum"),
            trades=("Trade ID", "count")
        )
        .reset_index()
    )

    result["pnl_per_trade"] = (
        result["total_pnl"] / result["trades"]
    )

    result["pnl_per_volume"] = (
        result["total_pnl"] / result["total_volume"]
    )

    result["fee_per_volume"] = (
        result["total_fee"] / result["total_volume"]
    )

    return result