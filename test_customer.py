#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel, Base
from models.customer import Customer
from models.user import User



customer1 = Customer(first_name="frimpong", last_name='Rijkaard', address='block 16/E', user1=User.id, phone_number='12345678')

customer1.save()