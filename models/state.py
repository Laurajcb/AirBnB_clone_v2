#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy.orm.base import attribute_str
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
import sqlalchemy
from models.city import City
import models
from os import getenv


class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    name = Column(String(128), nullable=False)
    cities = relationship(
        'City', cascade="all, delete-orphan", backref='state')

    @property
    def cities(self):
        """getter attribute cities that returns the list of City instances with state_id"""
        from models import storage
        from models.city import City

        new_list = []
        for city_id, city, in storage.all(City).items():
            if city.state_id == self.id:
                new_list.appent(city)
        return new_list
    name = ''
