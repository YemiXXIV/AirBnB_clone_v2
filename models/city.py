#!/usr/bin/python3
""" City Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class City(BaseModel, Base):
    """ The city class, contains state ID and name """
    __tablename__ = 'cities'
    # Check the storage type
    if STORAGE == "db":
        # Define columns for the database storage
        state_id = Column(String(60), ForeignKey('states.id'), nullable=False)
        name = Column(String(128), nullable=False)
        # Define relationship with Place class
        places = relationship('Place',
                              backref='cities',
                              cascade="all, delete-orphan")
    else:
        name = ""
        state_id = ""
