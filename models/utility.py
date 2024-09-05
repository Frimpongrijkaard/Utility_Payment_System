#!/usr/bin/python3
"""Module representation of utility syetem """
from models.base_model import BasseModel
from sqlalchemy.orm import ForeignKey, relationship
from sqlalchemy import column, Float, string
class Utility(BaseModel):
    """Repesentation of utility attribute for 
    utility payment system
    """
    __Tablename__ = "utility"

    name = column(string(128), nullable=False)
    description = column(text)
    rate_per_unit = column(Float, Default=0.0)
    customerutility = relatisonship("Customerutility", back_populates="Utility")

