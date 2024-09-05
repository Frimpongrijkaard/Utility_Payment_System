#!/usr/bin/python3
"""Module for a customer detail for utility payment"""
from models.base_model import BaseModel, Base
from sqlalchemy import string, Float, column
from sqlalchemy.orm import ForeignKey, relationship

class CustomerUtility(BaseModel, Base):
    """Representation for customer"""
    __Tablename__ = "customerutility"


    current_balance = column(Float, default=0.0)
    account_number = column(string(128), nullable=False)
    customer_id = column(string(60), ForeignKey("customer.id"), nullable=False)
    utility_id = column(string(60), ForeignKey("utility.id"), nullable=False)
    customer = relationship("Customer", back_populates="CustomerUtility")
    utility = relationship("utility", back_populate="CustomerUtility")
    payment = relationship("payment", back_populate="CustomerUtility")
