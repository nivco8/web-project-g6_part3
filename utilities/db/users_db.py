from flask import request, redirect, session, flash
from interact_with_DB import interact_db


class DBusers:

    def insert_User_DB(self, email, password, full_name, phone, address, birthday, country):
        check_input = "SELECT email FROM web_project_g6.users WHERE email='%s';" % email
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into web_project_g6.users (Password, Email, full_name, Phone, Address, Country, Birthday)\
                            value ('%s', '%s', '%s', '%s', '%s', '%s', '%s');" % (password, email, full_name, phone, address, country, birthday)
            interact_db(query=query, query_type='commit')
            # message
            return True
        else:
            flash('user already exists!')
            return False

    def find_user_in_db(self, email, password):
        get_user_name = "select email from web_project_g6.users where email='%s';" % email
        answer = interact_db(query=get_user_name, query_type='fetch')
        if len(answer) == 0:
            flash('No such user!')
            return False
        else:
            get_password = "SELECT Password FROM web_project_g6.users WHERE email='%s';" % email
            answer = interact_db(query=get_password, query_type='fetchone')
            if answer[0] == password:
                return True
            else:
                flash('Wrong password!')
                return False

    def get_user_details(self, email):
        get_details = "select * from web_project_g6.users where email='%s';" % email
        ans = interact_db(query=get_details, query_type='fetch')
        return ans


# Creates an instance for the DBusers class for export.
DBusers = DBusers()
