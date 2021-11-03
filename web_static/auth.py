from flask import Blueprint, render_template, request, flash, redirect, url_for
from .models import User, User_info, Session
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, login_required, logout_user, current_user
import re

local_session = Session()

auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")


        user = local_session.query(User).filter(User.email == email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                # next_page = request.args.get('next')
                # return redirect(next_page) if next_page else redirect(url_for('views.home'))
                return redirect(url_for('views.home'))
            else:
                flash('Sorry, Incorrect password, Try again!', category='error')
        else:
            flash('Email does not exist!', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/auth/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/auth/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        name1 = request.form.get("firstname")
        email = request.form.get("email")
        password = request.form.get("password")
        confirm_password = request.form.get("confirm_password")

        user = local_session.query(User).filter(User.email == email).first()
        name = local_session.query(User).filter(User.username == name1).first()

        if user:
            flash('Email already exists!', category='error')
        elif name:
            flash('Username has already been taken!', category="error")
        elif len(email) < 4:
            flash('Email must be greater the 4 characters.', category='error')
        # elif not re.match(r'[^@]+@[^@]+\.[^@]+', email):
        #     flash('Invalid email address !', category='error',)
        elif len(name1) < 2:
            flash('Your name must be greater than 2 characters.', category='error')
        elif password != confirm_password:
            flash('Your passwords did not match!', category='error')
        elif len(password) < 7:
            flash('Your password must be greater than 7 characters', category='error')
        else:
            user = User(username=name1, email=email, password=generate_password_hash(password, method='sha256'))
            local_session.add(user)
            local_session.commit()
            login_user(user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():

    return render_template("account.html", user=current_user)



@auth.route('/register_guide', methods=['GET', 'POST'])
@login_required
def register_guide():

    return render_template("guide_info.html", user=current_user)