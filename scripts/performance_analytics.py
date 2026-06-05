import pandas as pd
import numpy as np

print("="*50)
print("DAY 4 PERFORMANCE ANALYTICS")
print("="*50)

# Load NAV data
nav = pd.read_csv("../data/processed/clean_nav.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# ---------------------------------
# Daily Returns
# ---------------------------------

nav["daily_return"] = (
    nav.groupby("amfi_code")["nav"]
    .pct_change()
)

nav.to_csv(
    "../data/processed/returns_computed.csv",
    index=False
)

print("returns_computed.csv saved")

# ---------------------------------
# Performance Metrics
# ---------------------------------

results = []

for code in nav["amfi_code"].unique():

    df = nav[
        nav["amfi_code"] == code
    ]

    returns = (
        df["daily_return"]
        .dropna()
    )

    if len(returns) < 30:
        continue

    # CAGR

    start_nav = df["nav"].iloc[0]
    end_nav = df["nav"].iloc[-1]

    years = (
        (
            df["date"].max()
            -
            df["date"].min()
        ).days
    ) / 365.25

    if years <= 0:
        continue

    cagr = (
        (end_nav/start_nav)
        ** (1/years)
    ) - 1

    # Sharpe Ratio

    sharpe = (
        returns.mean()
        /
        returns.std()
    ) * np.sqrt(252)

    # Sortino Ratio

    downside = returns[
        returns < 0
    ]

    if len(downside) > 0:

        sortino = (
            returns.mean()
            /
            downside.std()
        ) * np.sqrt(252)

    else:
        sortino = np.nan

    # Maximum Drawdown

    running_max = (
        df["nav"]
        .cummax()
    )

    drawdown = (
        df["nav"]
        /
        running_max
    ) - 1

    max_dd = drawdown.min()

    results.append([
        code,
        round(cagr,4),
        round(sharpe,4),
        round(sortino,4),
        round(max_dd,4)
    ])

# Create metrics dataframe

metrics = pd.DataFrame(
    results,
    columns=[
        "amfi_code",
        "cagr",
        "sharpe_ratio",
        "sortino_ratio",
        "max_drawdown"
    ]
)

metrics.to_csv(
    "../data/processed/performance_metrics.csv",
    index=False
)

print("performance_metrics.csv saved")

# ---------------------------------
# Fund Scorecard
# ---------------------------------

metrics["rank"] = (
    metrics["cagr"]
    .rank(
        ascending=False
    )
)

metrics = metrics.sort_values(
    "rank"
)

metrics.to_csv(
    "../data/processed/fund_scorecard.csv",
    index=False
)

print("fund_scorecard.csv saved")

print("\nDAY 4 COMPLETED")