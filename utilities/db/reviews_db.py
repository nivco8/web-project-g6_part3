from flask import request, redirect, session, flash
from interact_with_DB import interact_db
from datetime import datetime, date


class DBreviews:

    def insert_review(self, email, product, rank, content):

        check_input = "SELECT email FROM web_project_g6.users WHERE email='%s';" % email
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            flash('Please sign in/up to write a review!')
            return False
        else:
            current_time = datetime.now()
            query = "insert into web_project_g6.reviews (ProductID, CustomerEmail, ReviewDateTime, Stars, Content)\
                                        values ('%s', '%s', '%s', '%s', '%s');" % (product, email, current_time, rank, content)
            interact_db(query=query, query_type='commit')
            flash('תודה נשמה')
            return True


# Creates an instance for the DBreviews class for export.
DBreviews = DBreviews()