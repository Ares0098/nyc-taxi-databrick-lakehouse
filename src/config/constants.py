CATALOG = "main"

# Schemas
BRONZE_SCHEMA = "bronze"
SILVER_SCHEMA = "silver"
GOLD_SCHEMA = "gold"

# Tables
BRONZE_TABLE = f"{CATALOG}.{BRONZE_SCHEMA}.bronze_taxi_trips"
SILVER_TABLE = f"{CATALOG}.{SILVER_SCHEMA}.silver_taxi_trips"
GOLD_MONTHLY_REVENUE_TABLE = f"{CATALOG}.{GOLD_SCHEMA}.gold_monthly_revenue"
GOLD_TRIPS_DISTANCE_STATS_TABLE = f"{CATALOG}.{GOLD_SCHEMA}.gold_trip_distance_stats"
GOLD_TIP_ANALYSIS_TABLE = f"{CATALOG}.{GOLD_SCHEMA}.gold_tip_analysis"

# Data source
DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

# Volume path
VOLUME_DATA_PATH = "/Volumes/main/bronze/raw_data/yellow_tripdata_2023-01.parquet"

# Partitioning
BRONZE_PARTITIONS = [
    "pickup_year",
    "pickup_month"
]