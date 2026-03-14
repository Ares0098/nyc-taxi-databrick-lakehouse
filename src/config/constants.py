CATALOG = "main"

BRONZE_SCHEMA = "bronze"
SILVER_SCHEMA = "silver"
GOLD_SCHEMA = "gold"

BRONZE_TABLE = f"{CATALOG}.{BRONZE_SCHEMA}.bronze_taxi_trips"

RAW_DATA_PATH = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"

BRONZE_PARTITIONS = [
    "pickup_year",
    "pickup_month"
]