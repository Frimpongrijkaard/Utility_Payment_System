#!/usr/bin/python3
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session
from os import getenv
#from models.base_model import Base
from models.base_model import BaseModel, Base
#from sqlalchemy.ext.declarative import declarative_base
from models.user import User
#from models.customer import Customer
from models.payment import Payment
#from models.utility import Utility
from models.payment_history import PaymentHistory
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
        db_url = "mariadb://DB_user:sorry@127.0.0.1/Dbshort"#.format(user, pwd, host, db)

        self.__engine = create_engine(db_url, pool_pre_ping=True, echo=True)

    #def classes(self):
     #   """ modules class for utility payment system"""
        #from models.base_model import BaseModel, Base
        #from models.user import User
        #from models.customer import Customer
        #from models.payment import Payment
        #from models.utility import Utility
        #from models.customutility import CustomerUtility
      #  classes = {"BaseModel": BaseModel,
       #            "User": User,
        #           "Utility": Utility,
         #          "Customer": Customer,
          #         #"Session": Session,
           #        "Payment": Payment,
            #       "CustomerUtility":CustomerUtility}
        #return classes
    
    def all(self, cls=None):
        """Method that retrives all object created from system"""
        #from models.base_model import BaseModel, Base
        #from models.user import User
        #from models.customer import Customer
        #from models.payment import Payment
        #from models.utility import Utility
        #from models.customutility import CustomerUtility
        dic = {}
        if cls:
            if type(cls) is str:
                cls = eval(cls)
            query = self.__session.query(cls)
            for elem in query:
                key = "{}.{}".format(type(elem).__name__, elem.id)
                dic[key] = elem
        else:
            list_1 = []#User, Customer, Utility, PaymentHistory]
            for clase in list_1:
                query = self.__session.query(clase)
                for elem in query:
                    key = "{}.{}".format(type(elem).__name__, elem.id)
                    dic[key] = elem
        return (dic)
    
    def new(self, obj):
       """Method created new object and it been store in DBstorage"""
       self.__session.add(obj)

    def save(self):
        self.__session.commit()

    def reload(self):
        """creating current session for our database """
        #from models.base_model import BaseModel, Base
        #from models.user import User
        #from models.utility import Utility
        #from models.payment import Payment
        #from models.customer import Customer
        #from models.customutility import CustomerUtility

        Base.metadata.create_all(self.__engine)

        Session = sessionmaker(bind=self.__engine, expire_on_commit=False)

        #Session = scoped_session(ses)

        self.__session = Session()

    def delete(self, obj=None):
        if obj:
            self.__session.delete(obj)

    def close(self):
        self.__session.close()

