import pandas as pd

# LOAD DATASET CSV FILE
sellers = pd.read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\sellers.csv")
print("CSV FILE IS SUCCESSFULY LOADED")

# PRINT FIRST 5 ROWS
print("\n FIRST 5 ROWS")
print(sellers.head())

# PRINT ABOUT THE DATASET INFORMATION
print("\n DATASET INFO")
print(sellers.info())

# DATASET COLUMNS 
print("\n DATASET COLUMNS")
print(sellers.columns)


# CHECK NULL VALUES
print("\n CHECK NULL VALUES")
print(sellers.isnull(). sum())

# PRINT TOTAL NO.OF NULL VALUES
print("\n TOATAL NO.OF NULL VALUES")
print(sellers.isnull(). sum(). sum())


# CHECK DUPLICATES IN DATASET
print("\n CHECK DUPLICATE VALUES")
print(sellers.duplicated(). sum())


# Check Unique Order Status
print("\n seller_id COUNTS")
print(sellers['seller_id'].value_counts())


# CHECK ABNORMAL DES
print("\n CHECK ABNORMAL DESCRIPTION")
print(sellers.describe())


# Convert city names to lowercase
print("\n Convert city names to lowercase")
sellers["seller_city"] = sellers["seller_city"].str.lower().str.strip()


# Strip spaces from state names
print("\n  Strip spaces from state names ")
sellers["seller_state"] = sellers["seller_state"].str.strip()

# PRINT FIRST 5 ROWS
print("\n FIRST 5 ROWS")
print(sellers.head())



sellers.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_sellers.csv",
    index = False
)

print("\n cleaned_sellers CSV FILE SAVED SUCCSSESS FULLY")



# py cleaned_sellers.py