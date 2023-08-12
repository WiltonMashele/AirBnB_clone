#!/usr/bin/python3
import sys
import cmd


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Exit the interpreter."""
        return True
    def help_help(self):
        """ Prints help command description """
        print("Provides description of a given command")

    def help_quit(self):
        print("Quit command to exit the program")

    def do_EOF(self, args):
        """handles end of file"""
        return True

    def emptyline(self):
        """overrides emptyline method"""
        pass


if __name__ == "__main__":
    HBNBCommand().cmdloop()
