SELECT 
    s.seller_id,
    ROUND(SUM(oi.price),2) AS revenue
FROM fact_order_items oi
JOIN dim_sellers s
    ON oi.seller_key = s.seller_key
GROUP BY s.seller_id
ORDER BY revenue DESC
LIMIT 10;