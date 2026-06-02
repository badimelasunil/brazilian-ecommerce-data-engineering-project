SELECT 
    c.customer_unique_id,
    ROUND(SUM(p.payment_value),2) AS lifetime_value
FROM fact_orders o
JOIN dim_customers c
    ON o.customer_key = c.customer_key
JOIN fact_payments p
    ON o.order_id = p.order_id
GROUP BY c.customer_unique_id
ORDER BY lifetime_value DESC;