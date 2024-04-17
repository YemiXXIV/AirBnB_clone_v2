#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    name = ""
