from flask import Blueprint
from flask_restful import Resource, Api
from core.apis.decoretor import accept_payload
from .Schema import LoginForgetSchema
from random import randint
from core.model.user import User
from core.apis.common import gen_token
from core.apis.responses import APIResponse
from werkzeug.security import generate_password_hash
import os
from core.apis.error_handler import handle_error

_Forget = Blueprint("forget password for every type user",__name__)

api = Api(_Forget)

class Forget(Resource):

    @accept_payload
    def post(incoming_payload ,self):
        data = LoginForgetSchema().load(incoming_payload)
        otp = randint(100000,999999)
        print(otp)
        User.forget(data)
        payload = {"email":data['email'],"password":generate_password_hash(data['password']),"type":data['type']}
        token = gen_token(payload,otp,15,'forget')
        message=APIResponse('{"successful":"please enter the otp. "}',200)
        message.headers[os.getenv('otp_verify_header_key')] = token
        return message
    
api.handle_error = handle_error
api.add_resource(Forget,"/forget")