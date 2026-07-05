from pyspark.sql import SparkSession
from pyspark.sql.functions import col, sum


spark = SparkSession.builder \
    .appName("Enterprise Retail Analytics") \
    .config("spark.jars", r"C:\jar\postgresql-42.7.12.jar") \
    .getOrCreate()

spark.sparkContext.setLogLevel("ERROR")


url = "jdbc:postgresql://localhost:5432/retail_enterprise"

properties = {
    "user": "postgres",
    "password": "Sree@9012",
    "driver": "org.postgresql.Driver"
}



customers_df = spark.read.jdbc(
    url=url,
    table='"Customers"',
    properties=properties
)

print("\n===== CUSTOMERS =====")
customers_df.show(5)



products_df = spark.read.jdbc(
    url=url,
    table='"Products"',
    properties=properties
)

print("\n===== PRODUCTS =====")
products_df.show(5)


orders_df = spark.read.jdbc(
    url=url,
    table='"Orders"',
    properties=properties
)

print("\n===== ORDERS =====")
orders_df.show(5)



customer_orders_df = customers_df.join(
    orders_df,
    customers_df.customer_id == orders_df.customer_id,
    "inner"
).drop(orders_df.customer_id)



sales_df = customer_orders_df.join(
    products_df,
    customer_orders_df.product_id == products_df.product_id,
    "inner"
).drop(products_df.product_id)



sales_df = sales_df.withColumn(
    "revenue",
    col("quantity") * col("price")
)


print("\n========== ORDER REVENUE ==========")

sales_df.select(
    "customer_name",
    "city",
    "product_name",
    "category",
    "brand",
    "quantity",
    "price",
    "revenue",
    "order_date"
).show(10, False)


print("\n========== TOP SELLING PRODUCTS ==========")

top_products = sales_df.groupBy("product_name") \
    .agg(sum("quantity").alias("total_quantity")) \
    .orderBy(col("total_quantity").desc())

top_products.show()



print("\n========== SALES BY CITY ==========")

sales_city = sales_df.groupBy("city") \
    .agg(
        sum("revenue").alias("total_revenue"),
        sum("quantity").alias("total_quantity")
    ) \
    .orderBy(col("total_revenue").desc())

sales_city.show(truncate=False)



print("\n========== TOP CUSTOMERS ==========")

top_customers = sales_df.groupBy("customer_name") \
    .agg(
        sum("quantity").alias("total_quantity"),
        sum("revenue").alias("total_revenue")
    ) \
    .orderBy(col("total_quantity").desc())

top_customers.show(truncate=False)



print("\n========== REVENUE BY PRODUCT ==========")

revenue_product = sales_df.groupBy(
    "product_name"
).agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    col("total_revenue").desc()
)

revenue_product.show()



print("\n========== REVENUE BY CATEGORY ==========")

category_sales = sales_df.groupBy(
    "category"
).agg(
    sum("revenue").alias("total_revenue")
).orderBy(
    col("total_revenue").desc()
)

category_sales.show(truncate=False)



sales_report = sales_df.select(
    "customer_name",
    "city",
    "product_name",
    "category",
    "brand",
    "quantity",
    "price",
    "revenue",
    "order_date"
)

print("\n========== FINAL SALES REPORT ==========")
sales_report.show(20, False)


print("\n========== SALES REPORT SCHEMA ==========")
sales_report.printSchema()


sales_report.write \
    .format("jdbc") \
    .option("url", "jdbc:postgresql://localhost:5432/retail_enterprise") \
    .option("dbtable", "sales_report") \
    .option("user", "postgres") \
    .option("password", "Sree@9012") \
    .option("driver", "org.postgresql.Driver") \
    .mode("overwrite") \
    .save()

print("Sales Report loaded into PostgreSQL successfully!")

spark.stop()
