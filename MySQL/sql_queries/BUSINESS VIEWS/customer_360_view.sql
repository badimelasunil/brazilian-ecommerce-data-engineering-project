

CREATE OR REPLACE VIEW vw_customer_360 AS
SELECT 
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,

    COUNT(DISTINCT o.order_id) AS total_orders,

    ROUND(SUM(p.payment_value),2) AS total_spent,

    ROUND(AVG(p.payment_value),2) AS avg_order_value,

    ROUND(AVG(r.review_score),2) AS avg_review_score,

    ROUND(AVG(o.delivery_days),2) AS avg_delivery_days

FROM fact_orders o

JOIN dim_customers c
    ON o.customer_key = c.customer_key

JOIN fact_payments p
    ON o.order_id = p.order_id

LEFT JOIN fact_reviews r
    ON o.order_id = r.order_id

GROUP BY
    c.customer_unique_id,
    c.customer_city,
    c.customer_state;