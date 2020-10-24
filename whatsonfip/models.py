from typing import List, Optional

from pydantic import BaseModel


class Song(BaseModel):
    title: str
    album: str
    artist: str
    year: int


class Station(BaseModel):
    name: str


class APIStatus(BaseModel):
    code: int
    message: Optional[str]
