import pandas as pd

try:
    input_path = "/data/delta-lake/clean_data.csv"
    output_path = "/data/output.csv"

    df = pd.read_csv(input_path)

    # Deduplication
    df = df.drop_duplicates(subset=["transaction_id"])

    # Filter invalid data
    df = df[df["amount"] > 0]

    # Extract date
    df["transaction_date"] = pd.to_datetime(df["timestamp"]).dt.date

    # Aggregation
    result = df.groupby(["customer_id", "transaction_date"])["amount"].sum().reset_index()
    result.rename(columns={"amount": "daily_total"}, inplace=True)

    # Save output
    result.to_csv(output_path, index=False)

    print("ETL Transformation Completed")

except Exception as e:
    print("ERROR:", e)
    exit(1)
