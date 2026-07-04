import pandas as pd
from faker import Faker
import random

fake = Faker("en_IN")

products = []

categories = ["Mobile", "Laptop","Headphones","Watch","Camera"]
brands = ["Apple","Samsung","Sony","Dell","HP"]

for product_id in range(101,111):

    category = random.choice(categories)
    brand = random.choice(brands)

    product = {
        "product_id": product_id,
        "product_name": fake.word().capitalize(),
        "category": category,
        "brand": brand,
        "price": random.randint(1000, 100000)
    }

    products.append(product)

df = pd.DataFrame(products)

print(df)

df.to_csv("../datasets/products.csv", index=False)
print("Products dataset generated and saved to products.csv")
