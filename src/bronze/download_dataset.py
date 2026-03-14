import urllib.request

from src.config.constants import (
    DATA_URL,
    DBFS_DATA_DIR,
    DBFS_DATA_PATH
)


def download_dataset(dbutils):

    local_tmp = "/tmp/yellow_tripdata_2023-01.parquet"

    print("Downloading dataset...")
    urllib.request.urlretrieve(DATA_URL, local_tmp)

    print("Creating DBFS directory...")
    dbutils.fs.mkdirs(DBFS_DATA_DIR)

    print("Copying dataset to DBFS...")
    dbutils.fs.cp(f"file:{local_tmp}", DBFS_DATA_PATH)

    print("Dataset ready at:", DBFS_DATA_PATH)