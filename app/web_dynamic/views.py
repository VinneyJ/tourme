"""
This files handles home features like display a list of tour guides.
"""
from flask import Blueprint, render_template, url_for, request, flash, redirect
from .db.models import User, User_info, Post, Message, Session
from flask_login import login_required, current_user
from sqlalchemy.sql.expression import desc


local_session = Session()

views = Blueprint('views', __name__)

@views.route('/')
@views.route('/home')
def home():
    users = local_session.query(User_info).order_by(User_info.guide_created_at.desc()).all()
    return render_template("home.html", users=users)



@views.route('/profile/<username>')
@login_required
def user_profile(username):
    """
    view user profile
    """
    user = local_session.query(User).filter(User.username == username).first()
    return render_template("profile.html", user=user)







@views.route('/Chat', methods=['GET', 'POST'])
@login_required
def message():
        users = local_session.query(User).filter(User.id != current_user.get_id())
        mess = local_session.query(Message).filter(Message.to_user_id == current_user.get_id()).order_by(desc(Message.Message_updated_at))
        messages22 = [u.__dict__ for u in mess]
        newmsg={}
        multimsg=dict()
        ii = 0
        for message in messages22:
            print( 'messaggggggggggggge' )
            for i ,v in message.items():
                #print( f">>'{i}' : '{v}' " )
                if i == 'Message_id':
                    newmsg[i]=v
                if i == 'Message_created_at':
                    newmsg[i]=v
                if i == 'from_user_id':
                    userss = local_session.query(User).filter(User.id == v).first()
                    tousername=userss.username
                    newmsg[i]=tousername
                if i == 'Message_text':
                    newmsg[i]=v
                if i == 'Message_updated_at':
                    newmsg[i]=v
            
            multimsg[str(ii)]=newmsg
            newmsg={}
            ii += 1
        print(multimsg)
        if request.method == 'POST':
            
            MSG_text = request.form.get("MSG_text")
            msg = Message(Message_text=MSG_text,
                from_user_id=current_user.get_id(),
                to_user_id=request.form.get("userid")
            )
            local_session.add(msg)
            local_session.commit()
            flash("Message sent successfully!", category='success')

        return render_template("message.html", user=current_user,Allusers=users,messages=multimsg)

