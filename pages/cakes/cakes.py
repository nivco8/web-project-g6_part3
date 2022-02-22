from flask import Blueprint, render_template, session, request, flash
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


def add_cake_to_cart():
    if session.get('login'):
        quantity = request.form['birthday']
        country = request.form['country']
        session['full_name'] = full_name
        email = session['email']
        product_to_review = request.form['product_selection']
        rank = request.form['rank_selection']
        content = request.form['contentMessage']
        if DBProduct_in_cart.add_product_to_cart(email, cartID, product, quantity):
            return render_template('home.html', message='תודה! הביקורת נשלח בהצלחה.')
    else:
        flash('flashh')
        return render_template('/review.html', message='FAILED ATTEMPT')
