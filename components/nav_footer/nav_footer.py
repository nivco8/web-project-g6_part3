from flask import Blueprint, render_template

# main_menu blueprint definition
nav_footer = Blueprint('nav_footer', __name__, static_folder='static', static_url_path='/nav_footer', template_folder='templates')
