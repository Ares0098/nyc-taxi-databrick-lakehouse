import urllib.request

from src.config.constants import (
    DATA_URL,
    DBFS_DATA_DIR,
    DBFS_DATA_PATH
)


def download_dataset(dbutils):

    print("Creating DBFS directory...")
    dbutils.fs.mkdirs(DBFS_DATA_DIR)

    print("Downloading dataset directly to DBFS...")

    local_dbfs_path = "/dbfs/FileStore/datasets/nyc_taxi/yellow_tripdata_2023-01.parquet"

    urllib.request.urlretrieve(DATA_URL, local_dbfs_path)

    print("Dataset ready at:", DBFS_DATA_PATH)