from core import app
from flask_cors import CORS
import os

from core.apis.system import _System_Apis
from core.apis.superuser import _root_Apis

app.register_blueprint(_System_Apis)
app.register_blueprint(_root_Apis)

CORS(
    app,
    resources={r"*": {"origins": "*"}},
    methods=['POST', 'GET'],
    expose_headers=['Content-Type', 'Access-Control-Allow-Origin', os.getenv('root_authorization_header_key'), os.getenv('emp_authorization_header_key'), os.getenv('user_authorization_header_key'), os.getenv('otp_verify_header_key')],
    allow_headers=['Content-Type', os.getenv('root_authorization_header_key'), os.getenv('emp_authorization_header_key'), os.getenv('user_authorization_header_key'),  os.getenv('otp_verify_header_key')]
)