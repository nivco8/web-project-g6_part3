from flask import Blueprint, render_template, session

# about blueprint definition
packs = Blueprint('packs', __name__, static_folder='static', static_url_path='/packs', template_folder='templates')


# Routes
@packs.route('/packs', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        return render_template('packs.html',
                               full_name=session.get('full_name'))
    return render_template('packs.html')
