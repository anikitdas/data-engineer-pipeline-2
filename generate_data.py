from faker import Faker
import csv, uuid, random
from datetime import datetime, timedelta

fake = Faker()

rows = []

for _ in range(1200):
    rows.append([
        str(uuid.uuid4()),
        f"C{random.randint(10000,99999)}",
        round(random.uniform(-50, 500), 2),
        (datetime.utcnow() - timedelta(days=random.randint(0,5))).isoformat(),
        f"STORE_{random.randint(1,50)}"
    ])

rows.extend(rows[:50])

with open("/data/data.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["transaction_id","customer_id","amount","timestamp","merchant"])
    writer.writerows(rows)

print("✅ Data Generated")