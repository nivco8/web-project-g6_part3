from flask import Flask

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')

###### Pages
## Cakes
from pages.cakes.cakes import cakes
app.register_blueprint(cakes)

## packs
from pages.packs.packs import packs
app.register_blueprint(packs)

## contact_us
from pages.contact_us.contact_us import contact_us
app.register_blueprint(contact_us)

## home
from pages.home.home import home
app.register_blueprint(home)

## signin
from pages.signin.signin import signin
app.register_blueprint(signin)

## signup
from pages.signup.signup import signup
app.register_blueprint(signup)

## delivery
from pages.delivery.delivery import delivery
app.register_blueprint(delivery)

## pickup
from pages.pickup.pickup import pickup
app.register_blueprint(pickup)

## product_page
from pages.product_page.product_page import product_page
app.register_blueprint(product_page)

## payment
from pages.payment.payment import payment
app.register_blueprint(payment)

## shopping_cart
from pages.shopping_cart.shopping_cart import shopping_cart
app.register_blueprint(shopping_cart)

## newsletter
from pages.newsletter.newsletter import newsletter
app.register_blueprint(newsletter)

## home
from pages.termsNprivacy.termsNprivacy import termsNprivacy
app.register_blueprint(termsNprivacy)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)


if __name__ == '__main__':
    app.run(debug=True)

###### Components
## Main menu
from components.nav_footer.nav_footer import nav_footer
app.register_blueprint(nav_footer)
