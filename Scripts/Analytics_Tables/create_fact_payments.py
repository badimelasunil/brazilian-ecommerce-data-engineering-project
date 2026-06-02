# ============================================
# CREATE fact_payments.csv
# ============================================

import pandas as pd

# ============================================
# LOAD DATASET
# ============================================

payments = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_order_payments.csv"
)

# ============================================
# CREATE PAYMENT TYPE DIMENSION
# ============================================

payment_types = payments[[
    "payment_type"
]].drop_duplicates()

payment_types["payment_type_key"] = range(
    1,
    len(payment_types) + 1
)

# ============================================
# MERGE PAYMENT TYPE KEY
# ============================================

fact_payments = payments.merge(
    payment_types,
    on="payment_type",
    how="left"
)

# ============================================
# FINAL FACT TABLE
# ============================================

fact_payments = fact_payments[[
    "order_id",
    "payment_type_key",
    "payment_sequential",
    "payment_installments",
    "payment_value"
]]

# ============================================
# NULL VALUES CHECK
# ============================================

print("\n NULL VALUES")
print(fact_payments.isnull().sum())

# ============================================
# DUPLICATES CHECK
# ============================================

print("\n DUPLICATES")
print(fact_payments.duplicated().sum())

# ============================================
# SAVE FACT TABLE
# ============================================

fact_payments.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\fact_payments.csv",
    index=False
)

# ============================================
# FINAL PAYMENT TYPE DIMENSION
# ============================================

payment_types = payment_types[[
    "payment_type_key",
    "payment_type"
]]

# ============================================
# SAVE DIMENSION TABLE
# ============================================

payment_types.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_payment_types.csv",
    index=False
)

print("\nfact_payments.csv CREATED SUCCESSFULLY")
print(fact_payments.head())

print("\ndim_payment_types.csv CREATED SUCCESSFULLY")
print(payment_types.head())





# py create_fact_payments.py