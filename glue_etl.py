import sys
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from awsglue.job import Job
from pyspark.sql.functions import hour, dayofweek

glueContext = GlueContext(SparkContext.getOrCreate())
spark = glueContext.spark_session
job = Job(glueContext)
job.init('TrafficETLJob', {})

print("🔄 Loading Parquet data...")
df = spark.read.parquet("s3://smart-traffic-data-rahul/raw/yellow_tripdata_2025-01.parquet")

print("🧹 Cleaning and filtering data...")
df = df.dropna()
df = df.filter(df["trip_distance"] < 50)

print("🧠 Extracting time features...")
df = df.withColumn("pickup_hour", hour("tpep_pickup_datetime"))
df = df.withColumn("pickup_day", dayofweek("tpep_pickup_datetime"))

print("📦 Writing cleaned data to processed/...")
df.write.mode("overwrite").parquet("s3://smart-traffic-data-rahul/processed/")

print("✅ Done! Written to processed/")
job.commit()
