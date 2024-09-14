from werkzeug.security import generate_password_hash
from random import randint
from datetime import datetime, timedelta
import jwt
from core.apis.responses import APIResponse
from core.libs.assertions import assert_valid


def gen_password(password):
    return generate_password_hash(password,method='pbkdf2:sha256')

def gen_token(data, secret_key, time, type):
    time = datetime.now()+ timedelta(minutes=time)
    exp = time.timestamp()
    payload={"data":data,"expire":exp,"type":type}
    temp = jwt.encode(payload, str(secret_key), alg='HS256')
    return 'hi'

def verify_token(token, secret_key):
    try:
        data=jwt.decode(token,str(secret_key), alg=['HS256'])
    except:
        return APIResponse('{"message":"please enter otp correctly !!!"}',406)
    assert_valid(data['expire']>int(datetime.now().timestamp()),"otp has been expired !!!")
    return data
