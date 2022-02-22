from flask import Blueprint, render_template, session, flash
from utilities.db.cart_db import DBcarts
from utilities.db.product_in_cart_db import DBProduct_in_cart

# about blueprint definition

delivery = Blueprint('delivery', __name__, static_folder='static', static_url_path='/delivery', template_folder='templates')


# Routes
@delivery.route('/delivery', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        email = session['email']
        flash('succeeded')
        cartID = DBcarts.get_current_cart(email)
        products = DBProduct_in_cart.get_product_in_cart(cartID)
        price_sum = 0
        for product in products:
            price_sum += product.Quantity * product.Price
        return render_template('delivery.html', price_sum=price_sum)
    else:
        flash('Failed')
        return render_template('home.html')