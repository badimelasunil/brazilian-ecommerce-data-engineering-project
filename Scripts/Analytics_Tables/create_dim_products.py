# ============================================
# CREATE dim_products.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASET
# ============================================

products = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_products.csv"
)

# ============================================
# CREATE PRODUCT KEY
# ============================================

products["product_key"] = range(
    1,
    len(products) + 1
)

# ============================================
# FINAL DIMENSION TABLE
# ============================================

dim_products = products[[
    "product_key",
    "product_id",
    "product_category_name",
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]]

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(dim_products.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(dim_products.duplicated().sum())

# ============================================
# SAVE FILE
# ============================================

dim_products.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_products.csv",
    index=False
)

print("\ndim_products.csv CREATED SUCCESSFULLY")
print(dim_products.head())






# py create_dim_products.py