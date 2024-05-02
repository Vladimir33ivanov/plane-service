import pytest
from app.api.models import PlaneIn, PlaneOut

planes = PlaneIn(
    name='Boeing 737',
    year='2010',
    count_passengers='189',
    country='USA'
)


def test_create_client(planes: PlaneIn = planes):
    assert dict(planes) == {'name': planes.name,
                              'year': planes.year,
                              'count_passengers': planes.count_passengers,
                              'country': planes.country
                              }


def test_update_client_age(planes: PlaneIn = planes):
    plane_upd = PlaneOut(
        name='Boeing 737',
        year='2010',
        count_passengers='189',
        country='USA',
        id=1
    )
    assert dict(plane_upd) == {'name': planes.name,
                              'year': planes.year,
                              'count_passengers': planes.count_passengers,
                              'country': planes.country,
                              'id': plane_upd.id
                              }


def test_update_client_genre(planes: PlaneIn = planes):
    plane_upd = PlaneOut(
        name='Boeing 737',
        year='2010',
        count_passengers='189',
        country='USA',
        id=1
    )
    assert dict(plane_upd) == {'name': planes.name,
                              'year': planes.year,
                              'count_passengers': planes.count_passengers,
                              'country': planes.country,
                              'id': plane_upd.id
                              }
