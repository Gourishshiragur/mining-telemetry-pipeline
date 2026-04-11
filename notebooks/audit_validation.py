%run ./config_notebook

watermark_df = spark.sql(f"""
SELECT last_processed_ts 
FROM watermark_table
WHERE pipeline_name = '{pipeline_name}'
""")

if watermark_df.count() == 0:
    last_processed_ts = "1900-01-01"
else:
    last_processed_ts = watermark_df.collect()[0][0]

print("Watermark:", last_processed_ts)