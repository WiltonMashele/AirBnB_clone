#!/usr/bin/python3
"""Console program"""
import sys
import cmd
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.city import City
from models.amenity import Amenity
from models.state import State
from models.review import Review
from models import storage
import shlex


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = {"BaseModel": BaseModel, "User": User, "Place": Place,
               "City": City, "Amenity": Amenity, "State": State,
               "Review": Review}
    com = ['create', 'show', 'update', 'all', 'destroy', 'count']

    def do_count(self, class_name):
        """counts number of objects of a class"""
        count = 0
        all_objs = storage.all()
        for key, value in all_objs.items():
            list_cls = key.split(".")
            if list_cls[0] == class_name:
                count += 1
        print(count)

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

    def do_create(self, arg):
        """create a new instance of BaseModel,
        save it and print it"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        class_name = args[0]
        if class_name in HBNBCommand.classes:
            new_instance = HBNBCommand.classes[class_name]()
            new_instance.save()
            print(new_instance.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """print the string representation of an instance"""
        if not arg:
            print("** class name missing **")
            return
        args = arg.split()
        cls_name = args[0]
        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_name = value.__class__.__name__
                obj_id = value.id
                if obj_name == cls_name and obj_id == args[1].strip('"'):
                    print(value)
                    return
            print("** no instance found **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split(' ')
        cls_name = args[0]
        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                ob_cls = value.__class__.__name__
                ob_id = value.id
                if ob_cls == cls_name and ob_id == args[1].strip('"'):
                    del value
                    del storage._FileStorage__objects[key]
                    storage.save()
                    return
            print("** no instance found **")

    def do_all(self, arg):
        """ Prints string represention of all instances of a given class """
        if not arg:
            print("** class name missing **")
            return
        args = arg.split(' ')
        cls_name = args[0]
        if cls_name not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            all_objs = storage.all()
            list_of_instances = []
            for key, value in all_objs.items():
                ob_name = value.__class__.__name__
                if ob_name == cls_name:
                    list_of_instances += [value.__str__()]
            print(list_of_instances)

    def do_update(self, arg):
        """ Updates an instance based on the class name and id """

        if not arg:
            print("** class name missing **")
            return

        a_empty = ""
        for argv in arg.split(','):
            a_empty = a_empty + argv

        args = shlex.split(a_empty)

        if args[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            for key, value in all_objs.items():
                obj_cls = value.__class__.__name__
                ob_id = value.id
                if obj_cls == args[0] and ob_id == args[1].strip('"'):
                    if len(args) == 2:
                        print("** attribute name missing **")
                    elif len(args) == 3:
                        print("** value missing **")
                    else:
                        setattr(value, args[2], args[3])
                        storage.save()
                    return
            print("** no instance found **")

    def precmd(self, arg):
        """parses command input"""
        if '.' in arg and '(' in arg and ')' in arg:
            l_cls = arg.split('.')
            cnd = list_cls[1].split('(')
            args = cnd[1].split(')')
            if l_cls[0] in HBNBCommand.classes and cnd[0] in HBNBCommand.com:
                arg = cnd[0] + ' ' + l_cls[0] + ' ' + args[0]
        return arg


if __name__ == "__main__":
    HBNBCommand().cmdloop()
