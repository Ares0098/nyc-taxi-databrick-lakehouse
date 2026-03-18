from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    year,
    month,
    sum,
    count,
    avg,
    col
)

from utils.config.constants import (
    SILVER_TABLE,
    GOLD_MONTHLY_REVENUE_TABLE
)

def run_pipeline():

    spark = SparkSession.builder.getOrCreate()

    df = spark.table(SILVER_TABLE)

    df_agg = (
        df.groupBy(
            year("tpep_pickup_datetime").alias("year"),
            month("tpep_pickup_datetime").alias("month")
        )
        .agg(
            count("*").alias("total_trips"),
            sum("fare_amount").alias("total_revenue"),
            avg("fare_amount").alias("avg_fare")
        )
    )

    (
        df_agg.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(GOLD_MONTHLY_REVENUE_TABLE)
    )