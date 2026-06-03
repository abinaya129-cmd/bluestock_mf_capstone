CREATE TABLE dim_fund(
    amfi_code TEXT PRIMARY KEY,
    fund_house TEXT,
    scheme_name TEXT,
    category TEXT
);

CREATE TABLE fact_nav(
    amfi_code TEXT,
    date DATE,
    nav REAL
);

CREATE TABLE fact_transactions(
    investor_id TEXT,
    transaction_date DATE,
    amfi_code TEXT,
    amount_inr REAL
);

CREATE TABLE fact_performance(
    amfi_code TEXT,
    sharpe_ratio REAL,
    alpha REAL,
    beta REAL
);