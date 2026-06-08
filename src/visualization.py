import matplotlib.pyplot as plt
import seaborn as sns


# ============================================================
# CHART 1
# Trade Count by Sentiment
# ============================================================

def plot_trade_count_by_sentiment(df):

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=df,
        x="classification",
        y="trade_count"
    )

    plt.title("Trade Count by Market Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Number of Trades")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/trade_count_by_sentiment.png"
    )

    plt.close()


# ============================================================
# CHART 2
# Average PnL by Sentiment
# ============================================================

def plot_avg_pnl_by_sentiment(df):

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=df,
        x="classification",
        y="avg_pnl"
    )

    plt.title("Average PnL by Market Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Average PnL")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/avg_pnl_by_sentiment.png"
    )

    plt.close()


# ============================================================
# CHART 3
# Win Rate by Sentiment
# ============================================================

def plot_win_rate_by_sentiment(df):

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=df,
        x="classification",
        y="win_rate"
    )

    plt.title("Win Rate by Market Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Win Rate")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/win_rate_by_sentiment.png"
    )

    plt.close()


# ============================================================
# CHART 4
# Total Trading Volume by Sentiment
# ============================================================

def plot_total_volume_by_sentiment(df):

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=df,
        x="classification",
        y="total_volume"
    )

    plt.title("Total Trading Volume by Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Volume (USD)")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/total_volume_by_sentiment.png"
    )

    plt.close()


# ============================================================
# CHART 5
# Average Position Size by Sentiment
# ============================================================

def plot_avg_position_size_by_sentiment(df):

    plt.figure(figsize=(10, 5))

    sns.barplot(
        data=df,
        x="classification",
        y="avg_position_size"
    )

    plt.title("Average Position Size by Sentiment")
    plt.xlabel("Sentiment")
    plt.ylabel("Position Size (USD)")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/avg_position_size_by_sentiment.png"
    )

    plt.close()


# ============================================================
# CHART 6
# Long vs Short Profitability
# ============================================================

def plot_long_short_performance(df):

    plt.figure(figsize=(12, 6))

    sns.barplot(
        data=df,
        x="classification",
        y="avg_pnl",
        hue="Direction"
    )

    plt.title("Long vs Short Profitability")
    plt.xlabel("Sentiment")
    plt.ylabel("Average PnL")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/long_short_performance.png"
    )

    plt.close()


# ============================================================
# CHART 7
# Top vs Bottom Traders Comparison
# ============================================================

def plot_top_vs_bottom_traders(
    top_traders,
    bottom_traders
):

    top_traders = top_traders.copy()
    bottom_traders = bottom_traders.copy()

    top_traders["group"] = "Top Traders"
    bottom_traders["group"] = "Bottom Traders"

    combined = sns.load_dataset("tips").head(0)

    import pandas as pd

    combined = pd.concat(
        [top_traders, bottom_traders],
        ignore_index=True
    )

    plt.figure(figsize=(10, 5))

    sns.boxplot(
        data=combined,
        x="group",
        y="total_pnl"
    )

    plt.title(
        "Top vs Bottom Trader Profitability"
    )

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/top_vs_bottom_traders.png"
    )

    plt.close()


# ============================================================
# CHART 8
# PnL Distribution by Sentiment
# ============================================================

def plot_pnl_distribution_boxplot(df):

    plt.figure(figsize=(12, 6))

    sns.boxplot(
        data=df,
        x="classification",
        y="Closed PnL",
        showfliers=False
    )

    plt.title(
        "PnL Distribution Across Sentiment Regimes"
    )

    plt.xlabel("Sentiment")
    plt.ylabel("Closed PnL")

    plt.tight_layout()

    plt.savefig(
        "outputs/figures/pnl_distribution_boxplot.png"
    )

    plt.close()