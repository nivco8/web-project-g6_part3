from flask import Blueprint, render_template

# about blueprint definition
pickup = Blueprint('pickup', __name__, static_folder='static', static_url_path='/pickup', template_folder='templates')


# Routes
@pickup.route('/pickup', methods=['GET', 'POST'])
def index():
    return render_template('pickup.html')
