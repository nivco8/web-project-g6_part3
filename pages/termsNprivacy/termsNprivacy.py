from flask import Blueprint, render_template, session

# about blueprint definition
termsNprivacy = Blueprint('termsNprivacy', __name__, static_folder='static', static_url_path='/termsNprivacy', template_folder='templates')


# Routes
@termsNprivacy.route('/termsNprivacy', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        return render_template('termsNprivacy.html',
                               full_name=session.get('full_name'))
    return render_template('termsNprivacy.html')
