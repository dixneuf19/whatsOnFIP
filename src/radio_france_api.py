import os
import logging
from typing import List

from dotenv import load_dotenv

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport
from requests.models import HTTPError

from src.models import Song

load_dotenv()

API_TOKEN = os.getenv("RADIO_FRANCE_API_TOKEN")

RADIO_FRANCE_API = "https://openapi.radiofrance.fr/v1/graphql"


class LiveUnavailableException(Exception):
    pass


def track_to_song(track) -> Song:
    doc = track["track"]
    artist = None
    try:
        artist = doc["mainArtists"][0]
    except IndexError:
        pass

    return Song(
        title=doc["title"],
        album=doc["albumTitle"],
        artist=artist,
        year=doc["productionDate"],
    )


class APIClient(Client):
    def __init__(self) -> None:
        try:
            logging.info("Initiating GraphQL API client")
            sample_transport = RequestsHTTPTransport(
                url=f"{RADIO_FRANCE_API}?x-token={API_TOKEN}",
                use_json=True,
                headers={"Content-type": "application/json",},
                verify=True,
            )
            super().__init__(
                retries=3, transport=sample_transport, fetch_schema_from_transport=True,
            )
        except HTTPError as e:
            if "403" in str(e):
                logging.warning("The API return 403, check your API token")
            raise
        except:
            raise

    def execute_grid_query(
        self, start: int, end: int, station: str = "FIP"
    ) -> List[Song]:
        logging.info(f"Querying the GraphQL API for {station} from {start} to {end}")
        query = gql(
            f"""{{ 
                grid(start: {start}, end: {end}, station: {station}) {{ 
                ... on TrackStep {{ 
                    track {{ 
                        title 
                        albumTitle 
                        mainArtists 
                        productionDate
                        }}
                    }} 
                }} 
            }} 
        """
        )
        try:
            tracks = super().execute(query)
            return [track_to_song(t) for t in tracks["grid"]]
        except:
            raise

    def execute_live_query(self, station: str = "FIP") -> Song:
        logging.info(f"Querying the GraphQL API for {station} from live")
        query = gql(
            f"""{{
                live(station: {station}) {{
                    song {{
                        id
                        track {{
                            title
                            albumTitle
                            mainArtists
                            productionDate
                        }}
                    }}
                }}
            }}
            """
        )
        res = super().execute(query)
        if res["live"]["song"] is None:
            raise LiveUnavailableException(
                f"invalid result for live {station} query : {res}"
            )
        return track_to_song(res["live"]["song"])
