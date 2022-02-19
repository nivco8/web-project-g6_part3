from flask import Blueprint, render_template

# about blueprint definition
review = Blueprint('review', __name__, static_folder='static', static_url_path='/review', template_folder='templates')


# Routes
@review.route('/review', methods=['GET', 'POST'])
def index():
    return render_template('review.html')
