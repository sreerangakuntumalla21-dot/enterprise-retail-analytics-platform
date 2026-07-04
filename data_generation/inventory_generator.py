
import pandas as pd
import random

inventory = []

warehouses = [
    "Hyderabad",
    "Bengaluru",
    "Chennai",
    "Mumbai",
    "Delhi"
]

for product_id in range(101, 111):

    inventory.append({
        "product_id": product_id,
        "warehouse": random.choice(warehouses),
        "available_stock": random.randint(10, 500)
    })

df = pd.DataFrame(inventory)

print(df)

df.to_csv("../datasets/inventory.csv", index=False)

print("\nInventory CSV created successfully!")
