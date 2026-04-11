# bronze_streaming.py

%run ./config_notebook

df = spark.readStream.format("json").load(paths["raw"] + "/stream")

df.writeStream \
  .format("delta") \
  .option("checkpointLocation", paths["checkpoint"] + "/bronze") \
  .start(paths["bronze"] + "/stream")