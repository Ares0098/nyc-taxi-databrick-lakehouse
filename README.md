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

Example table: main.bronze.bronze_taxi_trips

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

Example table: main.silver.silver_taxi_trips

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

Public Dataset (NYC Taxi)
↓
Bronze (Raw Delta Table)
↓
Silver (Cleaned & Enriched)
↓
Gold (Aggregated Analytics Tables)

---

## Key Features

- End-to-end **Medallion Architecture implementation**
- Use of **Delta Lake** for ACID-compliant data storage
- Separation of ingestion, transformation, and analytics layers
- Handling of real-world data issues (invalid records, division by zero)
- Modular and scalable project structure

---

## Project Structure
