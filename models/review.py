#!/usr/bin/python3
"""
Defines the implementation of reviww class
"""
from models.base_model import BaseModel


class Review(BaseModel):
    """the implementation of review class"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.place_id = ""
        self.user_id = ""
        self.text = ""
