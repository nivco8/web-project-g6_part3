from flask import Blueprint, render_template, session, request, url_for, redirect
from utilities.db.users_db import DBusers
# about blueprint definition
signin = Blueprint('signin', __name__, static_folder='static', static_url_path='/signin', template_folder='templates')


# Routes
@signin.route('/signin')
def index():
    if session.get('login'):
        return render_template('termsNprivacy.html',
                               full_name=session.get('full_name'))
    return render_template('signin.html')


@signin.route('/check_user', methods=['POST'])
def insert_user():
    email = request.form['email']
    password = request.form['password']
    if DBusers.find_user_in_db(email, password):
        session['login'] = True
        user_details = DBusers.get_user_details(email)
        session['full_name'] = user_details[0].full_name
        session['email'] = user_details[0].email
        return redirect(url_for('Home.html'))
    else:
        return render_template('SignIn.html', message='משתמש לא קיים! נא להזין אימייל אחר או להירשם')
