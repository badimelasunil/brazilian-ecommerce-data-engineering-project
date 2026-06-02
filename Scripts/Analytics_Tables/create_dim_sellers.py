# ============================================
# CREATE dim_sellers.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASET
# ============================================

sellers = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_sellers.csv"
)

# ============================================
# CREATE SELLER KEY
# ============================================

sellers["seller_key"] = range(
    1,
    len(sellers) + 1
)

# ============================================
# FINAL DIMENSION TABLE
# ============================================

dim_sellers = sellers[[
    "seller_key",
    "seller_id",
    "seller_zip_code_prefix",
    "seller_city",
    "seller_state"
]]

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(dim_sellers.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(dim_sellers.duplicated().sum())

# ============================================
# SAVE FILE
# ============================================

dim_sellers.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_sellers.csv",
    index=False
)

print("\ndim_sellers.csv CREATED SUCCESSFULLY")
print(dim_sellers.head())







# py create_dim_sellers.py