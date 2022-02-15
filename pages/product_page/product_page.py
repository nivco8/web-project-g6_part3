from flask import Blueprint, render_template

# about blueprint definition
product_page = Blueprint('product_page', __name__, static_folder='static', static_url_path='/product_page', template_folder='templates')


# Routes
@product_page.route('/product_page', methods=['GET', 'POST'])
def index():
    return render_template('product_page.html')
