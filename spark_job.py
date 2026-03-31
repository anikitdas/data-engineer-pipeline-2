import pandas as pd

try:
    input_path = "/data/delta-lake/clean_data.csv"
    output_path = "/data/output.csv"

    df = pd.read_csv(input_path)

    # Convert timestamp to date
    df["transaction_date"] = pd.to_datetime(df["timestamp"]).dt.date

    # Group by customer and date
    result = df.groupby(["customer_id", "transaction_date"])["amount"].sum().reset_index()

    result.rename(columns={"amount": "daily_total"}, inplace=True)

    result.to_csv(output_path, index=False)

    print("Spark ETL Completed")

except Exception as e:
    print("ERROR:", e)
    exit(1)