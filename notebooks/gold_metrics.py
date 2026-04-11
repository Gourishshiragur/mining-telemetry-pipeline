%run ./config_notebook

from pyspark.sql.functions import count, avg

df = spark.read.format("delta").load(paths["silver"] + "/messages")

gold_df = df.groupBy("truck_id").agg(
    count("*").alias("total_trips"),
    avg("speed").alias("avg_speed"),
    avg("fuel").alias("avg_fuel")
)

gold_df.write.format("delta") \
    .mode("overwrite") \
    .saveAsTable("gold_truck_metrics")