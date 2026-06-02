import pandas as pd

# LOAD DATASET CSV 
cleaned_customers = pd.read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\customers.csv")

# PRINT FIRST 5 ROWS
print("\n FIRST 5 ROWS DATA")
print(cleaned_customers.head())


# CSV DATASET INFORMATION
print("\n DATASET INFORMATION")
print(cleaned_customers.info())


# CHECK NULL VALUES
print("\n NULL VALUES CHECH")
print(cleaned_customers.isnull(). sum())

# CHECK DUPLICATES IN DATASET
print("\n CHECK DUPLICATES")
print(cleaned_customers.duplicated(). sum())


# SAVE cleaned_customers CSV FILE 
cleaned_customers.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_customers.csv",
    index = False
    )
print("\n cleaned_customers file successfuly save")




# py cleaned_customers.py