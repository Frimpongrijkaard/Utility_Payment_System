#!/usr/bin/python3
"""Module for payment app for utility system"""
from model.basemodel import BaseModel
from sqlalchemy.orm import ForeignKey, relationship
from sqlalchemy import column, string, Float, Datetime

class Payment(BaseModel):
    """Representation of the payement class and their attribute"""
    __Tablename__ = 'payment'

    amount_paid = column(Float, default=0.0, nullable=False)
    payment_date = column(Datetime, default=Datetime.utcnow, nullable=False)
    payment_method = column(Enum('Credit card', 'Debit Card', 'Bank Transfer', 'Paypal', name='payment methods', nullable=False))
    confirmation_number = column(string(128), unique=True, nullable=False)
    customerutility_id = column(string, nullable=False, ForeignKey('customerutility.id'))
    customerutility = relationship('CustomerUtility', back_populates='Payment')
