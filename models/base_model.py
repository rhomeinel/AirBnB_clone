#!/usr/bin/python3
'''Base Model Module For the project'''

import models
from uuid import uuid4
from datetime import datetime


class BaseModel:
    """Class for the Base Model"""

    def __init__(self, *args, **kwargs):
        """Initializes the Base instance"""
        datenow = datetime.now()
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ['created_at', 'updated_at']:
                    value = datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f")
                self.__setattr__(key, value)
        else:
            self.id = str(uuid4())
            self.created_at = datenow
            self.updated_at = datenow
            models.storage.new(self)

    def __str__(self):
        """String representation of an instance"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id,
                                     self.__dict__)

    def save(self):
        """Updates the updated_at public instance attribute"""
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """Convert object to dictionary representation"""
        dict = self.__dict__.copy()
        dict['__class__'] = self.__class__.__name__
        dict['created_at'] = self.created_at.isoformat()
        dict['updated_at'] = self.updated_at.isoformat()
        return dict
