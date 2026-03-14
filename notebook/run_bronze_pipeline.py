# Databricks notebook source

# COMMAND ----------
# download dataset

from src.bronze.download_dataset import download_dataset

download_dataset()

# COMMAND ----------
# run bronze ingestion

from src.bronze.ingest_taxi_data import run_pipeline

run_pipeline()

# COMMAND ----------
# validate result

spark.sql("""
SELECT *
FROM main.bronze.bronze_taxi_trips
LIMIT 10
""").display()