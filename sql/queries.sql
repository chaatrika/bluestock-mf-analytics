-- Query 1: Top 5 funds by AUM

SELECT
    scheme_name,
    fund_house,
    aum_crore
FROM fact_performance
ORDER BY aum_crore DESC
LIMIT 5;

-- Query 2: Average NAV per month

SELECT
    strftime('%Y-%m', nav_date) AS month,
    ROUND(AVG(nav), 2) AS average_nav
FROM fact_nav
GROUP BY strftime('%Y-%m', nav_date)
ORDER BY month;

-- Query 3: SIP inflow by year

SELECT
    strftime('%Y', transaction_date) AS year,
    ROUND(SUM(amount_inr), 2) AS sip_inflow
FROM fact_transactions
WHERE transaction_type = 'Sip'
GROUP BY strftime('%Y', transaction_date)
ORDER BY year;

-- Query 4: Transactions by state

SELECT
    state,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY state
ORDER BY total_transactions DESC;

-- Query 5: Funds with expense ratio below 1%

SELECT
    scheme_name,
    fund_house,
    expense_ratio_pct
FROM fact_performance
WHERE expense_ratio_pct < 1
ORDER BY expense_ratio_pct;

-- Query 6: Number of schemes by fund house

SELECT
    fund_house,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY fund_house
ORDER BY total_schemes DESC;

-- Query 7: Number of schemes by category

SELECT
    category,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY category
ORDER BY total_schemes DESC;

-- Query 8: Number of schemes by risk category

SELECT
    risk_category,
    COUNT(*) AS total_schemes
FROM dim_fund
GROUP BY risk_category
ORDER BY total_schemes DESC;

-- Query 9: Transactions by payment mode

SELECT
    payment_mode,
    COUNT(*) AS total_transactions
FROM fact_transactions
GROUP BY payment_mode
ORDER BY total_transactions DESC;

-- Query 10: Investors by KYC status

SELECT
    kyc_status,
    COUNT(*) AS total_investors
FROM fact_transactions
GROUP BY kyc_status
ORDER BY total_investors DESC;