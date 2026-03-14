# Databricks notebook source

# COMMAND ----------
from src.bronze.download_dataset import download_dataset

download_dataset(dbutils)

# COMMAND ----------
from src.bronze.ingest_taxi_data import run_pipeline

run_pipeline()

# COMMAND ----------
spark.sql("""
SELECT *
FROM main.bronze.bronze_taxi_trips
LIMIT 10
""").display()