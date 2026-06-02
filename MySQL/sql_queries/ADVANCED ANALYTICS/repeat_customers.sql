SELECT 
    c.customer_unique_id,
    COUNT(DISTINCT o.order_id) AS total_orders
FROM fact_orders o
JOIN dim_customers c
    ON o.customer_key = c.customer_key
GROUP BY c.customer_unique_id
HAVING total_orders > 1
ORDER BY total_orders DESC;