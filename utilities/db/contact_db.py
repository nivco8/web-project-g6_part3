from flask import request, redirect, session, flash
from interact_with_DB import interact_db
from datetime import date


class DBcontacts:

    def add_inquiry(self, email, name, content):

        current_date = date.today()
        query = "insert into web_project_g6.inquiries (CustomerEmail, FullName, InquiryDate, Content)\
                                    values ('%s', '%s', '%s', '%s');" % (email, name, current_date, content)
        interact_db(query=query, query_type='commit')




# Creates an instance for the DBcontacts class for export.
DBcontacts = DBcontacts()