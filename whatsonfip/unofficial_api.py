import os
from typing import List

from loguru import logger
from dotenv import load_dotenv

import requests

from whatsonfip.models import Song, Station

load_dotenv()

UNOFFICIAL_API_URL = os.getenv(
    "UNOFFICIAL_API_URL", "https://www.fip.fr/latest/api/graphql"
)
UNOFFICIAL_API_OPERATION_NOW = os.getenv(
    "UNOFFICIAL_API_OPERATION_NOW",
    "?operationName=Now&variables=%7B%22bannerPreset%22%3A%22266x266%22%2C%22stationId%22%3A7%7D&extensions=%7B%22persistedQuery%22%3A%7B%22version%22%3A1%2C%22sha256Hash%22%3A%2295ed3dd1212114e94d459439bd60390b4d6f9e37b38baf8fd9653328ceb3b86b%22%7D%7D",
)


def get_now_unofficial() -> Song:
    r = requests.get(url=UNOFFICIAL_API_URL + UNOFFICIAL_API_OPERATION_NOW)
    logger.info(r.json())
    song = r.json()["data"]["now"]["song"]

    song["artist"] = song["interpreters"][0] if len(song["interpreters"]) > 0 else ""

    song["external_urls"] = {}
    for key, value in song["external_links"].items():
        if not (key.startswith("__") or value is None):
            song["external_urls"][key] = value["link"]

    return Song(**song)
