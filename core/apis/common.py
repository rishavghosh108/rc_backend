from werkzeug.security import generate_password_hash
from random import randint
from datetime import datetime, timedelta
import jwt


def gen_password(password):
    return generate_password_hash(password,method='pbkdf2:sha256')

def gen_token(data, secret_key, time):
    time = datetime.now()+ timedelta(minutes=time)
    exp = time.timestamp()
    payload={"data":data,'expire':exp}
    temp = jwt.encode(payload, str(secret_key), algorithm='HS256')
    return 'hi'