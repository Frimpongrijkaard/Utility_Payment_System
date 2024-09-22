#!/usr/bin/python3
from models import storage
from models.base_model import BaseModel, Base
from models.user import User
from models.customer import Customer

user1 = User(username='frimpong Rijkaard', email='frimpongrijkaard@gmail.com', password='123456')
#user2 = User(username='lanmak frimpong', email='lanmakfrimpong@icloud.com', password='23d54f_3')
#customer1 = Customer(first_name="frimpong", last_name='Rijkaard', address='block 16/E', user1=user1, phone_number='12345678')


#customer1.save()
user1.save()



