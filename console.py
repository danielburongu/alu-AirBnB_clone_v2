#!/usr/bin/python3
'''
    Implementing the console for the HBnB project.
'''
import cmd
import json
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, args):
        return True

    def do_EOF(self, args):
        return True

    def do_create(self, args):
        if len(args) == 0:
            print("** class name missing **")
            return
        try:
            args = shlex.split(args)
            new_instance = eval(args[0])()
            for i in args[1:]:
                try:
                    key, value = i.split("=")
                    if hasattr(new_instance, key):
                        value = value.replace("_", " ")
                        try:
                            value = eval(value)
                        except Exception:
                            pass
                        setattr(new_instance, key, value)
                except (ValueError, IndexError) as e:
                    pass
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
            return

    def do_show(self, args):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        obj_dict = storage.all(args[0])
        try:
            eval(args[0])
        except NameError:
            print("** class doesn't exist **")
            return
        key = args[0] + "." + args[1]
        try:
            value = obj_dict[key]
            print(value)
        except KeyError:
            print("** no instance found **")

    def do_destroy(self, args):
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        class_name = args[0]
        class_id = args[1]
        storage.reload()
        obj_dict = storage.all()
        try:
            eval(class_name)
        except NameError:
            print("** class doesn't exist **")
            return
        key = class_name + "." + class_id
        try:
            del obj_dict[key]
        except KeyError:
            print("** no instance found **")
        storage.save()

    def do_all(self, args):
        args = args.split(" ")
        obj_list = []
        objects = storage.all(args[0])
        try:
            if args[0] != "":
                models.classes[args[0]]
        except (KeyError, NameError):
            print("** class doesn't exist **")
            return
        try:
            for key, val in objects.items():
                obj_list.append(val)
        except Exception:
            pass
        print(obj_list)

    def do_update(self, args):
        storage.reload()
        args = shlex.split(args)
        if len(args) == 0:
            print("** class name missing **")
            return
        elif len(args) == 1:
            print("** instance id missing **")
            return
        elif len(args) == 2:
            print("** attribute name missing **")
            return
        elif len(args) ==
