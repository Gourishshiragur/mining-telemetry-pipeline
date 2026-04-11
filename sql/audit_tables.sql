-- audit_tables.sql

CREATE TABLE IF NOT EXISTS audit_log (
    pipeline_name STRING,
    run_id STRING,
    layer STRING,
    status STRING,
    record_count INT,
    error_message STRING,
    created_at TIMESTAMP
)
USING DELTA;

CREATE TABLE IF NOT EXISTS watermark_table (
    pipeline_name STRING,
    last_processed_ts TIMESTAMP
)
USING DELTA;

-- Quarantine table for bad data
CREATE TABLE IF NOT EXISTS quarantine_table (
    truck_id STRING,
    event_time TIMESTAMP,
    fuel DOUBLE,
    error_reason STRING,
    created_at TIMESTAMP
)
USING DELTA;