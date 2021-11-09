#!/usr/bin/python3

"""
This file maps database tables to be created
"""
#import tourmeApp
from flask_login import UserMixin
import uuid
from enum import unique
from os import getenv
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import backref, sessionmaker, relationship
from sqlalchemy import Column, String, Integer, DateTime, ForeignKey, Boolean, create_engine
from datetime import datetime



Base = declarative_base()

MYSQL_DB_HOST = getenv('MYSQL_DB_HOST', default='db')
MYSQL_DB_NAME = getenv('MYSQL_DB_NAME', default='tourme')
MYSQL_DB_USER = getenv('MYSQL_DB_USER', default='vince2!')
MYSQL_DB_PASSWORD = getenv('MYSQL_DB_PASSWORD', default='')


# MYSQL_DB_HOST = getenv('MYSQL_DB_HOST')
# MYSQL_DB_NAME = getenv('MYSQL_DB_NAME')
# MYSQL_DB_USER = getenv('MYSQL_DB_USER')
# MYSQL_DB_PASSWORD = getenv('MYSQL_DB_PASSWORD')


engine = create_engine('mysql+mysqldb://{0}:{1}@{2}/{3}'.format(MYSQL_DB_USER, MYSQL_DB_PASSWORD, MYSQL_DB_HOST, MYSQL_DB_NAME), echo=True)


# engine = create_engine('mysql+mysqldb://{0}:{1}@{2}/{3}'.format(
#     'vince2', 'Nairobi00!', 'localhost', 'tourme'), echo=True)

Session = sessionmaker(bind=engine)


class User(Base, UserMixin):
    """
    users table
    """
    __tablename__ = "users"
    id = Column(String(60), primary_key=True)
    username = Column(String(25), nullable=False, unique=True)
    email = Column(String(25), nullable=False, unique=True)
    password = Column(String(150), nullable=False)
    is_guide = Column(Boolean, unique=False, default=False)
    created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    updated_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    user_info = relationship('User_info', backref='user',
                             cascade="all, delete, delete-orphan", uselist=False)
    posts = relationship('Post', backref='author',
                         cascade="all, delete, delete-orphan")

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
    region = Column(String(25), nullable=False)
    city = Column(String(25), nullable=False)
    date_of_birth = Column(DateTime, nullable=False)
    about = Column(String(250), nullable=False)
    guide_created_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    guide_updated_at = Column(DateTime(timezone=True), default=datetime.utcnow)
    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, first_name, last_name, phone_number, country, region, city, date_of_birth, about, user_id, person_info_id=None):

        if person_info_id == None:
            self.person_info_id = str(uuid.uuid4())
        self.first_name = first_name
        self.last_name = last_name
        self.phone_number = phone_number
        self.country = country
        self.region = region
        self.city = city
        self.date_of_birth = date_of_birth
        self.about = about
        self.user_id = user_id
        self.guide_created_at = datetime.utcnow()
        self.guide_updated_at = self.guide_created_at

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


class Message(Base, UserMixin):
    __tablename__ = "messages"
    Message_id = Column(String(60), primary_key=True)
    Message_text = Column(String(2500), nullable=False)
    Message_created_at = Column(DateTime(), default=datetime.utcnow)
    Message_updated_at = Column(DateTime(), default=datetime.utcnow)
    from_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    to_user_id = Column(String(60), ForeignKey('users.id'), nullable=False)

    def __init__(self, Message_text, from_user_id, to_user_id, Message_id=None):

        if Message_id == None:
            self.Message_id = str(uuid.uuid4())
        self.Message_text = Message_text
        self.from_user_id = from_user_id
        self.to_user_id = to_user_id
        self.Message_created_at = datetime.utcnow()
        self.Message_updated_at = self.Message_updated_at

    def __repr__(self):
        return "<{}, {}, {}>".format(self.Message_text, self.Message_created_at, self.Message_updated_at, self.from_user_id, self.to_user_id)
