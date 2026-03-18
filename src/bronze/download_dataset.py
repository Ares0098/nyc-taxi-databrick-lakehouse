import urllib.request

from utils.config.constants import (
    DATA_URL,
    VOLUME_DATA_PATH
)


def download_dataset():

    print("Downloading dataset...")

    urllib.request.urlretrieve(DATA_URL, VOLUME_DATA_PATH)

    print("Dataset ready at:", VOLUME_DATA_PATH)