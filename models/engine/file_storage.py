#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.base_model import BaseModel
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review,
           "State": State, "User": User}


class FileStorage:
    """
    This class manages storage of hbnb models in JSON format
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self, cls=None):
        """
        Returns a dict of objects that are instantiated
        """
        if cls is not None:
            objects = {}
            for key, value in self.__objects.items():
                if cls == value.__class__ or cls == value.__class__.name__:
                    objects[key] = value
            return objects
        return self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized = {}
        for key in self.__objects:
            serialized[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(self.__file_path, "r") as f:
                deserialized = json.load(f)
                for key in deserialized:
                    self.__objects[key] =
                    classes[deserialized[key]["__class"]](**deserialized[key])
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete a given object from __objects, if it exists.
        """
        if obj is not None:
            key = obj.__class__.__name__ + '.' + obj.id
            if key in self.__objects:
                del self.__objects[key]

    def close(self):
        """
        Calls the reload method.
        """
        self.reload()
