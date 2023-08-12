#!/usr/bin/python3
"""BaseModel Module
   description:
       defines all common attributes/methods
"""
import uuid
import datetime
import json
from models import storage


class BaseModel:
    """BaseModel class"""
    def __init__(self, *args, **kwargs):
        """Constructor
        Args:
            args: list of arguments
            kwargs: dictionary
        """
        if kwargs:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == "created_at" or key == "updated_at":
                    str_format = "%Y-%m-%dT%H:%M:%S.%f"
                    value = datetime.datetime.strptime(value, str_format)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            current_time = datetime.datetime.now()
            self.created_at = current_time
            self.updated_at = current_time
            storage.new(self)

    def __str__(self):
        """Magic function
            return a string to be printed
        """
        class_name = "[" + self.__class__.__name__ + "]"
        obj_dict = self.__dict__.copy()
        dct = {k: v for k, v in obj_dict.items() if (not v) is False}
        return class_name + " (" + self.id + ") " + str(dct)

    def save(self):
        """Updates the public instance attribute updated_at
        with the current time"""
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
