# ============================================
# CREATE fact_orders.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASETS
# ============================================

orders = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_orders.csv"
)

customers = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_customers.csv"
)

geolocation = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_geolocation.csv"
)

# ============================================
# CREATE CUSTOMER KEY
# ============================================

customers["customer_key"] = range(
    1,
    len(customers) + 1
)

# ============================================
# CREATE GEO KEY
# ============================================

geolocation["geo_key"] = range(
    1,
    len(geolocation) + 1
)

# ============================================
# MERGE CUSTOMER KEY + ZIP CODE
# ============================================

fact_orders = orders.merge(
    customers[[
        "customer_id",
        "customer_key",
        "customer_zip_code_prefix"
    ]],
    on="customer_id",
    how="left"
)

# ============================================
# MERGE GEO KEY
# ============================================

fact_orders = fact_orders.merge(
    geolocation[[
        "geo_key",
        "geolocation_zip_code_prefix"
    ]],
    left_on="customer_zip_code_prefix",
    right_on="geolocation_zip_code_prefix",
    how="left"
)

# ============================================
# CONVERT DATE COLUMNS
# ============================================

date_columns = [
    "order_purchase_timestamp",
    "order_approved_at",
    "order_delivered_customer_date",
    "order_estimated_delivery_date"
]

for col in date_columns:
    fact_orders[col] = pd.to_datetime(
        fact_orders[col]
    )

# ============================================
# CREATE DATE KEYS
# ============================================

fact_orders["purchase_date_key"] = (
    fact_orders["order_purchase_timestamp"]
    .dt.strftime("%Y%m%d")
)

fact_orders["approved_date_key"] = (
    fact_orders["order_approved_at"]
    .dt.strftime("%Y%m%d")
)

fact_orders["delivered_date_key"] = (
    fact_orders["order_delivered_customer_date"]
    .dt.strftime("%Y%m%d")
)

fact_orders["estimated_delivery_date_key"] = (
    fact_orders["order_estimated_delivery_date"]
    .dt.strftime("%Y%m%d")
)

# ============================================
# DELIVERY METRICS
# ============================================

fact_orders["delivery_days"] = (
    fact_orders["order_delivered_customer_date"] -
    fact_orders["order_purchase_timestamp"]
).dt.days

fact_orders["estimated_vs_actual_days"] = (
    fact_orders["order_delivered_customer_date"] -
    fact_orders["order_estimated_delivery_date"]
).dt.days

# ============================================
# FINAL FACT TABLE
# ============================================

fact_orders = fact_orders[[
    "order_id",
    "customer_key",
    "geo_key",
    "purchase_date_key",
    "approved_date_key",
    "delivered_date_key",
    "estimated_delivery_date_key",
    "order_status",
    "delivery_days",
    "estimated_vs_actual_days"
]]

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(fact_orders.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(fact_orders.duplicated().sum())

# ============================================
# SAVE FILE
# ============================================

fact_orders.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\fact_orders.csv",
    index=False
)

print("\n fact_orders.csv CREATED SUCCESSFULLY")
print(fact_orders.head())



# py create_fact_orders.py