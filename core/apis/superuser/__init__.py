from flask import Blueprint

from .createtoken import _createtoken

_root_Apis=Blueprint('all apis for superuser', __name__, url_prefix='/super')

_root_Apis.register_blueprint(_createtoken)