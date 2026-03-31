from cassandra.cluster import Cluster
import pandas as pd

cluster = Cluster(["scylla"])
session = cluster.connect()

session.execute("""
CREATE KEYSPACE IF NOT EXISTS test_keyspace
WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
""")

session.set_keyspace("test_keyspace")

session.execute("""
CREATE TABLE IF NOT EXISTS daily_customer_totals (
    customer_id TEXT,
    transaction_date DATE,
    daily_total FLOAT,
    PRIMARY KEY (customer_id, transaction_date)
);
""")

df = pd.read_parquet("/data/output")

for _, row in df.iterrows():
    session.execute("""
        INSERT INTO daily_customer_totals (customer_id, transaction_date, daily_total)
        VALUES (%s, %s, %s)
    """, (row["customer_id"], row["transaction_date"], float(row["daily_total"])))

print("✅ Loaded to Scylla")