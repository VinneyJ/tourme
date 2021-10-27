#!/usr/bin/python3
from flask import Flask, render_template, url_for
from tourmeApp.db.base_model import User, User_info, Session, engine
from forms import RegistrationForm, LoginForm
app = Flask(__name__)

app.config['SECRET_KEY'] = 'LongAndRandomSecretKey'

local_session = Session(bind=engine)


@app.route('/', strict_slashes=False)
def home():
    return "<p>Hello, World!</p>"


@app.route("/register/", methods=['GET', 'POST'])
def register_user():
    form = RegistrationForm()

    return render_template('register.html', title='Register', form=form)



@app.route("/login/", methods=['GET', 'POST'])
def login_user():
    form = LoginForm()

    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=5000)