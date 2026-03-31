import pandas as pd
import os

try:
    # Input & Output paths
    input_path = "/data/data.csv"
    output_path = "/data/delta-lake"

    # Read data
    df = pd.read_csv(input_path)

    # Remove duplicate transactions
    df = df.drop_duplicates(subset=["transaction_id"])

    # Filter invalid transactions (amount <= 0)
    df = df[df["amount"] > 0]

    # Create output folder if not exists
    os.makedirs(output_path, exist_ok=True)

    # Save cleaned data
    output_file = os.path.join(output_path, "clean_data.csv")
    df.to_csv(output_file, index=False)

    print("✅ Delta Load Successful")

except Exception as e:
    print("❌ ERROR:", e)
    exit(1)