from flask import Flask


###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## Cakes
from pages.cakes.cakes import cakes
app.register_blueprint(cakes)

## Catalog
from pages.catalog.catalog import catalog
app.register_blueprint(catalog)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


if __name__ == '__main__':
    app.run(debug=True)

###### Components
## Main menu
from components.nav_footer.nav_footer import nav_footer
app.register_blueprint(nav_footer)
