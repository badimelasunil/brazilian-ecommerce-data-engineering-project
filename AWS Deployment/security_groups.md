# Security Group Configuration

## Overview

This document describes the AWS Security Group configuration used for the Brazilian E-Commerce Data Engineering Project deployed on Amazon EC2.

---

## Security Group Details

| Parameter           | Value                                       |
| ------------------- | ------------------------------------------- |
| Security Group Name | brazilian-ecommerce-sg                      |
| VPC                 | Default VPC                                 |
| Purpose             | Control inbound and outbound network access |

---

## Inbound Rules

### SSH Access

Used to connect securely to the EC2 instance.

| Type | Protocol | Port | Source |
| ---- | -------- | ---- | ------ |
| SSH  | TCP      | 22   | My IP  |

---

### MariaDB Access

Used to allow database connections.

| Type       | Protocol | Port | Source |
| ---------- | -------- | ---- | ------ |
| Custom TCP | TCP      | 3306 | My IP  |

---

## Outbound Rules

Default outbound access was enabled.

| Type        | Protocol | Port Range | Destination |
| ----------- | -------- | ---------- | ----------- |
| All Traffic | All      | All        | 0.0.0.0/0   |

---

## Security Best Practices

* Restricted SSH access to trusted IP addresses.
* Restricted MariaDB access to authorized connections only.
* Avoided exposing database ports publicly to all internet users.
* Used AWS Security Groups as the primary network firewall.

---

## Validation

Verified EC2 connectivity using:

```bash
ssh -i key.pem ec2-user@<public-ip>
```

Verified MariaDB service:

```bash
sudo systemctl status mariadb
```

Verified active listening port:

```bash
sudo ss -tulpn | grep 3306
```

---

## Deployment Status

Security Groups were successfully configured to provide secure access to the EC2 instance and MariaDB Data Warehouse while following AWS security best practices.
