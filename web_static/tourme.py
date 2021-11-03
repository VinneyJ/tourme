#!/usr/bin/python3 Bash
""" RapScore Flask routing file """
from flask import Flask, render_template, request, redirect, jsonify
from models import storage
from models.address import Address
from models.contact_info import Contact_info
from models.investment import Investment
from models.tourist import tourist
from models.loan import Loan
from models.person import Person
from models.request import Request
from models.type_loan import Type_loan
from models.user import User
from models.Guide import Guide
import uuid


app = Flask(__name__)

# Close session when error connection to database
@app.teardown_appcontext
def close_db(error):
    """
    Remove SQLalchemy session
    Closes an open session
    """
    storage.close()

# Print error when API fails.
@app.errorhandler(400)
def error_db(error):
    """
    Remove SQLalchemy session
    When an error 400 appears show
    the error in terminal
    """
    print(error)

# Home landing web appplication page
# This home page is where the client lands for the first time
# to read about the project and choos which type of account it wants.
@app.route('/')
@app.route('/home', strict_slashes=False)
def index():
    """ Display index html """
    return render_template('index.html', id=str(uuid.uuid4()))

# SIGNIN OPTION
# Login in is an option for already subscribed clients.
@app.route('/signin', strict_slashes=False, methods=['POST'])
def sign_in():
    """ Method that searches login credentials in database """
    try:
        print("enter signin")
        form = request.form.to_dict(flat=False)
        print(form.keys())
        user = form['email'][0]
        passd = form['password'][0]
        print(user, passd)
        users = storage.all(User)
        print(users)
        for us in users.values():
            if us.email == user and us.psswd == passd:
                user = us
        persons = storage.all(Person)
        for per in persons.values():
            if per.user == user.id:
                person = per 
        print(person.id)
        guide = storage.all(Guide)
        for wor in guide.values():
            if wor.guide == person.id:
                return redirect('/profileguide/{}'.format(person.id), code=302)

        tourists = storage.all(Tourist)
        for inv in tourists.values():
            if inv.tourist == person.id:
                return redirect('/profile-tourist/{}'.format(person.id), code=302)
        
            # return redirect('/home')
    except Exception as e:
        print(e)
        return redirect('/home')

# touristS TWO FIRST OPTIONS PAGE
# tourists can choose from two profiles, PERSON or COMPANY
@app.route('/signup/id', strict_slashes=False)
def tourist():
    """ Display tourists html """
    return render_template('s_tourist.html', id=str(uuid.uuid4()))    

# Guide SUBCRIPTION PAGE
# The client (Guide) can create an account from this page
@app.route('/signup/id-Guide', strict_slashes=False, methods=['POST', 'GET'])
def id_Guide():
    """ Guide subscription form """
    if request.method == "POST":
        info = request.form
        obj = User()
        obj.username = info['username']
        obj.email = info['email']
        obj.psswd = info['password']
        obj.status = "active"
        data = Person()
        data.user = obj.id
        data.first_name = info['fname']
        data.last_name = info['lname']
        data.type_id = info['tipo-identificacion']
        data.number_identification = info['numberID']
        data.born_date = info['date']
        wor = Guide()
        wor.Guide = data.id
        mka = storage
        mka.reload()
        mka.new(obj)
        mka.save()
        mka.new(data)
        mka.save()
        mka.new(wor)
        mka.save()
        mka.close()        
        return redirect('/profile-Guide/{}'.format(data.id), code=302)
    return render_template('sign_up_Guide.html', id=str(uuid.uuid4()))

# MAIN Guide PAGE
@app.route('/profile-Guide/<person_id>', strict_slashes=False, methods=['POST', 'GET'])
def profile_Guide(person_id):
    """ Guide profile edit profile form """
    print("profile Guide", request.method)
    if request.method == "POST":
        print("mijo")
        info = request.form
        contacts = storage.all(Contact_info)        
        number = None
        for contact in contacts.values():
            if contact.person == person_id:
                number = contact
        if number is None:
            number = Contact_info()
        number.person = person_id
        number.type_contact = info['type-contact']
        number.data_contact = info['data-contact']
        
        addresses = storage.all(Address)
        add = None
        for adding in addresses.values():
            if adding.person == person_id:
                add = adding
        if add is None:
            add = Address()
        add.address = info['address']
        add.person = person_id

        objects = storage.all(Person)
        obj = None
        for ob in objects.values():
            if ob.id == person_id:
                obj = storage.get(User, ob.user)
        if obj is None:
            obj = User()
        obj.email = info['email']
        obj.psswd = info['password']
        mka = storage
        mka.new(number)
        mka.save()
        mka.new(add)
        mka.save()
        mka.new(obj)
        mka.save()
        mka.close()
        return redirect('/profile-Guide/{}'.format(obj.id), code=302)
    print(person_id)
    return render_template('profile_Guide.html', id=str(uuid.uuid4()), person_id=person_id)

# This code gets the information from the database to display in already
# filled fields from the clients profile. When the edit window popups, fields
# should have the information already added to the system. This feature is not
# active.
@app.route('/profile-Guide/<person_id>/info', strict_slashes=False, methods=['GET'])
def get_person_info(person_id):
    """ Method that gets info to post in edit profile form filled fields """
    print("getting user info")
    contacts = storage.all(Contact_info)
    for contact in contacts.values():
        if contact.person == person_id:
            number = contact
    if number is None:
        number = Contact_info()

    addresses = storage.all(Address)
    for adding in addresses.values():
        if adding.person == person_id:
            add = adding
    if add is None:
        add = Address()

    objects = storage.all(Person)
    for ob in objects.values():
        if ob.id == person_id:
            obj = storage.get(User, ob.user)
    if obj is None:
        obj = User()

    resp = {}
    resp['contact'] = number.type_contact
    resp['address'] = add.address
    resp['user'] = obj.email
    print(resp)
    return jsonify(resp), 200
    
# Apply loan html
# This section is for Guides to request a loan.
@app.route('/apply-loan/<Guide_id>', strict_slashes=False, methods=['POST', 'GET'])
def apply_tourme(Guide_id):
    """
    Display Guides apply-loan html fill out form
    """
    if request.method == "POST":
        info = request.form
        Guides = storage.all(Guide)
        number = None
        for wor in Guides.values():
            if wor.Guide == Guide_id:
                number = wor
        if number is None:
            number = Guide()
        number.Guide = Guide_id
        number.request_date = info['date']
        number.type_toure = info['type-toure']
        number.amount_request = info['amount']

        mka = storage
        mka.new(number)
        mka.save()
        mka.close()

        return redirect('/loan-details/{}'.format(number.id), code=302)
    return render_template('apply_tourme.html', id=str(uuid.uuid4()), person_id=Guide_id)

# Loan details site
# This sections displays loan details requested. This site is not active
@app.route('/loan-details', strict_slashes=False)
def tourme_details():
    """ Display Guides loan-details """
    return render_template('tourme_details.html', id=str(uuid.uuid4()))    

# When a client chooses tourist option, here they will be able to
# create a new user by filling the form.
@app.route('/users/id-person', strict_slashes=False, methods=['POST', 'GET'])
def tourist_person():
    """ Display tourists subscription for a person form """
    if request.method == "POST":
        info = request.form
        obj = User()
        obj.username = info['username']
        obj.email = info['email']
        obj.psswd = info['password']
        obj.status = "active"
        data = Person()
        data.user = obj.id
        data.first_name = info['fname']
        data.last_name = info['lname']
        data.type_id = info['type-identificacion']
        data.number_identification = info['numberID']
        data.born_date = info['date']
        inv = turist()
        inv.turist = data.id
        mka = storage
        mka.reload()
        mka.new(obj)
        mka.save()
        mka.new(data)
        mka.save()
        mka.new(inv)
        mka.save()
        mka.close()
        return redirect('/profile_Tourist.html/{}'.format(obj.id), code=302)
    return render_template('signup_naturalperson.html', id=str(uuid.uuid4()))

# tourists subscription form
# Companies will be able to create their profile as tourists
@app.route('/users/id-company', strict_slashes=False, methods=['POST', 'GET'])
def tourist_company():
    """ Display tourists subscription for a company form """
    if request.method == "POST":
        info = request.form
        print("hola, cómo estás?")
        print(info)
        obj = User()
        obj.username = info['username']
        print(obj.username)
        obj.email = info['email']
        obj.psswd = info['password']
        obj.status = "active"
        data = Person()
        data.user = obj.id
        data.name_company = info['ncompany']
        data.business_name = info['bname']
        data.tradename = info['tname']
        data.legal_status = info['lstatus']
        data.legal_repre_full_name = info['lrepre_name']
        data.legal_repre_type_id = info['tipo-identificacion']
        data.legal_repre_number_id = info['lrepre_id']
        data.born_date = info['date']
        inv = tourist()
        inv.tourist = data.id
        mka = storage
        mka.reload()
        mka.new(obj)
        mka.save()
        mka.new(data)
        mka.save()
        mka.new(inv)
        mka.save()
        mka.close()
        return redirect('/profile-tourist/{}'.format(obj.id), code=302)
    return render_template('signup_company.html', id=str(uuid.uuid4()))

# Main tourists profile page
@app.route('/profile-tourist/<tourist_id>', strict_slashes=False)
def profile_tourist(tourist_id):
    """ Display tourists profile, status, investment, edit profile, add bank details """
    return render_template('profile_tourist.html', id=str(uuid.uuid4()))


# tourists edit profile form
@app.route('/edit-profile', strict_slashes=False)
def edit_profile():
    """ Display tourists edit profile form """
    return render_template('edit_profile.html', id=str(uuid.uuid4()))

# tourists investment form
@app.route('/investment', strict_slashes=False)
def investment():
    """ Display tourists investment form """
    return render_template('investment.html', id=str(uuid.uuid4()))

# tourists add bank details form when adding new bank accounts
@app.route('/bank-details', strict_slashes=False)
def bank_details():
    """ Display bank details form """
    return render_template('bank_details.html', id=str(uuid.uuid4()))

# Test Deployment Strategy for adding new features or trying out new ones.
@app.route('/tests', strict_slashes=False)
def tests():
    """ Display tests
    Tests was made to make tests before adding any new features to the code
    as Deployment Strategy
    """
    return render_template('tests.html', id=str(uuid.uuid4()))
  
if __name__ == "__main__":
    """ Main Function redirecting to host 0.0.0.0 and port 5000 """
    app.run(host='0.0.0.0', port=5000)
