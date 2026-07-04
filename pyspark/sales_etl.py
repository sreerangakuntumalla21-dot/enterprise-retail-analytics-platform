from pyspark.sql import SparkSession

spark = SparkSession.builder \
    .appName("RetailMart ETL") \
    .getOrCreate()

customers_df = spark.read.csv(
    "../datasets/customers.csv",
    header=True,
    inferSchema=True
)

selected_df = customers_df.select("Customer Name", "City")

selected_df.show()

spark.stop()
