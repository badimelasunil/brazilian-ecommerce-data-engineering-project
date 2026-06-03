# EC2 Instance Setup

## Overview

This document describes the AWS EC2 setup used for deploying the Brazilian E-Commerce Data Engineering Project.

## EC2 Configuration

| Parameter         | Value                          |
| ----------------- | ------------------------------ |
| Cloud Provider    | AWS                            |
| Service           | Amazon EC2                     |
| Region            | Asia Pacific (Mumbai)          |
| Availability Zone | ap-south-1b                    |
| Operating System  | Amazon Linux 2023              |
| Instance Type     | t3.micro                       |
| Instance Name     | brazilian-ecommerce-etl-server |

---

## Launch EC2 Instance

1. Open AWS Console.
2. Navigate to EC2 Dashboard.
3. Click **Launch Instance**.
4. Configure the following:

### Instance Details

* Name: `brazilian-ecommerce-etl-server`
* AMI: Amazon Linux 2023
* Instance Type: t3.micro
* Key Pair: Existing or New Key Pair
* Network: Default VPC

---

## Security Group Configuration

Inbound Rules:

| Type       | Port | Source |
| ---------- | ---- | ------ |
| SSH        | 22   | My IP  |
| Custom TCP | 3306 | My IP  |

---

## Connect to EC2

AWS Console → EC2 → Instances → Connect

Use EC2 Instance Connect to open a browser-based terminal.

---

## Verify Instance

Run:

```bash
hostname
```

Run:

```bash
cat /etc/os-release
```

Expected:

```text
Amazon Linux 2023
```

---

## Update Server

```bash
sudo dnf update -y
```

---

## Install Python

```bash
sudo dnf install python3 python3-pip git -y
```

Verify:

```bash
python3 --version
pip3 --version
```

---

## Clone GitHub Repository

```bash
git clone https://github.com/YOUR_USERNAME/brazilian-ecommerce-data-engineering-project.git
```

```bash
cd brazilian-ecommerce-data-engineering-project
```

---

## Create Virtual Environment

```bash
python3 -m venv venv
```

Activate:

```bash
source venv/bin/activate
```

---

## Install Project Dependencies

```bash
pip install -r requirements.txt
```

---

## Deployment Status

EC2 instance successfully configured and used to deploy the Brazilian E-Commerce Data Engineering Project.
