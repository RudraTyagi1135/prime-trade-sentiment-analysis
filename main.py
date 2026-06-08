from pathlib import Path

from src.data_loader import *
from src.preprocessing import *
from src.sentiment_analysis import *
from src.trader_analysis import *
from src.visualization import *

def main():


    print("=" * 60)
    print("PRIME TRADE SENTIMENT ANALYSIS")
    print("=" * 60)

# ============================================================
# Create output folders
# ============================================================

Path("outputs").mkdir(exist_ok=True)

Path("outputs/figures").mkdir(
    parents=True,
    exist_ok=True
)

Path("outputs/tables").mkdir(
    parents=True,
    exist_ok=True
)

# ============================================================
# Load datasets
# ============================================================

trader_df = load_trader_data(
    "data/historical_data.csv"
)

sentiment_df = load_sentiment_data(
    "data/fear_greed_index.csv"
)

# ============================================================
# Preprocess datasets
# ============================================================

trader_df = preprocess_trader_data(
    trader_df
)

sentiment_df = preprocess_sentiment_data(
    sentiment_df
)

# ============================================================
# Merge datasets
# ============================================================

merged_df = merge_datasets(
    trader_df,
    sentiment_df
)

print(
    f"\nMerged Dataset Shape: {merged_df.shape}"
)

# ============================================================
# Question 1
# Profitability Analysis
# ============================================================

profitability_df = (
    profitability_by_sentiment(
        merged_df
    )
)

profitability_df.to_csv(
    "outputs/tables/profitability_analysis.csv",
    index=False
)

# ============================================================
# Question 2
# Trading Activity Analysis
# ============================================================

activity_df = (
    trading_activity_by_sentiment(
        merged_df
    )
)

activity_df.to_csv(
    "outputs/tables/trading_activity_analysis.csv",
    index=False
)

# ============================================================
# Question 3
# Trader Behavior Analysis
# ============================================================

behavior_df = (
    trader_behavior_by_sentiment(
        merged_df
    )
)

behavior_df.to_csv(
    "outputs/tables/trader_behavior_analysis.csv",
    index=False
)

# ============================================================
# Question 5
# Long vs Short Analysis
# ============================================================

long_short_df = (
    long_short_performance(
        merged_df
    )
)

long_short_df.to_csv(
    "outputs/tables/long_short_analysis.csv",
    index=False
)

# ============================================================
# Question 6
# Risk Analysis
# ============================================================

risk_df = risk_analysis(
    merged_df
)

risk_df.to_csv(
    "outputs/tables/risk_analysis.csv",
    index=False
)

# ============================================================
# Question 4
# Top vs Bottom Traders
# ============================================================

top_traders_df, bottom_traders_df = (
    top_bottom_traders(
        merged_df
    )
)

top_traders_df.to_csv(
    "outputs/tables/top_traders.csv",
    index=False
)

bottom_traders_df.to_csv(
    "outputs/tables/bottom_traders.csv",
    index=False
)

# ============================================================
# Generate Charts
# ============================================================

plot_trade_count_by_sentiment(
    activity_df
)

plot_avg_pnl_by_sentiment(
    profitability_df
)

plot_win_rate_by_sentiment(
    profitability_df
)

plot_total_volume_by_sentiment(
    activity_df
)

plot_avg_position_size_by_sentiment(
    activity_df
)

plot_long_short_performance(
    long_short_df
)

plot_top_vs_bottom_traders(
    top_traders_df,
    bottom_traders_df
)

plot_pnl_distribution_boxplot(
    merged_df
)

print("\nAnalysis Complete")
print(
    "Charts saved to outputs/figures/"
)
print(
    "Tables saved to outputs/tables/"
)


if __name__ == "__main__":
     main()
