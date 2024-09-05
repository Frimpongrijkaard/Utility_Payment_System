#!/usr/bin/python3
""" Module represenntation for a utility payment system
"""
from datetime import datetime
import uuid
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import column, string, datetime, integer

Base = declarative_base()

class BaseModel:
    """ Representation of models where all the class is inherit
    from the Base of this module for utility payment system
    """
    id = column(string(60), unique=True, nullable=False, primary_key=True)
    created_at = column(datetime, nullable=False, default=datetime.utcnow())
    updated_at = column(datetime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):

        tform = "%Y/%m/%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        if kwargs:
            for k, v in kwargs.items():
                if k == "created_at" or k == "updated_at":
                    kwargs[k] = datetime.strptime(v, tform)
                if k != "__class__":
                    self.__dict__[k] = v
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            if "updated_at" not in kwargs:
                self.updated_at = datetime.now()
            if "created_at" not in kwargs:
                self.created_at = datetime.now()
        else:
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()

    def to_dict(self):
        clas_n = self.__class__.__name__
        dict_1 = self.__dict__.copy()
        dict_1["__class__"] = clas_n
        dict_1["created_at"] = datetime.now()
        dict_1["updated_at"] = datetime.now()
        return dict_1

    def __str__(self):
        clas_n = self.__class__.__name__
        return "[{}] ---  ({}) -- {}".format(clas_n, self.id, self.__dict__)

    def save(self):
        from models import storage
        self.updated_at = datetime.now()
        storage.new()
        storage.save()

    def delete(self):
        """ Method delete the instance of the object"""
        from models import storage
        storage.delete(self)



