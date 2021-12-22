#!/usr/bin/python3
""" Defines a New engine DBStorage"""

from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel, Base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv


class DBStorage():
    """DBStorages Class"""
    __engine = None
    __session = None

    def __init__(self):
        user = getenv('HBNB_MYSQL_USER')
        passwd = getenv('HBNB_MYSQL_PWD')
        localhost = getenv('HBNB_MYSQL_HOST')
        db = getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'.format(
            user, passwd, host, db), pool_pre_ping=True)

        if getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """ Query on the current database session """
        new_list = [User, State, City, Amenity, Place, Review]
        new_dict = {}
        result = []

        if cls is None:
            for clas in new_list:
                result.extend(self.__session.query(clas).all())
            else:
                result = self.__session.query(cls).all()

            for r in result:
                id = r.__class__.__name__ + '.' + r.id
                new_dict[id] = r
        return new_dict

    def new(self, obj):
        """Add the object to the current database session """
        self.__session.commit()

    def save(self):
        """commit all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """ remove an object from the current session """
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        Base.metadata.create_all(self.__engine)
        maker = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(maker)
        self.__session = Session()

    def close(self):
        self.__session.invalidate()
