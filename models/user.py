#!/usr/bin/python3
"""This module defines a class User"""
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from os import getenv

STORAGE = getenv("HBNB_TYPE_STORAGE")


class User(BaseModel, Base):
    """
    This class defines a user
    """
    __tablename__ = "users"
    if STORAGE == "db":
        email = Column(String(128), nullable=False)
        password = Column(String(128), nullable=False)
        first_name = Column(String(128), nullable=True)
        last_name = Column(String(128), nullable=True)
        places = relationship('Place', backref='user',
                              cascade="all, delete-orphan")
        reviews = relationship('Review', backref='user',
                               cascade="all, delete-orphan")
    else:
        email = ''
        password = ''
        first_name = ''
        last_name = ''
