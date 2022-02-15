from flask import Blueprint, render_template, request, session
from utilities.db.users_db import DBusers

# about blueprint definition
signup = Blueprint('signup', __name__, static_folder='static', static_url_path='/signup', template_folder='templates')


# Routes
@signup.route('/signup', methods=['GET', 'POST'])
def index():
    return render_template('signup.html')


@signup.route('/insert_user', methods=['POST'])
def insert_user():
    email = request.form['email']
    password = request.form['password']
    full_name = request.form['full_name']
    address = request.form['address']
    phone = request.form['phone']
    birthday = request.form['birthday']
    country = request.form['country']

    if DBusers.insert_User_DB(email, password, full_name, phone, address, birthday, country):
        return render_template('/home.html')
    else:
        return render_template('/SignUp.html', message='משתמש קיים! נא להזין אימייל אחר או להתחבר')
