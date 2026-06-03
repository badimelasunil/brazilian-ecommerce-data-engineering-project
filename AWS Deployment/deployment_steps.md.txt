# AWS Deployment Steps

## Project Overview

This document describes the complete deployment workflow of the Brazilian E-Commerce Data Engineering Project on AWS EC2 using Python, MariaDB, SQL Analytics, and Power BI.

---

# Deployment Architecture

```text
Brazilian E-Commerce Dataset
            │
            ▼
      Data Cleaning
       (Python ETL)
            │
            ▼
   Analytics Table Creation
            │
            ▼
      AWS EC2 Instance
            │
            ▼
    MariaDB Data Warehouse
            │
            ▼
      SQL Analytics Layer
            │
            ▼
     Power BI Dashboard
            │
            ▼
      Business Insights
```

---

# Step 1: Upload Project to GitHub

Push the complete project repository to GitHub.

Repository includes:

* Data
* Scripts
* MySQL
* Dashboard
* Documentation
* README.md

---

# Step 2: Launch AWS EC2 Instance

Configuration:

| Parameter     | Value                        |
| ------------- | ---------------------------- |
| OS            | Amazon Linux 2023            |
| Instance Type | t3.micro                     |
| Region        | Mumbai                       |
| Purpose       | ETL & Data Warehouse Hosting |

---

# Step 3: Connect to EC2

Use EC2 Instance Connect through AWS Console.

Verify:

```bash
hostname
```

---

# Step 4: Install Required Software

Install Python:

```bash
sudo dnf install python3 python3-pip git -y
```

Install MariaDB:

```bash
sudo dnf install mariadb105-server -y
```

Start MariaDB:

```bash
sudo systemctl start mariadb
sudo systemctl enable mariadb
```

---

# Step 5: Clone Repository

```bash
git clone <repository-url>
cd brazilian-ecommerce-data-engineering-project
```

---

# Step 6: Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
```

---

# Step 7: Install Python Libraries

```bash
pip install -r requirements.txt
```

Libraries include:

* pandas
* numpy
* sqlalchemy
* pymysql
* matplotlib
* seaborn

---

# Step 8: Create Data Warehouse

Login:

```bash
sudo mysql
```

Create database:

```sql
CREATE DATABASE brazilian_ecommerce_dw;
```

---

# Step 9: Configure Database User

```sql
CREATE USER 'sunil'@'localhost' IDENTIFIED BY 'Sunil123';
GRANT ALL PRIVILEGES ON brazilian_ecommerce_dw.* TO 'sunil'@'localhost';
FLUSH PRIVILEGES;
```

---

# Step 10: Load Dimension Tables

Executed ETL scripts:

```text
load_dim_customers.py
load_dim_dates.py
load_dim_geolocation.py
load_dim_payment_types.py
load_dim_products.py
load_dim_sellers.py
```

Created:

```text
dim_customers
dim_dates
dim_geolocation
dim_payment_types
dim_products
dim_sellers
```

---

# Step 11: Load Fact Tables

Executed ETL scripts:

```text
load_fact_order_items.py
load_fact_orders.py
load_fact_payments.py
load_fact_reviews.py
```

Created:

```text
fact_order_items
fact_orders
fact_payments
fact_reviews
```

---

# Step 12: Validate Data Warehouse

Verify tables:

```sql
SHOW TABLES;
```

Result:

```text
10 tables created successfully
```

Verify record counts:

| Table            | Records |
| ---------------- | ------: |
| dim_customers    |  99,441 |
| dim_products     |  32,951 |
| dim_sellers      |   3,095 |
| fact_order_items | 112,650 |
| fact_orders      |  99,441 |
| fact_payments    | 103,886 |
| fact_reviews     |  99,224 |

---

# Step 13: Execute SQL Analytics

Created analytics queries for:

* KPI Analysis
* Sales Analysis
* Customer Analysis
* Product Analysis
* Seller Analysis
* Delivery Analysis
* Payment Analysis
* Review Analysis
* Geolocation Analysis
* Advanced Analytics
* Window Functions

---

# Step 14: Build Power BI Dashboard

Dashboard Modules:

* Executive KPI Dashboard
* Sales Analysis
* Customer Analysis
* Product Analysis
* Seller Analysis
* Delivery Analysis
* Payment Analysis
* Review Analysis

---

# Deployment Outcome

Successfully deployed an end-to-end Data Engineering and Business Intelligence solution on AWS EC2 using MariaDB as a cloud-hosted data warehouse and Power BI for interactive analytics and reporting.
