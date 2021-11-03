#!/usr/bin/python3


if __name__ == '__main__':
    """
    deletes all the tables and creates them again with a dummy data
    """

    from models import User, User_info, Post, Base, Session, engine
    from werkzeug.security import generate_password_hash

    name = "Vince"
    email = "vince@gmail.com"
    password1 = "123Kenya00"

    local_session = Session()
    def create_all_tables_again():
        Base.metadata.create_all(engine)



    def create_dummy_user():
        user = User(username=name, email=email, password=generate_password_hash(password1, method='sha256'))
        local_session.add(user)
        local_session.commit()

    def reload():
        Post.__table__.drop(engine)
        User_info.__table__.drop(engine)
        User.__table__.drop(engine)
        create_all_tables_again()
        create_dummy_user()

    reload()