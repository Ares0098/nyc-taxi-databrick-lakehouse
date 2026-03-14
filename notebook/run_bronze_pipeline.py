# Databricks notebook source

# COMMAND ----------
# Import bronze ingestion pipeline

from src.bronze.ingest_taxi_data import run_pipeline

# COMMAND ----------
# Execute bronze ingestion

run_pipeline()

# COMMAND ----------
# Validate table

spark.sql("""
SELECT *
FROM main.bronze.bronze_taxi_trips
LIMIT 10
""").display()