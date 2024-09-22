#!/usr/bin/python3
"""Module representation of utility syetem """
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Float, String, ForeignKey
#from models.payment import Payment
#from models.customer import Customer


class Utility(BaseModel, Base):
    """Repesentation of utility attribute for 
    utility payment system
    """
    __table_args__ = {'extend_existing': True}
    __tablename__ = "utilities"

    company_name = Column(String(128), nullable=False)
    service_type = Column(String(128), nullable=False)
    rate_per_unit = Column(Float, default=0.0)
    customer = relationship("Customer", back_populates="utilities")
    payment = relationship("Payment", back_populates="utilities")