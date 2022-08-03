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



if __name__ == '__main__':
    HBNBCommand().cmdloop()
        
