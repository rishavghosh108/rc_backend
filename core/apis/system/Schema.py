from marshmallow import Schema, fields, validates_schema, ValidationError

class UserDataSchema(Schema):
    name = fields.String(required=False)
    dob = fields.String(required=False)
    mobile = fields.Integer(required=False)
    email = fields.Email(required=False)
    user_id = fields.String(required=False)
    password = fields.String(required=False)
    token = fields.String(required=False)

    @validates_schema
    def User_type(self, data, **kwargs):
        name = data.get('name')
        dob = data.get('dob')
        mobile = data.get('mobile')
        email = data.get('email')
        user_id = data.get('user_id')
        password = data.get('token')

        if name:
            raise ValidationError('testing')