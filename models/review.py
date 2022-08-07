#!/usr/bin/python3
''' module for Review class '''
from .base_model import BaseModel

class Review(BaseModel):
    """class 'Review' that inherits from BaseModel"""

    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """class constructor"""
        super().__init__(*args, **kwargs)
