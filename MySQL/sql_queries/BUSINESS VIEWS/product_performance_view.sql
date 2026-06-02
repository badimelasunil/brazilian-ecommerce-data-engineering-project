
CREATE OR REPLACE VIEW vw_product_performance AS
SELECT 
    pr.product_category_name,

    COUNT(*) AS total_items_sold,

    ROUND(SUM(oi.price),2) AS total_sales,

    ROUND(SUM(oi.freight_value),2) AS total_freight,

    ROUND(AVG(oi.price),2) AS avg_product_price,

    ROUND(AVG(r.review_score),2) AS avg_review_score

FROM fact_order_items oi

JOIN dim_products pr
    ON oi.product_key = pr.product_key

LEFT JOIN fact_reviews r
    ON oi.order_id = r.order_id

GROUP BY
    pr.product_category_name;
    
    

SELECT *
FROM vw_product_performance
LIMIT 10;