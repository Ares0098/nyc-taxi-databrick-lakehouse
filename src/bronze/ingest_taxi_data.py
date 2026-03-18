from pyspark.sql import SparkSession
from pyspark.sql.functions import (
    current_timestamp,
    year,
    month,
    col
)

from src.config.constants import (
    BRONZE_TABLE,
    VOLUME_DATA_PATH,
    BRONZE_PARTITIONS
)


def run_pipeline():

    spark = SparkSession.builder.getOrCreate()

    df = spark.read.parquet(VOLUME_DATA_PATH)

    df = (
        df.withColumn("ingestion_timestamp", current_timestamp())
        .withColumn("pickup_year", year("tpep_pickup_datetime"))
        .withColumn("pickup_month", month("tpep_pickup_datetime"))
        .withColumn("source_file", col("_metadata.file_path"))
    )

    (
        df.write.format("delta")
        .mode("overwrite")
        .partitionBy(*BRONZE_PARTITIONS)
        .saveAsTable(BRONZE_TABLE)
    )