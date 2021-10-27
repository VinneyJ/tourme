#!/usr/bin/python3
#import tourmeApp
import uuid
from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, create_engine
from datetime import datetime
import secrets



Base = declarative_base()

engine = create_engine('mysql+mysqldb://{0}:{1}@{2}/{3}'.format('vince2', 'Nairobi00!', 'localhost', 'tourme'))

Session =  sessionmaker()
"""
class User():
    user_id
    username
    email
    password
    created_at
    updated_at


class User_info(User):
    user
    first_name
    last_name
    phone_number
    date_of_birth
    status
    created_at
    updated_at

class Address(User):
    user_foreign_key
    country
    city
    address

class Tourist(User):


"""

class User(Base):
    __tablename__ = "users"
    id =  Column(String(60), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(25), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.utcnow)
    updated_at = Column(DateTime(), default=datetime.utcnow)
    user_info = relationship('User_info', backref='user', uselist=False)


    def __init__(self, username, email, password, user_id=None):
        if user_id == None:
            self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        

    def __repr__(self):
        return "<{}, {}, {}, {}>".format(self.username, self.email, self.password, self.created_at)


class User_info(User, Base):
    __tablename__ = "user_info"
    person_info_id = Column(String(60), primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    phone_number = Column(Integer(), nullable=False)
    date_of_birth = Column(Integer(), nullable=False)
    about = Column(String(250), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    

    def __init__(self, username, email, password, first_name, last_name, phone_number, date_of_birth, about, person_info_id=None):
        super().__init__(username, email, password)
        if person_info_id == None:
            self.person_info_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.date_of_birth = date_of_birth
        self.about = about

    def __repr__(self):
        return "<{}, {} {}, {}, {}>".format(self.username, self.first_name, self.last_name, self.about, self.created_at)








user = User(username="Vincent", email="vince@company.com", password="123456")


print(user)