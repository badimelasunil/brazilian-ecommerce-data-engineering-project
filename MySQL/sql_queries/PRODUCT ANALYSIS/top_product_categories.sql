SELECT 
    pr.product_category_name,
    COUNT(*) AS total_sales
FROM fact_order_items oi
JOIN dim_products pr
    ON oi.product_key = pr.product_key
GROUP BY pr.product_category_name
ORDER BY total_sales DESC
LIMIT 10;