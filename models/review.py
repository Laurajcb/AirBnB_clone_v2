#!/usr/bin/python3
""" Review module for the HBNB project """
from sqlalchemy.orm.base import attribute_str
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy
from models.city import City
import models
from os import 


class Review(BaseModel):
    """ Review classto store review information """
    place_id = ""
    user_id = ""
    text = ""
