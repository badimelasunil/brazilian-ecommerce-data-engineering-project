SELECT 
    seller_id,
    revenue,
    RANK() OVER (ORDER BY revenue DESC) AS seller_rank
FROM (
    SELECT 
        s.seller_id,
        SUM(oi.price) AS revenue
    FROM fact_order_items oi
    JOIN dim_sellers s
        ON oi.seller_key = s.seller_key
    GROUP BY s.seller_id
) t;