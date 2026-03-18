from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    avg,
    max,
    min,
    col
)

from src.config.constants import (
    SILVER_TABLE,
    GOLD_TRIPS_DISTANCE_STATS_TABLE
)

def run_pipeline():

    spark = SparkSession.builder.getOrCreate()

    df = spark.table(SILVER_TABLE)

    df_agg = (
        df.groupBy("pickup_date")
        .agg(
            avg("trip_distance").alias("avg_distance"),
            max("trip_distance").alias("max_distance"),
            min("trip_distance").alias("min_distance")
        )
    )

    (
        df_agg.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(GOLD_TRIPS_DISTANCE_STATS_TABLE)
    )