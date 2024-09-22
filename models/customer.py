#!/usr/bin/python3
"""Module for a customer detail for utility payment"""
from models.base_model import BaseModel, Base
from sqlalchemy import String, Column, ForeignKey
from sqlalchemy.orm import relationship
from models.utility import Utility

class Customer(BaseModel, Base):
    """Representation for customer"""
    __table_args__ = {'extend_existing': True}
    __tablename__ = "customers"


    first_name = Column(String(128), unique=True, nullable=False)
    last_name = Column(String(128), unique=True, nullable=False)
    address = Column(String(128))
    phone_number = Column(String(128))
    user_id = Column(String(60), ForeignKey("users.id"))
    utility = relationship("Utility", back_populates="customers")
    payment = relationship("Payment", back_populates='customers')
