from flask_restful import Resource, reqparse
from flask import jsonify, make_response, request
from flask_jwt_extended import jwt_required, get_jwt_identity

from ....utils.validators_schema import ProductValidate
from ..models.product_models import ProductRecord
from ..models.base_models import BaseModels


class Product(ProductRecord, Resource):
    def __init__(self):
        self.record = ProductRecord()
        self.check = BaseModels('users')

    @jwt_required
    def post(self):
        author = get_jwt_identity()
        credentials = self.check.get_data("email",author)

        """Checks that the user has admin credentials"""
        if credentials['isadmin'] != True:
            return make_response(jsonify({"status":401,
                                       "message":" This service is for admin only"}), 401)
        data = request.get_json()
        data, errors = ProductValidate().load(data)
        if errors:
            return make_response(jsonify({"status" : 400,
                                          "error": errors}), 400)

        response = self.record.add_product(data, author)
        return make_response(jsonify({"status" : 201,
                                      "message":"Record added succesfully",
                                      "data": response}), 201)
    def get(self):
        return make_response(jsonify({"status":200,
                                    "message":"The available products",
                                    "data": self.record.get_all_products()}), 200)


class SpecificProduct(ProductRecord, Resource):
    def __init__(self):
        self.record = ProductRecord()
        self.check = BaseModels('products')

    def get(self,id):
        if self.check.get_data("id",id) == None:
            return make_response(jsonify({"status":404,
                                        "message":"The product not found"
                                        }), 404)

        return make_response(jsonify({"status":200,
                                    "message":"The available products",
                                    "data": self.record.get_specific_product(id)}), 200)

    def delete(self,id):
        if self.check.get_data("id",id) == None:
            return make_response(jsonify({"status":404,
                                        "message":"The product not found"
                                        }), 404)

        return make_response(jsonify({"status":200,
                                    "message":"The following product has been deleted",
                                    "data": self.record.delete_product(id)}), 200)
