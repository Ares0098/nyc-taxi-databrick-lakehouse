from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    current_timestamp,
    year,
    month,
    input_file_name
)

from src.config.constants import (
    BRONZE_TABLE,
    RAW_DATA_PATH,
    BRONZE_PARTITIONS
)


def run_pipeline():

    spark = SparkSession.builder.getOrCreate()

    df = spark.read.parquet(RAW_DATA_PATH)

    df = (
        df.withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("pickup_year", year("tpep_pickup_datetime"))
        .withColumn("pickup_month", month("tpep_pickup_datetime"))
        .withColumn("source_file", input_file_name())
    )

    (
        df.write.format("delta")
        .mode("overwrite")
        .partitionBy(*BRONZE_PARTITIONS)
        .saveAsTable(BRONZE_TABLE)
    )