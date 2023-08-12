#!/usr/bin/python3
"""
the implementation amenity class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """amenity implementation"""
    def __init__(self, *args, **kwargs):
    super().__init__(*args, **kwargs)
    self.name = ""
