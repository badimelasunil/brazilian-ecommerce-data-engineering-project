SELECT
    ROUND(AVG(payment_value),2) AS avg_order_value
FROM fact_payments;