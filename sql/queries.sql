-- Analytical SQL Queries for Mutual Fund Reporting

-- 1. Calculate 1-Year Cumulative Return & CAGR per Fund
SELECT 
    f.fund_name,
    f.category,
    f.plan_type,
    MIN(n.nav_date) AS start_date,
    MAX(n.nav_date) AS end_date,
    FIRST_VALUE(n.nav_value) OVER (PARTITION BY f.fund_id ORDER BY n.nav_date ASC) AS initial_nav,
    LAST_VALUE(n.nav_value) OVER (PARTITION BY f.fund_id ORDER BY n.nav_date ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) AS latest_nav,
    ((LAST_VALUE(n.nav_value) OVER (PARTITION BY f.fund_id ORDER BY n.nav_date ASC ROWS BETWEEN UNBOUNDED PRECEDING AND UNBOUNDED FOLLOWING) - 
      FIRST_VALUE(n.nav_value) OVER (PARTITION BY f.fund_id ORDER BY n.nav_date ASC)) / 
      FIRST_VALUE(n.nav_value) OVER (PARTITION BY f.fund_id ORDER BY n.nav_date ASC)) * 100 AS cumulative_return_pct
FROM fund_master f
JOIN nav_history n ON f.fund_id = n.fund_id
GROUP BY f.fund_id;

-- 2. Direct vs Regular Plan Expense Ratio & Return Comparison
SELECT 
    sub_category,
    plan_type,
    AVG(expense_ratio) AS avg_expense_ratio,
    COUNT(fund_id) AS total_funds
FROM fund_master
GROUP BY sub_category, plan_type;

-- 3. Top 5 Volatile Funds by Volatility (Standard Deviation of Daily Returns)
SELECT 
    f.fund_name,
    f.category,
    SQRT(AVG(n.daily_return * n.daily_return) - (AVG(n.daily_return) * AVG(n.daily_return))) AS volatility
FROM fund_master f
JOIN nav_history n ON f.fund_id = n.fund_id
GROUP BY f.fund_id
ORDER BY volatility DESC
LIMIT 5;