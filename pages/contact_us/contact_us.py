from flask import Blueprint, render_template, request, redirect, url_for
from utilities.db.contact_db import DBcontacts


# about blueprint definition
contact_us = Blueprint('contact_us', __name__, static_folder='static', static_url_path='/contact_us', template_folder='templates')


# Routes
@contact_us.route('/contact_us', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        email = request.form['ContactEmail']
        name = request.form['Name']
        content = request.form['contentMessage']
        DBcontacts.add_inquiry(email, name, content)
        return render_template('/contact_us.html', message='תודה! הטופס נשלח בהצלחה.')
    else:
        return render_template('/contact_us.html')


# @contact_us.route('/contact_us_submitted', methods=['GET', 'POST'])
# def contact_us_submitted():
#     return render_template('/contact_us.html', message='תודה! הטופס נשלח בהצלחה.')