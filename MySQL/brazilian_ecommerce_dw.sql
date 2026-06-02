CREATE DATABASE brazilian_ecommerce_dw;

USE brazilian_ecommerce_dw;

-- To See Data From Every Table

SELECT * FROM dim_customers LIMIT 500;

SELECT * FROM dim_sellers LIMIT 500;

SELECT * FROM dim_products LIMIT 500;

SELECT * FROM dim_dates LIMIT 500;

SELECT * FROM dim_geolocation LIMIT 500;

SELECT * FROM dim_payment_types LIMIT 10;

SELECT * FROM fact_orders LIMIT 500;

SELECT * FROM fact_payments LIMIT 500;

SELECT * FROM fact_reviews LIMIT 500;

SELECT * FROM fact_order_items LIMIT 500;


-- To See Structure of Every Table

DESCRIBE dim_customers;

DESCRIBE dim_sellers;

DESCRIBE dim_products;

DESCRIBE dim_dates;

DESCRIBE dim_geolocation;

DESCRIBE dim_payment_types;

DESCRIBE fact_orders;

DESCRIBE fact_order_items;

DESCRIBE fact_payments;

DESCRIBE fact_reviews;


-- To Count Rows in Every Table

SELECT COUNT(*) FROM dim_customers;

SELECT COUNT(*) FROM dim_sellers;

SELECT COUNT(*) FROM dim_products;

SELECT COUNT(*) FROM dim_dates;

SELECT COUNT(*) FROM dim_geolocation;

SELECT COUNT(*) FROM dim_payment_types;

SELECT COUNT(*) FROM fact_orders;

SELECT COUNT(*) FROM fact_order_items;

SELECT COUNT(*) FROM fact_payments;

SELECT COUNT(*) FROM fact_reviews;


ALTER TABLE dim_dates
MODIFY full_date DATE;


DESCRIBE dim_customers;
DESCRIBE dim_products;
DESCRIBE dim_dates;
DESCRIBE dim_geolocation;
DESCRIBE dim_payment_types;
DESCRIBE dim_sellers;
DESCRIBE fact_orders;
DESCRIBE fact_payments;
DESCRIBE fact_order_items;
DESCRIBE dm_reviews;

drop table dm_reviews;




CREATE OR REPLACE VIEW vw_customer_360 AS
SELECT 
    c.customer_unique_id,
    c.customer_city,
    c.customer_state,

    COUNT(DISTINCT o.order_id) AS total_orders,

    ROUND(SUM(p.payment_value),2) AS total_spent,

    ROUND(AVG(p.payment_value),2) AS avg_order_value,

    ROUND(AVG(r.review_score),2) AS avg_review_score,

    ROUND(AVG(o.delivery_days),2) AS avg_delivery_days

FROM fact_orders o

JOIN dim_customers c
    ON o.customer_key = c.customer_key

JOIN fact_payments p
    ON o.order_id = p.order_id

LEFT JOIN fact_reviews r
    ON o.order_id = r.order_id

GROUP BY
    c.customer_unique_id,
    c.customer_city,
    c.customer_state;


SELECT * FROM vw_customer_360
LIMIT 10;



