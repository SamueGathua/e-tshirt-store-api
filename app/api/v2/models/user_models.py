import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from .base_models import BaseModels


class UserRecord():
    """ Views for user records """
    def __init__(self):
        self.models = BaseModels('users')

    def register_user(self, user_data, role):
        """ Creates a new user record"""
        if user_data['password'] != user_data['repeat_password']:
            return "No match"
        if self.models.get_data("email",user_data['email']):
            return False
        data = {
            "isadmin" : False,
            "firstname" : user_data['firstname'],
            "lastname" : user_data['lastname'],
            "othername" : user_data['othername'],
            "phonenumber" : user_data['phonenumber'],
            "email" : user_data['email'],
            "registered_on":datetime.datetime.now(),
            "password" : generate_password_hash( user_data['password'],method='pbkdf2:sha256', salt_length=8)
        }
        if role: # if admin
            data['isadmin'] = True
        query = """INSERT INTO users(isadmin,firstname,lastname,phonenumber,\
                                          othername,email,registered_on,password)
        VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s');""" % \
        (data['isadmin'], data['firstname'], data['lastname'],\
          data['othername'],\
         data['phonenumber'], data['email'], data['registered_on'],data['password'])
        return self.models.save(query, data)

    def get_all_users(self):
        """Get the records for all the registered users"""
        return self.models.get_all_records()

    def login_user(self, data):
        user_data = None,
        user_data = self.models.get_data("email",data['email'])
        print(user_data)
        if user_data == None:
            return False

        return user_data
