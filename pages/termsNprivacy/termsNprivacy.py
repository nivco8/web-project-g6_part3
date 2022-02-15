from flask import Blueprint, render_template

# about blueprint definition
termsNprivacy = Blueprint('termsNprivacy', __name__, static_folder='static', static_url_path='/termsNprivacy', template_folder='templates')


# Routes
@termsNprivacy.route('/termsNprivacy', methods=['GET', 'POST'])
def index():
    return render_template('termsNprivacy.html')
