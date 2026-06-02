# Brazilian E-Commerce Data Engineering Project
------------------------------------------------

## Project Overview
-------------------
Designed and developed an end-to-end Data Engineering and Business Intelligence solution using the Brazilian E-Commerce Public Dataset. The project transforms raw transactional data into a scalable analytical platform through ETL processing, dimensional data modeling, SQL analytics, interactive Power BI dashboards, and AWS cloud deployment architecture.

\## Objectives
---------------
\* Build a scalable data pipeline

\* Design a Star Schema Data Warehouse

\* Perform business analytics using SQL

\* Create interactive Power BI dashboards

\* Deploy the solution on AWS


\## Technology Stack
-------------------
\### Programming
\* Python

\* SQL

\### Data Processing
\* Pandas

\* NumPy 

\* VS Code

\### Database
\* MySQL

\### Business Intelligence
\* Power BI
\* DAX

\### Cloud
\* AWS

##Development Tools
\*VS Code, Git, GitHub


-------------------------------------------------
| Category               | Technologies         |
| ---------------------- | -------------------- |
| Programming            | Python, SQL          |
| Data Processing        | Pandas, NumPy        |
| Database               | MySQL                |
| Data Warehousing       | Star Schema Modeling |
| Business Intelligence  | Power BI, DAX        |
| Workflow Orchestration | Apache Airflow       |
| Cloud Platform         | AWS (EC2, S3, RDS)   |
| Development Tools      | VS Code, Git, GitHub |
-------------------------------------------------

\## Project Architecture
------------------------
Raw Data (CSV Files)

↓

Python ETL Pipeline

↓

Data Cleaning \& Transformation

↓

MySQL Data Warehouse

↓

Fact \& Dimension Tables

↓

Analytics SQL Views

↓

Power BI Dashboards

↓

Business Insights



\## PROJECT STUCTURE
----------------
Brazilian\_Ecommerce\_Data/
│
├── README.md
│
├── requirements.txt
│
├── .gitignore
│
├── Data/
│   │
│   ├── raw\_data/
│   │   │
│   │   ├── customers.csv
│   │   │
│   │   ├── sellers.csv
│   │   │
│   │   ├── products.csv
│   │   │
│   │   ├── product\_category.csv
│   │   │
│   │   ├── geolocation.csv
│   │   │
│   │   ├── orders.csv
│   │   │
│   │   ├── order\_items.csv
│   │   │
│   │   ├── order\_payments.csv
│   │   │
│   │   └── order\_reviews.csv
│   │  
│   │
│   └── cleaned\_data/
│   │   │
│   │   ├── cleaned\_customers.csv
│   │    │
│   │    ├── cleaned\_sellers.csv
│   │    │
│   │    ├── cleaned\_products.csv
│   │    │
│   │    ├── cleaned\_product\_category.csv
│   │    │
│   │    ├── cleaned\_geolocation.csv
│   │    │
│   │    ├── cleaned\_orders.csv
│   │    │
│   │    ├── cleaned\_order\_items.csv
│   │    │
│   │    ├── cleaned\_order\_payments.csv
│   │    │
│   │    └── cleaned\_order\_reviews.csv
│   │
│   │
│   └── Analytics_Tables/
│        │
│        ├── fact_orders.csv   
│        │
│        ├── fact_reviews.csv
│        │
│        ├── fact_payments.csv
│        │
│        ├── fact_order_items.csv
│        │
│        ├── dim_customers.csv
│        │
│        ├── dim_sellers.csv
│        │
│        ├── dim_products.csv
│        │
│        ├── dim_geolocation.csv
│        │
│        ├── dim_dates.csv
│        │
│        └── dim_payment_types.csv
│
│
├── scripts/
│   │
│   ├── cleaning/
│   │   │
│   │   ├── clean\_customers.py
│   │   │
│   │   ├── clean\_sellers.py
│   │   │
│   │   ├── clean\_products.py
│   │   │
│   │   ├── clean\_product\_category.py
│   │   │
│   │   ├── clean\_geolocation.py
│   │   │
│   │   ├── clean\_orders.py
│   │   │
│   │   ├── clean\_order\_items.py
│   │   │
│   │   ├── clean\_order\_payments.py
│   │   │
│   │   ├── clean\_order\_reviews.py
│   │   │
│   │   └── create\_state\_lookup.py
│   │
│   │
│   │
│   ├── warehouse/Analytics_Tables
│   │   │
│   │   ├── create\_dim\_customers.py
│   │   │
│   │   ├── create\_dim\_sellers.py
│   │   │
│   │   ├── create\_dim\_products.py
│   │   │
│   │   ├── create\_dim\_geolocation.py
│   │   │
│   │   ├── create\_dim\_dates.py
│   │   │
│   │   ├── create\_fact\_orders.py
│   │   │
│   │   ├── create\_fact\_order\_items.py
│   │   │
│   │   ├── create\_fact\_payments.py
│   │   │
│   │   └── create\_fact\_reviews.py
│   │
│   │
│   │
│   ├── loading/
│        │
│    	 ├── db\_connection.py
│   	 │
│   	 ├── load\_dim\_customers.py
│ 		 │
│  		 ├── load\_dim\_sellers.py
│  		 │
│  		 ├── load\_dim\_products.py
│  		 │
│  		 ├── load\_dim\_geolocation.py
│   	 │
│  		 ├── load\_dim\_dates.py
│  		 │
│  		 ├── load\_dim\_payment\_types.py
│  		 │
│  		 ├── load\_fact\_orders.py
│  		 │
│  		 ├── load\_fact\_order\_items.py
│  		 │
│  		 ├── load\_fact\_payments.py
│  		 │
│  		 └── load\_fact\_reviews.py
│   
│
│
├── MySQL/
│   │
│   ├── sql_queries
│
│
│
├── dashboard/
│    │
│    ├── POWER BI/
│         │
│         ├── E-commerce.pbix
│         │
│         └── Power BI Dashboards Screen Shorts/
│
│
└── Documentation/
    │
    └── Brazilian E-Commerce Data Engineering & Business Intelligence Project.PPT/
    │
    └── Brazilian E-Commerce Analytics Platform.final document/
    │
    └──Images/



\### Data Warehouse Schema
--------------------------
Dimension Tables
----------------
dim\_customers

dim\_products

dim\_sellers

dim\_dates

dim\_geolocation

dim\_payment\_types


 Fact Tables
-------------
fact\_orders

fact\_order\_items

fact\_payments

fact\_reviews


\### ETL Pipeline Features
--------------------------
Raw Data Validation

Data Cleaning & Standardization

Missing Value Handling

Duplicate Removal

Data Transformation

Fact & Dimension Table Creation

Automated Data Loading

Data Quality Checks



\### SQL Analytics
-------------------
Developed 30+ analytical SQL queries covering:

Revenue Analytics

Customer Analytics

Product Analytics

Seller Analytics

Payment Analytics

Delivery Analytics

Review Analytics

Geographical Analytics

Window Functions

Advanced Business Intelligence Queries


\## Power BI Dashboards
------------------------
Executive Dashboard
-------------------
Revenue KPIs
Order KPIs
Customer KPIs
Business Performance Metrics

Sales Dashboard
----------------
Revenue Trends
Category Performance
Top Products
Growth Analysis

Customer Dashboard
-------------------
Customer Segmentation
Customer Distribution
Purchase Behavior

Seller Dashboard
-----------------
Seller Performance
Revenue Contribution
Order Fulfillment Metrics

Delivery Dashboard
-------------------
Delivery Performance
Shipping Analysis
Order Completion Trends

Payment Dashboard
------------------
Payment Method Analysis
Payment Distribution
Revenue Contribution


\## Key Achievements
---------------------
Processed 9 Raw Datasets

Built 6 Dimension Tables

Created 4 Fact Tables

Developed 30+ SQL Analytics Queries

Designed 7 Business Intelligence Views

Implemented 35+ DAX Measures

Built Multiple Interactive Power BI Dashboards

Designed AWS Cloud Deployment Architecture


\## AWS Deployment Architecture
----------------------------------
The solution is designed for cloud deployment using AWS services:
Amazon EC2 – Application Hosting
Amazon RDS – Managed MySQL Database
Amazon S3 – Data Storage
AWS IAM – Security & Access Control
Amazon CloudWatch – Monitoring & Logging


\## Skills Demonstrated
------------------------
Data Engineering

ETL Pipeline Development

Data Warehousing

Dimensional Modeling

SQL Analytics

Business Intelligence

Power BI Development

DAX

Cloud Architecture

AWS Services

Data Visualization




# How to Run the Project
------------------------

## Prerequisites

- Python 3.10+
- MySQL Server 8.0+
- Power BI Desktop
- Git

## Step 1: Clone the Repository

```bash
git clone https://github.com/yourusername/Brazilian_Ecommerce_Analytics.git
cd Brazilian_Ecommerce_Analytics
```

## Step 2: Install Required Packages

```bash
pip install -r requirements.txt
```

## Step 3: Create MySQL Database

```sql
CREATE DATABASE brazilian_ecommerce_dw;
```

## Step 4: Run ETL Pipeline

Execute the ETL scripts to clean, transform, and load data into the data warehouse.

```bash
python etl/customer_etl.py
python etl/product_etl.py
python etl/seller_etl.py
python etl/order_etl.py
```

## Step 5: Create Data Warehouse Objects

Run SQL scripts to create dimension tables, fact tables, and business views.

```sql
SOURCE sql/create_dimension_tables.sql;
SOURCE sql/create_fact_tables.sql;
SOURCE sql/create_business_views.sql;
```

## Step 6: Open Power BI Dashboard

1. Open the `Brazilian E-Commerce Data Engineering & Business Intelligence Project.pbix` file in Power BI Desktop.
2. Connect to the MySQL Data Warehouse.
3. Refresh the dataset.
4. Explore the dashboards.

## Available Dashboards

- KPI Analysis
- Sales Analysis
- Customer Analysis
- Product Analysis
- Seller Analysis
- Delivery Analysis
- Payment Analysis
- Review Analysis
- Geolocation Analysis




\## Author
------------

Sunil Badimela

Email:badimelasunil92@gmail.com

Data Engineer | Business Intelligence Developer



