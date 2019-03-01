from flask_restful import Api, Resource
from flask import Blueprint

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version_two)

from .views.user_views import RegisterUser, LoginUser
from .views.product_views import AddProduct

api.add_resource(RegisterUser, '/user/register')
api.add_resource(LoginUser, '/user/login')
api.add_resource(AddProduct, '/products')
