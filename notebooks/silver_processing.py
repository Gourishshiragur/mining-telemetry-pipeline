%run ./config_notebook

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, col

df = spark.read.format("delta").load(paths["bronze"] + "/messages")

window = Window.partitionBy("truck_id", "event_time") \
               .orderBy(col("ingestion_time").desc())

df = df.withColumn("rn", row_number().over(window)) \
       .filter("rn = 1") \
       .drop("rn")

df = df.filter("fuel >= 0")

df.write.format("delta") \
  .mode("overwrite") \
  .save(paths["silver"] + "/messages")