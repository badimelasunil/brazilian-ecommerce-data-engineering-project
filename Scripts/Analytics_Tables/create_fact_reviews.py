# ============================================
# CREATE fact_reviews.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASET
# ============================================

reviews = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_order_reviews.csv"
)

# ============================================
# CONVERT DATE COLUMNS
# ============================================

reviews["review_creation_date"] = pd.to_datetime(
    reviews["review_creation_date"]
)

reviews["review_answer_timestamp"] = pd.to_datetime(
    reviews["review_answer_timestamp"]
)

# ============================================
# CREATE DATE KEYS
# ============================================

reviews["review_creation_date_key"] = (
    reviews["review_creation_date"]
    .dt.strftime("%Y%m%d")
)

reviews["review_answer_timestamp_key"] = (
    reviews["review_answer_timestamp"]
    .dt.strftime("%Y%m%d")
)

# ============================================
# FINAL FACT TABLE
# ============================================

fact_reviews = reviews[[
    "review_id",
    "order_id",
    "review_score",
    "review_creation_date_key",
    "review_answer_timestamp_key"
]]

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(fact_reviews.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(fact_reviews.duplicated().sum())

# ============================================
# SAVE FACT TABLE
# ============================================

fact_reviews.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\fact_reviews.csv",
    index=False
)

print("\n fact_reviews.csv CREATED SUCCESSFULLY")
print(fact_reviews.head())



# py create_fact_reviews.py