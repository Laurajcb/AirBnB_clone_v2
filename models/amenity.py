#!/usr/bin/python3
""" State Module for HBNB project """
from os import getenv
from sqlalchemy.sql.schema import Column
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import 

class Amenity(BaseModel):
    name = ""
