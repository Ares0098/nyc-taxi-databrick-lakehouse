import os
import urllib.request

DATA_URL = "https://d37ci6vzurychx.cloudfront.net/trip-data/yellow_tripdata_2023-01.parquet"
DATA_DIR = "data"
FILE_NAME = "yellow_tripdata_2023-01.parquet"

os.makedirs(DATA_DIR, exist_ok=True)

file_path = os.path.join(DATA_DIR, FILE_NAME)

if not os.path.exists(file_path):
    print("Downloading dataset...")
    urllib.request.urlretrieve(DATA_URL, file_path)
    print("Download complete.")
else:
    print("Dataset already exists.")