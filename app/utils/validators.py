import re

class Validations():


    def validate_email(self, email):
        expects = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(expects, email)


    def validate_password(self, password):

        valid = "^(((?=.*[a-z])(?=.*[A-Z]))|((?=.*[a-z])(?=.*[0-9]))|((?=.*[A-Z])(?=.*[0-9])))(?=.{6,})"
        return re.match(valid, password)

    def validate_white_space(self,field):
        return re.match(r'^[a-zA-Z]+$', field)

    def check_type(self,data):
        if type(data)== int:
            return True
        return False

    def check_password_match(self,password,repeat_password):
        if password != repeat_password:
            return False
        return True
