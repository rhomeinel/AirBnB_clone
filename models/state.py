#!/usr/bin/python3
''' module for State class '''
from .base_model import BaseModel

class State(BaseModel):
    """class 'State' that inherits from BaseModel"""

    name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
