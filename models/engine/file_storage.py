#!/usr/bin/python3
"""File Storage Class"""

import json
import os
import datetime
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User


class FileStorage:
    """ FileStorage class to manage instances """

    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """ return dictionary objects """
        return type(self).__objects

    def new(self, obj):
        """ put object in __objects """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        type(self).__objects[key] = obj

    def save(self):
        """ save the objects dictionary into file
        make serializable dict objects """
        temp = {}
        for key, value in type(self).__objects.items():
            temp[key] = value.to_dict()
        with open(type(self).__file_path, 'w', encoding='utf-8') as f:
            f.write(json.dump(temp) + '\n')

    def classes(self):
        """returns objects from valid classes and their refs"""
        classes = {'BaseModel': BaseModel, 'State': State, 'City': City,
                   'Amenity': Amenity, 'Place': Place, 'Review': Review,
                   'User': User}
        try:
            with open(type(self).__file_path, 'r', encoding='utf-8') as f:
                temp = json.load(f)
                for key, value in temp.items():
                    self.new(classes[value['__class__']](**value))
        except FileNotFoundError:
            pass
