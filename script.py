import pyspark
from pyspark.sql import SparkSession

# ------------------------------------------------------

spark = SparkSession.builder \
        .appName("Python Spark SQL basic example") \
        .config("spark.some.config.option", "some-value") \
        .getOrCreate()
        
# # read df from json file
orders_df = spark.read.option("multiline", "true").json("data/orders.json")
addresses_df = spark.read.option("multiline", "true").json("data/addresses.json")
prices_df = spark.read.option("multiline", "true").json("data/prices.json")
products_df = spark.read.option("multiline", "true").json("data/products.json")
