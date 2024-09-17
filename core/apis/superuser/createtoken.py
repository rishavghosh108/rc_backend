from flask import Blueprint
from flask_restful import Resource,Api
from core.apis.decoretor import accept_payload
from .Schema import TokenSchema
from core.model.token import Token
from core import db
from core.apis.responses import APIResponse
from core.apis.error_handler import handle_error

_createtoken=Blueprint("to create employ",__name__)

api=Api(_createtoken)

class CreateToken(Resource):

    @accept_payload
    def post(incoming_payload,self):
        data = TokenSchema().load(incoming_payload)
        Token.create_token(data)
        db.session.commit()
        return APIResponse('{"successful":"token created successfully"}',200)
    
api.handle_error=handle_error
api.add_resource(CreateToken,'/createtoken/')