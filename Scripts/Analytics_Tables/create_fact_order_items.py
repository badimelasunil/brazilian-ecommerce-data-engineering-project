



# ============================================
# CREATE fact_order_items.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASETS
# ============================================

order_items = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_order_items.csv"
)

products = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_products.csv"
)

sellers = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_sellers.csv"
)

# ============================================
# CREATE PRODUCT KEY
# ============================================

products["product_key"] = range(
    1,
    len(products) + 1
)

# ============================================
# CREATE SELLER KEY
# ============================================

sellers["seller_key"] = range(
    1,
    len(sellers) + 1
)

# ============================================
# MERGE PRODUCT KEY
# ============================================

fact_order_items = order_items.merge(
    products[["product_id", "product_key"]],
    on="product_id",
    how="left"
)

# ============================================
# MERGE SELLER KEY
# ============================================

fact_order_items = fact_order_items.merge(
    sellers[["seller_id", "seller_key"]],
    on="seller_id",
    how="left"
)

# ============================================
# CONVERT SHIPPING DATE
# ============================================

fact_order_items["shipping_limit_date"] = pd.to_datetime(
    fact_order_items["shipping_limit_date"]
)

# ============================================
# CREATE SHIPPING DATE KEY
# ============================================

fact_order_items["shipping_limit_date_key"] = (
    fact_order_items["shipping_limit_date"]
    .dt.strftime("%Y%m%d")
)

# ============================================
# FINAL FACT TABLE
# ============================================

fact_order_items = fact_order_items[[
    "order_id",
    "product_key",
    "seller_key",
    "shipping_limit_date_key",
    "price",
    "freight_value"
]]

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(fact_order_items.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(fact_order_items.duplicated().sum())

# ============================================
# SAVE FACT TABLE
# ============================================

fact_order_items.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\fact_order_items.csv",
    index=False
)

print("\nfact_order_items.csv CREATED SUCCESSFULLY")
print(fact_order_items.head())



fact_order_items[
    fact_order_items.duplicated()
].head()



# py create_fact_order_items.py