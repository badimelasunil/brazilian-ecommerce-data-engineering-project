# ============================================
# CREATE dim_dates.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASETS
# ============================================

orders = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_orders.csv"
)

reviews = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_order_reviews.csv"
)

order_items = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_order_items.csv"
)

# ============================================
# COLLECT ALL DATE COLUMNS
# ============================================

all_dates = pd.concat([

    pd.to_datetime(orders["order_purchase_timestamp"]),
    pd.to_datetime(orders["order_approved_at"]),
    pd.to_datetime(orders["order_delivered_customer_date"]),
    pd.to_datetime(orders["order_estimated_delivery_date"]),

    pd.to_datetime(reviews["review_creation_date"]),
    pd.to_datetime(reviews["review_answer_timestamp"]),

    pd.to_datetime(order_items["shipping_limit_date"])

], ignore_index=True)

# ============================================
# REMOVE NULL VALUES
# ============================================

all_dates = all_dates.dropna()

# ============================================
# CREATE UNIQUE DATE TABLE
# ============================================

dim_dates = pd.DataFrame({
    "full_date": all_dates.dt.date.unique()
})

# ============================================
# CONVERT TO DATETIME
# ============================================

dim_dates["full_date"] = pd.to_datetime(
    dim_dates["full_date"]
)

# ============================================
# CREATE DATE ATTRIBUTES
# ============================================

dim_dates["date_key"] = (
    dim_dates["full_date"]
    .dt.strftime("%Y%m%d")
)

dim_dates["day"] = dim_dates["full_date"].dt.day

dim_dates["month"] = dim_dates["full_date"].dt.month

dim_dates["month_name"] = (
    dim_dates["full_date"]
    .dt.month_name()
)

dim_dates["quarter"] = (
    dim_dates["full_date"]
    .dt.quarter
)

dim_dates["year"] = dim_dates["full_date"].dt.year

dim_dates["week_day"] = (
    dim_dates["full_date"]
    .dt.day_name()
)

dim_dates["weekend_flag"] = (
    dim_dates["full_date"]
    .dt.weekday >= 5
)

# ============================================
# REORDER COLUMNS
# ============================================

dim_dates = dim_dates[[
    "date_key",
    "full_date",
    "day",
    "month",
    "month_name",
    "quarter",
    "year",
    "week_day",
    "weekend_flag"
]]

# ============================================
# SORT VALUES
# ============================================

dim_dates = dim_dates.sort_values(
    by="full_date"
)

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(dim_dates.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(dim_dates.duplicated().sum())

# ============================================
# SAVE FILE
# ============================================

dim_dates.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_dates.csv",
    index=False
)

print("\ndim_dates.csv CREATED SUCCESSFULLY")
print(dim_dates.head())







# py create_dim_dates.py