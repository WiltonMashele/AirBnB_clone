#!/usr/bin/python3
"""
Defines the implementation of reviww class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the implementation of review class"""
    place_id = ""
    user_id = ""
    text = ""
