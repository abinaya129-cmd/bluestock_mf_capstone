import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# -----------------------------------
# Create charts folder
# -----------------------------------

charts_dir = Path("../reports/charts")

charts_dir.mkdir(
    parents=True,
    exist_ok=True
)

# -----------------------------------
# Load datasets
# -----------------------------------

fund = pd.read_csv(
    "../data/raw/01_fund_master.csv"
)

nav = pd.read_csv(
    "../data/processed/clean_nav.csv"
)

aum = pd.read_csv(
    "../data/raw/03_aum_by_fund_house.csv"
)

sip = pd.read_csv(
    "../data/raw/04_monthly_sip_inflows.csv"
)

tx = pd.read_csv(
    "../data/raw/08_investor_transactions.csv"
)

# -----------------------------------
# Chart 1 - NAV Trend
# -----------------------------------

print("Generating NAV Trend...")

sample_code = nav["amfi_code"].iloc[0]

sample = nav[
    nav["amfi_code"] == sample_code
]

plt.figure(figsize=(12,6))

plt.plot(
    pd.to_datetime(sample["date"]),
    sample["nav"]
)

plt.title("NAV Trend")
plt.xlabel("Date")
plt.ylabel("NAV")

plt.tight_layout()

plt.savefig(
    "../reports/charts/nav_trend.png"
)

plt.close()

# -----------------------------------
# Chart 2 - AUM by Fund House
# -----------------------------------

print("Generating AUM Chart...")

plt.figure(figsize=(12,6))

aum.groupby(
    "fund_house"
)["aum_crore"].mean().sort_values(
    ascending=False
).head(10).plot(
    kind="bar"
)

plt.title("Top Fund Houses by AUM")

plt.tight_layout()

plt.savefig(
    "../reports/charts/aum_by_fund_house.png"
)

plt.close()

# -----------------------------------
# Chart 3 - SIP Trend
# -----------------------------------

print("Generating SIP Trend...")

plt.figure(figsize=(12,6))

plt.plot(
    sip["month"],
    sip["sip_inflow_crore"]
)

plt.title("Monthly SIP Inflows")

plt.xticks(rotation=45)

plt.tight_layout()

plt.savefig(
    "../reports/charts/sip_trend.png"
)

plt.close()

# -----------------------------------
# Chart 4 - Age Distribution
# -----------------------------------

print("Generating Age Distribution...")

plt.figure(figsize=(8,8))

tx["age_group"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title(
    "Investor Age Distribution"
)

plt.savefig(
    "../reports/charts/age_distribution.png"
)

plt.close()

# -----------------------------------
# Chart 5 - State Transactions
# -----------------------------------

print("Generating State Chart...")

plt.figure(figsize=(12,6))

tx["state"].value_counts().head(10).plot(
    kind="bar"
)

plt.title(
    "Top States by Transactions"
)

plt.tight_layout()

plt.savefig(
    "../reports/charts/state_transactions.png"
)

plt.close()

# -----------------------------------
# Chart 6 - Fund Categories
# -----------------------------------

print("Generating Category Chart...")

plt.figure(figsize=(10,6))

fund["category"].value_counts().plot(
    kind="bar"
)

plt.title(
    "Fund Categories"
)

plt.tight_layout()

plt.savefig(
    "../reports/charts/category_distribution.png"
)

plt.close()

# -----------------------------------
# Chart 7 - Risk Categories
# -----------------------------------

print("Generating Risk Chart...")

plt.figure(figsize=(10,6))

fund["risk_category"].value_counts().plot(
    kind="bar"
)

plt.title(
    "Risk Category Distribution"
)

plt.tight_layout()

plt.savefig(
    "../reports/charts/risk_categories.png"
)

plt.close()

# -----------------------------------
# Chart 8 - Transaction Types
# -----------------------------------

print("Generating Transaction Type Chart...")

plt.figure(figsize=(8,8))

tx["transaction_type"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.ylabel("")

plt.title(
    "Transaction Type Distribution"
)

plt.savefig(
    "../reports/charts/transaction_types.png"
)

plt.close()

print("\nAll charts generated successfully!")
print("Saved in reports/charts/")