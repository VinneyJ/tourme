from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import Place
from . import db
import json

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    if request.method == 'POST':
        place = request.form.get('place')

        if len(place) < 1:
            flash('place is too short!', category='error')
        else:
            new_place = Place(data=place, user_id=current_user.id )
            db.session.add(new_place)
            db.session.commit()
            flash('place added!', category='success')

    return render_template("home.html", user=current_user)


@views.route('/delete-place', methods=['POST'])
def delete_place():
    place = json.loads(request.data)
    placeId = place['placeId']
    place = Place.query.get(placeId)
    if place:
        if place.user_id == current_user.id:
            db.session.delete(place)
            db.session.commit()

    return jsonify({})

@views.route('/places')
def showall(): 
    return render_template("allplaces.html", user=current_user, alluser='all')
