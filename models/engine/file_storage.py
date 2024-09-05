#!/usr/bin/python3
import json
import os
from models.base_model import BaseModel
from models.payment import Payment
from models.utility import utility
from models.customer import Customer
from models.customutility import CustomerUtility
from models.user import User
"""
module store file of any instance created write and read them

"""
class FileStorage:
    """
    json file serialize and deserialize instances
        Private class attribute:
        __file_path: json file name
        __object: dictionary in python
    
    """
    __file_path = "file.json"
    __objects = {}

    def classes(self):
        """ modules class for utility payment system"""
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Utility": Utility,
                   "Customer": Customer,
                   "CustomerUtility" : CustomerUtility,
                   "Payment": Payment}
        return classes
    
    def all(self, cls=None):
        """Method that retrives all object created from system"""
        if cls is not None:
            dict1 = {}
            for k, v in self.__objects.items():
                   if isinstance(v, cls):
                        dict1[k] = v
            return dict1
        return FileStorage.__objects
    
    def new(self, obj):
        """Method created new object and it been store in filestorage"""
        class_n = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(class_n, obj.id)] = obj

    def save(self):
        """
        serialize __object to the json file 
        __object that store all that instance created
        __file_path that receive all json string into json file

        """

        with open(FileStorage.__file_path, 'w', encoding='utf-8') as file:
            mydict = {}
            obj_dict = FileStorage.__objects
            for k, v in obj_dict.items():
                mydict[k] = v.to_dict()
            json.dump(mydict, file)

    def reload(self):
        """deserialize the json file
       load back the file thaat contain the json_string

        """
        try:
            with open(FileStorage.__file_path) as f:
                obj = json.load(f)
                mydict = {}
                for k, v in obj.items():
                    clas_n = v["__class__"]
                    mydict[k] = self.classes()[v["__class__"]](**v)
                    del v["__class__"]
                FileStorage.__object = mydict
        except FileNotFoundError:
            return

