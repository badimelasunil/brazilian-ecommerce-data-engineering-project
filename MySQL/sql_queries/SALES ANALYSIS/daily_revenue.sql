SELECT
    d.full_date AS order_date,
    ROUND(SUM(p.payment_value),2) AS revenue,

    ROUND(
        AVG(SUM(p.payment_value))
        OVER(
            ORDER BY d.full_date
            ROWS BETWEEN 6 PRECEDING AND CURRENT ROW
        ),2
    ) AS moving_avg_7days

FROM fact_orders o

JOIN fact_payments p
    ON o.order_id = p.order_id

JOIN dim_dates d
    ON o.purchase_date_key = d.date_key

GROUP BY d.full_date

ORDER BY d.full_date;


