-- scd2_tables.sql

CREATE TABLE IF NOT EXISTS driver_dimension (
    truck_id STRING,
    driver_id STRING,
    start_time TIMESTAMP,
    end_time TIMESTAMP,
    is_current BOOLEAN
)
USING DELTA;