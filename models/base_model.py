#!/usr/bin/python3
"""BaseModel Module
   description:
       defines all common attributes/methods
"""
import uuid
import datetime
import json


class BaseModel:
    """BaseModel class"""
    def __init__(self):
        """Constructor"""
        self.id = str(uuid.uuid4())
        current_time = datetime.datetime.now()
        self.created_at = current_time
        self.updated_at = current_time

    def __str__(self):
        """Magic function
            return a string to be printed
        """
        obj_dict = self.__dict__.copy()
        obj_dict["created_at"] = obj_dict["created_at"].isoformat()
        obj_dict["updated_at"] = obj_dict["updated_at"].isoformat()
        class_name = "BaseModel"
        final_str = f"[{class_name}] ({self.id}) {json.dumps(obj_dict)}"
        return final_str

    def save(self):
        """Updates the public instance attribute updated_at
        with the current time"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Returns a dictionary containing all keys/values
        of __dict__ of the instance
        """
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = dict_copy["created_at"].isoformat()
        dict_copy["updated_at"] = dict_copy["updated_at"].isoformat()
        dict_copy["__class__"] = self.__class__.__name__
        return dict_copy
