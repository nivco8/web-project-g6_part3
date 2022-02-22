from flask import request, redirect, session, flash
from interact_with_DB import interact_db
from datetime import date


class DBProduct_in_cart:

    def add_product_to_cart(self, email, cartID, product, quantity):
        check_input = "SELECT quantity FROM web_project_g6.productsincart WHERE CustomerEmail='%s' and CartID='%s' and ProductID='%s';" % (email, cartID, product)
        answer = interact_db(query=check_input, query_type='fetch')
        count = 0
        for prod in answer:
            if prod.quantity:
                count = prod.quantity
        if count == 0:
            query = "insert into web_project_g6.productsincart (CustomerEmail, CartID, ProductID, Quantity)\
                                                    value ('%s', '%s', '%s', '%s');" % (email, cartID, product, quantity)
            interact_db(query=query, query_type='commit')
            flash('added successfully!')
            return True
        else:
            new_quantity = count + quantity
            query = "UPDATE web_project_g6.productsincart set Quantity='%s' WHERE CartID='%s' and ProductID='%s';" % (new_quantity, cartID, product)
            interact_db(query=query, query_type='commit')
            flash('updated successfully!')
            return False


    def clear_cart(self, cartID):
        query = "delete from web_project_g6.productsincart where CartID='%s';" % (cartID)
        interact_db(query=query, query_type='commit')
        return True

    def get_product_in_cart(self, cartID):
        query = "SELECT * FROM web_project_g6.productsincart as PIC join web_project_g6.products as P using (ProductID)  WHERE PIC.CartID='%s';" % (cartID)
        ans = interact_db(query=query, query_type='fetch')
        return ans


    def delete_product_from_cart(self, cartID, product):
        query = "delete from web_project_g6.productsincart where CartID = '%s' and ProductID='%s';" % (cartID, product)
        interact_db(query=query, query_type='commit')
        return True


    def update_product_quantity(self, cartID, product, quantity, type_of_update):
        if type_of_update == "plus":
            query = "UPDATE web_project_g6.productsincart set Quantity='%s'+1 WHERE CartID='%s' and productID='%s';" % (quantity, cartID, product)
        if type_of_update == "minus":
            query = "UPDATE web_project_g6.productsincart set Quantity='%s'-1 WHERE CartID='%s' and productID='%s';" % (quantity, cartID, product)
        interact_db(query=query, query_type='commit')
        return True




# # Creates an instance for the DBProduct_in_cart class for export.
DBProduct_in_cart = DBProduct_in_cart()
