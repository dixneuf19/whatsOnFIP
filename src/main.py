import logging

from fastapi import FastAPI

from src.radio_france_api import APIClient

app = FastAPI()
api_client = APIClient()


@app.get("/now")
def read_root():
    return {"Hello": "World"}


@app.get("/grid")
def read_item(start: int, end: int, station: str = "FIP"):
    return api_client.execute_grid_query(start, end, station)
