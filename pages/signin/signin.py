from flask import Blueprint, render_template

# about blueprint definition
signin = Blueprint('signin', __name__, static_folder='static', static_url_path='/signin', template_folder='templates')


# Routes
@signin.route('/signin', methods=['GET', 'POST'])
def index():
    return render_template('signin.html')
