from flask import Blueprint
from flask_restful import Resource,Api
from core.apis.decoretor import accept_payload
from .Schema import LoginForgetSchema
from core.model.user import User
from core.apis.common import gen_token
from random import randint
from core.apis.responses import APIResponse
import os
from core.apis.error_handler import handle_error

_Login=Blueprint("for login api",__name__)
api=Api(_Login)

class Login(Resource):

    @accept_payload
    def post(incoming_payload,self):
        data=LoginForgetSchema().load(incoming_payload)
        otp = randint(100000,999999)
        print(otp)
        User.login(data)
        token = gen_token({"email":data['email'],"type":data['type']},otp,15,'login')
        message=APIResponse('{"successful":"please enter the otp. "}',200)
        message.headers[os.getenv('otp_verify_header_key')] = token
        return message
    
api.handle_error = handle_error
api.add_resource(Login,"/login/")