import pandas as pd
import matplotlib.pyplot as plt

funds = pd.read_csv(
    "../data/processed/top_recommended_funds.csv"
)

funds = funds.head(10)

plt.figure(figsize=(10,5))

plt.bar(
    funds["amfi_code"].astype(str),
    funds["cagr"]
)

plt.title(
    "Top Recommended Funds"
)

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "../reports/charts/top_funds_day6.png"
)

print("Chart saved")