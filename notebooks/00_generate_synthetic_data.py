"""
00_generate_synthetic_data.py
------------------------------
Generates synthetic data matching data_dictionary.md schema, ONLY so the
Performance_Analytics notebook can run end-to-end for development/demo.

>>> REPLACE THIS STEP WITH YOUR REAL DATA <<<
Once you have real data/raw/01_fund_master.csv, 02_nav_history.csv, and
10_benchmark_indices.csv (from fetch_multiple_nav.py / your own sourcing),
just delete or skip this script. The analytics notebook reads from
data/raw/ and doesn't care whether the CSVs came from here or real APIs.
"""

import numpy as np
import pandas as pd

np.random.seed(42)
RAW_DIR = "../data/raw"

N_SCHEMES = 40
N_YEARS = 5
END_DATE = pd.Timestamp("2026-08-01")
START_DATE = END_DATE - pd.DateOffset(years=N_YEARS)
dates = pd.bdate_range(START_DATE, END_DATE)  # business days

fund_houses = ["SBI MF", "ICICI Prudential", "HDFC MF", "Axis MF", "Kotak MF",
               "Nippon India", "UTI MF", "Mirae Asset", "Franklin Templeton", "DSP MF"]
categories = ["Large Cap", "Mid Cap", "Small Cap", "Flexi Cap", "ELSS"]

# ---- 1) Fund Master ----
schemes = []
for i in range(N_SCHEMES):
    amfi_code = 100000 + i
    schemes.append({
        "amfi_code": amfi_code,
        "fund_house": fund_houses[i % len(fund_houses)],
        "scheme_name": f"{fund_houses[i % len(fund_houses)]} {categories[i % len(categories)]} Fund - Direct Growth",
        "category": "Equity",
        "sub_category": categories[i % len(categories)],
        "plan": "Direct",
        "launch_date": (START_DATE - pd.DateOffset(years=np.random.randint(2, 15))).date(),
        "benchmark": "Nifty 100" if i % 2 == 0 else "Nifty 50",
        "expense_ratio_pct": round(np.random.uniform(0.35, 1.85), 2),
        "exit_load_pct": round(np.random.choice([0.0, 0.5, 1.0]), 2),
        "min_sip_amount": int(np.random.choice([500, 1000, 2500])),
        "min_lumpsum_amount": int(np.random.choice([1000, 5000, 10000])),
        "fund_manager": f"Manager {chr(65 + i % 26)}",
        "risk_category": np.random.choice(["Moderate", "Moderately High", "High"]),
        "sebi_category_code": f"EQ-{i % 10 + 1}",
    })
fund_master = pd.DataFrame(schemes)
fund_master.to_csv(f"{RAW_DIR}/01_fund_master.csv", index=False)

# ---- 2) Benchmark Indices (Nifty 50, Nifty 100) ----
bench_rows = []
for idx_name, drift, vol in [("Nifty 50", 0.00045, 0.011), ("Nifty 100", 0.00042, 0.0105)]:
    level = 18000 if idx_name == "Nifty 50" else 17000
    for d in dates:
        level *= (1 + np.random.normal(drift, vol))
        bench_rows.append({"date": d.date(), "index_name": idx_name, "close_value": round(level, 2)})
benchmark_df = pd.DataFrame(bench_rows)
benchmark_df.to_csv(f"{RAW_DIR}/10_benchmark_indices.csv", index=False)

# ---- 3) NAV History (correlated to benchmark + fund-specific alpha/beta/noise) ----
nifty100_returns = (
    benchmark_df[benchmark_df.index_name == "Nifty 100"]
    .sort_values("date")["close_value"].pct_change().fillna(0).values
)

nav_rows = []
for s in schemes:
    code = s["amfi_code"]
    true_beta = np.random.uniform(0.7, 1.3)
    true_alpha_daily = np.random.uniform(-0.0003, 0.0006)  # skill component
    idio_vol = np.random.uniform(0.006, 0.016)
    nav = 100 * np.random.uniform(0.8, 3.0)
    for i, d in enumerate(dates):
        mkt_ret = nifty100_returns[i]
        ret = true_alpha_daily + true_beta * mkt_ret + np.random.normal(0, idio_vol)
        nav *= (1 + ret)
        nav_rows.append({
            "date": d.date(),
            "amfi_code": code,
            "nav": round(nav, 4),
            "daily_return": None,  # computed later in the notebook, not pre-filled
        })

nav_history = pd.DataFrame(nav_rows)
nav_history.to_csv(f"{RAW_DIR}/02_nav_history.csv", index=False)

print("Synthetic data generated:")
print(f"  {RAW_DIR}/01_fund_master.csv       -> {fund_master.shape}")
print(f"  {RAW_DIR}/10_benchmark_indices.csv -> {benchmark_df.shape}")
print(f"  {RAW_DIR}/02_nav_history.csv       -> {nav_history.shape}")
