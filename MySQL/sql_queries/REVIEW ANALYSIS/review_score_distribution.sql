SELECT 
    review_score,
    COUNT(*) AS total_reviews
FROM fact_reviews
GROUP BY review_score
ORDER BY review_score;