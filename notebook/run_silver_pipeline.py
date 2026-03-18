# Databricks notebook source

# COMMAND ----------
from src.silver.transform_taxi_data import run_pipeline

run_pipeline()

# COMMAND ----------
spark.sql("""
SELECT *
FROM main.silver.silver_taxi_trips
LIMIT 10
""").display()