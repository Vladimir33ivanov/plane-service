from pydantic import BaseModel
from typing import List, Optional

class PlaneIn(BaseModel):
    name: str
    year: str
    count_passengers: str
    country: str


class PlaneOut(PlaneIn):
    id: int
