from flask import Blueprint
from flask_restful import Api

from .resources import SingleUserResource, UserResource

user_endpoint = 'users'
user_bp = Blueprint(user_endpoint, __name__)
user_api = Api(user_bp)

# Add endpoints
user_api.add_resource(UserResource, '/', '')
user_api.add_resource(SingleUserResource, '/<string:id>')
