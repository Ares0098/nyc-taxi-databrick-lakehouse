# NYC Taxi Lakehouse (Databricks + Delta)

## Overview

This project implements a modern **Lakehouse data pipeline** using Databricks and Delta Lake, based on the public **NYC Taxi Trip dataset**.

The objective is to simulate a realistic **end-to-end data engineering workflow**, transforming raw data into analytics-ready datasets using a structured, production-inspired approach.

The pipeline follows the **Medallion Architecture**, organizing data into progressive layers:

- **Bronze** → raw ingestion  
- **Silver** → cleaned and validated data  
- **Gold** → business-level aggregations  

---

## Dataset

This project uses the **NYC Taxi Trip Record Data**, a large-scale public dataset containing detailed records of taxi trips in New York City.

Each record includes:

- pickup and dropoff timestamps  
- passenger count  
- trip distance  
- fare and tip amounts  
- location identifiers  

This dataset is commonly used to benchmark distributed data processing and analytics workloads.

---

## Architecture

The pipeline is built using a **Lakehouse architecture** with Delta Lake tables.

### Bronze Layer

The Bronze layer stores **raw ingested data** with minimal transformation.

Responsibilities:

- ingest raw Parquet data from external source  
- preserve original schema  
- append ingestion metadata (e.g. ingestion timestamp, source file)  

Data is stored as **Delta tables backed by external storage**, following lakehouse principles by decoupling compute and storage.

Example table: `main.bronze.bronze_taxi_trips`

In semi-structured use cases, the Bronze layer can also store raw JSON payloads to accommodate schema evolution and unpredictable data structures.

---

### Silver Layer

The Silver layer transforms raw data into a **clean and reliable dataset**.

Key operations:

- remove invalid records (e.g. negative fares, zero distance)  
- standardize timestamp fields  
- handle null values  
- derive new features  

Derived columns include:

- `trip_duration_minutes`  
- `trip_speed_kmh`  
- `pickup_date`  

Example table: `main.silver.silver_taxi_trips`

---

### Gold Layer

The Gold layer contains **aggregated, business-ready datasets** optimized for analytics and reporting.

Example tables:

- `gold_monthly_revenue` → revenue trends over time  
- `gold_trip_distance_stats` → trip behavior analysis  
- `gold_tip_analysis` → tipping patterns by passenger count  

These tables are designed for:

- dashboarding  
- business insights  
- analytical queries  

---

## Data Flow

NYC Taxi Dataset (External Source)  
→ Bronze Layer (Raw Ingestion - Delta)  
→ Silver Layer (Cleaned & Standardized)  
→ Gold Layer (Business Aggregations)

---

## Key Features

- End-to-end **Medallion Architecture implementation**  
- Use of **Delta Lake** for ACID-compliant data storage  
- Separation of ingestion, transformation, and analytics layers  
- Handling of real-world data issues (invalid records, division by zero)  
- Modular and scalable project structure  

---

## Project Structure

The repository is organized into a modular and scalable structure:

- `src/` → core data pipeline logic (Bronze, Silver, Gold, configuration)  
- `notebooks/` → Databricks entry points to execute pipelines  
- `sql/` → schema and volume setup scripts  
- `tests/` → (planned) unit and integration tests  

---

## Technologies Used

- Databricks  
- Apache Spark (PySpark)  
- Delta Lake  
- Python  
- Git / GitHub  

---

## Key Learnings

Through this project, I explored:

- Designing a **Lakehouse architecture** from scratch  
- Implementing **Medallion data modeling (Bronze/Silver/Gold)**  
- Using Delta Lake for reliable and scalable data storage  
- Handling platform-specific constraints (e.g. Unity Catalog, metadata columns)  
- Building modular and maintainable data pipelines  

---

## Future Improvements

Planned enhancements:

- Migrate data storage to external cloud storage (e.g. S3 / ADLS) for better scalability and production alignment  
- Incremental processing using Delta MERGE  
- Data quality validation layer  
- Unit and integration testing (pytest)  
- CI/CD pipeline integration  
- Workflow orchestration (e.g. scheduling pipelines)  
- Performance optimization (partitioning, OPTIMIZE, VACUUM)  
- Local-first development workflow to enable debugging and validation outside Databricks  
- Environment parity between local Spark and Databricks runtime (configs, dependencies, data access)  
- Decoupling pipeline logic from platform-specific utilities (e.g. dbutils)  

---

## License

This project is intended for educational and portfolio purposes.