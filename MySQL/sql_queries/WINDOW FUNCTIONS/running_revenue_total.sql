SELECT 
    d.year,
    d.month,
    ROUND(SUM(p.payment_value),2) AS monthly_revenue,
    
    ROUND(
        SUM(SUM(p.payment_value)) OVER (
            ORDER BY d.year, d.month
        ),2
    ) AS running_total
FROM fact_orders o
JOIN dim_dates d
    ON o.purchase_date_key = d.date_key
JOIN fact_payments p
    ON o.order_id = p.order_id
GROUP BY d.year, d.month;