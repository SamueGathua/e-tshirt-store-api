from flask_restful import Api, Resource
from flask import Blueprint

version_two = Blueprint('api_v2', __name__, url_prefix='/api/v2')
api = Api(version_two)

from .views.user_views import User,Admin,Login
from .views.product_views import Product,SpecificProduct

api.add_resource(User, '/user/register')
api.add_resource(Admin, '/admin/register')
api.add_resource(Login, '/user/login')
api.add_resource(Product, '/products')
api.add_resource(SpecificProduct, '/products/<int:id>')
