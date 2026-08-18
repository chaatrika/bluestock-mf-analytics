import os
import pandas as pd

# Paths and file mappings
RAW_DIR = "data/raw"
REPORTS_DIR = "reports"

RAW_FILES = {
    "fund_master": "01_fund_master.csv",
    "nav_history": "02_nav_history.csv",
    "aum_by_fund_house": "03_aum_by_fund_house.csv",
    "monthly_sip_inflows": "04_monthly_sip_inflows.csv",
    "category_inflows": "05_category_inflows.csv",
    "industry_folio_count": "06_industry_folio_count.csv",
    "scheme_performance": "07_scheme_performance.csv",
    "investor_transactions": "08_investor_transactions.csv",
    "portfolio_holdings": "09_portfolio_holdings.csv",
    "benchmark_indices": "10_benchmark_indices.csv",
}


def load_all_datasets():
    datasets = {}
    
    for name, filename in RAW_FILES.items():
        file_path = os.path.join(RAW_DIR, filename)
        print("-" * 50)
        print(f"Loading: {name} ({filename})")
        
        if not os.path.exists(file_path):
            print(f"WARNING: File not found at {file_path}")
            continue
            
        df = pd.read_csv(file_path)
        datasets[name] = df
        
        # Display basic information
        print(f"Shape: {df.shape}")
        print("Data Types:\n", df.dtypes)
        print("First 3 rows:\n", df.head(3))
        
        # Simple data quality checks
        nulls = df.isnull().sum()
        cols_with_nulls = nulls[nulls > 0]
        if not cols_with_nulls.empty:
            print("Null values found:\n", cols_with_nulls.to_dict())
            
        duplicates = df.duplicated().sum()
        if duplicates > 0:
            print(f"Duplicate rows: {duplicates}")
            
        print()
        
    return datasets


def explore_fund_master(datasets):
    df = datasets.get("fund_master")
    if df is None:
        print("fund_master dataset not found.")
        return
        
    print("=" * 50)
    print("FUND MASTER SUMMARY")
    print("=" * 50)
    
    important_cols = ["fund_house", "category", "sub_category", "risk_category"]
    for col in important_cols:
        if col in df.columns:
            unique_vals = df[col].dropna().unique()
            print(f"Unique {col} ({len(unique_vals)}): {sorted(list(unique_vals))}")
            
    if "amfi_code" in df.columns:
        print(f"Total Unique AMFI Codes: {df['amfi_code'].nunique()}")


def validate_amfi_codes(datasets):
    fund_master = datasets.get("fund_master")
    nav_history = datasets.get("nav_history")
    
    if fund_master is None or nav_history is None:
        print("Cannot validate AMFI codes: fund_master or nav_history missing.")
        return
        
    print("=" * 50)
    print("AMFI CODE VALIDATION")
    print("=" * 50)
    
    fm_codes = set(fund_master["amfi_code"].dropna().astype(str))
    nh_codes = set(nav_history["amfi_code"].dropna().astype(str))
    
    missing_in_nav = fm_codes - nh_codes
    missing_in_master = nh_codes - fm_codes
    
    coverage = 100 * (len(fm_codes) - len(missing_in_nav)) / len(fm_codes) if fm_codes else 0
    
    summary = f"""DATA QUALITY SUMMARY — AMFI Scheme Code Validation
---------------------------------------------------
Fund Master Unique Codes : {len(fm_codes)}
NAV History Unique Codes : {len(nh_codes)}
Master Codes Missing in NAV: {len(missing_in_nav)}
NAV Codes Missing in Master: {len(missing_in_master)}
Coverage                 : {coverage:.2f}%
"""
    print(summary)
    
    # Save validation summary report
    os.makedirs(REPORTS_DIR, exist_ok=True)
    report_path = os.path.join(REPORTS_DIR, "data_quality_summary.txt")
    with open(report_path, "w") as f:
        f.write(summary)
        
    print(f"Summary written to {report_path}")


def main():
    os.makedirs(RAW_DIR, exist_ok=True)
    datasets = load_all_datasets()
    
    if not datasets:
        print("No datasets loaded. Check your files in data/raw/")
        return
        
    explore_fund_master(datasets)
    validate_amfi_codes(datasets)
    print("\nData ingestion step complete!")


if __name__ == "__main__":
    main()