from flask import Blueprint, render_template, session

# about blueprint definition
home = Blueprint('home', __name__, static_folder='static', static_url_path='/home', template_folder='templates')


# Routes
@home.route('/home')
@home.route('/')
def index():
    if session.get('login'):
        return render_template('Home.html',
                               full_name=session.get('full_name'))
    return render_template('Home.html')


@home.route('/logout', methods=['GET', 'POST'])
def logout_func():
    session.clear()
    return render_template('Home.html')

