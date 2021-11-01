from flask import Flask
from flask_login import LoginManager
#from sqlalchemy import SQLAlchemy

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'sbfbwfvnioocnibiwurvosdnjs'


    from .views import views
    from .auth import auth
    from .post import post


    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    app.register_blueprint(post, url_prefix='/')
    

    from .models import User, User_info, Session
    local_session = Session()

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return local_session.query(User).filter(User.id == id).first()

    return app