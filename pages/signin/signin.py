from flask import Blueprint, render_template, session, request, url_for, redirect
from utilities.db.users_db import DBusers
# about blueprint definition
signin = Blueprint('signin', __name__, static_folder='static', static_url_path='/signin', template_folder='templates')


# Routes
@signin.route('/signin', methods=['GET', 'POST'])
def index():
    if 'logged_in' not in session:
        session['logged_in'] = False
    if request.method == 'POST':
        email = request.form['Email']
        password = request.form['Password']

        if DBusers.find_user_in_db(email, password):
            session['logged_in'] = True
            user_details = DBusers.get_user_details(email)
            # dbcart.insert(username)
            # cartid = dbcart.get_last_cart_id(username)
            session['user_data'] = {
                'username': email,
                'password': password,
                'full_name': user_details[0].FullName,
                'address': user_details[0].address,
                'birthdate': user_details[0].birthday,
                'country': user_details[0].country
                # 'cart_id': cartid
            }
            session['user_not_match'] = False
            session.pop('user_not_match')
            return redirect(url_for('home.index'))

        else:
            session['user_not_match'] = True
            return render_template('SignIn.html')

    if 'user_not_match' in session:
        session.pop('user_not_match')
    session['logged_in'] = False
    return render_template('signin.html')






    # return render_template('signin.html')
