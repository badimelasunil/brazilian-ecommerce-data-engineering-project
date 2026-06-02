SELECT
    pr.product_category_name,
    ROUND(SUM(py.payment_value),2) AS revenue

FROM fact_order_items oi

JOIN dim_products pr
    ON oi.product_id = pr.product_id

JOIN fact_payments py
    ON oi.order_id = py.order_id

GROUP BY pr.product_category_name

ORDER BY revenue DESC
LIMIT 10;