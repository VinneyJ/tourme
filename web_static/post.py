from flask import Blueprint, render_template, url_for, request, flash, redirect
from .models import User, User_info, Post, Session
from flask_login import login_required, current_user
from .views import views

local_session = Session()

post = Blueprint('post', __name__)


@post.route('/post', methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == 'POST':
        data = request.form.get('content')
        if len(data) < 1:
            flash('No post to add.', category='error')

        else:
            post = Post(content=data, user_id=current_user.id)
            local_session.add(post)
            local_session.commit()
            flash('Post added successfully!', category='success')
            
    return render_template("create_post.html", user=current_user)


@post.route('/posts')

def show_posts():
    return render_template("posts.html", user=current_user)