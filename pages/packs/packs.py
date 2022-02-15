from flask import Blueprint, render_template

# about blueprint definition
packs = Blueprint('packs', __name__, static_folder='static', static_url_path='/packs', template_folder='templates')


# Routes
@packs.route('/packs', methods=['GET', 'POST'])
def index():
    return render_template('packs.html')
