CREATE OR REPLACE VIEW vw_executive_sales_summary AS
SELECT 
    d.year,
    d.quarter,
    d.month,
    d.month_name,

    COUNT(DISTINCT o.order_id) AS total_orders,

    ROUND(SUM(p.payment_value),2) AS total_revenue,

    ROUND(
        SUM(p.payment_value) /
        COUNT(DISTINCT o.order_id),
    2) AS avg_order_value,

    ROUND(AVG(o.delivery_days),2) AS avg_delivery_days

FROM fact_orders o

JOIN dim_dates d
    ON o.purchase_date_key = d.date_key

JOIN fact_payments p
    ON o.order_id = p.order_id

GROUP BY
    d.year,
    d.quarter,
    d.month,
    d.month_name;