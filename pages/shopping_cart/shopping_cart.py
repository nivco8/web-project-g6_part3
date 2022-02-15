from flask import Blueprint, render_template

# about blueprint definition
shopping_cart = Blueprint('shopping_cart', __name__, static_folder='static', static_url_path='/shopping_cart', template_folder='templates')


# Routes
@shopping_cart.route('/shopping_cart', methods=['GET', 'POST'])
def index():
    return render_template('shopping_cart.html')
