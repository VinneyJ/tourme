"""
This file handles the creation and posting of posts
"""

from flask import Blueprint, render_template, url_for, request, flash, redirect
from .db.models import User, User_info, Post, Session
from sqlalchemy.orm import Query
from flask_login import login_required, current_user
from .views import views

local_session = Session()

post = Blueprint('post', __name__)

@post.route('/posts')
def show_posts():
    """
    Display or list all the posts from the latest by date
    """

    posts = local_session.query(Post).order_by(Post.post_created_at.desc()).all()

    return render_template("posts.html", posts=posts)


@post.route('/post', methods=['GET', 'POST'])
@login_required
def create_post():
    """
    Create new post
    """
    if request.method == 'POST':
        data = request.form.get('content')
        if len(data) < 1:
            flash('No post to add.', category='error')

        else:
            post = Post(content=data, user_id=current_user.id)
            local_session.add(post)
            local_session.commit()
            flash('Post added successfully!', category='success')
            return redirect(url_for('post.show_posts'))
            
    return render_template("create_post.html", user=current_user)


