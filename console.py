#!/usr/bin/python3
"""This is the console module"""

import re
import cmd
import sys
import json
import models
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models import storage
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.base_model import BaseModel
from models.city import City


class HBNBCommand(cmd.Cmd):
    """
    The class HBNBCommand
    This is the entry point to the command interpreter
    """

    prompt = "(hbnb) "

    def precmd(self, inp):
        """ A function that checks for specified input format
            and groups the input to create a proper command line
        """
        args = "\(\"(\S*)\"\,\ \"(\S*)\"\,\ (\S*)\)$"
        fm = "^(\w*)\.(\w*)" + args
        search_list = ["^(\w*)\.(\w*)\((\w*)\)$",
                       "^(\w*)\.(\w*)\(\"(\S*)\"\)$", fm]
        for search in search_list:
            s = re.search(search, inp)
            if s:
                break
        if not s:
            return inp
        model = s.group(1)
        cmd = s.group(2)
        args = s.group(3)
        line = cmd + " " + model + " " + args
        if len(s.groups()) > 3:
            if s.group(4):
                line += " " + s.group(4)
        if len(s.groups()) > 4:
            if s.group(5):
                line += " " + s.group(5)

        self.onecmd(line)
        return ""


    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, line):
        """Quit command to exit the program at end of file"""
        print()
        return True

    def emptyline(self):
        """Ingnore empty line"""
        pass

    def do_create(self, line):
        """
        Creates a new instance of BaseModel, saves it
        (to the JSON file) and prints the id.
        """
        if line == "":
            print("** class name is missing **")
        elif line != "BaseModel":
            print("** class does not exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print("{}".format(new_model.id))

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            _input = line.split(' ')
            if _input[0] not in class_check:
                print("** class doesn't exist **")
            elif len(_input) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(_input[0], _input[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    print(storage.all()[key])

    def do_destroy(self, line):
        """
        Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        if line == "" or line is None:
            print("** class name missing **")
        else:
            _input = line.split(' ')
            if _input[0] not in class_check:
                print("** class doesn't exist **")
            elif len(_input) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(_input[0], _input[1])
                if key not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[key]
                    storage.save()

    def do_all(self, name):
        """
        Prints all string representation of all instances
        bases on a class name
        """
        if name != "":
            inputt = name.split(' ')
            if inputt[0] not in class_check:
                print("** class doesn't exist **")
            else:
                list_str = [str(obj) for key, obj in storage.all().items()
                            if type(obj).__name__ == inputt[0]]
                print(list_str)
        else:
            list_str = [str(obj) for key, obj in storage.all().items()]
            print(list_str)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute(save the change into the JSON file)
        """
        objs = models.storage.all()
        inpu = line.split()
        if line == "" or line is None:
            print("** class name missing **")
        elif inpu[0] in class_check:
            if len(inpu) < 2:
                print("** instance id missing **")
            elif len(inpu) < 3:
                print("** attribute name missing **")
            elif len(inpu) < 4:
                print("** value missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in objs:
                    if type(inpu[3]) is dict:
                        objs[key].setattr(inpu[2], inpu[3])
                    objs[key].__setattr__(inpu[2], inpu[3])
                    objs[key].save()
                    models.storage.reload()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_update_dict(self, arg):
        '''Updates an object using a dictionary'''
        args = arg.split(' ', 1)
        oid = args[0]
        dict1 = args[1]
        if dict1 is None or dict1 == '':
            print("** Dictionary missing **")
            return
        instances = storage.all()
        if oid not in instances:
            print("** no instance found **")
            return
        dict1 = json.loads(dict1)
        utime = datetime.now()
        dict1['updated_at'] = utime
        instances[oid].update(dict1)
        storage.new(instances)
        storage.save()
        return


if __name__ == '__main__':
    class_check = {"Amenity", "BaseModel", "City" "Place", "Review",
                   "State", "User"}
    HBNBCommand().cmdloop()
