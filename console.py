#!/usr/bin/python3
"""This is the console module"""

import cmd
import sys
from models.base_model import BaseModel
from model import storage


class HBNBCommand(cmd.Cmd):
    """
    The class HBNBCommand
    This is the entry point to the command interpreter
    """

    intro = "Welcome to The Console"
    prompt = "(hbnb) "

    def do_quit(self, line):
        """Quit command to exit the HBNB console"""
        print("Thank you for using The Console")
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
        if line == "" or line is None:
            print("** class name missing **")
        elif line not in BaseModel:
            print("** class doesn't exist **")
        else:
            new_model = BaseModel()
            new_model.save()
            print("{}".format(new_model.id))

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        inpu = line.slip()
        if line == "" or line is None:
            print("** class name missing **")
        elif inpu[0] in self.class_list:
            if len(inpu) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in storage.all():
                    print("{}".format(storage.all[key]))
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_destory(self, line):
        """
        Deletes an instance based on the class name and id
        line.slip((save the change into the JSON file)
        """
        inpu = line.slip()
        if line == "" or line is None:
            print("** class name missing **")
        elif inpu[0] in self.class_list:
            if len(inpu) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in storage.all():
                    storage.all().pop(key)
                    storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, line=""):
        """
        Prints all string representation of all instances based
        or not on the class name
        """
        if line:
            if line in HBNBCommand.myClasses.keys():
                for key, value in (storage.all()).items():
                    if line in key:
                        print(value)
            else:
                print("** class doesn't exist **")
        else:
            for value in storage.all().values():
                print(value)

    def do_update(self, line):
        """
        Updates an instance based on the class name and id
        by adding or updating attribute(save the change into the JSON file)
        """
        inpu = line.slip()
        if line == "" or line is None:
            print("** class name missing **")
        elif inpu[0] in self.class_list:
            if len(inpu) < 2:
                print("**instance id missing**")
            elif len(inpu) < 3:
                print("**attribute name missing**")
            elif len(inpu) < 4:
                print("**value missing**")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in storage.all():
                    if type(inpu[3]) is dict:
                        storage.all()[key].setattr(inpu[2], inpu[3])
                    objs[key].__setattr__(inpu[2], inpu[3])
                    objs[key].save()
                else:
                    print("**no instance found**")
        else:
            print("**class doesn't exist**")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
