SELECT 
    seller_state,
    COUNT(*) AS total_sellers
FROM dim_sellers
GROUP BY seller_state
ORDER BY total_sellers DESC;