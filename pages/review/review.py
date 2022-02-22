from flask import Blueprint, render_template, request, session
from utilities.db.reviews_db import DBreviews


# about blueprint definition
review = Blueprint('review', __name__, static_folder='static', static_url_path='/review', template_folder='templates')


@review.route('/review')
def index():
    if session.get('login'):
        return render_template('review.html',
                               full_name=session.get('full_name'))
    return render_template('/review.html')

@review.route('/add_review', methods=['POST'])
def add_review():
    email = session['email']
    product_to_review = request.form['product_selection']
    rank = request.form['rank_selection']
    content = request.form['contentMessage']
    if DBreviews.insert_review(email, product_to_review, rank, content):
        return render_template('home.html', message='תודה! הביקורת נשלחה בהצלחה.')
    else:
        return render_template('/review.html', message='FAILED ATTEMPT')