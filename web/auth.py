from flask import Blueprint, render_template,request
from flask.helpers import flash

auth = Blueprint('auth', __name__)
@auth.route('/login')
def login():
    return render_template('login.html', text="the MvP")

@auth.route('/logout')
def logout():
    return "your loged out"

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')

        if len(email) < 4:
            flash('Email filde is wrong ',catagorey='error')
        else:
            flash('aacount created', category='success')

    return render_template('signup.html', text="the MvP")