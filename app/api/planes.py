from fastapi import APIRouter, HTTPException
from typing import List

from app.api.models import PlaneOut, PlaneIn
from app.api import db_manager

planes = APIRouter()

@planes.post('/', response_model=PlaneOut, status_code=201)
async def create_plane(payload: PlaneIn):
    plane_id = await db_manager.add_plane(payload)

    response = {
        'id': plane_id,
        **payload.dict()
    }

    return response


@planes.get('/', response_model=List[PlaneOut])
async def get_planes():
    return await db_manager.get_all_plane()


@planes.get('/{id}/', response_model=PlaneOut)
async def get_plane(id: int):
    company = await db_manager.get_plane(id)
    if not company:
        raise HTTPException(status_code=404, detail="plane not found")
    return company


@planes.delete('/{id}/', response_model=None)
async def delete_plane(id: int):
    company = await db_manager.get_plane(id)
    if not company:
        raise HTTPException(status_code=404, detail="plane not found")
    return await db_manager.delete_plane(id)