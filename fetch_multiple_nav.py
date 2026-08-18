"""
Day 1 — Live NAV Fetch (multiple schemes)
Fetches live NAV history from mfapi.in for 5 key blue-chip schemes and
saves each as a raw CSV.

Usage:
    python fetch_multiple_nav.py
"""

import os
import time
import requests
import pandas as pd

RAW_DIR = "data/raw"
BASE_URL = "https://api.mfapi.in/mf/{code}"

# scheme_name -> AMFI scheme code
SCHEMES = {
    "sbi_bluechip": 119551,
    "icici_bluechip": 120503,
    "nippon_large_cap": 118632,
    "axis_bluechip": 119092,
    "kotak_bluechip": 120841,
}


def fetch_scheme_nav(scheme_code: int) -> pd.DataFrame:
    url = BASE_URL.format(code=scheme_code)
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    payload = resp.json()

    meta = payload.get("meta", {})
    data = payload.get("data", [])

    df = pd.DataFrame(data)
    if not df.empty:
        df["date"] = pd.to_datetime(df["date"], format="%d-%m-%Y")
        df["nav"] = pd.to_numeric(df["nav"], errors="coerce")
        df["scheme_code"] = scheme_code
        df["fund_house"] = meta.get("fund_house")
        df["scheme_name"] = meta.get("scheme_name")
        df = df.sort_values("date").reset_index(drop=True)

    return df


def main():
    os.makedirs(RAW_DIR, exist_ok=True)

    for label, code in SCHEMES.items():
        print(f"Fetching {label} (code {code})...")
        try:
            df = fetch_scheme_nav(code)
        except requests.RequestException as e:
            print(f"  [ERROR] {label}: {e}")
            continue

        out_path = os.path.join(RAW_DIR, f"live_nav_{label}_{code}.csv")
        df.to_csv(out_path, index=False)
        print(f"  Saved {len(df)} rows -> {out_path}")

        time.sleep(0.5)  # be polite to the free API

    print("\nDone. Live NAV CSVs are in data/raw/")


if __name__ == "__main__":
    main()