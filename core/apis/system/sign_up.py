from flask import Blueprint
from flask_restful import Resource
from core.apis.decoretor import accept_payload
from .Schema import UserDataSchema

_Signup=Blueprint("sign up api",__name__)

# class Signup(Resource):

#     @accept_payload
#     def post(self,incoming_payload):
#         data = UserDataSchema.load(incoming_payload)
#         return "hi"

@_Signup.route('/signup',methods=['post'], strict_slashes=False)
@accept_payload
def signup(incoming_payload):
    data = UserDataSchema().load(incoming_payload)
    return 'hello'