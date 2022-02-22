from flask import Blueprint, render_template, session

# about blueprint definition
delivery = Blueprint('delivery', __name__, static_folder='static', static_url_path='/delivery', template_folder='templates')


# Routes
@delivery.route('/delivery', methods=['GET', 'POST'])
def index():

    if session.get('login'):
        return render_template('delivery.html',
                               price = session.get('price'),
                               full_name=session.get('full_name'))
    return render_template('delivery.html')
