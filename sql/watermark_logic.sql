-- watermark_logic.sql

-- 1. Read watermark (used in audit_validation)
SELECT last_processed_ts 
FROM watermark_table
WHERE pipeline_name = 'mining_pipeline';


-- 2. Example incremental filter logic (conceptual)
-- (Actual filtering happens in PySpark)

-- SELECT * FROM source_data
-- WHERE event_time > last_processed_ts;


-- 3. Update watermark after successful pipeline run
MERGE INTO watermark_table t
USING (
  SELECT 'mining_pipeline' AS pipeline_name,
         current_timestamp() AS last_processed_ts
) s
ON t.pipeline_name = s.pipeline_name

WHEN MATCHED THEN 
  UPDATE SET t.last_processed_ts = s.last_processed_ts

WHEN NOT MATCHED THEN 
  INSERT *;