#!/usr/bin/python3

#from models.engine.file_storage import FileStorage
from models.engine.dbstorage import DBStorage
from os import getenv

#if getenv('PAY_TYPE_STORAGE') == 'db':
    
storage = DBStorage()
#else:
    
    #storage = FileStorage()
storage.reload()
print(storage)
