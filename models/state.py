#!/usr/bin/python3
""" State Module for our HBNB project """
from models.base_model import BaseModel, Base
from models.city import City
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class State(BaseModel, Base):
    """
    State class
    """
    __tablename__ = 'states'
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref="states",
                              cascade="all, delete-orphan")

        # Define a property to retrieve cities associated with the state
        @property
        def cities(self):
            from models import storage
            city_list = []
            all_in = storage.all(City)
            for value in all_in.values():
                if value.state_id == self.id:
                    city_list.append(value)
            return city_list
