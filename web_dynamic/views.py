"""
This files handles home features like display a list of tour guides.
"""
from flask import Blueprint, render_template, url_for, request, flash, redirect
from .db.models import User, User_info, Post, Session
#from flask_login import login_required, current_user


local_session = Session()

views = Blueprint('views', __name__)

@views.route('/')

def home():
    users = local_session.query(User).all()
    return render_template("home.html", users=users)



