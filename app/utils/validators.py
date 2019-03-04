import re
from marshmallow import ValidationError


class Views():
    """ Validate views endpoints data """
    def validate_email(self, email):
        """ Valiadte email format """
        if re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email) is None:
            raise ValidationError("Invalid email address!")
        return email

    def validate_password(self, password):
        """ Validate user password"""
        self.validate_all_values(password)
        if re.search('[0-9]', password) is None:
            raise ValidationError('Password must have at least one number!')

        elif re.search('[a-z]', password) is None:
            raise ValidationError('Password must have at least one alphabet letter!')

        else:
            return password

    def validate_all_values(self, value):
        """ Validate if all fields are provided """
        if isinstance(value, str):
            if not value.strip(" "):
                raise ValidationError('This field cannot be empty!')
        elif value:
            return value

    
