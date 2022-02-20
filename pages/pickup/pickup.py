from flask import Blueprint, render_template, session

# about blueprint definition
pickup = Blueprint('pickup', __name__, static_folder='static', static_url_path='/pickup', template_folder='templates')


# Routes
@pickup.route('/pickup', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        return render_template('pickup.html',
                               full_name=session.get('full_name'))
    return render_template('pickup.html')
