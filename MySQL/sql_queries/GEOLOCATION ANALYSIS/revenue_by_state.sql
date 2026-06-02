SELECT 
    c.customer_state,
    ROUND(SUM(p.payment_value),2) AS revenue
FROM fact_orders o
JOIN dim_customers c
    ON o.customer_key = c.customer_key
JOIN fact_payments p
    ON o.order_id = p.order_id
GROUP BY c.customer_state
ORDER BY revenue DESC;