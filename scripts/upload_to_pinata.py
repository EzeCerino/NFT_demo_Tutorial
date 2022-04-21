import os
from pathlib import Path
import requests


PINATA_BASE_URL = "https://api.pinata.cloud/"
end_point = "pinning/pinFileToIpfs"
filepath = "./img/pug.png"
filename = filepath.split("/")[-1:][0]
headers = {
    "pinata_api_key": os.getenv("PINATA_API_KEY"),
    "pinata_secret_api_key": os.getenv("PINATA_API_SECRET"),
}


def main():
    with Path(filepath).open("rb") as fp:
        image_binary = fp.read()
        response = requests.post(
            PINATA_BASE_URL + end_point,
            files={"file": (filename, image_binary)},
            headers=headers,
        )
        print(response.json())
