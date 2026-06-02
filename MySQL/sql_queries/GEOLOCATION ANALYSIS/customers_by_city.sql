SELECT 
    customer_city,
    COUNT(*) AS total_customers
FROM dim_customers
GROUP BY customer_city
ORDER BY total_customers DESC
LIMIT 10;
