from datetime import datetime
from flask import Blueprint
from flask_restful import Api, Resource
from core.apis.decoretor import accept_payload, verification_payload
from core.apis.system.Schema import OtpSchema
from core.apis.error_handler import handle_error
from core.apis.common import verify_token, root_authentication_token, emp_authentication_token, user_authentication_token
from core.model.user import User
from core.model.token import Token
from core import db
from core.apis.responses import APIResponse
import os
from core.libs.assertions import base_error

_Otp=Blueprint("otp verify",__name__)

api=Api(_Otp)

class OtpVerify(Resource):

    @accept_payload
    @verification_payload
    def post(token,incoming_payload,self):
        data=OtpSchema().load(incoming_payload)
        data=verify_token(token,data['otp'])
        if data['type']=='signup':
            temp=data['data']
            if temp['type']==4:
                temp['dob']=datetime.strptime(temp['dob'], '%Y-%m-%d').date()
            User.signup(temp)
            if temp['type']==2:
                token = Token.check_token(temp)
                db.session.delete(token)
            db.session.commit()
            message = APIResponse('{"successful":"sign up successful"}',200)
        
        elif data['type']=='login':
            temp = data['data']
            message = APIResponse('{"successful":"login successful"}',200)

            if temp['type']==1:
                token = root_authentication_token(temp)
                message.headers[os.getenv('root_authorization_header_key')] = token
            elif temp['type']==2:
                token = emp_authentication_token(temp)
                message.headers[os.getenv('emp_authorization_header_key')] = token
            elif temp['type']==4:
                token = user_authentication_token(temp)
                message.headers[os.getenv('user_authorization_header_key')] = token

        elif data['type']=='forget':
            temp = data['data']
            message = APIResponse('{"successful":"password has been changed"}')
            User.change_password(temp)
            db.session.commit()

        else:
            base_error(400, "something went wrong !!!")
                
        return message
        
    
api.handle_error=handle_error
api.add_resource(OtpVerify,'/otpverify/')