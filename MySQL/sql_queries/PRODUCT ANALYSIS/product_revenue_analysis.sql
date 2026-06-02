SELECT 
    pr.product_category_name,
    ROUND(SUM(oi.price),2) AS revenue
FROM fact_order_items oi
JOIN dim_products pr
    ON oi.product_key = pr.product_key
GROUP BY pr.product_category_name
ORDER BY revenue DESC;