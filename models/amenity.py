#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class Amenity(BaseModel, Base):
    """
    To add amenity to place
    """
    __tablename__ = "amenities"
    if STORAGE == "db":
        name = Column(String(128), nullable=False)
        place_amenities = Table('place_amenities', Base.metadata,
                            Column('amenity_id', String(60), ForeignKey('amenities.id'),
                                   primary_key=True, nullable=False),
                            Column('place_id', String(60), ForeignKey('places.id'),
                                   primary_key=True, nullable=False)
                            )
