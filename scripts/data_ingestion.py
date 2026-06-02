import pandas as pd
from pathlib import Path

# Data folder path
DATA_PATH = Path("../data/raw")

# Dataset list
files = [
    "01_fund_master.csv",
    "02_nav_history.csv",
    "03_aum_by_fund_house.csv",
    "04_monthly_sip_inflows.csv",
    "05_category_inflows.csv",
    "06_industry_folio_count.csv",
    "07_scheme_performance.csv",
    "08_investor_transactions.csv",
    "09_portfolio_holdings.csv",
    "10_benchmark_indices.csv"
]

print("=" * 70)
print("DATA INGESTION STARTED")
print("=" * 70)


for file in files:
    print("\n" + "=" * 70)
    print(f"Dataset: {file}")

    df = pd.read_csv(DATA_PATH / file)

    print("\nShape:")
    print(df.shape)

    print("\nData Types:")
    print(df.dtypes)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

print("\n\nAll datasets loaded successfully.")



print("\n" + "=" * 70)
print("FUND MASTER ANALYSIS")
print("=" * 70)

fund_master = pd.read_csv(DATA_PATH / "01_fund_master.csv")

print("\nUnique Fund Houses:")
print(fund_master["fund_house"].unique())

print("\nUnique Categories:")
print(fund_master["category"].unique())

print("\nUnique Sub Categories:")
print(fund_master["sub_category"].unique())

print("\nUnique Risk Categories:")
print(fund_master["risk_category"].unique())



print("\n" + "=" * 70)
print("AMFI CODE VALIDATION")
print("=" * 70)

nav_history = pd.read_csv(DATA_PATH / "02_nav_history.csv")

master_codes = set(fund_master["amfi_code"])
nav_codes = set(nav_history["amfi_code"])

missing_codes = master_codes - nav_codes

print("\nTotal Fund Master Codes:", len(master_codes))
print("Total NAV History Codes:", len(nav_codes))

if len(missing_codes) == 0:
    print("\n✅ All AMFI codes are present in nav_history.")
    print("✅ Referential integrity validated successfully.")
else:
    print("\n❌ Missing AMFI Codes:")
    print(missing_codes)



print("\n" + "=" * 70)
print("DATA QUALITY SUMMARY")
print("=" * 70)

print("""
1. All datasets loaded successfully.
2. Dataset structures verified using shape, dtypes and head().
3. Fund house, category, sub-category and risk category values explored.
4. AMFI scheme code validation completed.
5. Referential integrity between fund_master and nav_history checked.
6. Any missing values displayed above for further investigation.
""")

print("\nDAY 1 TASKS COMPLETED SUCCESSFULLY.")