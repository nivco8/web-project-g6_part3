from flask import Blueprint, render_template, session
from utilities.db.cart_db import DBcarts


# about blueprint definition
shopping_cart = Blueprint('shopping_cart', __name__, static_folder='static', static_url_path='/shopping_cart', template_folder='templates')


# Routes
@shopping_cart.route('/shopping_cart', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        email = session['email']
        carts = DBcarts.get_current_cart(email)
        return render_template('shopping_cart.html', carts)
    return render_template('home.html')



