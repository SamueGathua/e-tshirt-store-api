from flask_restful import Resource,reqparse
from flask import jsonify, make_response, request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token

from ..models.user_models import UserRecords
from ..models.base_models import User
from ....utils.validators import Validations

class RegisterUser(Resource, UserRecords):
    def __init__(self):
        self.records = UserRecords()
        self.parser = reqparse.RequestParser()
        self.validate = Validations()
        self.check = User()
        """validates the key and data types  for the meetup record"""
        self.parser.add_argument('firstname', type=str, required=True,
                                help='Invalid key for firstname')
        self.parser.add_argument('lastname', type=str, required=True,
                                help='Invalid key for lastname')
        self.parser.add_argument('othername', type=str, required=True,
                                help='Invalid key for othername')
        self.parser.add_argument('email', type=str, required=True,
                                help='Invalid key for email')
        self.parser.add_argument('phonenumber', type=str, required=True,
                                help='Invalid key for phonenumber')
        self.parser.add_argument('password', type=str, required=True,
                                help='Invalid key for password')
        self.parser.add_argument('repeat_password', type=str, required=True,
                                help='Invalid key for repeat_password')



    def post(self):
         data = self.parser.parse_args(strict=True)
         """Checks that the fields are not empty"""
         if not data:
             return make_response(jsonify({"status":400,
                                        "error":" All the fields are required"}), 400)
         if not data['firstname'].strip():
             return make_response(jsonify({"status":400,
                                        "error":" The firstname field is required"}), 400)
         if not data['firstname'].strip():
             return make_response(jsonify({"status":400,
                                        "error":"The lastname field is required"}), 400)
         if not data['othername'] or not data['othername'].strip() :
             return make_response(jsonify({"status":400,
                                        "error":"The othername field is required"}), 400)
         if not data['email'].strip():
             return make_response(jsonify({"status":400,
                                        "error":"The email field is required"}), 400)
         if not data['phonenumber'].strip():
             return make_response(jsonify({"status":400,
                                        "Error":"The phoneNumber field is required"}), 400)
         if not data['password'].strip():
             return make_response(jsonify({"status":400,
                                       "error":"The password field is required"}), 400)
         if not data['repeat_password'].strip():
             return make_response(jsonify({"status":400,
                                       "error":"The repeat password field is required"}), 400)
         if not self.validate.validate_email(data['email']):
             return make_response(jsonify({"status":400,
                                        "error":"Invalid email format"}), 400)
         if self.check.get_user_details(data['email']):
              return make_response(jsonify({"status":400,
                                         "error":"Email already exists"}), 400)
         if not self.validate.validate_password(data['password']):
             return make_response(jsonify({"status":400,
                                        "error":"Password should have atleast 1 character,1 uppercase,and a number"}), 400)
         if not self.validate.validate_white_space(data['firstname']):
             return make_response(jsonify({"status":400,
                                         "error":"First name should not contain spaces"}), 400)
         if not self.validate.validate_white_space(data['lastname']):
             return make_response(jsonify({"status":400,
                                         "error":"Lastname should not contain spaces"}), 400)
         if not self.validate.validate_white_space(data['othername']):
             return make_response(jsonify({"status":400,
                                         "error":"Othername should not contain spaces"}), 400)
         if not self.validate.check_password_match(data['password'],data['repeat_password']):
             return make_response(jsonify({"status":400,
                                         "error":"Passwords donot match"}), 400)

         else:
             res = self.records.register_user(data)
             return make_response(jsonify({
                                        "message": "Records for {} {} has beed added".format( data['firstname'],data['lastname']),
                                        "status":201,
                                        "data":data}), 201)


class LoginUser(UserRecords, Resource):
    """ class to login a user """
    def __init__(self):
        self.records = UserRecords()
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True,
                                help='Invalid key for email')
        self.parser.add_argument('password', type=str, required=True,
                                help='Invalid key for password')

    def post(self):
        """ post request endpoint for user login """
        data= self.parser.parse_args(strict=True)

        if not data['email'].strip():
            return make_response(jsonify({"status":400,
                                       "error":"email field is required"}
                                       ), 400)
        if not data['password'].strip():
            return make_response(jsonify({"status":400,
                                       "error":"Password field is required"}
                                       ), 400)

        if self.records.login_user(data['email']):
            password,email = self.records.login_user(data['email'])
            access_token = create_access_token(identity= email.strip())
            if check_password_hash(password.strip(), data['password']):

                return make_response(jsonify({"message":"Login for {} is succesful".format(data['email']),
                                              "status":200,
                                             "token":access_token}), 200)
            else:
                return make_response(jsonify({"status":400,
                                            "error":"Incorrect password"}), 400)

        return make_response(jsonify({"status":404,
                                    "error":"user does not exist"}), 404)
