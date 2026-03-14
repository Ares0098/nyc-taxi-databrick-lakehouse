# NYC Taxi Lakehouse (Databricks + Delta)

## Overview

This project demonstrates a modern **Lakehouse data pipeline** built using Databricks and Delta Lake with the public **NYC Taxi Trip dataset**.

The goal of this project is to simulate a realistic **data engineering workflow**:

- ingest raw data into a Bronze layer
- clean and standardize data in a Silver layer
- build analytics-ready tables in a Gold layer

The implementation follows the **Medallion Architecture**, which separates data processing into progressive layers of refinement.

---

## Dataset

This project uses the **NYC Taxi Trip Record Data**, a public dataset containing millions of taxi trips in New York City.

Each record contains trip-level information such as:

- pickup and dropoff timestamps
- passenger count
- trip distance
- fare amount
- pickup and dropoff locations

The dataset is widely used for benchmarking distributed data processing systems.

---

## Architecture

The pipeline follows a **Lakehouse architecture** built on top of Delta Lake tables.

### Bronze Layer

The Bronze layer stores **raw ingested data** with minimal transformation.

Responsibilities:

- ingest raw parquet files
- preserve original schema
- add ingestion metadata if necessary

Example table : bronze_taxi_trips

### Silver Layer

The Silver layer contains **cleaned and standardized data**.

Typical transformations include:

- removing invalid or corrupt records
- standardizing timestamp fields
- handling null values
- deriving useful columns

Example derived fields:

- trip duration
- trip hour
- day of week

Example table : silver_taxi_trips

### Gold Layer

The Gold layer contains **business-level aggregations and analytics tables**.

Example outputs:

- daily trip statistics
- revenue per location
- hourly trip demand

Example tables : gold_daily_trip_metrics, gold_location_revenue
These tables are optimized for analytics queries and dashboarding.

---

## Project Structure

### src/

Contains the main data pipeline logic.

- **bronze** – raw data ingestion
- **silver** – cleaning and transformation logic
- **gold** – analytics and aggregations

### notebooks/

Contains orchestration notebooks used to execute pipelines inside Databricks.

### tests/

Reserved for unit tests of transformation logic.

---

## Technologies Used

This project uses the following technologies:

- Databricks
- Apache Spark
- Delta Lake
- Python / PySpark
- Git + GitHub

---

## Learning Objectives

This project demonstrates several important data engineering concepts:

- Lakehouse architecture
- Medallion data modeling
- Delta Lake table management
- Distributed data processing with Spark
- Data pipeline structuring
- Version-controlled data engineering workflows

---

## Future Improvements

Possible extensions for this project include:

- partition optimization for large tables
- Delta table maintenance (OPTIMIZE / VACUUM)
- automated pipeline orchestration
- dashboarding and analytics layer
- streaming ingestion pipeline

---

## License

This project is intended for educational and portfolio purposes.