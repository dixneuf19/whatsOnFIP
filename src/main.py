import logging
from typing import List

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.radio_france_api import APIClient, LiveUnavailableException
from src.models import Song

app = FastAPI()
api_client = APIClient()


@app.get("/live")
def get_live(station: str = "FIP") -> Song:
    try:
        return api_client.execute_live_query(station)
    except LiveUnavailableException as e:
        logging.warning(e)
        return JSONResponse(
            content=jsonable_encoder({}), status_code=status.HTTP_204_NO_CONTENT
        )


@app.get("/grid")
def get_grid(start: int, end: int, station: str = "FIP") -> List[Song]:
    return api_client.execute_grid_query(start, end, station)
