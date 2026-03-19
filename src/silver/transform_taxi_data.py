from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    unix_timestamp,
    to_date,
    round
)

from src.config.constants import (
    BRONZE_TABLE,
    SILVER_TABLE
)


def run_pipeline():

    spark = SparkSession.builder.getOrCreate()

    df = spark.table(BRONZE_TABLE)

    # -------------------------
    # 1. Data Quality Filters
    # -------------------------
    df_clean = (
        df
        .filter(col("passenger_count") > 0)
        .filter(col("trip_distance") > 0)
        .filter(col("fare_amount") >= 0)
        .filter(col("tpep_pickup_datetime").isNotNull())
        .filter(col("tpep_dropoff_datetime").isNotNull())
    )

    # -------------------------
    # 2. Derived Columns
    # -------------------------
    df_clean = (
        df_clean
        .withColumn(
            "trip_duration_minutes",
            (
                unix_timestamp("tpep_dropoff_datetime")
                - unix_timestamp("tpep_pickup_datetime")
            ) / 60
        )
        .withColumn(
            "trip_speed_kmh",
            round(
                col("trip_distance") /
                (col("trip_duration_minutes") / 60),
                2
            )
        )
        .withColumn(
            "pickup_date",
            to_date("tpep_pickup_datetime")
        )
    )

    # -------------------------
    # 3. Remove unrealistic data
    # -------------------------
    df_clean = (
        df_clean
        .filter(col("trip_duration_minutes") > 0)
        .filter(col("trip_speed_kmh") < 200)
    )

    # -------------------------
    # 4. Write to Silver
    # -------------------------
    (
        df_clean.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(SILVER_TABLE)
    )

    print("Silver pipeline completed.")