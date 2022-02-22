from flask import Blueprint, render_template, session, flash, request, redirect, url_for
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
        price_sum = 0
        for product in products:
            price_sum += product.Quantity * product.Price
        return render_template('shopping_cart.html', products = products, price_sum = price_sum,  full_name=session.get('full_name'))
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

@shopping_cart.route('/delete_product', methods=['GET', 'POST'])
def delete_product():
    if session.get('login'):
        email = session['email']
        cartID = DBcarts.get_current_cart(email)
        productID = int(request.form['productID'])
        DBProduct_in_cart.delete_product_from_cart(cartID, productID)
        flash('succeeded')
        return redirect(url_for('shopping_cart.index', message='מוצר נמחק!', full_name=session.get('full_name')))
    else:
        flash('Failed')
        return render_template('shopping_cart.html', message='לא ניתן למחוק מהעגלה, נא להתחבר למערכת בבקשה תודה')


@shopping_cart.route('/delivery', methods=['GET', 'POST'])
def delivery():
    if session.get('login'):
        email = session['email']
        cartID = DBcarts.get_current_cart(email)
        price = int(request.form['price'])
        flash('succeeded')
        session['price'] = price
        return redirect(url_for('delivery.index'))
    else:
        flash('Failed')
        return render_template('home.html')




