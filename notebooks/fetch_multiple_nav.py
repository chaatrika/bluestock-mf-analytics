import os
import requests
import pandas as pd

# RapidAPI / AMFI API configurations for fetching live scheme NAVs
SCHEME_CODES = {
    "Axis Bluechip Fund": "119092",
    "ICICI Prudential Bluechip Fund": "120503",
    "Kotak Bluechip Fund": "120841",
    "Nippon India Large Cap Fund": "118632",
    "SBI Bluechip Fund": "119551"
}

OUTPUT_DIR = "data/raw"

def fetch_nav_data(scheme_code):
    """Fetch NAV history for a given AMFI scheme code from mfapi.in."""
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    try:
        response = requests.get(url, timeout=10)
        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data['data'])
            df['scheme_code'] = scheme_code
            df['scheme_name'] = data['meta']['scheme_name']
            df['fund_house'] = data['meta']['fund_house']
            return df
        else:
            print(f"Failed to fetch data for scheme {scheme_code}: HTTP {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching scheme {scheme_code}: {e}")
        return None

def main():
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    combined_df = pd.DataFrame()

    print("Fetching live NAV data for multiple mutual funds...")
    for fund_name, scheme_code in SCHEME_CODES.items():
        print(f"Fetching: {fund_name} (Code: {scheme_code})...")
        df = fetch_nav_data(scheme_code)
        if df is not None:
            # Save individual file
            filename = f"live_nav_{fund_name.lower().replace(' ', '_')}_{scheme_code}.csv"
            df.to_csv(os.path.join(OUTPUT_DIR, filename), index=False)
            combined_df = pd.concat([combined_df, df], ignore_index=True)

    if not combined_df.empty:
        combined_file = os.path.join(OUTPUT_DIR, "combined_live_nav.csv")
        combined_df.to_csv(combined_file, index=False)
        print(f"Successfully saved all NAV data to {combined_file}")

if __name__ == "__main__":
    main()