# ============================================
# CREATE dim_customers.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASET
# ============================================

customers = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_customers.csv"
)

# ============================================
# CREATE CUSTOMER KEY
# ============================================

customers["customer_key"] = range(
    1,
    len(customers) + 1
)

# ============================================
# FINAL DIMENSION TABLE
# ============================================

dim_customers = customers[[
    "customer_key",
    "customer_id",
    "customer_unique_id",
    "customer_zip_code_prefix",
    "customer_city",
    "customer_state"
]]

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(dim_customers.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(dim_customers.duplicated().sum())

# ============================================
# SAVE FILE
# ============================================

dim_customers.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_customers.csv",
    index=False
)

print("\ndim_customers.csv CREATED SUCCESSFULLY")
print(dim_customers.head())





#  py create_dim_customers.py