# import pandas as pd

# # LOAD DATASET CSV
# geolocation = pd.read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\geolocation.csv")
# print("\n DATASET SUCCESSFULY LOADED")

# # PRINT FIRST 5 ROWS
# print("\n FIRST 5 ROWS")
# print(geolocation.head())

# # PRINT ABOUT THE DATASET INFORMATION
# print("\n DATASET INFO")
# print(geolocation.info())

# # COLUMNS
# print("\n COLUMN NAME")
# print(geolocation.columns)

# # CHECK NULL VALUES
# print("\n CHECK NULL VALUES")
# print(geolocation.isnull(). sum())

# # CHECK DUPLICATES
# print("\n CHECK DUPLICATE VALUES")
# print(geolocation.duplicated(). sum())  



# You can explain in interviews:

# "The raw geolocation dataset contained multiple coordinate 
# samples for the same ZIP code prefix.I aggregated the data to create 
# a standardized ZIP-level geolocation lookup table for efficient analytics and joins."

# That sounds very professional.
import pandas as pd

# LOAD DATASET
geolocation = pd.read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\geolocation.csv")
print("\n DATASET SUCCESSFULY LOADED")

print("\n DATASET SUCCESSFULLY LOADED")

# LOWERCASE CITY NAMES
geolocation["geolocation_city"] = geolocation["geolocation_city"].str.lower().str.strip()

# GROUP BY ZIP CODE PREFIX
cleaned_geo = (
    geolocation.groupby("geolocation_zip_code_prefix")
    .agg({
        "geolocation_lat": "mean",
        "geolocation_lng": "mean",
        "geolocation_city": "first",
        "geolocation_state": "first"
    })
    .reset_index()
)

print("\n FINAL CLEANED DATA")
print(cleaned_geo.head())

# CHECK NULL VALUES
print("\n CHECK NULL VALUES")
print(cleaned_geo.isnull(). sum())

# CHECK DUPLICATES
print("\n CHECK DUPLICATE VALUES")
print(cleaned_geo.duplicated().sum())


print("\n SHAPE AFTER CLEANING")
print(cleaned_geo.shape)



# SAVE CLEANED FILE
cleaned_geo.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_geolocation.csv",
    index=False
)

print("\n CLEANED GEOLOCATION FILE SAVED SUCCESSFULLY")



# Interview-Level Explanation
# You can explain:

# "The raw geolocation dataset contained multiple coordinate samples per ZIP prefix. 
# I aggregated the records to create a standardized ZIP-level lookup table using mean latitude and longitude,
#  improving storage efficiency and analytical performance."

# Very strong explanation.






# py cleaned_geolocation.py