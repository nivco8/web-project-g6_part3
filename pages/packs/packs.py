from flask import Blueprint, render_template, session, request
from utilities.db.product_in_cart_db import DBProduct_in_cart
from utilities.db.cart_db import DBcarts

# about blueprint definition
packs = Blueprint('packs', __name__, static_folder='static', static_url_path='/packs', template_folder='templates')


# Routes
@packs.route('/packs')
def index():
    if session.get('login'):
        return render_template('packs.html',
                               full_name=session.get('full_name'))
    return render_template('packs.html')



@packs.route('/add_mini_crack', methods=['GET', 'POST'])
def add_mini_crack():
    if session.get('login'):
        email = session['email']
        quantity = 16

        product = 6
        DBProduct_in_cart.add_product_to_cart(email, 2, product, quantity)
        return render_template('packs.html', message='פריט נוסף לעגלה!')
    else:
        return render_template('packs.html', message='לא ניתן להוסיף לעגלה, נא להתחבר למערכת בבקשה תודה')


@packs.route('/add_mini_petel', methods=['GET', 'POST'])
def add_mini_petel():
    if session.get('login'):
        email = session['email']
        quantity = request.form['quantity2']
        cartID = DBcarts.get_current_cart(email)
        product = 5
        DBProduct_in_cart.add_product_to_cart(email, cartID, product, quantity)
        return render_template('packs.html', message='פריט נוסף לעגלה!')
    else:
        return render_template('packs.html', message='לא ניתן להוסיף לעגלה, נא להתחבר למערכת בבקשה תודה')


@packs.route('/add_mini_saint', methods=['GET', 'POST'])
def add_mini_saint():
    if session.get('login'):
        email = session['email']
        quantity = request.form['quantity3']
        cartID = DBcarts.get_current_cart(email)
        product = 8
        DBProduct_in_cart.add_product_to_cart(email, cartID, product, quantity)
        return render_template('packs.html', message='פריט נוסף לעגלה!')
    else:
        return render_template('packs.html', message='לא ניתן להוסיף לעגלה, נא להתחבר למערכת בבקשה תודה')


@packs.route('/add_mini_blueberries', methods=['GET', 'POST'])
def add_mini_blueberries():
    if session.get('login'):
        email = session['email']
        quantity = request.form['quantity1']
        cartID = DBcarts.get_current_cart(email)
        product = 7
        DBProduct_in_cart.add_product_to_cart(email, cartID, product, quantity)
        return render_template('packs.html', message='פריט נוסף לעגלה!')
    else:
        return render_template('packs.html', message='לא ניתן להוסיף לעגלה, נא להתחבר למערכת בבקשה תודה')


