from flask import Blueprint, render_template, session, request
from utilities.db.subscribers_db import DBsubscribers


# about blueprint definition
newsletter = Blueprint('newsletter', __name__, static_folder='static', static_url_path='/newsletter', template_folder='templates')


# Routes
@newsletter.route('/newsletter', methods=['GET', 'POST'])
def index():
    if session.get('login'):
        return render_template('newsletter.html',
                               full_name=session.get('full_name'))
    return render_template('newsletter.html')


@newsletter.route('/submit_newsletter', methods=['POST'])
def submit_newsletter():
    email = request.form['email']
    phone = request.form['phone']
    full_name = request.form['full_name']
    DBsubscribers.insert_subscriber_DB(email, full_name, phone)
    if session.get('login'):
        return render_template('Home.html',
                               full_name=session.get('full_name'),
                               message='תודה! נרשמת כמנוי.')
    return render_template('home.html', message='תודה! נרשמת כמנוי.')
