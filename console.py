def do_update(self, args):
    args = shlex.split(args)
    if len(args) == 0:
        print("** class name missing **")
        return
    if len(args) == 1:
        print("** instance id missing **")
        return
    if len(args) == 2:
        print("** attribute name missing **")
        return
    if len(args) == 3:
        print("** value missing **")
        return
    obj_dict = storage.all(args[0])
    try:
        eval(args[0])
    except NameError:
        print("** class doesn't exist **")
        return
    key = args[0] + "." + args[1]
    try:
        obj = obj_dict[key]
    except KeyError:
        print("** no instance found **")
        return
    setattr(obj, args[2], args[3])
    storage.save()
