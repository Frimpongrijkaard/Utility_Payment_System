#!/usr/bin/python3
"""Module for a customer detail for utility payment"""
from models.base_model import BaseModel, Base
from sqlalchemy import string, column
from sqlalchemy.orm import ForeignKey, relationship

class Customer(BaseModel, Base):
    """Representation for customer"""
    __Tablename__ = "customer"


    first_name = column(string(128), unique=True, nullable=False)
    last_name = column(string(128), unique=True, nullable=False)
    address = column(string(128))
    phone_number = column(string(128))
    user_id = column(string(60), ForeignKey("user.id"), nullable=False)
    user = relationship("User", back_populates="Customer")
    customerutility = relationship("customerutility", back_populates='Customer')
