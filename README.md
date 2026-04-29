# 🚀 Mining Telemetry Lakehouse Pipeline (ADF + Databricks + Delta Lake)

## 📌 Overview
This project simulates a real-world enterprise data engineering pipeline for mining fleet telemetry data.

The system processes **daily snapshot-based telemetry data** (messages, logs, audit files) using Azure Data Factory for orchestration and Databricks (PySpark) for distributed processing, implementing a robust **Bronze–Silver–Gold Lakehouse architecture**.

---

## 🏗️ Architecture

- **Azure Data Factory (ADF)** → Orchestration using metadata-driven pipeline  
- **Azure Data Lake Storage (ADLS Gen2)** → Raw + Processed storage  
- **Azure Databricks** → PySpark-based transformations  
- **Delta Lake** → ACID-compliant storage with versioning  

---

## 🔄 End-to-End Data Flow

1. **Snapshot ingestion**
   - Daily telemetry snapshot contains:
     - `messages/` → equipment telemetry data  
     - `logs/` → operational logs  
     - `audit/` → ingestion trigger  

2. **Event-driven orchestration**
   - ADF pipeline triggers on **audit file arrival**

3. **ADF pipeline execution**
   - Lookup → ForEach (customer/site/date)
   - Pass dynamic parameters to Databricks

4. **Databricks processing**
   - Bronze → Raw ingestion  
   - Silver → Cleaning, validation, deduplication  
   - Gold → KPI aggregation  

---

## 📂 Project Structure


adf/ → ADF pipeline configurations (Lookup, ForEach, triggers)
notebooks/ → Databricks notebooks (Bronze, Silver, Gold processing)
data/ → Sample telemetry snapshots (messages, logs, audit)
sql/ → Analytical queries (KPIs, validation checks)
cicd/ → Deployment configs (Databricks CLI / CI-CD ready)
README.md → Project documentation


---

## 🥉 Bronze Layer (Raw Ingestion)
- Ingest raw telemetry and logs from ADLS
- Append metadata:
  - ingestion timestamp
  - file source
- Store as **Delta tables**

---

## 🥈 Silver Layer (Data Processing)
- Data cleaning & validation:
  - Remove duplicates using window functions
  - Validate fuel values (invalid < 0)
- Log parsing for operational insights
- Schema enforcement

---

## 🥇 Gold Layer (Business KPIs)

Generate analytics-ready datasets:

- 🚛 Load & Dump Cycles  
- ⛽ Fuel Consumption Analysis  
- ⚙️ Equipment Utilization  
- 📉 Idle Time Detection  

---

## ⚙️ Key Features

- ✔ Snapshot-based ingestion design  
- ✔ Metadata-driven ADF orchestration  
- ✔ Bronze–Silver–Gold architecture  
- ✔ Delta Lake ACID guarantees  
- ✔ Idempotent pipeline design  
- ✔ Window functions for deduplication  
- ✔ Scalable PySpark transformations  

---

## 🔁 Failure Handling & Replay Strategy

- Audit/control mechanism tracks snapshot processing status  
- Failed loads can be safely **reprocessed from Bronze layer**  
- Ensures:
  - No data loss  
  - No duplicate processing  

---

## 📊 Sample Technologies Used

- PySpark (Data processing)
- SQL (Analytics)
- Delta Lake (Storage)
- Azure Data Factory (Orchestration)
- ADLS Gen2 (Storage)

---

## 🚀 How to Run (Conceptual)

1. Upload telemetry snapshot data to ADLS
2. Trigger ADF pipeline (via audit file)
3. ADF orchestrates Databricks notebooks
4. Data flows through Bronze → Silver → Gold
5. Query Gold tables for insights

---



---

## 💡 Interview Talking Points

This project demonstrates:
- Real-world lakehouse architecture design  
- Distributed data processing using Spark  
- Handling of data quality and replay scenarios  
- Enterprise pipeline orchestration using ADF  

---

## 👨‍💻 Author
**Gourish Shiragur**
