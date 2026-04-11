%run ./config_notebook

source_df = spark.read.format("delta").load(paths["silver"] + "/messages")

source_df.createOrReplaceTempView("source")

spark.sql("""
MERGE INTO driver_dimension t
USING source s
ON t.truck_id = s.truck_id AND t.is_current = true

WHEN MATCHED AND t.driver_id != s.driver_id THEN
  UPDATE SET is_current = false, end_time = current_timestamp()

WHEN NOT MATCHED THEN
  INSERT (truck_id, driver_id, start_time, end_time, is_current)
  VALUES (s.truck_id, s.driver_id, current_timestamp(), NULL, true)
""")