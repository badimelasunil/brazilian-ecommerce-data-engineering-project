import pandas as pd 

# LOAD DATA FILE CSV
product_category = pd.read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\product_category.csv")

# PRINT FIRST 5 ROWS
print("\n FIRST 5 ROWS")
print(product_category.head())

# PRINT ABOUT THE DATASET INFORMATION
print("\n DATASET INFO")
print(product_category.info())

# COLUMNS 
print("\n COLUMN CHECK")
print(product_category.columns)

# CHECK DATA TYPES 
print("DATA TYPES CHECKING ")
print(product_category.dtypes)

# CKECK NULL VALUES
print("\n NULL VALUES ")
print(product_category.isnull(). sum())

# DUPLICATES CHECKING
print("\n DUPLICATES CHECKING")
print(product_category.duplicated(). sum())



# SAVE cleaned_product_category CSV FILE 
product_category.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_product_category.csv",
    index = False
)
print("\n cleaned_product_category file successfuly save")




# py cleaned_product_category.py