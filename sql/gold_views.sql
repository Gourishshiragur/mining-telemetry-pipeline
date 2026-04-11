-- gold_views.sql

-- Truck KPI View
CREATE OR REPLACE VIEW vw_truck_metrics AS
SELECT 
    truck_id,
    COUNT(*) AS total_trips,
    AVG(speed) AS avg_speed,
    AVG(fuel) AS avg_fuel
FROM delta.`/mnt/mining/dev/silver/messages`
GROUP BY truck_id;


-- Latest Driver per Truck (SCD2 usage)
CREATE OR REPLACE VIEW vw_truck_driver_current AS
SELECT 
    truck_id,
    driver_id
FROM driver_dimension
WHERE is_current = true;


-- Join KPI + Driver (Business View)
CREATE OR REPLACE VIEW vw_business_metrics AS
SELECT 
    m.truck_id,
    d.driver_id,
    m.total_trips,
    m.avg_speed,
    m.avg_fuel
FROM vw_truck_metrics m
LEFT JOIN vw_truck_driver_current d
ON m.truck_id = d.truck_id;