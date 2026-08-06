# Mutual Fund Data Dictionary

## Project Overview

This document describes all datasets used in the Mutual Fund Data Analysis project. It includes the source file, columns, data types, and descriptions for each dataset.

---

# Dataset 1: Fund Master

**Source:** `data/raw/01_fund_master.csv`

**Purpose:** Contains master information about mutual fund schemes.

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Unique AMFI scheme code |
| fund_house | TEXT | Mutual fund company |
| scheme_name | TEXT | Scheme name |
| category | TEXT | Equity/Debt category |
| sub_category | TEXT | Fund sub-category |
| plan | TEXT | Direct or Regular plan |
| launch_date | DATE | Scheme launch date |
| benchmark | TEXT | Benchmark index |
| expense_ratio_pct | REAL | Expense ratio (%) |
| exit_load_pct | REAL | Exit load (%) |
| min_sip_amount | INTEGER | Minimum SIP investment |
| min_lumpsum_amount | INTEGER | Minimum lump sum investment |
| fund_manager | TEXT | Fund manager |
| risk_category | TEXT | Risk level |
| sebi_category_code | TEXT | SEBI category code |

---

# Dataset 2: NAV History

**Source:** `data/raw/02_nav_history.csv`

**Purpose:** Historical Net Asset Value (NAV) for mutual fund schemes.

| Column | Type | Description |
|--------|------|-------------|
| date | DATE | NAV date |
| amfi_code | INTEGER | Scheme AMFI code |
| nav | REAL | Net Asset Value |
| daily_return | REAL | Daily percentage return |

---

# Dataset 3: AUM by Fund House

**Source:** `data/raw/03_aum_by_fund_house.csv`

**Purpose:** Assets Under Management statistics by fund house.

| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Reporting date |
| fund_house | TEXT | Mutual fund company |
| aum_lakh_crore | REAL | AUM in lakh crore |
| aum_crore | REAL | AUM in crore |
| num_schemes | INTEGER | Number of schemes |

---

# Dataset 4: Monthly SIP Inflows

**Source:** `data/raw/04_monthly_sip_inflows.csv`

**Purpose:** Monthly SIP investment statistics.

| Column | Type | Description |
|--------|------|-------------|
| month | TEXT | Reporting month |
| sip_inflow_crore | REAL | SIP inflow (crore) |
| active_sip_accounts_crore | REAL | Active SIP accounts |
| new_sip_accounts_lakh | REAL | New SIP accounts |
| sip_aum_lakh_crore | REAL | SIP AUM |
| yoy_growth_pct | REAL | Year-over-year growth (%) |

---

# Dataset 5: Category Inflows

**Source:** `data/raw/05_category_inflows.csv`

**Purpose:** Net inflows grouped by mutual fund category.

| Column | Type | Description |
|--------|------|-------------|
| month | TEXT | Reporting month |
| category | TEXT | Fund category |
| net_inflow_crore | REAL | Net inflow (crore) |

---

# Dataset 6: Industry Folio Count

**Source:** `data/raw/06_industry_folio_count.csv`

**Purpose:** Monthly folio statistics across mutual fund categories.

| Column | Type | Description |
|--------|------|-------------|
| month | TEXT | Reporting month |
| total_folios_crore | REAL | Total folios |
| equity_folios_crore | REAL | Equity folios |
| debt_folios_crore | REAL | Debt folios |
| hybrid_folios_crore | REAL | Hybrid folios |
| others_folios_crore | REAL | Other folios |

---

# Dataset 7: Scheme Performance

**Source:** `data/raw/07_scheme_performance.csv`

**Purpose:** Performance metrics of mutual fund schemes.

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Scheme AMFI code |
| scheme_name | TEXT | Scheme name |
| fund_house | TEXT | Mutual fund company |
| category | TEXT | Fund category |
| plan | TEXT | Direct or Regular plan |
| return_1yr_pct | REAL | One-year return (%) |
| return_3yr_pct | REAL | Three-year return (%) |
| return_5yr_pct | REAL | Five-year return (%) |
| benchmark_3yr_pct | REAL | Benchmark return |
| alpha | REAL | Alpha |
| beta | REAL | Beta |
| sharpe_ratio | REAL | Sharpe ratio |
| sortino_ratio | REAL | Sortino ratio |
| std_dev_ann_pct | REAL | Annualized volatility |
| max_drawdown_pct | REAL | Maximum drawdown |
| aum_crore | REAL | Assets under management |
| expense_ratio_pct | REAL | Expense ratio |
| morningstar_rating | INTEGER | Morningstar rating |
| risk_grade | TEXT | Overall risk grade |

---

# Dataset 8: Investor Transactions

**Source:** `data/raw/08_investor_transactions.csv`

**Purpose:** Investor transaction records.

| Column | Type | Description |
|--------|------|-------------|
| investor_id | TEXT | Unique investor ID |
| transaction_date | DATE | Transaction date |
| amfi_code | INTEGER | Scheme AMFI code |
| transaction_type | TEXT | SIP, Lumpsum or Redemption |
| amount_inr | REAL | Transaction amount |
| state | TEXT | Investor state |
| city | TEXT | Investor city |
| city_tier | TEXT | T30/B30 classification |
| age_group | TEXT | Investor age group |
| gender | TEXT | Investor gender |
| annual_income_lakh | REAL | Annual income (lakh) |
| payment_mode | TEXT | Payment method |
| kyc_status | TEXT | KYC verification status |

---

# Dataset 9: Portfolio Holdings

**Source:** `data/raw/09_portfolio_holdings.csv`

**Purpose:** Equity holdings of mutual fund schemes.

| Column | Type | Description |
|--------|------|-------------|
| amfi_code | INTEGER | Scheme AMFI code |
| stock_symbol | TEXT | Stock ticker |
| stock_name | TEXT | Company name |
| sector | TEXT | Industry sector |
| weight_pct | REAL | Portfolio weight (%) |
| market_value_cr | REAL | Market value (crore) |
| current_price_inr | REAL | Current stock price |
| portfolio_date | DATE | Portfolio reporting date |

---

# Dataset 10: Benchmark Indices

**Source:** `data/raw/10_benchmark_indices.csv`

**Purpose:** Historical benchmark index values.

| Column | Type | Description |
|--------|------|-------------|
| date | DATE | Trading date |
| index_name | TEXT | Benchmark index |
| close_value | REAL | Closing index value |