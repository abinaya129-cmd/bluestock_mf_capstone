-- 1. Total Funds
SELECT COUNT(*) FROM dim_fund;

-- 2. Total NAV Records
SELECT COUNT(*) FROM fact_nav;

-- 3. Average NAV
SELECT AVG(nav)
FROM fact_nav;

-- 4. Top 5 Funds by Expense Ratio
SELECT scheme_name, expense_ratio_pct
FROM dim_fund
ORDER BY expense_ratio_pct DESC
LIMIT 5;

-- 5. Fund Categories
SELECT category,
COUNT(*)
FROM dim_fund
GROUP BY category;

-- 6. Transactions by Type
SELECT transaction_type,
COUNT(*)
FROM fact_transactions
GROUP BY transaction_type;

-- 7. Average Transaction Amount
SELECT AVG(amount_inr)
FROM fact_transactions;

-- 8. Top States by Transactions
SELECT state,
COUNT(*)
FROM fact_transactions
GROUP BY state
ORDER BY COUNT(*) DESC;

-- 9. Highest Sharpe Ratio
SELECT amfi_code,
sharpe_ratio
FROM fact_performance
ORDER BY sharpe_ratio DESC
LIMIT 5;

-- 10. Highest Alpha
SELECT amfi_code,
alpha
FROM fact_performance
ORDER BY alpha DESC
LIMIT 5;