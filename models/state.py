#!/usr/bin/python3
"""
The implementation of the state class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """state class implementation"""
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.name = ""
