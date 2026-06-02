SELECT 
    COUNT(*) AS late_deliveries
FROM fact_orders
WHERE estimated_vs_actual_days > 0;