from flask import request, redirect, session, flash
from interact_with_DB import interact_db
from datetime import datetime

class DBcarts:


    def get_current_cart(self, CustomerEmail):
        query = "select CartID from web_project_g6.carts where CreationTime = (select max(CreationTime) from web_project_g6.carts where CustomerEmail='%s');" % CustomerEmail
        ans = interact_db(query=query, query_type='fetch')
        return ans

    def add_cart(self, CustomerEmail):
        current_dt = datetime.now()
        query = "insert into web_project_g6.carts (CustomerEmail, CreationTime, Price, ShippingCost, TotalPrice)\
                                    values ('%s', '%s', '%s', '%s','%s');" % (CustomerEmail, current_dt, 0, 0, 0)
        interact_db(query=query, query_type='commit')
        return True





# Creates an instance for the DBcarts class for export.
DBcarts = DBcarts()