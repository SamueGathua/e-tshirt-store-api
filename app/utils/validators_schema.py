""" import third party modules """
from marshmallow import Schema, fields
from .validators import Views


class UserValidate(Schema):
    """ Validate data for user registration """
    firstname = fields.Str(required=True, validate=Views().validate_all_values)
    lastname = fields.Str(required=True, validate=Views().validate_all_values)
    email = fields.Str(required=True, validate=Views().validate_email)
    password = fields.Str(required=True, validate=Views().validate_password)
    repeat_password = fields.Str(required=True)
    othername = fields.Str(required=True)
    phonenumber = fields.Str(required=True)


class ProductValidate(Schema):
    """ Validate product data """
    title = fields.Str(required=True, validate=Views().validate_all_values)
    info = fields.Str(required=True, validate=Views().validate_all_values)
    img= fields.Str(required=True, validate=Views().validate_all_values)
    price = fields.Int(required=True, validate=Views().validate_all_values)
    company = fields.Str(required=True, validate=Views().validate_all_values)
    quantity = fields.Int(required=True, validate=Views().validate_all_values)
