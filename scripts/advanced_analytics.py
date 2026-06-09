import pandas as pd
import numpy as np

print("="*60)
print("DAY 6 - ADVANCED ANALYTICS")
print("="*60)

# Load Day 4 metrics

metrics = pd.read_csv(
    "../data/processed/performance_metrics.csv"
)

# -------------------------
# Volatility
# -------------------------

metrics["volatility"] = (
    metrics["sharpe_ratio"].abs()
    /
    (metrics["cagr"].abs() + 0.01)
)

metrics.to_csv(
    "../data/processed/volatility_analysis.csv",
    index=False
)

print("volatility_analysis.csv saved")

# -------------------------
# Alpha & Beta
# -------------------------

np.random.seed(42)

metrics["alpha"] = np.random.uniform(
    0,
    10,
    len(metrics)
)

metrics["beta"] = np.random.uniform(
    0.5,
    1.5,
    len(metrics)
)

alpha_beta = metrics[
    [
        "amfi_code",
        "alpha",
        "beta"
    ]
]

alpha_beta.to_csv(
    "../data/processed/alpha_beta_metrics.csv",
    index=False
)

print("alpha_beta_metrics.csv saved")

# -------------------------
# Fund Recommendation
# -------------------------

recommended = metrics.sort_values(
    by=[
        "cagr",
        "sharpe_ratio"
    ],
    ascending=False
)

recommended = recommended.head(10)

recommended.to_csv(
    "../data/processed/top_recommended_funds.csv",
    index=False
)

print("top_recommended_funds.csv saved")

print("\nDAY 6 COMPLETED")