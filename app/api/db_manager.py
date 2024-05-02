from app.api.models import PlaneIn, PlaneOut
from app.api.db import planes, database


async def add_plane(payload: PlaneIn):
    query = planes.insert().values(**payload.dict())
    return await database.execute(query=query)


async def get_all_plane():
    query = planes.select()
    return await database.fetch_all(query=query)


async def get_plane(id):
    query = planes.select().where(planes.c.id == id)
    return await database.fetch_one(query=query)


async def delete_plane(id: int):
    query = planes.delete().where(planes.c.id == id)
    return await database.execute(query=query)

