from marshmallow import Schema,fields

class TokenSchema(Schema):
    email = fields.Email(required=True)