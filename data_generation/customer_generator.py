import pandas as pd
from faker import Faker
fake = Faker("en_IN")
customers = []
print("RetailMart Customer Data Generator Started...")

for customer_id in range(1,11):

    customer_name = fake.name()
    email = fake.email()
    phone = fake.numerify("##########")
    city = fake.city()
    country = fake.country()
    registration_date = fake.date()
    customer = {
        "Customer ID": customer_id,
        "Customer Name": customer_name,
        "Email": email,
        "Phone": phone,
        "City": city,
        "Country": country,
        "Registration Date": registration_date
    }   
    customers.append(customer)
    
df = pd.DataFrame(customers)

print(df)

df.to_csv("../datasets/customers.csv", index=False)
print("RetailMart Customer Data Generator Completed. Data saved to datasets/customers.csv")
