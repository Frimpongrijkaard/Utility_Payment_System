#!/usr/bin/python3
"""Module repesentation of the utility system
"""
from models.base_model import BaseModel, Base
from sqlalchemy import column, string, integer, datetime
from sqlalchemy.orm import relationship

class User(BaseModel, Base):

    """ Representation fusers for the reistrationn and
    login
    """
    __Tablename__ = 'users'

    username = column(string(128),unique=True,  nullable=False)
    email = column(string(128), unique=True, nullable=False)
    password = column(string(128), nullable=False)
    customer = relationship("Customer", back_populates="User", uselist=False)


