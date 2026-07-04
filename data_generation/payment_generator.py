import pandas as pd
import random

payments = []

payment_methods = [
    "UPI",
    "Credit Card",
    "Debit Card",
    "Net Banking",
    "Cash"
]

payment_status = [
    "Success",
    "Pending",
    "Failed"
]

for payment_id in range(5001, 5101):

    order_id = random.randint(1001, 1100)

    payment = {
        "payment_id": payment_id,
        "order_id": order_id,
        "payment_method": random.choice(payment_methods),
        "payment_status": random.choice(payment_status),
        "amount": random.randint(500, 100000)
    }

    payments.append(payment)

df = pd.DataFrame(payments)

print(df)

df.to_csv("../datasets/payments.csv", index=False)

print("\nPayments CSV created successfully!")
