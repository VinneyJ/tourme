#!/usr/bin/python3
"""
Create tables
"""


#import tourmeApp
from base_model import User, User_info, Base, engine

Base.metadata.create_all(engine)