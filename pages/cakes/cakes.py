from flask import Blueprint, render_template

# about blueprint definition
cakes = Blueprint('cakes', __name__, static_folder='static', static_url_path='/cakes', template_folder='templates')


# Routes
@cakes.route('/cakes')
def index():
    return render_template('cakes.html')
