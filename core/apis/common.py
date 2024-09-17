from werkzeug.security import generate_password_hash
from datetime import datetime, timedelta
import jwt,os
from core.libs.assertions import assert_valid, base_error


def gen_password(password):
    return generate_password_hash(password,method='pbkdf2:sha256')

def gen_token(data, secret_key, time, type):
    time = datetime.now()+ timedelta(minutes=time)
    exp = time.timestamp()
    payload={"data":data,"expire":exp,"type":type}
    temp = jwt.encode(payload, str(secret_key), algorithm='HS256').decode('utf-8')
    return temp

def verify_token(token, secret_key):
    try:
        data=jwt.decode(token,str(secret_key), algorithms=['HS256'])
    except:
        base_error(406,{"message":"please enter otp correctly !!!"})
    assert_valid(data['expire']>int(datetime.now().timestamp()),"otp has been expired !!!")
    return data

def root_authentication_token(data):
    time = datetime.now()+timedelta(minutes=1500)
    exp = time.timestamp()
    payload = {"email":data['email'], "type":data['type'], "expire":exp}
    temp = jwt.encode(payload, os.getenv('root_authorization_secret_key'), algorithm='HS256').decode('utf-8')
    return temp

def emp_authentication_token(data):
    time = datetime.now()+timedelta(minutes=480)
    exp = time.timestamp()
    payload = {"email":data['email'], "type":data['type'], "expire":exp}
    temp = jwt.encode(payload, os.getenv('emp_authorization_secret_key'), algorithm='HS256').decode('utf-8')
    return temp

def user_authentication_token(data):
    time = datetime.now()+timedelta(minutes=43200)
    exp = time.timestamp()
    payload = {"email":data['email'], "type":data['type'], "expire":exp}
    temp = jwt.encode(payload, os.getenv('user_authorization_secret_key'), algorithm='HS256').decode('utf-8')
    return temp
