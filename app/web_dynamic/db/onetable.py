#!/usr/bin/python3
"""
Create tables
"""
#import tourmeApp
if __name__ == '__main__':
    from models import User, User_info, Message, Base, engine
    def create_one():
        User_info.__table__.create(engine)


    create_one()