from flask import Blueprint, render_template

# about blueprint definition
signup = Blueprint('signup', __name__, static_folder='static', static_url_path='/signup', template_folder='templates')


# Routes
@signup.route('/signup', methods=['GET', 'POST'])
def index():
    return render_template('signup.html')
