from flask import Blueprint, render_template, session, request, url_for, redirect
from utilities.db.users_db import DBusers
from utilities.db.cart_db import DBcarts

# about blueprint definition
signin = Blueprint('signin', __name__, static_folder='static', static_url_path='/signin', template_folder='templates')


# Routes
@signin.route('/signin')
def index():
    if session.get('login'):
        return render_template('home.html',
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
        session['cartID'] = DBcarts.get_current_cart(email)
        return redirect(url_for('home.index'))
    else:
        session.clear()
        return render_template('SignIn.html', message='משתמש לא קיים! נא להזין אימייל אחר או להירשם')
