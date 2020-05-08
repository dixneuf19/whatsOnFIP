from typing import List
from dataclasses import dataclass


@dataclass
class Song:
    title: str
    album: str
    artist: str
    year: int
