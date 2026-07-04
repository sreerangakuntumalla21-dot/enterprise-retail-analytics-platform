import pandas as pd
import random
from faker import Faker

fake = Faker("en_IN")

orders = []

for order_id in range(1001, 1101):

    customer_id = random.randint(1, 10)
    product_id = random.randint(101, 110)
    quantity = random.randint(1, 5)

    order = {
        "order_id": order_id,
        "customer_id": customer_id,
        "product_id": product_id,
        "order_date": fake.date_between(start_date="-1y", end_date="today"),
        "quantity": quantity
    }

    orders.append(order)

df = pd.DataFrame(orders)

print(df)

df.to_csv("../datasets/orders.csv", index=False)

print("\nOrders CSV created successfully!")
