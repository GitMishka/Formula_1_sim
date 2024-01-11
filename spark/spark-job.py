from pyspark.sql import SparkSession
from pyspark.sql.functions import col, max

# Initialize Spark Session
spark = SparkSession.builder \
    .appName("F1 Race Simulation") \
    .getOrCreate()

# Read from Kafka
df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "race_data") \
    .load()

# Assuming the value is in JSON format
df = df.selectExpr("CAST(value AS STRING)")

# Define your data processing logic here
# For example, you might aggregate data to find the current leader

# Start the query and print the output to the console
query = df.writeStream \
    .outputMode("complete") \
    .format("console") \
    .start()

query.awaitTermination()
