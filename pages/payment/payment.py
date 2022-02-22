from flask import Blueprint, render_template, session, flash
from utilities.db.cart_db import DBcarts

# about blueprint definition
payment = Blueprint('payment', __name__, static_folder='static', static_url_path='/payment', template_folder='templates')


# Routes
@payment.route('/payment', methods=['GET', 'POST'])
def index():
    if session.get('login'):

        return render_template('payment.html',
                               full_name=session.get('full_name'))
    return render_template('payment.html')


@payment.route('/after_payment', methods=['GET', 'POST'])
def after_payment():
    if session.get('login'):
        email = session['email']
        DBcarts.add_cart(email)
        flash('yuhooo')
        return render_template('home.html', message="התשלום בוצע בהצלחה! תודה.", full_name=session.get('full_name'))
    return render_template('home.html')

