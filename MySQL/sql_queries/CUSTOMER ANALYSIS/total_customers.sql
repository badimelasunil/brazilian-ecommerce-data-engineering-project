SELECT 
    COUNT(DISTINCT customer_unique_id) AS total_customers
FROM dim_customers;