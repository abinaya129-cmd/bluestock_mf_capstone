import pandas as pd
from sqlalchemy import create_engine

print("Loading data into SQLite...")

# Database
engine = create_engine("sqlite:///../data/bluestock_mf.db")

# Read datasets
fund = pd.read_csv("../data/raw/01_fund_master.csv")
nav = pd.read_csv("../data/processed/clean_nav.csv")
tx = pd.read_csv("../data/processed/clean_transactions.csv")
perf = pd.read_csv("../data/processed/clean_performance.csv")

# Load tables
fund.to_sql(
    "dim_fund",
    engine,
    if_exists="replace",
    index=False
)

nav.to_sql(
    "fact_nav",
    engine,
    if_exists="replace",
    index=False
)

tx.to_sql(
    "fact_transactions",
    engine,
    if_exists="replace",
    index=False
)

perf.to_sql(
    "fact_performance",
    engine,
    if_exists="replace",
    index=False
)

print("Database created successfully!")