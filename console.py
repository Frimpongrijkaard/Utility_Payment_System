!/usr/bin/env python3
""" A test command interpreter that is helps test our codebase 
file from the storage base 
"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.payments import Payment
from models.utility import Utility
from models.customutility import CustomerUtility
from models.customer import Customer
from Datetime import Datetime
import json

class HBNBCommand(cmd.Cmd):
    """ Represent entry point of command interpreter
    """
    prompt = "(hbnb) "
    

    def do_quit(self, arg):
        """ Quit from the program"""
        print()
        return True
    
    def do_EOF(self, arg):
        """ this should be the end of line"""
        print()
        return True

    def emptyline(self):
        """ when No argment is enter repeat the prompt"""
        pass

    def do_create(self, line):
        """Method create instance of classes base on id and save it"""
        if not line:
            print("** class name missing **")
            return 
       if line not in storage.classes():
            print("** class doesn't exist **")
        else:
            obj = storage.classes()[line]()
            obj.save()
            print(obj.id)

    def do_show(self, line):
        """method that print string representation of instance of classses"""
        if line == '' or line == None:
            print("** class name missing **")
        else:
            args = line.split(" ")

            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                sh = "{}.{}".format(args[0], args[1])
                if sh not in storage.all():
                    print("** no instance found ** ")
                else:
                    print(storage.all()[sh])

    def do_destroy(self, line):
        """method delete instance of the class for id"""
        if line == "" or line == None:
            print("** class name missing **")
        else:
            args = line.split(" ")
           if args[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")
            else:
                sh = "{}.{}".format(args[0], args[1])
                if sh not in storage.all():
                    print("** no instance found **")
                else:
                    del storage.all()[sh]

    def do_all(self, line):
        """ method print string representation of all the instance
        based or not class name 
        """
        if line != "":
            args = line.split(' ')
            if args[0] not in storage.classes():
                print("** class doesn't exist **")
            else:
                lis = [str(obj) for key, obj in storage.all().items()
                      if type(obj).__name__ == args[0]]
                print(lis)
        else:
            ob_l = [str(obj) for key, obj in storage.all().items()]
            print(ob_l)

    def do_update(self, line):
        """method update the instance of the class with an id and save the update 
        instance inside the storage.
        """
        if len(line)  == 0:
            print(" ** class name missing **")
        else:
            arg = line.split(" ")
            if arg[0] not in storage.classes():
                print("** class doesn't exist **")
            elif len(arg) < 2:
                print("** instance id misssing **")
            else:
                key = "{}.{}".format(arg[0], arg[1])
                if key not in storage.all():
                    print("** no instance found **")
                elif len(arg) < 3:
                    print(" ** attribute name missing **")
                elif len(arg) < 4:
                    print("** missing value **")
                else:
                    if len(arg) == 4:
                        arg1 = arg[3].strip('""')
                        key = "{}.{}".format(arg[0], arg[1])
                        print(key)
                        if hasattr(storage.all()[key], arg[2]):
                            attr_type  = type(getattr(storage.all()[key], arg[2]))
                            setattr(storage.all()[key], arg[2], attr_type(arg1))
                            storage.all()[key].save()
                            print(storage.all()[key].save())
                        else:
                            setattr(storage.all()[key], arg[2], arg1
)
                            storage.all()[key].save()

if  __name__ == '__main__':
    HBNBCommand().cmdloop()
