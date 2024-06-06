#!/usr/bin/python3
"""Database storage engine using SQLAlchemy with mysql+mysqldb database
"""

import os
import models
from models.base_model import Base, BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.user import User
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

name_class = {
    'Amenity': Amenity,
    'City': City,
    'Place': Place,
    'State': State,
    'Review': Review,
    'User': User
}


class DBStorage:
    """
    A class for interacting with the Database Storage
    """
    __engine = None
    __session = None

    def __init__(self):
        """
        Initializes the object
        """
        user = os.getenv('HBNB_MYSQL_USER')
        passwd = os.getenv('HBNB_MYSQL_PWD')
        host = os.getenv('HBNB_MYSQL_HOST')
        database = os.getenv('HBNB_MYSQL_DB')
        self.__engine = create_engine('mysql+mysqldb://{}:{}@{}/{}'
                                      .format(user, passwd, host, database))
        if os.getenv('HBNB_ENV') == 'test':
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """
        returns a dictionary of all the objects present
        """
        objects = {}
        for clss in classes:
            if cls is None or cls is classes[clss] or cls is clss:
                objs = self.__session.query(classes[clss]).all()
                for obj in objs:
                    key = obj.__class__.name__ + '.' + obj.id
                    objects[key] = obj
        return (objects)

    def reload(self):
        """
        reloads objects from the Database Storage
        """
        Base.metadata.create_all(self.__engine)
        session_factory = sessionmaker(bind=self.__engine,
                                       expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session

    def new(self, obj):
        """
        creates a new object
        """
        self.__session.add(obj)

    def save(self):
        """
        saves the current session
        """
        self.__session.commit()

    def delete(self, obj=None):
        """
        deletes an object
        """
        if obj is not None:
            self.__session.delete(obj)

    def close(self):
        """
        Disposal of current session if active
        """
        self.__session.remove()

    def get(self, cls, id):
        """
        Retrieve an object
        """
        if cls is not None and type(cls) is str and id is not None and\
           type(id) is str and cls in name_class:
            cls = name_class[cls]
            result = self.__session.query(cls).filter(cls.id == id).first()
            return result
        else:
            return None

    def count(self, cls=None):
        """
        Count number of objects in the Database Storage
        """
        total = 0
        if type(cls) is str and cls in name_class:
            cls = name_class[cls]
            total = self.__session.query(cls).count()
        elif cls is None:
            for cls in name_class.values():
                total += self.__session.query(cls).count()
        return total
