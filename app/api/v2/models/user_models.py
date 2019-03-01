import datetime
from werkzeug.security import generate_password_hash

from ....utils.dbconnect import init_db

class UserRecords():
    def __init__(self):
        self.db = init_db()

    def register_user(self, data):
        data = {
        "registered_on":datetime.datetime.now(),
        "firstname": data['firstname'],
        "lastname": data['lastname'],
        "othername": data['othername'],
        "email": data['email'],
        "phonenumber":data['phonenumber'],
        "password":generate_password_hash(
        data['password'],method='pbkdf2:sha256', salt_length=8),
        }
        query = """INSERT INTO users(FirstName, LastName, OtherName,\
        Email,Password,RegisteredOn,PhoneNumber)
        VALUES ('%s', '%s', '%s', '%s','%s','%s','%s');""" % \
        (data['firstname'], data['lastname'], data['othername'], data['email'],\
        data['password'], data['registered_on'],data['phonenumber'])
        cur = self.db.cursor()
        cur.execute(query)
        self.db.commit()
        return data

    def login_user(self, email):
        cursor = self.db.cursor()
        cursor.execute(
        "SELECT password, email FROM users WHERE email = '{}'".format(email))
        user_data = cursor.fetchone()
        if user_data:
            return user_data
        return None
