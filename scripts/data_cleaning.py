import pandas as pd
from pathlib import Path

print("=" * 60)
print("DATA CLEANING STARTED")
print("=" * 60)

# Paths
RAW_PATH = Path("../data/raw")
PROCESSED_PATH = Path("../data/processed")

# --------------------------------------------------
# 1. CLEAN NAV HISTORY
# --------------------------------------------------

print("\nCleaning NAV History...")

nav = pd.read_csv(RAW_PATH / "02_nav_history.csv")

# Convert date
nav["date"] = pd.to_datetime(nav["date"])

# Sort
nav = nav.sort_values(
    ["amfi_code", "date"]
)

# Remove duplicates
nav = nav.drop_duplicates()

# Keep valid NAV values
nav = nav[nav["nav"] > 0]

# Save
nav.to_csv(
    PROCESSED_PATH / "clean_nav.csv",
    index=False
)

print("clean_nav.csv saved")

# --------------------------------------------------
# 2. CLEAN TRANSACTIONS
# --------------------------------------------------

print("\nCleaning Transactions...")

tx = pd.read_csv(
    RAW_PATH / "08_investor_transactions.csv"
)

# Standardize transaction type
tx["transaction_type"] = (
    tx["transaction_type"]
    .str.strip()
    .str.title()
)

# Amount should be positive
tx = tx[
    tx["amount_inr"] > 0
]

# Remove duplicates
tx = tx.drop_duplicates()

# Save
tx.to_csv(
    PROCESSED_PATH / "clean_transactions.csv",
    index=False
)

print("clean_transactions.csv saved")

# --------------------------------------------------
# 3. CLEAN PERFORMANCE
# --------------------------------------------------

print("\nCleaning Performance Data...")

perf = pd.read_csv(
    RAW_PATH / "07_scheme_performance.csv"
)

perf = perf.drop_duplicates()

perf.to_csv(
    PROCESSED_PATH / "clean_performance.csv",
    index=False
)

print("clean_performance.csv saved")

# --------------------------------------------------

print("\nDATA CLEANING COMPLETED")