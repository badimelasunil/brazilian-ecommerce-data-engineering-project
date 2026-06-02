# load_dim_customers.py

import pandas as pd
from sqlalchemy import create_engine

# MYSQL CONNECTION
username = "root"
password = "Sunil123"
host = "localhost"
database = "brazilian_ecommerce_dw"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

# LOAD CSV
df = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_customers.csv"
)

print(df.head())

# LOAD TO MYSQL
df.to_sql(
    name="dim_customers",
    con=engine,
    if_exists="replace",
    index=False
)

print("dim_customers LOADED SUCCESSFULLY")




# py load_dim_customers.py