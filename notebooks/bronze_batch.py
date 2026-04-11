%run ./config_notebook
%run ./audit_validation

from pyspark.sql.functions import col, current_timestamp

df = spark.read.json(paths["raw"] + "/messages")

# 🔥 incremental logic
df = df.filter(col("event_time") > last_processed_ts)

if df.count() == 0:
    dbutils.notebook.exit("NO_DATA")

df = df.withColumn("ingestion_time", current_timestamp())

df.write.format("delta") \
  .mode("append") \
  .save(paths["bronze"] + "/messages")