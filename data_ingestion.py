import os
import pandas as pd


folder_path = "data/raw"

csv_files = sorted(
    [file for file in os.listdir(folder_path) if file.endswith(".csv")]
)

print(f"Found {len(csv_files)} CSV files.\n")

for file in csv_files:
    file_path = os.path.join(folder_path, file)

    print("=" * 60)
    print(f"Dataset: {file}")

    try:
        
        df = pd.read_csv(file_path)

        print("\nShape:")
        print(df.shape)

        print("\nData Types:")
        print(df.dtypes)

        print("\nFirst 5 Rows:")
        print(df.head())

    except Exception as e:
        print(f"\nError reading {file}: {e}")

    print("=" * 60)
    print()