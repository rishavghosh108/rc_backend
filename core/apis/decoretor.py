from functools import wraps
from flask import request
import os,jwt
from core.libs.assertions import assert_found, assert_valid, base_error
from datetime import datetime

def accept_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        incoming_payload = request.json
        return func(incoming_payload, *args, **kwargs)
    return wrapper

def verification_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token=request.headers.get(os.getenv('otp_verify_header_key'))
        assert_found(token,"verification token is missing !")
        return func(token, *args, **kwargs)
    return wrapper

def verify_token(token, secret_key):
    try:
        data=jwt.decode(token, secret_key, algorithms=['HS256'])
    except:
        base_error(406,{"message":"invalid token"})
        assert_valid(data['expire']>int(datetime.now().timestamp()),"otp has been expired !!!")

def root_authorization_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token=request.headers.get(os.getenv('root_authorization_header_key'))
        assert_found(token, "Authorization token is missing")
        verify_token(token, os.getenv('root_authorization_secret_key'))
        return func(*args, **kwargs)
    return wrapper

def emp_authorization_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token=request.headers.get(os.getenv('emp_authorization_header_key'))
        assert_found(token, "Authorization token is missing")
        verify_token(token, os.getenv('emp_authorization_secret_key'))
        return func(*args, **kwargs)
    return wrapper

def user_authorization_payload(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token=request.headers.get(os.getenv('user_authorization_header_key'))
        assert_found(token, "Authorization token is missing")
        verify_token(token, os.getenv('user_authorization_secret_key'))
        return func(*args, **kwargs)
    return wrapper