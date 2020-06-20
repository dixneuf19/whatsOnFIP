import logging
from typing import List

from fastapi import FastAPI, status
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from src.radio_france_api import APIClient, LiveUnavailableException
from src.models import Song, Station

app = FastAPI()
api_client = APIClient()


@app.get("/live")
async def get_live(station: str = "FIP") -> Song:
    try:
        return api_client.execute_live_query(station)
    except LiveUnavailableException as e:
        logging.warning(e)
        return JSONResponse(
            content=jsonable_encoder({"message": "No track information"}), status_code=status.HTTP_204_NO_CONTENT
        )


@app.get("/grid")
async def get_grid(start: int, end: int, station: str = "FIP") -> List[Song]:
    return api_client.execute_grid_query(start, end, station)

@app.get("/stations")
async def get_stations() -> List[Station]:
    return api_client.execute_stations_enum_query()

@app.get("/health")
async def get_health():
    return {"message": "OK"}
