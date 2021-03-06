#!/usr/bin/python3
"""base model"""
import uuid
from datetime import datetime
import models


class BaseModel:
    """class model"""

    def __init__(self, *args, **kwargs):
        """init"""
        date = "%Y-%m-%dT%H:%M:%S.%f"
        if kwargs is not None and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != "__class__":
                    if key == "created_at":
                        value = datetime.strptime(value, date)
                    elif key == "updated_at":
                        value = datetime.strptime(value, date)
                    setattr(self, key, value)
        else:
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            self.id = str(uuid.uuid4())
            models.storage.new(self)

    def __str__(self):
        """str representation"""
        return("[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__))

    def save(self):
        """saves"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """returns dictionary of the instance"""
        dAux = self.__dict__.copy()
        for key in dAux:
            if key == "created_at":
                dAux[key] = dAux[key].isoformat()
            if key == "updated_at":
                dAux[key] = dAux[key].isoformat()
        dAux["__class__"] = self.__class__.__name__
        return dAux
