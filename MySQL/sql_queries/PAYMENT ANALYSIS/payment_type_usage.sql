SELECT 
    pt.payment_type,
    COUNT(*) AS total_transactions
FROM fact_payments fp
JOIN dim_payment_types pt
    ON fp.payment_type_key = pt.payment_type_key
GROUP BY pt.payment_type
ORDER BY total_transactions DESC;