from flask import Blueprint, render_template

# about blueprint definition
payment = Blueprint('payment', __name__, static_folder='static', static_url_path='/payment', template_folder='templates')


# Routes
@payment.route('/payment', methods=['GET', 'POST'])
def index():
    return render_template('payment.html')
