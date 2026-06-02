import pandas as pd

# LOAD DATA
order_payments = pd.read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\order_payments.csv")

# show first 5 rows
print("\n FIRST 5 ROWS" )
print(order_payments.head())

# data information
print("\n DATA INFO")
print(order_payments.info())

# check null values
print("\n NULL VALUES")
print(order_payments.isnull(). sum())

# TOTAL NULL VALUES IN ENTIRE DATASET
print("\n TOTAL NULL VALUES ")
print(order_payments. isnull(). sum(). sum())

# CHECH DUPLICATES
print("\n CHECK ANY DUPLICATES")
print(order_payments.duplicated(). sum())

# DROP DUPLICATS
print("\n DROP DUPLICATES")
print(order_payments.drop_duplicates())


# CHECH DUPLICATES
print("\n CHECK ANY DUPLICATES")
print(order_payments.duplicated(). sum())


# CHECK ANY OBNARMAL VALUES
print("\n ANY OBNARMAL VALUES")
print(order_payments.describe())


# COLUMN NAMES
print("\n COLUMN NAMES")
print(order_payments.columns)

# IDENTIFY DATATYPES
print("\n DATA TYPES")
print(order_payments.dtypes)

# CHECK NEGATIVE VALUES
print("\n CHECK NEGATIVE VALUES")

numeric_cols = ['payment_sequential',  'payment_installments',  'payment_value']

for col in numeric_cols:
    print(F"{col} :", (order_payments[col] < 0) . sum())

# UNIQUE PAYMENT TYPES
print("\n UNIQUE PAYMENT TYPES")
print(order_payments['payment_type'].unique())

# STANDARDIZE PAYMENT TYPE
order_payments['payment_type'] = order_payments['payment_type'].str.lower().str.strip()

# FINAL SHAPE
# shape gives the size of the DataFrame
print("\n FINAL SHAPE")
print(order_payments.shape)


# payment_installments has minimum value 0
print(order_payments[order_payments['payment_installments'] == 0])


# Very high payments may be outliers.
print(order_payments[order_payments['payment_value'] > 5000])

# replace payment mode 'unknown', TO 'COD'
order_payments['payment_type'] = order_payments["payment_type"].replace('not_defined', 'unknown')

print(order_payments['payment_type'].unique())

# installments usually start from 1 to n
# avoids abnormal values in dashboards/analytics
order_payments['payment_installments'] = order_payments['payment_installments'].replace(0, 1)




# Save Cleaned File CSV
order_payments.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_order_payments.csv",
    index=False
)
print("Cleaned file saved successfully")





#py cleaned_order_payments.py
