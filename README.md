# FinOps-project
# 📊 FinOps Dashboard for AWS Free Tier Tracking

This project tracks AWS usage and costs using the Cost Explorer API, storing daily cost metrics in a local SQLite database, and visualizing trends in Grafana. It helps ensure that AWS Free Tier limits aren't breached unknowingly.

## 🚀 Features
- Fetches daily AWS cost data using boto3
- Stores data in SQLite for persistence
- Visualizes usage trends in Grafana
- Optional alerts for Free Tier breaches
- Automated with CRON for daily monitoring

## 🧰 Technologies Used
- **AWS EC2 Ubuntu 22.04**
- **Python (boto3)**
- **SQLite**
- **AWS CLI**
- **Grafana**
- **Cron Jobs**

## 📦 Setup Instructions

### 1. Configure AWS CLI
```bash
aws configure

### 2. Run the Cost Fetch Script
python3 fetch_costs.py

**### 3. Automate with Cron**
crontab -e
# Add:
0 1 * * * /usr/bin/python3 /home/ubuntu/fetch_costs.py


