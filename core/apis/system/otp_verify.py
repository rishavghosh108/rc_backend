from flask import Blueprint,request
from flask_restful import Api, Resource
from core.apis.decoretor import accept_payload, verification_payload
from core.apis.system.Schema import OtpSchema
from core.apis.error_handler import handle_error

_Otp=Blueprint("otp verify",__name__)

api=Api(_Otp)

class OtpVerify(Resource):

    @accept_payload
    @verification_payload
    def post(self):
        data=OtpSchema().load(request.json)
        return 'hi'
    
api.handle_error=handle_error
api.add_resource(OtpVerify,'/otpverify/')