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
        if cls is None:
            return FileStorage.__objects
        else:
            return {k: v for k, v in FileStorage.__objects.items() if isinstance(v, cls)}


    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        """
        key = obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).
        """
        serialized = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(serialized, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        """
        try:
            with open(FileStorage.__file_path, "r") as f:
                deserialized = json.load(f)
                for key, value in deserialized.items():
                    cls_name, obj_id = key.split(".")
                    cls = eval(cls_name)
                    obj = cls(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """
        Delete a given object from __objects, if it exists.
        """
        if obj is not None:
            key = "{}.{}".format(obj.__class__.__name__, obj.id)
            if key in FileStorage.__objects:
                del FileStorage.__objects[key]

    def close(self):
        """
        Calls the reload method.
        """
        self.reload()
