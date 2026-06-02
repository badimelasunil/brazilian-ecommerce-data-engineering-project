import pandas as pd 

#LOAD CSV FILE DATA 
order_reviews = pd.read_csv(r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\Raw data\order_reviews.csv")

#PRINT FIRST 5 ROWS
print("\n FIRST 5 ROWS")
print(order_reviews.head())

#INFORMATION ABOUT DATASET
print("\n DATASET INFO")
print(order_reviews.info())

#CONVERT review_creation_date STR TO DATATIME
print("\n review_creation_date Str TO DATETIME  ")
order_reviews["review_creation_date"] = pd.to_datetime(
    order_reviews["review_creation_date"]
)


#INFORMATION ABOUT DATASET
print("\n DATASET INFO")
print(order_reviews.info())

#CONVERT review_answer_timestamp Str TO DATETIME 
print("\n CONVERT review_answer_timestamp Str TO DATETIME " )
order_reviews["review_answer_timestamp"] = pd.to_datetime(
    order_reviews["review_answer_timestamp"]
)


#INFORMATION ABOUT DATASET
print("\n DATASET INFO")
print(order_reviews.info())

#TOTAL NULL VALUES IN ENTIRE DATASET
print("\n  TOTAL NULL VALUES IN ENTIRE DATASET" )
print(order_reviews.isnull(). sum().sum())

#CHECK NULL VALUES
print("\n CHECK NULL VALUES")
print(order_reviews.isnull(). sum())



#Fill Null Values IDENTIFY THE NULL VALUES COLUMNS
order_reviews["review_comment_title"] = order_reviews["review_comment_title"].fillna("No Title")
order_reviews["review_comment_message"] = order_reviews["review_comment_message"].fillna("No Comment")


# Verify Nulls Again
print("\n AFTER FIX NULL VALUES Verify Nulls Again")
print(order_reviews.isnull(). sum())


# CHECK DUPLICATES
print("\n CHECK DUPLICATES")
print(order_reviews.duplicated(). sum())


#COLUMN NAMES 
print("\n COLUMN VALUES")
print(order_reviews.columns)



# CHECK INVALIDATE REVIEWS 
print("\n Validate Review Scores")
print(order_reviews["review_score"]. unique())




# Save Cleaned File CSV
order_reviews.to_csv(
    r"C:\Users\manip\Downloads\HYD IN\PYTHON IMP\DATA ENGINEERING PROJECT\Brazilian_Ecommerce_Data\Data\cleaned data\cleaned_order_reviews.csv",
    index=False
)
print("Cleaned file saved successfully")

# py cleaned_order_reviews.py
