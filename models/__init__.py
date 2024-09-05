#!/usr/bin/python3
from models.engine.filestorage import FileStorage
from model.engine.dbstorage import DBStorage
from os import getenv

if getenv('') == 'db':
    storage = DBStorage()
else:
    storage = FileStorage()
storage.reload()
