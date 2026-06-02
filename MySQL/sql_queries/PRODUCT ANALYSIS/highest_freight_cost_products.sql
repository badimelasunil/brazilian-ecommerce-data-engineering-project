SELECT 
    pr.product_category_name,
    ROUND(AVG(oi.freight_value),2) AS avg_freight
FROM fact_order_items oi
JOIN dim_products pr
    ON oi.product_key = pr.product_key
GROUP BY pr.product_category_name
ORDER BY avg_freight DESC
LIMIT 10;