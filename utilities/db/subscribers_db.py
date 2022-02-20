from flask import request, redirect, session, flash
from interact_with_DB import interact_db

class DBsubscribers:

    def insert_subscriber_DB(self, email, full_name, phone):
        check_input = "SELECT email FROM web_project_g6.users WHERE email='%s';" % email
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into web_project_g6.users ( email, full_name, phone)\
                            value ('%s', '%s', '%s');" % ( email, full_name, phone)
            interact_db(query=query, query_type='commit')
            flash('טופס נשלח')
            return True
        else:
            flash('user already exists!')
            return False

DBsubscribers = DBsubscribers()

