# ads-measurement-conversion-tracking-simulator
Production-grade simulator for Ads measurement, conversion tracking, and attribution workflows. Demonstrates event validation, attribution models, SQL analytics, ROI optimization, and troubleshooting of advertiser measurement pipelines at scale.


This project demonstrates how accurate measurement, validation, and troubleshooting directly impact advertiser trust and return on investment (ROI).

---

##  Overview

Ads measurement is one of the most critical components of digital advertising.  
Incorrect conversion tracking, attribution errors, or data inconsistencies can lead to:

- Misreported performance
- Incorrect optimization decisions
- Loss of advertiser trust

This simulator models an **end-to-end ads measurement pipeline**, allowing teams to ingest events, apply attribution models, validate data accuracy, and analyze ROI.

---

##  Key Capabilities

- **Event Ingestion**
  - Simulates ad events such as impressions, clicks, and conversions
  - Supports structured event validation

- **Attribution Modeling**
  - Last-Click Attribution
  - Linear Attribution
  - Time-Decay Attribution

- **Measurement Validation**
  - Detects missing or duplicate events
  - Validates timestamps, user identifiers, and campaign mapping
  - Highlights data inconsistencies using SQL analytics

- **ROI Analysis**
  - Calculates advertiser ROI based on revenue and ad spend
  - Identifies anomalies caused by measurement errors

- **Dashboard Visualization**
  - Simple frontend to inspect measurement outputs
  - Enables quick debugging and insights

---

## 🧠 Why This Project Matters

In large-scale advertising systems, **measurement accuracy is as important as delivery**.

This project reflects real responsibilities of:
- Customer & Partner Solutions Engineers
- Ads Measurement Specialists
- gTech Ads / Scaled Technical Services teams

It demonstrates how **bespoke partner issues** can be transformed into **reusable, scalable solutions**.

---

## 🏗️ Architecture
Frontend (Dashboard)
↓
Backend API (Event Ingestion & Attribution)
↓
Attribution Engine & Validation Layer
↓
SQL Analytics & ROI Computation


The system is modular by design, enabling independent scaling and troubleshooting of each layer.

---

## 🧩 Tech Stack

| Layer | Technology |
|-----|-----------|
| Backend | Python (Flask) |
| Frontend | JavaScript, HTML, CSS |
| Database | SQLite / PostgreSQL |
| Analytics | SQL |
| Infra | Docker, Docker Compose |
| CI | GitHub Actions |

---

## ▶️ Getting Started

### Prerequisites
- Docker
- Docker Compose

### Run Locally
```bash
docker-compose up --build
```
Backend API: http://localhost:5000

Dashboard: http://localhost:3000

📊 Attribution Models Explained

Last Click
Credits the final interaction before conversion.

Linear
Distributes credit equally across all interactions.

Time Decay
Assigns higher weight to interactions closer to conversion.

These models help simulate how attribution choices affect performance reporting and optimization.

🔍 Measurement Troubleshooting Examples

This simulator can help identify:

Missing conversion tags

Duplicate events

Invalid timestamps

Incorrect attribution windows

ROI inconsistencies caused by data errors

🧪 Testing & Reliability

Unit tests validate attribution logic

Modular services simplify debugging

CI pipeline ensures code consistency

📁 Repository Structure
backend/        → API, attribution logic, validation services
frontend/       → Dashboard UI
sql/            → Schemas and analytics queries
docs/           → Architecture & best practices
scripts/        → Event simulation tools
.github/        → CI workflows

📈 Future Enhancements

Support for multi-touch conversion paths

Configurable attribution windows

Real-time event streaming simulation

Advanced advertiser reporting dashboards

📌 Intended Audience

This project is designed for:

Ads & measurement engineers

Partner solutions engineers

Technical consultants

Anyone interested in large-scale advertising systems

