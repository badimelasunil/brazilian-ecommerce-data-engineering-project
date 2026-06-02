# ============================================
# CREATE dim_geolocation.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASET
# ============================================

geo = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_geolocation.csv"
)

# ============================================
# REMOVE DUPLICATES
# ============================================

geo = geo.drop_duplicates()

# ============================================
# CREATE GEOLOCATION KEY
# ============================================

geo["geo_key"] = range(
    1,
    len(geo) + 1
)

# ============================================
# FINAL DIMENSION TABLE
# ============================================

dim_geolocation = geo[[
    "geo_key",
    "geolocation_zip_code_prefix",
    "geolocation_city",
    "geolocation_state",
    "geolocation_lat",
    "geolocation_lng"
]]

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(dim_geolocation.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(dim_geolocation.duplicated().sum())

# ============================================
# SAVE FILE
# ============================================

dim_geolocation.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_geolocation.csv",
    index=False
)

print("\ndim_geolocation.csv CREATED SUCCESSFULLY")
print(dim_geolocation.head())






# py create_dim_geolocation.py