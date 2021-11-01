from flask import Blueprint, render_template, url_for, request, flash, redirect
from .models import User, User_info, Post, Session
from flask_login import login_required, current_user

local_session = Session()

views = Blueprint('views', __name__)

@views.route('/')
@login_required
def home():
    
    return render_template("home.html", user=current_user)