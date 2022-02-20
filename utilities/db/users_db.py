from flask import request, redirect, session, flash
from interact_with_DB import interact_db


class DBusers:

    def insert_User_DB(self, email, password, full_name, phone, address, birthday, country):
        check_input = "SELECT email FROM web_project_g6.users WHERE email='%s';" % email
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into web_project_g6.users (Password, Email, FullName, Phone, Address, Country, Birthday)\
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
            return False
        else:
            get_password = "SELECT Password FROM web_project_g6.users WHERE email='%s';" % email
            answer = interact_db(query=get_password, query_type='fetchone')
            if answer[0] == password:
                return True
            else:
                return False

    def get_user_details(self, email):
        get_details = "select * from web_project_g6.users where email='%s';" % email
        ans = interact_db(query=get_details, query_type='fetch')
        return ans



    # def update_user_email(self, username, detail):
    #     query = "UPDATE web_project_g16.users SET email='%s' WHERE username='%s';" % (detail, username)
    #     answer = interact_db(query=query, query_type='commit')
    #
    # def update_user_password(self, username, detail):
    #     query = "UPDATE web_project_g16.users SET password='%s' WHERE username='%s';" % (detail, username)
    #     answer = interact_db(query=query, query_type='commit')
    #
    # def update_user_phone(self, username, detail):
    #     query = "UPDATE web_project_g16.users SET phone='%s' WHERE username='%s';" % (detail, username)
    #     answer = interact_db(query=query, query_type='commit')
    #
    # def update_user_address(self, username, detail):
    #     print(detail)
    #     query = "UPDATE web_project_g16.users SET address='%s' WHERE username='%s';" % (detail, username)
    #     answer = interact_db(query=query, query_type='commit')
    #
    #
    # def get_detail_by_username(self, username, detail):
    #     if detail == 'phone':
    #         get_address = "SELECT phone FROM web_project_g16.users WHERE username='%s';" % username
    #         answer = interact_db(query=get_address, query_type='fetchone')
    #
    #     elif detail == 'address':
    #         get_address = "SELECT address FROM web_project_g16.users WHERE username='%s';" % username
    #         answer = interact_db(query=get_address, query_type='fetchone')
    #
    #     elif detail == 'email':
    #         get_address = "SELECT email FROM web_project_g16.users WHERE username='%s';" % username
    #         answer = interact_db(query=get_address, query_type='fetchone')
    #
    #     elif detail == 'password':
    #         get_address = "SELECT password FROM web_project_g16.users WHERE username='%s';" % username
    #         answer = interact_db(query=get_address, query_type='fetchone')
    #
    #     elif detail == 'birthdate':
    #         get_address = "SELECT birthdate FROM web_project_g16.users WHERE username='%s';" % username
    #         answer = interact_db(query=get_address, query_type='fetchone')
    #
    #     return answer[0]
    #
    # def get_all_details(self, username):
    #     get_details = "SELECT * FROM web_project_g16.users WHERE username='%s';" % username
    #     answer = interact_db(query=get_details, query_type='fetch')
    #     return answer
    #
    # def delete_user_profile(self,username):
    #     query = "delete from web_project_g16.users WHERE username='%s';" % username
    #     interact_db(query=query, query_type='commit')
    #     return True


# Creates an instance for the DBusers class for export.
DBusers = DBusers()
