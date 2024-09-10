#!/usr/bin/python3
import json
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
from models.base_model import Base
from sqlalchemy.ext.declarative import declarative_base
from models.user import User
from models.customer import Customer
from models.payment import Payment
from models.utility import Utility
from models.customutility import CustomerUtility
"""
module store file of any instance created write and read them
"""
#Base = declarative_base()

class DBStorage:
    """
        Private class attribute:
        __engine: get conneced to database
        __session: store object
   
    """
    __engine = None
    __session = None

    def __init__(self):

        user = getenv('PAY_MYSQL_USE')
        pwd = getenv('PAY_MYSQL_PWD')
        host = getenv('PAY_MYSQL_HOST')
        db = getenv('PAY_MYSQL_DB')
        db_url = 'mysql+mysqldb://{}:{}@{}/{}?charset=utf8mb4'.format(user, pwd, host, db)

        self.__engine = create_engine(db_url, pool_pre_ping=True, echo=True)

    def classes(self):
        """ modules class for utility payment system"""
        classes = {"BaseModel": BaseModel,
                   "User": User,
                   "Utility": Utility,
                   "Customer": Customer,
                   "Session": Session,
                   "Payment": Payment,
                   "CustomerUtility":CustomerUtility}
        return classes
    
    def all(self, cls=None):
        """Method that retrives all object created from system"""
        if cls:
            objs = self.__session.query(self.classes()[cls]).all()
        else:
            objs += self.__session.query(User).all()
            objs += self.__session.query(Customer).all()
            objs += self.__session.query(Payment).all()
            objs += self.__session.query(Utility).all()

        ob_dic = {}
        for obj in objs:
            key = "{}.{}".format(self.classes()[cls], obj.id)
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
        from models.customer import Customer
        from models.customutility import CustomerUtility

        Base.metadata.create_all(self.__engine)

        sess = sessionmaker(bind=self.__session, expire_on_commit=False)

        Session = scoped_session(sess)

        self.__session = Session()

    def close(self):
        return self.__session.close()

