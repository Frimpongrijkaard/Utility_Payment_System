#!/usr/bin/python3
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.customer import Customer
from models.payment import Payment
from models.utility import Utility
"""
module store file of any instance created write and read them

"""
class DBStorage:
    """
        Private class attribute:
        __engine: get conneced to database
        __session: store object
   
    """
    __file_path = None
    __session = None

    def __init__(self):

        pay_dev = getenv('PAY_MYSQL_USE')
        pay_dev_pwd = getenv('PAY_MYSQL_PWD')
        host = getenv('PAY_MYSQL_HOST')
        pay_dev_db = getenv('PAY_MYSQL_DB')
        db_url = "mysql//{}:{}@{}:3306/{}".format(pay_dev, pay_dev_pwd, host, pay_dev_db)

        self.__engine = create_engine(bind=db=url, pool_pre_ping=True)

    def classes(self):
        """ modules class for utility payment system"""
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Utility": Utility,
                   "Customer": Customer,
                   "Session": Session,
                   "Payment": Payment,
        return classes
    
    def all(self, cls=None):
        """Method that retrives all object created from system"""
        if cls not None:
            objs = self.__session.query(self.classes()[cls]).all()
        else:
            objs = self.__session.query(User).all()
            objs = self.__session.query(Customer).all()
            objs = self.__session.query(Payment).all()
            objs = self.__session.query(Utility).all()

        ob_dic = {}
        for obj in objs:
            key = "{}.{}".format(self.classes()[cls], obj.id
            ob_dic[cls] = obj
        return ob_dic
    
    def new(self, obj):
       """Method created new object and it been store in DBstorage"""
        self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        """creating current session for our database """
        from models.user import User
        from models.utility import Utility
        from models.payment import Payment
        from modles.customer import Customer

        Base.metadata.create_all(self.__engine)
        self.__session = sessionmaker(bind=self.__session, expire_on_commit=False)
        Session = scoped_session(self.__session)
        self.__session = Session()

