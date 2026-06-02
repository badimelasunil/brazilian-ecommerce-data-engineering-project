import pandas as pd

#LOAD DATA 
orders = pd.read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\orders.csv")

#PRINT FIRST 5 ROWS
print("\n FIRST 5 ROWS")
print(orders.head())

#PRINT DATA INFORMATION
print("\n DATA INFO")
print(orders.info())

# COLUMNS
print("\n PRINT ALL COLUMNS")
print(orders.columns)


# CONVERT DATATYPE str TO DATETIME
# # SINGLE Str CONVERTS TO DATETIME
# orders[" order_purchase_timestamp"] = pd.to_datetime(
#     orders[" order_purchase_timestamp"]
# )


# MULTIPLE DATATYPES CONVERTED str to DATETIME
print("\n MULTIPLE DATATYPES CONVERTED str to DATETIME")
date_columns = [
    'order_purchase_timestamp',
    'order_approved_at',
    'order_delivered_carrier_date',
    'order_delivered_customer_date',
    'order_estimated_delivery_date'
]
for col in date_columns:
    orders[col] = pd.to_datetime(orders[col])


#OFTER DATATYPE CONVERT
print("\n OFTER DATATYPE CONVERT")
print(orders.info())


# CHECK TOTAL NO.OF NULL VALUES 
print("\n CHECK TOTAL NO.OF NULL VALUES ")
print(orders.isnull(). sum(). sum())


# CHECK NULL VALUES
print("\n CHECK NULL VALUES ")
print(orders.isnull(). sum())

# CHECK DUPLICATE VALUES
print("\n CHECK DUPLICATE VALUES ")
print(orders.duplicated(). sum())

# Check Unique Order Status
print("\n ORDER STATUS COUNTS")
print(orders['order_status'].value_counts())



# Save Cleaned_orders  CSV file
orders.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_orders.csv",
    index = False
)

print("\n Cleaned_orders successfuly saves ")




# py cleaned_orders.py


