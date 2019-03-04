from flask_restful import Resource,reqparse
from flask import jsonify, make_response, request
from werkzeug.security import check_password_hash
from flask_jwt_extended import create_access_token, jwt_required,get_jwt_identity


from ..models.user_models import UserRecord
from ..models.base_models import BaseModels
from ....utils.validators_schema import UserValidate


class User(UserRecord, Resource):
    """User record endpoints"""
    def __init__(self):
        self.models = UserRecord()
        self.check = BaseModels('users')

    def post(self):
        """ post endpoint for user registration """
        json_data = request.get_json()
        data, errors = UserValidate().load(json_data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "error": errors}), 400)
        response = self.models.register_user(json_data, False)

        access_token = create_access_token(identity=json_data['email'])
        if response is "No match":
            return make_response(jsonify({"status" : 400,
                                          "error": "The passwords do not match!"}), 400)
        if response is False:
            return make_response(jsonify({"status" : 400,
                                          "error": "A user with the provided email exists"}), 400)
        return make_response(jsonify({"status" : 201,
                                      "message" : "User registration succesful",
                                     "data": response}), 201)

    @jwt_required
    def get(self):
        author = get_jwt_identity()
        credentials = self.check.get_data("email",author)
        """Checks that the user has admin credentials"""
        if credentials['isadmin'] != True:
            return make_response(jsonify({"status":401,
                                       "error":" This service is for admin only"}), 401)
        return make_response(jsonify({"status":200,
                                    "message":"The available users",
                                    "data": self.models.get_all_users()}), 200)

class Admin(User, Resource):
    """Admin Admin signup endpoint"""
    def __init__(self):
        self.models = UserRecord()

    def post(self):
        """ post endpoint for admin registration """
        json_data = request.get_json()
        data, errors = UserValidate().load(json_data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "error": errors}), 400)
        response = self.models.register_user(json_data, True)
        if not response:
            return make_response(jsonify({"status" : 400,
                                          "error": "A user with the given Email exists"}), 400)
        access_token = create_access_token(identity=response['email'])
        return make_response(jsonify({"status" : 201,
                                      "message" : "Admin registration succesful",
                                      "data": response}), 201)


class Login(UserRecord, Resource):
    """ Class to authenticate a user"""
    def __init__(self):
        self.models = UserRecord()

    def post(self):
        """ endpoint for user login"""
        json_data = request.get_json()
        response = self.models.login_user(json_data)
        if response == "not_found":
            return make_response(jsonify({"status" : 404,
                                          "error": "User does not exists!"}), 404)
        elif response is False:
            return make_response(jsonify({"status" : 400,
                                          "error": "Wrong usernamepassword combination!"}), 400)
        access_token = create_access_token(identity=json_data['email'],)
        return make_response(jsonify({"status" : 200,
                                      "message": "Logged in as {}"\
                                      .format(json_data['email'].split("@")[0]),
                                      "access_token" : access_token}), 200)
