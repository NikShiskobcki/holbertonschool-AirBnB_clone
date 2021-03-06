#!/usr/bin/python3
"""File Storage"""

from models.user import User
from models.base_model import BaseModel
import json
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

model = {"BaseModel": BaseModel,
         "User": User,
         "State": State,
         "City": City,
         "Amenity": Amenity,
         "Place": Place,
         "Review": Review
         }


class FileStorage:
    """class FileStorage"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj is not None:
            key = obj.__class__.__name__ + "." + obj.id
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        json_obj = {}
        for key in self.__objects:
            json_obj[key] = self.__objects[key].to_dict()
        with open(self.__file_path, "w", encoding="utf=8") as f:
            json.dump(json_obj, f)

    def reload(self):
        """deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, "r", encoding="utf=8") as f:
                jo = json.load(f)
            for key in jo:
                self.__objects[key] = model[jo[key]["__class__"]](**jo[key])
        except FileNotFoundError:
            pass
