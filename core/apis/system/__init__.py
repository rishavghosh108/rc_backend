from flask import Blueprint

from .sign_up import _Signup
from .otp_verify import _Otp

_System_Apis=Blueprint('all system apis', __name__, url_prefix='/system')

_System_Apis.register_blueprint(_Signup)
_System_Apis.register_blueprint(_Otp)