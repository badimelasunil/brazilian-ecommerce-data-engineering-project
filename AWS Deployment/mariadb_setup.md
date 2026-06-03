# MariaDB Data Warehouse Setup

## Overview

This document describes the installation and configuration of MariaDB on AWS EC2 for the Brazilian E-Commerce Data Engineering Project.

---

## Install MariaDB

Update the server:

```bash
sudo dnf update -y
```

Install MariaDB Server:

```bash
sudo dnf install mariadb105-server -y
```

---

## Start MariaDB Service

Start MariaDB:

```bash
sudo systemctl start mariadb
```

Enable automatic startup:

```bash
sudo systemctl enable mariadb
```

Verify service status:

```bash
sudo systemctl status mariadb
```

Expected Status:

```text
active (running)
```

---

## Access MariaDB

Open MariaDB console:

```bash
sudo mysql
```

Expected:

```text
Welcome to the MariaDB monitor
```

---

## Create Data Warehouse Database

Create database:

```sql
CREATE DATABASE brazilian_ecommerce_dw;
```

Verify database creation:

```sql
SHOW DATABASES;
```

Expected:

```text
brazilian_ecommerce_dw
```

---

## Create Application User

Create user:

```sql
CREATE USER 'sunil'@'localhost' IDENTIFIED BY 'Sunil123';
```

Grant privileges:

```sql
GRANT ALL PRIVILEGES ON brazilian_ecommerce_dw.* TO 'sunil'@'localhost';
```

Apply changes:

```sql
FLUSH PRIVILEGES;
```

---

## Load Data Warehouse Tables

Python ETL scripts were executed to load dimension and fact tables into MariaDB.

Dimension Tables:

```text
dim_customers
dim_dates
dim_geolocation
dim_payment_types
dim_products
dim_sellers
```

Fact Tables:

```text
fact_order_items
fact_orders
fact_payments
fact_reviews
```

---

## Validate Tables

```sql
USE brazilian_ecommerce_dw;
SHOW TABLES;
```

Expected:

```text
10 Tables
```

---

## Validate Record Counts

```sql
SELECT
(SELECT COUNT(*) FROM dim_customers) AS customers,
(SELECT COUNT(*) FROM dim_products) AS products,
(SELECT COUNT(*) FROM dim_sellers) AS sellers,
(SELECT COUNT(*) FROM fact_order_items) AS order_items,
(SELECT COUNT(*) FROM fact_orders) AS orders,
(SELECT COUNT(*) FROM fact_payments) AS payments,
(SELECT COUNT(*) FROM fact_reviews) AS reviews;
```

Results:

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

## Deployment Status

MariaDB was successfully installed on AWS EC2 and configured as the cloud-hosted data warehouse for the Brazilian E-Commerce Data Engineering Project.
