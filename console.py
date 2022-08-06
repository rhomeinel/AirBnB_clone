#!/usr/bin/python3
"""This is the console module"""

import cmd
import sys


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
        if not line:
            print("** class name missing **")
        elif line in class_check:
            _input = line.split()
            new_obj = class_check[_input[0]]()
            new_obj.save()
            storage.reload()
            print(new_obj.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        """
        Prints the string representation of an instance
        based on the class name and id
        """
        inpu = line.slip()
        switch = 0
        switch1 = 0
        objects = storage.all()
        if inpu[0] not in class_check:
            print("** class doesn't exist **")
        elif len(inpu) < 2:
            num_list = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
            for letter in _input[0]:
                if letter in num_list:
                    switch1 = 1
            if switch1 == 1:
                print("** class name missing **")
            else:
                print("** instance id missing **")
        elif len(inpu) == 2:
            for key in objects.keys():
                if key == inpu[1]:
                    print(objects[key])
                    switch = 1
            if switch == 0:
                print("** no instance found **")

    def do_destory(self, line):
        """
        Deletes an instance based on the class name and id
        line.slip((save the change into the JSON file)
        """
        inpu = line.slip()
        objs = models.storage.all()
        key = ""
        if not inp:
            print("** class name missing **")
        elif inpu[0] in self.class_list:
            if len(inpu) < 2:
                print("** instance id missing **")
            else:
                key = "{}.{}".format(inpu[0], inpu[1])
                if key in objs:
                    objs.pop(key)
                    models.storage.save()
                else:
                    print("** no instance found **")
        else:
            print("** class doesn't exist **")

    def do_all(self, usr_in):
        _input = usr_in.split()
        objects = storage.all()
        for key in objects.keys():
            if _input:
                if _input[0] not in class_check:
                    print("** class doesn't exist **")
                    break
                if _input[0] == objects[key].__dict__['__class__']:
                    print(objects[key])
            else:
                print(objects[key])

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
    class_check = {"Amenity", "BaseModel", "City" "Place", "Review",
                   "State", "User"}
    HBNBCommand().cmdloop()
