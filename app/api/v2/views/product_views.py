from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ..models.product_models import ProductRecord
from ..models.base_models import User
from ....utils.validators import Validations

class AddProduct(Resource, ProductRecord):
    def __init__(self):

        self.records = ProductRecord()
        self.parser = reqparse.RequestParser()
        self.check = User()
        self.validate = Validations()
        """validates the key and data types  for the meetup record"""

        self.parser.add_argument('title', type=str, required=True, help='Invalid key for title')
        self.parser.add_argument('info', type=str, required=True, help='Invalid key for info')
        self.parser.add_argument('img', type=str, required=True, help='Invalid key for img')
        self.parser.add_argument('price', type=str, required=True, help='Invalid key for price')
        self.parser.add_argument('company', type=str, required=True, help='Invalid key in company')
        self.parser.add_argument('quantity', type=str, required=True, help='Invalid key in quantity')

    def get(self):
        return make_response(jsonify({"status":200,
                                    "message":"The available products records are",
                                    "data": self.records.get_all_products()}), 200)

    @jwt_required
    def post(self):
        reqdata = self.parser.parse_args(strict=True)
        author = get_jwt_identity()
        """validates that the data received is not null"""
        """"if the null an error message is thrown"""
        if not self.check.check_is_admin(author):
            return make_response(jsonify({"status":401,
                                       "message":" This service is for admin only"}), 401)
        title= reqdata['title']
        if self.validate.check_type(title):
            return make_response(jsonify({"status":400,
                                       "error":"The title cannot be an integer"}), 400)
        if not reqdata['title'] or not reqdata['title'].strip():
            return make_response(jsonify({"status":400,
                                       "error":" The title field is required"}), 400)
        if not reqdata['info'] or  not reqdata['info'].strip():
            return make_response(jsonify({"status":400,
                                       "error":"The info field is required"}), 400)
        if not reqdata['img'] or not reqdata['img'].strip() :
            return make_response(jsonify({"status":400,
                                       "error":"The image field is required"}), 400)
        if not reqdata['price']:
            return make_response(jsonify({"status":400,
                                       "error":"The price field is required"}), 400)
        if not reqdata['company']:
            return make_response(jsonify({"status":400,
                                       "error":"The company field is required"}), 400)
        if not reqdata['quantity']:
            return make_response(jsonify({"status":400,
                                       "error":"The quantity field is required"}), 400)

        else:
            """Executed when all the above validations pass"""


            return make_response(jsonify({"status":201,
                                         "message":"A new record with the following data has been added",
                                         "data": self.records.add_product(reqdata,author)}), 201)
