# Bluestock Mutual Fund Analytics — Data Dictionary

This document provides a comprehensive schema description for all raw datasets, cleaned target tables, and metric outputs used in the Bluestock Mutual Fund Analytics (`bluestock-mf-analytics`) ETL pipeline.

---

## 1. Raw Datasets (`data/raw/`)

### 1.1 `01_fund_master.csv`
Contains metadata and master classifications for tracked mutual fund schemes.

| Field Name | Data Type | Key Type | Description | Sample Values |
| :--- | :--- | :--- | :--- | :--- |
| `fund_id` | VARCHAR(50) | Primary Key | Unique identifier for the fund scheme | `MF_EQUITY_001` |
| `fund_name` | VARCHAR(255)| — | Full official name of the fund | `Axis Bluechip Fund - Direct Plan - Growth` |
| `amc_name` | VARCHAR(255)| — | Asset Management Company (Fund House) | `Axis Mutual Fund` |
| `category` | VARCHAR(100)| — | Major asset classification | `Equity`, `Debt`, `Hybrid` |
| `sub_category` | VARCHAR(100)| — | Specific mandate sub-class | `Large Cap`, `Mid Cap`, `Flexi Cap` |
| `plan_type` | VARCHAR(50) | — | Pricing model structure | `Direct`, `Regular` |
| `option_type` | VARCHAR(50) | — | Income distribution structure | `Growth`, `IDCW` |
| `inception_date`| DATE | — | Official launch date (`YYYY-MM-DD`) | `2010-01-05` |
| `benchmark_id` | VARCHAR(50) | Foreign Key| Target comparison benchmark index | `IND_NIFTY_50_TRI` |

---

### 1.2 `02_nav_history.csv`
Daily time-series record of Net Asset Values (NAV) across fund schemes.

| Field Name | Data Type | Key Type | Description | Sample Values |
| :--- | :--- | :--- | :--- | :--- |
| `nav_id` | INT (Auto) | Primary Key | Unique surrogate key for entry | `100293` |
| `fund_id` | VARCHAR(50) | Foreign Key| Link to `01_fund_master.csv` | `MF_EQUITY_001` |
| `nav_date` | DATE | Composite | Date of valuation (`YYYY-MM-DD`) | `2024-03-15` |
| `nav_value` | DECIMAL(10,4)| — | Net Asset Value per unit (in INR) | `52.4180` |
| `aum_crores` | DECIMAL(12,2)| — | Total Assets Under Management in ₹ Cr | `34250.75` |

---

### 1.3 `10_benchmark_indices.csv`
Daily closing prices and Total Return Index (TRI) values for market benchmarks.

| Field Name | Data Type | Key Type | Description | Sample Values |
| :--- | :--- | :--- | :--- | :--- |
| `index_id` | VARCHAR(50) | Foreign Key| Unique index identifier | `IND_NIFTY_50_TRI` |
| `index_name` | VARCHAR(255)| — | Full index description | `Nifty 50 Total Return Index` |
| `trade_date` | DATE | Composite | Trading session date (`YYYY-MM-DD`) | `2024-03-15` |
| `closing_price`| DECIMAL(10,4)| — | Index benchmark closing level | `22023.35` |
| `daily_return` | DECIMAL(8,6) | — | Percentage daily change in index value | `0.004521` |

---

## 2. Processed & Cleaned Tables (`data/cleaned/`)

### 2.1 `clean_nav.csv`
Transformed NAV series with computed return metrics and missing-value imputation.

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `fund_id` | VARCHAR(50) | Unique identifier for the fund |
| `nav_date` | DATE | Market date (`YYYY-MM-DD`) |
| `nav_value` | DECIMAL(10,4)| Cleaned NAV (forward-filled for non-trading days) |
| `daily_return` | DECIMAL(8,6) | Logarithmic / Percentage daily change `(NAV_t / NAV_{t-1}) - 1` |
| `rolling_30d_vol`| DECIMAL(8,6) | Annualized standard deviation over trailing 30 trading days |

---

### 2.2 `fund_scorecard.csv`
Aggregated quantitative performance summary per fund scheme.

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `fund_id` | VARCHAR(50) | Unique identifier for the fund |
| `cagr_1yr` | DECIMAL(6,4) | 1-Year Compound Annual Growth Rate |
| `cagr_3yr` | DECIMAL(6,4) | 3-Year Compound Annual Growth Rate |
| `cagr_5yr` | DECIMAL(6,4) | 5-Year Compound Annual Growth Rate |
| `sharpe_ratio` | DECIMAL(6,4) | Excess return per unit of total risk `(R_p - R_f) / σ_p` |
| `sortino_ratio`| DECIMAL(6,4) | Excess return per unit of downside risk `(R_p - R_f) / σ_d` |
| `max_drawdown` | DECIMAL(6,4) | Peak-to-trough peak loss percentage over trailing 5 years |

---

### 2.3 `alpha_beta.csv`
Calculated systematic risk metrics benchmarked against broad-market indices.

| Field Name | Data Type | Description |
| :--- | :--- | :--- |
| `fund_id` | VARCHAR(50) | Unique identifier for the fund |
| `benchmark_id` | VARCHAR(50) | Corresponding benchmark identifier |
| `beta` | DECIMAL(6,4) | Systematic market sensitivity factor |
| `jensen_alpha` | DECIMAL(6,4) | Excess risk-adjusted annualized alpha relative to CAPM |
| `r_squared` | DECIMAL(6,4) | Proportion of return variance explained by benchmark |
| `tracking_error`| DECIMAL(6,4)| Standard deviation of residual return differences |

---

## 3. Data Type Standards & Business Rules

* **Currency:** All monetary values (`nav_value`, `aum_crores`) are represented in **Indian Rupees (INR)**.
* **Dates:** ISO-8601 standard date format (`YYYY-MM-DD`).
* **Handling Missing Data:** Weekend and non-trading days in NAV time-series are forward-filled (`ffill`).
* **Risk-Free Rate Assumption ($R_f$):** Set at **6.5% per annum** (based on standard RBI 91-day T-Bill yields).