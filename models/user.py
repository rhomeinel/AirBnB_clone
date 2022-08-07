#!/usr/bin/python3
''' module for User class '''
from .base_model import BaseModel

class User(BaseModel):
    """class 'User' that inherits from BaseModel"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
