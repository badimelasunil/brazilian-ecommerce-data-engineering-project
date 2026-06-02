SELECT
    d.year,
    d.month_name,
    ROUND(SUM(p.payment_value),2) AS revenue

FROM fact_orders o

JOIN fact_payments p
ON o.order_id = p.order_id

JOIN dim_dates d
ON o.purchase_date_key = d.date_key

GROUP BY d.year, d.month_name
ORDER BY d.year, revenue DESC;



-- Ctrl + Shift + P
-- SQLTools: Add New Connection