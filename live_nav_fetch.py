import requests
import pandas as pd

url = "https://api.mfapi.in/mf/125497"
response = requests.get(url)

print("Status Code:", response.status_code)

json_data = response.json()
nav_data = json_data["data"]
print(nav_data[:5])

df = pd.DataFrame(nav_data)
print("\n DataFrame Preview:")
print(df.head())

output_file = "data/raw/hdfc_top100_live_nav.csv"
df.to_csv(output_file, index=False)

print(f"\nCSV saved successfully: {output_file}")