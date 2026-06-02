import pandas as pd

# Load Dataset
order_items = pd. read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\order_items.csv")

# Show First 5 Rows
print("\n FIRST 5 ROWS")
print(order_items.head())

# Dataset Information
print("\n DATASET INFO")
print(order_items.info())

# Null Values
print("\n NULL VALUES")
print(order_items.isnull().sum())

# Duplicate Values
print("\n DUPLICATES")
print(order_items.duplicated().sum())

# Convert Datetime
order_items["shipping_limit_date"] = pd.to_datetime(
    order_items["shipping_limit_date"]
)

# Verify Datatype
print("\n UPDATED DATA TYPES")
print(order_items.info())


# Save Cleaned File CSV
order_items.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_order_items.csv",
    index=False
)
print("Cleaned file saved successfully")


#py cleaned_order_items.py