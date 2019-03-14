import os
from flask import Flask, Blueprint
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from .utils.dbconnect import create_tables

from .api.v2 import version_two as v2

def create_app():
    app = Flask(__name__)
    CORS(
        app,
        resources={r"/api/*": {"origins": "*"}},
        supports_credentials=True
        )
    app.register_blueprint(v2)
    app.config['JWT_SECRET_KEY'] =  os.getenv('SECRET_KEY')
    jwt = JWTManager(app)
    create_tables()
    return app
