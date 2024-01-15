#!/usr/bin/python3
"""
Module for the BaseModel class.
"""

import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        dateformat = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                elif key == "created_at" or key == "updated_at":
                    setattr(self, key, datetime.strptime(value, dateformat))
                else:
                    setattr(self, key, value)
                    models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance,
        displaying the class name, id, and the dictionary
        representation of the instance
        """
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """
        Updates the updated_at attribute with
        the current datetime when called
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
        to_dict: Returns a dictionary containing all the
        key-value pairs from the instance's __dict__.
        Adds the __class__ key with the class name,
        and converts created_at and updated_at to ISO format strings.
        """
        dict_obj = self.__dict__.copy()
        dict_obj["__class__"] = self.__class__.__name__
        dict_obj["created_at"] = self.created_at.isoformat()
        dict_obj["updated_at"] = self.updated_at.isoformat()
        return dict_obj
