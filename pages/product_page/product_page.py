from flask import Blueprint, render_template, session

# about blueprint definition
product_page = Blueprint('product_page', __name__, static_folder='static', static_url_path='/product_page', template_folder='templates')


# Routes
@product_page.route('/product_page', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        return render_template('product_page.html',
                               full_name=session.get('full_name'))
    return render_template('product_page.html')
