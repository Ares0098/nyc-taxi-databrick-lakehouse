# Databricks notebook source

# COMMAND ----------
from src.gold.gold_monthly_revenue import run_pipeline as run_revenue
run_revenue()

# COMMAND ----------
from src.gold.gold_trip_distance_stats import run_pipeline as run_distance
run_distance()

# COMMAND ----------
from src.gold.gold_tip_analysis import run_pipeline as run_tip
run_tip()

# COMMAND ----------
spark.sql("""
SELECT * FROM main.gold.gold_monthly_revenue LIMIT 10
""").display()