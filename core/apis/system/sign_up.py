from flask import Blueprint, jsonify
from flask_restful import Resource, Api
from core.apis.decoretor import accept_payload
from .Schema import UserDataSchema
from core.apis.common import gen_password, gen_token
from random import randint
from core.apis.responses import APIResponse
import os
from core.apis.error_handler import handle_error

_Signup=Blueprint("sign up api",__name__)

api=Api(_Signup)

class Signup(Resource):

    @accept_payload
    def post(incoming_payload, self):
        data = UserDataSchema().load(incoming_payload)
        data['password'] = gen_password(data['password'])
        print(data)
        otp = randint(100000,999999)
        print(otp)
        # token = gen_token(data=data,secret_key=otp,time=15)
        message=APIResponse('{"successful":"please enter the otp. "}',200)
        message.headers[os.getenv('verification_token_key')] = 'token'
        return message


api.handle_error=handle_error
api.add_resource(Signup, '/signup/')