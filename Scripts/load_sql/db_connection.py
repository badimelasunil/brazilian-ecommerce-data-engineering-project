# db_connection.py

from sqlalchemy import create_engine

username = "root"
password = "Sunil123"
host = "localhost"
database = "brazilian_ecommerce_dw"

engine = create_engine(
    f"mysql+pymysql://{username}:{password}@{host}/{database}"
)

print("MYSQL CONNECTION SUCCESSFUL")



# py db_connection.py