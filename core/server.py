from core import app
from flask_cors import CORS
import os

from core.apis.system import _System_Apis

app.register_blueprint(_System_Apis)

CORS(
    app,
    resources={r"*": {"origins": "*"}},
    methods=['POST', 'GET'],
    expose_headers=['Content-Type', 'Access-Control-Allow-Origin', os.getenv('authorization_header_key'), os.getenv('otp_verify_header_key')],
    allow_headers=['Content-Type',  os.getenv('otp_verify_header_key'), os.getenv('authorization_header_key')]
)