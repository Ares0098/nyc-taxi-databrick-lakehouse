from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    col,
    avg,
    count,
    expr
)

from utils.config.constants import (
    SILVER_TABLE,
    GOLD_TIP_ANALYSIS_TABLE
)

def run_pipeline():

    spark = SparkSession.builder.getOrCreate()

    df = spark.table(SILVER_TABLE)

    df = df.withColumn(
        "tip_percentage",
        expr("try_divide(tip_amount, fare_amount)")
    )

    df_agg = (
        df.groupBy("passenger_count")
        .agg(
            avg("tip_percentage").alias("avg_tip_percentage"),
            count("*").alias("total_trips")
        )
    )

    (
        df_agg.write
        .format("delta")
        .mode("overwrite")
        .saveAsTable(GOLD_TIP_ANALYSIS_TABLE)
    )