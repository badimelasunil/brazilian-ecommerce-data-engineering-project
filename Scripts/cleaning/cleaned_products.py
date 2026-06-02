import pandas as pd 

# LOAD DATA CSV FILE
products =pd.read_csv (r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\products.csv")

# PRINT FIRST 5 ROWS
print("\n FIRST 5 ROWS")
print(products.head())

# PRINT ABOUT THE DATASET INFORMATION
print("\n DATASET INFO ")
print(products.info())

# DATASET COLUMNS
print("\n DATASET COLUMNS")
print(products.columns)


# CHECK NULL VALUES
print("\n CHECK NULL VALUES")
print(products.isnull().sum())


# CHECK TOTAL NO.OF DUPLICATE VALUES
print("\n TOTAL NO.OF DUPLICATES")
print(products.isnull(). sum().sum())

# CHECK DUPLICATES IN DATASET
print("\n CHECK DUPLICATED VALUES")
print(products.duplicated().sum())


# Handle categorical nulls
products["product_category_name"] = products["product_category_name"].fillna("unknown")

# Handle metadata numeric nulls
metadata_cols = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty"
]

for col in metadata_cols:
    products[col] = products[col].fillna(0)

# Handle dimension nulls using median
dimension_cols = [
    "product_weight_g",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for col in dimension_cols:
    products[col] = products[col].fillna(products[col].median())

# Convert datatypes
int_cols = [
    "product_name_lenght",
    "product_description_lenght",
    "product_photos_qty",
    "product_length_cm",
    "product_height_cm",
    "product_width_cm"
]

for col in int_cols:
    products[col] = products[col].astype("int64")


# PRINT ABOUT THE DATASET INFORMATION
print("\n DATASET INFO AFTER CLEANING ")
print(products.info())

# CHECK NULL VALUES
print("\n CHECK NULL VALUES")
print(products.isnull().sum())

# Check duplicate rows
print("\n Check duplicate rows ")
print(products.duplicated().sum())

# Check duplicate product IDs
print("\n Check duplicate product IDs")
print(products["product_id"].duplicated().sum())

# Final shape
print("\n Final shape")
print(products.shape)


# SPELLING MISTAKES 
print("\n CORRECT SPELLING IN COLUMN NAMES")

products.rename(columns={
    "product_name_lenght": "product_name_length",
    "product_description_lenght": "product_description_length"
}, inplace=True)

print(products.columns)

# Save Cleaned_products CSV FILE
products.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\Cleaned_products.csv",
    index=False
)
print("Cleaned_products file saved successfully")





# py cleaned_products.py