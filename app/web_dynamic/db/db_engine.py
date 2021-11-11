#!/usr/bin/python3
"""
Create tables
"""
#import tourmeApp
if __name__ == '__main__':
    from models import User, User_info, Message, Base, engine
    def create_all_tables():
        Base.metadata.create_all(engine)


    create_all_tables()