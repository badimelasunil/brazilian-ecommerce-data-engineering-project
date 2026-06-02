SELECT 
    customer_state,
    COUNT(*) AS total_customers
FROM dim_customers
GROUP BY customer_state
ORDER BY total_customers DESC;