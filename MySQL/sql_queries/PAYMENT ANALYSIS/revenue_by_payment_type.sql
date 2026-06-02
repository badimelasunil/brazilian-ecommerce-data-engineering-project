SELECT 
    pt.payment_type,
    ROUND(SUM(fp.payment_value),2) AS revenue
FROM fact_payments fp
JOIN dim_payment_types pt
    ON fp.payment_type_key = pt.payment_type_key
GROUP BY pt.payment_type
ORDER BY revenue DESC;