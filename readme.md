# Prime Trade Sentiment Analysis

## Overview

This project analyzes the relationship between **Bitcoin market sentiment** and **trader performance** using historical trading data from Hyperliquid and the Bitcoin Fear & Greed Index.

The objective is to explore how different market sentiment regimes influence:

* Trader profitability
* Trading activity
* Position sizing behavior
* Long vs Short performance
* Risk efficiency

The analysis aims to uncover hidden behavioral patterns and generate actionable insights that can support smarter trading strategies.

---

## Business Objective

The goal of this project is to answer the following questions:

### Q1. How does market sentiment affect trader profitability?

Metrics analyzed:

* Total PnL
* Average PnL
* Median PnL
* Win Rate

### Q2. How does market sentiment affect trading activity?

Metrics analyzed:

* Trade Count
* Total Trading Volume
* Average Position Size

### Q3. Do traders behave differently under different sentiment regimes?

Metrics analyzed:

* Trade Direction
* Position Sizing
* Trading Fees

### Q4. Are top-performing traders different from bottom-performing traders?

Metrics analyzed:

* Total PnL
* Win Rate
* Trading Volume
* Position Size

### Q5. Which performs better: Long or Short positions?

Metrics analyzed:

* Average PnL
* Total PnL
* Trade Count

### Q6. How does risk efficiency vary across sentiment regimes?

Metrics analyzed:

* PnL per Trade
* PnL per Volume
* Fee per Volume

---

## Dataset Information

### 1. Bitcoin Fear & Greed Index

Columns:

* timestamp
* value
* classification
* date

Sentiment Classes:

* Extreme Fear
* Fear
* Neutral
* Greed
* Extreme Greed

---

### 2. Hyperliquid Historical Trader Data

Columns:

* Account
* Coin
* Execution Price
* Size Tokens
* Size USD
* Side
* Timestamp IST
* Start Position
* Direction
* Closed PnL
* Transaction Hash
* Order ID
* Crossed
* Fee
* Trade ID
* Timestamp

---

## Project Structure

```text
prime-trade-sentiment-analysis/
│
├── data/
│   ├── historical_data.csv
│   └── fear_greed_index.csv
│
├── outputs/
│   ├── figures/
│   └── tables/
│
├── src/
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── sentiment_analysis.py
│   ├── trader_analysis.py
│   └── visualization.py
│
├── main.py
├── requirements.txt
├── README.md
└── .gitignore
```

---

## Methodology

### Step 1: Data Loading

* Load historical trader dataset
* Load Fear & Greed Index dataset

### Step 2: Data Preprocessing

* Convert timestamps to datetime format
* Clean numerical columns
* Create common date key
* Handle missing values

### Step 3: Data Integration

Merge trading data with daily market sentiment data using trading date.

Merge Success Rate:

* Total Trades: 211,224
* Missing Sentiment Records: 6
* Match Rate: 99.997%

### Step 4: Sentiment-Based Analysis

Analyze profitability, behavior, activity, and risk metrics under different sentiment regimes.

---

# Key Visualizations

## Trade Count by Market Sentiment

Shows how trading activity varies across sentiment regimes.

**File:** `outputs/figures/trade_count_by_sentiment.png`

---

## Average PnL by Market Sentiment

Compares profitability across sentiment regimes.

**File:** `outputs/figures/avg_pnl_by_sentiment.png`

---

## Win Rate by Market Sentiment

Measures trading success rate under different market conditions.

**File:** `outputs/figures/win_rate_by_sentiment.png`

---

## Total Trading Volume by Sentiment

Analyzes capital deployment behavior.

**File:** `outputs/figures/total_volume_by_sentiment.png`

---

## Average Position Size by Sentiment

Examines risk appetite and trade sizing behavior.

**File:** `outputs/figures/avg_position_size_by_sentiment.png`

---

## Long vs Short Performance

Compares profitability of directional trading strategies.

**File:** `outputs/figures/long_short_performance.png`

---

## Top vs Bottom Trader Comparison

Highlights behavioral differences between successful and unsuccessful traders.

**File:** `outputs/figures/top_vs_bottom_traders.png`

---

## PnL Distribution by Sentiment

Visualizes the distribution of realized profits and losses.

**File:** `outputs/figures/pnl_distribution_boxplot.png`

---

# Key Findings

## Finding 1

Extreme Greed generated the highest average profit per trade.

| Sentiment     | Average PnL |
| ------------- | ----------: |
| Extreme Greed |       67.89 |
| Fear          |       54.29 |
| Greed         |       42.74 |
| Extreme Fear  |       34.54 |
| Neutral       |       34.31 |

### Interpretation

Strong bullish sentiment appears to create favorable conditions for profitable trades.

---

## Finding 2

Fear periods generated the highest aggregate profits.

### Observation

Fear periods contained the largest number of trades:

* Fear: 61,837 trades
* Greed: 50,303 trades
* Extreme Greed: 39,992 trades

### Interpretation

Higher trading activity during Fear periods contributed to larger overall realized profits.

---

## Finding 3

Extreme Greed achieved the highest win rate.

| Sentiment     | Win Rate |
| ------------- | -------: |
| Extreme Greed |   46.49% |
| Fear          |   42.08% |
| Neutral       |   39.70% |
| Greed         |   38.48% |
| Extreme Fear  |   37.06% |

### Interpretation

Traders were more successful during strong bullish sentiment environments.

---

## Finding 4

Fear periods produced the largest average position sizes.

### Interpretation

Traders were willing to deploy larger amounts of capital during Fear periods, potentially reflecting higher conviction opportunities.

---

## Finding 5

Most trades generated little or no realized profit.

### Evidence

Median PnL = 0 across all sentiment regimes.

### Interpretation

Overall profitability was driven by a relatively small number of highly profitable trades rather than consistent gains across all trades.

This was the most important hidden pattern discovered in the analysis.

---

# Trading Strategy Recommendations

## Recommendation 1

Monitor sentiment regimes before increasing market exposure.

Historical results suggest that Extreme Greed periods delivered the highest average profitability and win rates.

---

## Recommendation 2

Focus on risk-adjusted returns rather than trade frequency.

Higher trading activity did not always translate into better trading efficiency.

---

## Recommendation 3

Prioritize position-sizing discipline.

Large position sizes alone were not sufficient to guarantee profitability.

---

## Recommendation 4

Identify and preserve high-conviction trading opportunities.

The results suggest that a small number of highly profitable trades drive the majority of overall gains.

---

# Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* SciPy
* Jupyter Notebook

---

# How to Run

## Clone Repository

```bash
git clone <repository-url>
cd prime-trade-sentiment-analysis
```

## Install Dependencies

```bash
pip install -r requirements.txt
```

## Execute Analysis

```bash
python main.py
```

Generated outputs will be available in:

```text
outputs/
├── figures/
└── tables/
```

---

# Conclusion

This project demonstrates that market sentiment has a measurable relationship with trader performance, trading activity, and capital allocation behavior.

The analysis reveals that Extreme Greed periods produced the strongest average trading outcomes, while Fear periods generated the highest aggregate profits due to increased participation. Additionally, profitability was heavily concentrated in a small subset of trades, highlighting the importance of identifying and managing high-conviction opportunities rather than maximizing trade frequency.
