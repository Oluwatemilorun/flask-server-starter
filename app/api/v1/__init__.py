from flask import Blueprint

from .user import user_bp, user_endpoint

api_v1_bp = Blueprint("v1", __name__)

# register API (v1) blueprints
api_v1_bp.register_blueprint(user_bp, url_prefix=user_endpoint)
