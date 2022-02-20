from flask import Blueprint, render_template, session

# about blueprint definition
payment = Blueprint('payment', __name__, static_folder='static', static_url_path='/payment', template_folder='templates')


# Routes
@payment.route('/payment', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        return render_template('payment.html',
                               full_name=session.get('full_name'))
    return render_template('payment.html')
