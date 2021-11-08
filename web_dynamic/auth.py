"""
This file handles authentication features
"""

from flask import Blueprint, render_template, request, flash, redirect, url_for
from .db.models import User, User_info, Session
from werkzeug.security import generate_password_hash, check_password_hash
from werkzeug.datastructures import MultiDict
from flask_login import login_user, login_required, logout_user, current_user,login_manager
#import re

local_session = Session()

auth = Blueprint('auth', __name__)


@auth.route('/auth/login', methods=['GET', 'POST'])
def login():
    
    """
    Login user
    """
    
    if request.method == 'POST':
        email = request.form.get("email")
        password = request.form.get("password")


        user = local_session.query(User).filter(User.email == email).first()
        if user:
            if check_password_hash(user.password, password):
                flash('Logged in successfully!', category='success')
                login_user(user, remember=True)
                next_page = request.args.get('next')
                return redirect(url_for('views.home'))
            else:
                flash('Sorry, Incorrect password, Try again!', category='error')
        else:
            flash('Email does not exist!', category='error')

    return render_template("login.html", user=current_user)


@auth.route('/auth/logout')
@login_required
def logout():
    
    """
    Log out User
    """
    
    logout_user()
    return redirect(url_for('auth.login'))


@auth.route('/auth/sign-up', methods=['GET', 'POST'])
def sign_up():
    """
    Register a new user
    """
    
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
            user = User(username=name1, email=email, is_guide=False, password=generate_password_hash(password, method='sha256'))
            local_session.add(user)
            local_session.commit()
            login_user(user, remember=True)
            flash('Account created', category='success')
            return redirect(url_for('views.home'))

    return render_template("sign_up.html", user=current_user)


@auth.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    """
    View user profile
    """

    return render_template("account.html", user=current_user)




@auth.route('/register_guide', methods=['GET', 'POST'])
@login_required
def register_guide():
    """
    Takes more info about guide registration
    """

    if request.method == 'POST':
        firstname = request.form.get('firstname')
        lastname = request.form.get('second_name')
        phonenumber = request.form.get('phone_number')
        country = request.form.get('country')
        region = request.form.get('region')
        city = request.form.get('city')
        dob = request.form.get('date_of_birth')
        about = request.form.get('about')

        user = local_session.query(User).filter(User.id == current_user.get_id()).first()


        add_info = User_info(first_name=firstname, last_name=lastname, phone_number=phonenumber, country=country, city=city, region=region, date_of_birth=dob, about=about, user_id=user.id)
        local_session.add(add_info)
        local_session.commit()
        flash("Congratulations, you are now a guide!", category="success")
        return redirect(url_for('views.home'))

    return render_template("guide_info.html", user=current_user)
