import logging
from typing import List

from fastapi import FastAPI, status, Query
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder

from whatsonfip.radio_france_api import APIClient, LiveUnavailableException
from whatsonfip.models import Song, Station, APIStatus, Message

app = FastAPI(
    title="What's on FIP ?",
    description="Let's find out what your listening on this eclectic radio!",
    version="0.1.0",
)

api_client = APIClient()


@app.get(
    "/live",
    response_model=Song,
    responses={
        201: {
            "model": Message,
            "description": "No information available about the current song",
        },
        200: {"description": "Current song live"},
    },
)
async def get_live(
    station: str = Query(
        "FIP",
        title="Station Name",
        description="Short name of the Radio France station",
    )
) -> Song:
    try:
        return await api_client.execute_live_query(station)
    except LiveUnavailableException as e:
        logging.warning(e)
        return JSONResponse(
            content=jsonable_encoder(
                {
                    "message": f"No information available about the current song at {station}"
                }
            ),
            status_code=status.HTTP_204_NO_CONTENT,
        )


@app.get("/grid", response_model=List[Song])
async def get_grid(start: int, end: int, station: str = "FIP") -> List[Song]:
    return await api_client.execute_grid_query(start, end, station)


@app.get("/stations", response_model=List[Station])
async def get_stations() -> List[Station]:
    return await api_client.execute_stations_enum_query()


@app.get("/health")
async def get_health():
    return {"message": "OK"}


@app.get("/api-status", response_model=APIStatus)
async def get_api_status():
    return {"code": await api_client.get_api_status()}
