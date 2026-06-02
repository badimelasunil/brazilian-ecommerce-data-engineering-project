SELECT
    ROUND(SUM(payment_value),2) AS total_revenue
FROM fact_payments;