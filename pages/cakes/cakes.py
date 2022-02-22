from flask import Blueprint, render_template, session, request, flash
from utilities.db.cart_db import DBcarts
from utilities.db.product_in_cart_db import DBProduct_in_cart

# about blueprint definition
cakes = Blueprint('cakes', __name__, static_folder='static', static_url_path='/cakes', template_folder='templates')


# Routes
@cakes.route('/cakes', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        return render_template('cakes.html',
                               full_name=session.get('full_name'))
    return render_template('cakes.html')

@cakes.route('/add_strawberry', methods=['GET', 'POST'])
def add_strawberry():
    if session.get('login'):
        email = session['email']
        quantity = int(request.form['quantity1'])
        cartID = DBcarts.get_current_cart(email)
        product = 2
        DBProduct_in_cart.add_product_to_cart(email, cartID, product, quantity)
        return render_template('cakes.html', message='פריט נוסף לעגלה!')
    else:
        return render_template('cakes.html', message='לא ניתן להוסיף לעגלה, נא להתחבר למערכת בבקשה תודה')


@cakes.route('/add_saint', methods=['GET', 'POST'])
def add_saint():
    if session.get('login'):
        email = session['email']
        quantity = int(request.form['quantity2'])
        cartID = DBcarts.get_current_cart(email)
        product = 1
        DBProduct_in_cart.add_product_to_cart(email, cartID, product, quantity)
        return render_template('cakes.html', message='פריט נוסף לעגלה!')
    else:
        return render_template('cakes.html', message='לא ניתן להוסיף לעגלה, נא להתחבר למערכת בבקשה תודה')


@cakes.route('/add_crack_pie', methods=['GET', 'POST'])
def add_crack_pie():
    if session.get('login'):
        email = session['email']
        quantity = int(request.form['quantity3'])
        cartID = DBcarts.get_current_cart(email)
        product = 4
        DBProduct_in_cart.add_product_to_cart(email, cartID, product, quantity)
        return render_template('cakes.html', message='פריט נוסף לעגלה!')
    else:
        return render_template('cakes.html', message='לא ניתן להוסיף לעגלה, נא להתחבר למערכת בבקשה תודה')


@cakes.route('/add_pie_chocolate', methods=['GET', 'POST'])
def add_pie_chocolate():
    if session.get('login'):
        email = session['email']
        quantity = int(request.form['quantity4'])
        cartID = DBcarts.get_current_cart(email)
        product = 3
        DBProduct_in_cart.add_product_to_cart(email, cartID, product, quantity)
        return render_template('cakes.html', message='פריט נוסף לעגלה!')
    else:
        return render_template('cakes.html', message='לא ניתן להוסיף לעגלה, נא להתחבר למערכת בבקשה תודה')

