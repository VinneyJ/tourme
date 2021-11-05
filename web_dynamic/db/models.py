#!/usr/bin/python3

"""
This file maps database tables to be created
"""
#import tourmeApp
from flask_login import UserMixin
import uuid
from enum import unique
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey,Boolean, create_engine
from datetime import datetime






Base = declarative_base()

engine = create_engine('mysql+mysqldb://{0}:{1}@{2}/{3}'.format('root', 'brro', 'localhost', 'tourme'), echo=True)

Session =  sessionmaker(bind=engine)


class User(Base, UserMixin):
    """
    users table
    """
    __tablename__ = "users"
    id =  Column(String(60), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(25), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    is_guide = Column(Boolean, unique=False, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    user_info = relationship('User_info', backref='user', cascade="all, delete, delete-orphan", uselist=False)
    posts = relationship('Post', backref='author', cascade="all, delete, delete-orphan")


    def __init__(self, username, email, password, is_guide, user_id=None):
        if user_id == None:
            self.id = str(uuid.uuid4())
        self.user_id = user_id
        self.username = username
        self.email = email
        self.password = password
        self.is_guide = is_guide
        self.created_at = datetime.utcnow()
        self.updated_at = self.created_at
        

    def __repr__(self):
        return "<{}, {}, {}, {}>".format(self.username, self.email, self.password, self.is_guide, self.created_at)



class User_info(Base, UserMixin):
    """
    User Info table
    """
    __tablename__ = "user_info"
    person_info_id = Column(String(60), primary_key=True)
    first_name = Column(String(25), nullable=False)
    last_name = Column(String(25), nullable=False)
    phone_number = Column(Integer(), nullable=False)
    country = Column(String(25), nullable=False)
    city = Column(String(25), nullable=False)
    date_of_birth = Column(Integer(), nullable=False)
    about = Column(String(250), nullable=False)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    

    def __init__(self, first_name, last_name, phone_number, country, city, date_of_birth, about, user_id=None):
    
        if user_id == None:
            self.person_info_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.country = country
        self.city = city
        self.date_of_birth = date_of_birth
        self.about = about
        self.user_id = user_id

    def __repr__(self):
        return "<{}, {} {}, {}, {}>".format(self.first_name, self.last_name, self.phone_number, self.date_of_birth, self.about)


class Post(Base, UserMixin):
    __tablename__ = "posts"
    content_id = Column(String(60), primary_key=True)
    content = Column(String(250), nullable=False)
    post_created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    post_updated_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, content, user_id, content_id=None):

        if content_id == None:
            self.content_id = str(uuid.uuid4())
        self.content = content
        self.user_id = user_id
        self.post_created_at = datetime.utcnow()
        self.post_updated_at = self.post_created_at

    def __repr__(self):
        return "<{}, {}, {}>".format(self.content, self.post_created_at, self.post_updated_at)
