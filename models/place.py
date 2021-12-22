#!/usr/bin/python3
""" Place Module for HBNB project """
from os import getenv
from sqlalchemy.sql.expression import column
from sqlalchemy.sql.schema import ColumnDefault, Table
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer, ForeignKey, Float
from sqlalchemy.orm import relationship


class Place(BaseModel):
    """ A place to stay """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []
