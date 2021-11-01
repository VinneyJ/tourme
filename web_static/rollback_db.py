#!/usr/bin/python3

if __name__ == '__main__':
    """
    script to roll back the db
    """
    from models import User, User_info, Post, Session 

    local_session = Session()
    def rollback():
        local_session.rollback()

    rollback()