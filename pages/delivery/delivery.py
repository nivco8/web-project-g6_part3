from flask import Blueprint, render_template

# about blueprint definition
delivery = Blueprint('delivery', __name__, static_folder='static', static_url_path='/delivery', template_folder='templates')


# Routes
@delivery.route('/delivery', methods=['GET', 'POST'])
def index():
    return render_template('delivery.html')
