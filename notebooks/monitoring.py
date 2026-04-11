%run ./config_notebook

# Update watermark
spark.sql(f"""
MERGE INTO watermark_table t
USING (
  SELECT '{pipeline_name}' AS pipeline_name,
         current_timestamp() AS last_processed_ts
) s
ON t.pipeline_name = s.pipeline_name

WHEN MATCHED THEN UPDATE SET last_processed_ts = s.last_processed_ts
WHEN NOT MATCHED THEN INSERT *
""")

print("Pipeline completed successfully")