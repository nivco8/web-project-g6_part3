from flask import Blueprint, render_template

# about blueprint definition
newsletter = Blueprint('newsletter', __name__, static_folder='static', static_url_path='/newsletter', template_folder='templates')


# Routes
@newsletter.route('/newsletter', methods=['GET', 'POST'])
def index():
    return render_template('newsletter.html')


@newsletter.route('/submit_newsletter', methods=['GET', 'POST'])
def submit_newsletter():
    return render_template('newsletter.html', message = 'תודה! הטופס נשלח בהצלחה')