from flask import Blueprint, render_template, session, flash
from utilities.db.cart_db import DBcarts
from utilities.db.product_in_cart_db import DBProduct_in_cart

# about blueprint definition
shopping_cart = Blueprint('shopping_cart', __name__, static_folder='static', static_url_path='/shopping_cart', template_folder='templates')


# Routes
@shopping_cart.route('/shopping_cart', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        email = session['email']
        carts = DBcarts.get_current_cart(email)
        products = DBProduct_in_cart.get_product_in_cart(carts)
        return render_template('shopping_cart.html', products = products,  full_name=session.get('full_name'))
    return render_template('home.html')

@shopping_cart.route('/clear_cart', methods=['GET', 'POST'])
def clear_cart():
    if session.get('login'):
        email = session['email']
        cartID = DBcarts.get_current_cart(email)
        DBProduct_in_cart.clear_cart(cartID)
        flash('succeeded')
        return render_template('shopping_cart.html', message='העגלה רוקנה ומרוקנת!', full_name=session.get('full_name'))
    else:
        flash('Failed')
        return render_template('shopping_cart.html', message='לא ניתן לרוקן לעגלה, נא להתחבר למערכת בבקשה תודה')