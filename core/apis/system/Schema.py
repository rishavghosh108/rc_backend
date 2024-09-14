from marshmallow import Schema, fields, validates_schema, ValidationError, validate

def validate_integer_length(n):
    def validator(value):
        if len(str(value))!=n:
            raise ValidationError(f'The integer must have exactly {n} digits.')
    return validator

class UserDataSchema(Schema):
    name = fields.String(required=False)
    dob = fields.String(required=False)
    mobile = fields.Integer(required=False, validate=validate_integer_length(10))
    email = fields.Email(required=False)
    user_id = fields.String(required=False)
    password = fields.String(required=False)
    token = fields.String(required=False)
    type = fields.Integer(required=True, validate=validate.OneOf([1, 2, 4], error="Type must be 1, 2, or 3"))

    @validates_schema
    def User_type(self, data, **kwargs):
        type = data.get('type')
        name = data.get('name')
        dob = data.get('dob')
        mobile = data.get('mobile')
        email = data.get('email')
        user_id = data.get('user_id')
        token = data.get('token')
        password = data.get('password')

        if type == 1 and email is not None and password is not None:
            if not(name is None and dob is None and mobile is None and user_id is None and token is None):
                raise ValidationError("please enter valid data for admin user")
        elif type == 2 and password is not None and email is not None and token is not None:
            if not(name is None and dob is None and mobile is None and user_id is None):
                raise ValidationError("please enter valid data for employee")
        elif type == 4 and password is not None and email is not None and user_id is not None and dob is not None and name is not None and mobile is not None:
            if not(token is None):
                raise ValidationError("please enter valid data for normal user")
        else:
            raise ValidationError("please enter valid data")
        
class OtpSchema(Schema):
    otp = fields.Integer(required=True, validate=validate_integer_length(6))