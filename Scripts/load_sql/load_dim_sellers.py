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

print("MYSQL CONNECTION SUCCESSFUL")

# LOAD CSV
df = pd.read_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Analytics_Tables\dim_sellers.csv"
)

print("\n FIRST 5 ROWS")
print(df.head())

print("\n DATA INFO")
print(df.info())

# LOAD TO MYSQL
df.to_sql(
    name="dim_sellers",
    con=engine,
    if_exists="replace",
    index=False
)

print("\n dim_sellers LOADED SUCCESSFULLY")




# py load_dim_sellers.py